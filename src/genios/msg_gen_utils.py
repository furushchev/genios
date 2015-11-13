#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp>

import collections
import rospkg


class DependenceGraph(object):
    def __init__(self, pkgname):
        self.pkgname = pkgname
        self.nodes = {}
        self.generateGraph(self.pkgname)
        print self.nodes

    def generateGraph(self, pkgname):
        r = rospkg.RosPack()
        stack = r.get_depends(pkgname, False)
        while stack:
            p = stack.pop()
            d = r.get_depends(p)
            if d:
                if not p in self.nodes:
                    self.nodes[p] = d
                stack += d

if __name__ == '__main__':
    g = DependenceGraph('sensor_msgs')
