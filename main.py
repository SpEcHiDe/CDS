#!/usr/bin/env python2

import os
import paramiko

if __name__ == "__main__" :
  lfile = raw_input("complete path of \'large\' file: ")
  ssh = paramiko.SSHClient()
  ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
  rlst = list_sys(11, 84, 40)
  for ip in rlst :
    ssh.connect(ip, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(lfile, rempath)
    # copy this file to remote system
    # call this python script in the remote system
    sftp.close()
  ssh.close()
    
