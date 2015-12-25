#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import datetime
from logger import logger

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Tell me what you want todo")
    else:
        mywords = " ".join(sys.argv[1:])
        print(mywords)
        logger.write(word = mywords)
