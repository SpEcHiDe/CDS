#!/usr/bin/env python2

def list_sys(start, end, subnet) :
  rlst = []
  for i in range(start, end + 1) :
    rlst.append("192.168." + str(subnet) + "." + str(i))
  return rlst

