#!/usr/bin/env python2

import os
import paramiko
import socket

## somehow "randomize" this function ???
def get_cur_ip() :
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("gmail.com",80))
  a = s.getsockname()[0]
  s.close()
  return a

USER = 'guest'
PASS = 'guest@ssl'

if __name__ == "__main__" :
  lfile = raw_input("complete path of \'large\' file: ")
  lfile = lfile.rsplit('/',1)
  ldir = lfile[0]
  lpath = lfile[1]
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  rlst = list_sys(11, 84, 40)
  for ip in rlst :
    ssh.connect(ip, username=USER, password=PASS)
    command1 = 'wget -c http://' + str(get_cur_ip()) + ':8000/' + str(lpath)
    stdin, stdout, stderr = ssh.exec_command(command1)
    command2 = 'python -m SimpleHTTPServer'
    stdin, stdout, stderr = ssh.exec_command(command2)
  ssh.close()
    
