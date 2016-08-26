#!/usr/bin/python

import os
import socket
import argparse
import signal
import time
from sendfile import sendfile

def handler(signum, frame):
    print "Exiting"
    exit()

def get_client(nw_prefix, scanport):
    hostid = 33
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            print "Scanning " + nw_prefix + str(hostid) + " on port " + str(scanport)
            sock.connect((nw_prefix + str(hostid), scanport))
        except:
            time.sleep(2)
            hostid += 1
            hostid %= 255
            continue
        break
    return (sock, hostid)
    
def start_server(scanport, filename, nw_prefix):
    print "Initializing Server"
    while True:
        client, hid = get_client(nw_prefix, scanport)
        print "Sending to " + nw_prefix + str(hid)
        send_file(client, filename)
    



def recv_file(filepath, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("", port))
        s.listen(5)
    except:
        print "bind/listen failed"
        exit()
    try:
        acc, addr = s.accept()
    except:
        print "Interrupted"
        s.close()
        exit()
    print "Got connection from " + addr[0]
    s.close()
    l = acc.recv(1024)
    f = open(filepath, "w")
    while(l):
        print "recv.."
        f.write(l)
        l = acc.recv(1024)
    f.close()
    acc.shutdown(socket.SHUT_WR)
    acc.close()
    print "Success"


def send_file(sock, filepath):
    print "Sending file" + filepath
    size = os.path.getsize(filepath)
    f = open(filepath, "rb")

    offset = 0
    while True:
        sent = sendfile(sock.fileno(), f.fileno(), offset, size)
        if sent == 0:
            break
        offset += sent
    f.close()
    sock.shutdown(socket.SHUT_WR)
    sock.close()


def main():

    parser = argparse.ArgumentParser(description="LAN file distribution program")
    group = parser.add_argument_group("network arguments")
    group.add_argument('-nwid', type=str, required=True, help='Network to distribute files')
    group.add_argument('-p', type=int, required=True, help='Listen port of listener nodes')
   
    subparsers = parser.add_subparsers()
    parser_starter = subparsers.add_parser('starter', help='Starter node')
    parser_starter.add_argument('-f',type=str,required=True, help='File path of file to send')
    parser_starter.set_defaults(mode='starter')

    parser_node = subparsers.add_parser('node', help='Listener Node')
    parser_node.add_argument('-filename', type=str, required=True, help='Filename to save the file as')
    parser_node.set_defaults(mode='node')

    #parser.add_argument('--mode',choices=['starter', 'node'],required=True, help = 'Mode')
    #parser.add_argument('--port',type = int,help="Listener Port") 
    args = parser.parse_args()
    print args
    #socket.setdefaulttimeout(4)
    signal.signal(signal.SIGINT, handler)
    if(args.mode == 'starter'):
        start_server(args.p, args.f, args.nwid)
    else:
        print "starting in node mode"
        recv_file(args.filename, args.p)
        start_server(args.p, args.filename, args.nwid)




main()
