#!/usr/bin/env python2
#  -*- coding: utf-8 -*-
import os
from fabric.api import *
from fabric.contrib.console import confirm

env.host = 'SunnyHao'
CURRENT_PATH = os.path.abspath(__file__).rsplit('/', 1)[0]

def addAlias():
    run("alias {}={}".format("dailyadd", CURRENT_PATH+"/daily_logger.py"))
    run("alias {}={}".format("dailyread", CURRENT_PATH+"/read.py"))
    pass

def chmod():
    local("chmod +x {}".format(CURRENT_PATH+"/daily_logger.py"))
    local("chmod +x {}".format(CURRENT_PATH+"/read.py"))

def fabfile():
    addAlias()
    chmod()
    local("whoami")

if __name__ == "__main__":
    fabfile()