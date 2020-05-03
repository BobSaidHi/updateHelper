#Module:  main
#SubComponet:   none
#COMPONET:  updateHelper
#Projet:    Generic updateHelper

#Author:    Noah Fouts
#Version:   0.1.0.0
#Version Name:  INDEV 0.1
#Updated:   2020-05-02T05:25 PM PST

#This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import os
import sys
from datetime import datetime
from CORE import core

#Start Logger
logger = logging.getLogger("updateHelper")
logger.setLevel(logging.DEBUG)

#Log to file
def CreateLoggingFh():
    Current_time = datetime.now().strftime('%Y-%m-%d__%H-%M-%S')
    fh = logging.FileHandler('logs/updateHelper-' + Current_time + '.log')
    fh.setLevel(logging.DEBUG)
    formatterFh = logging.Formatter('%(asctime)s - %(pathname)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
    fh.setFormatter(formatterFh)
    logger.addHandler(fh)
    logger.debug("Log to file handler created!")
try:
    CreateLoggingFh()
except(FileNotFoundError):
    os.mkdir('logs')
    CreateLoggingFh()
    logger.info("Couldn't find log direcotry and created a new one instead.")
    pass

#Log to the console/termainl
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
formatterCh = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')
ch.setFormatter(formatterCh)
logger.addHandler(ch)
logger.debug("Log to console handler created!")
logger.info("Imported modules and started Logger.")

argsCount = 0
for i in sys.argv:
    argsCount += 1

if(argsCount > 2):
    logger.error("Invalid agrs")
elif(argsCount > 1):
    logger.info("Starting without gui")
    core.startCore()
    
else:
    logger.info("Starting with gui")
