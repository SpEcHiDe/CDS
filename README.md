# CDS
----------

## AIM
* To develop a program to copy large files to all computers in a network in a distributed manner.

## Strategies
1. One strategy would be to use one pc as a server initially and copy the file to another one and then use both as servers to copy to another two pcs and so on.
2. Another would be to broadcast the entire transfer so that each station can listen.

## Requirements
* python 2.7
* pysendfile 2.0.1

## Concept

The script can be run in 2 modes: "starter" and "node".The "starter" is a node which has the resource to distribute.

A "starter" scans the network in a round robin fashion to check for listening "nodes". On finding a "node", it transfers the file and continues to scan the network forever.

The "node"s wait for a "starter" to connect to it and to transfer the resource. Once a "node" gets the resource from a "starter", it itself becomes a "starter".

### Usage
  ```
  $ python test_server.py -h
  usage: test_server.py [-h] -nwid NWID -p P {starter,node} ...

  LAN file distribution program

  positional arguments:
    {starter,node}
      starter       Starter node
      node          Listener Node

  optional arguments:
    -h, --help      show this help message and exit

  network arguments:
    -nwid NWID      Network to distribute files
    -p P            Listen port of listener nodes
  ```
`-nwid` and `-p` are mandatory options.
`-nwid` is used to specify the network part of an ip address in the LAN network.`-p` is the port on which a "node" listens.

#### Starting in "starter" mode
```

$ python test_server.py starter -h
usage: test_server.py starter [-h] -f F

optional arguments:
  -h, --help  show this help message and exit
  -f F        File path of file to send
```
`-f` is to specify the path of the file to share

##### Example
    $ python test_server.py -nwid 127.0.0. -p 50000 starter -f <filename>

#### Starting in "node" mode
```
$ python test_server.py node -h
  usage: test_server.py node [-h] -filename FILENAME
  optional arguments:
    -h, --help          show this help message and exit
    -filename FILENAME  Filename to save the file as
```
`-filename` is to specify the filepath to store the received file

##### Example
    $ python test_server.py -nwid 127.0.0. -p 50000 node -filename <filename>
