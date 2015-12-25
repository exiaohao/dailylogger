#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import datetime
from logger import logger

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.read()
    else:
        logger.read(sys.argv[1])
