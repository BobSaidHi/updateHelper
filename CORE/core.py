#Module:  core
#SubComponet:   CORE
#COMPONET:  updateHelper
#Projet:    Generic updateHelper

#Author:    Noah Fouts
#Version:   0.0.1.0
#Version Name:  INDEV 0.0.1
#Updated:   2020-05-02T05:45 PM PSTT

#This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import json
import os

#Start Logger
logger = logging.getLogger("updateHelper")

#non-GUI
def startCore():
    checkVersion.readConfig(checkVersion, "../config/updateConfig.cfg", "0.0.1.0")

#CORE
class checkVersion:
    def readConfig(self, location, minVersion):
        try:
            newLocation = os.path.relpath(location, os.path.dirname(os.getcwd()))
            configFile = open(newLocation, "r")
            configFileText = configFile.read()
            configFileDump = json.loads(configFileText)
            logger.info("Checking")
            if(configFileDump["format"].split(".")[1] == "1"):
                logger.info("Config File Version: " + configFileDump["format"] + " [OK]")
                logger.info("module: " + configFileDump["module"])
                logger.info("uuid: " + configFileDump["uuid"])
                logger.info("description: " + configFileDump["description"])
                logger.info("website: " + configFileDump["website"])
                self.checkVersionCompat(checkVersion, configFileDump["version"], minVersion)
            else:
                logger.error("Wrong updateConfig fomrat! in file: " + newLocation)
        except(FileNotFoundError):
            logger.error("Update Configuration file not found in " + newLocation)
            pass

    def checkVersionCompat(self, current, min):
        currentArgs = current.split(".")
        minArgs = current.split(".")
        print("e")
        #Max
        if(int(currentArgs[0]) + 1 > int(minArgs[0])):
            logger.warning("Version to new")
        #Version to old
        elif(int(currentArgs[1])) < int(minArgs[1]):
            logger.warning("Version signifacitnly outdated")
        elif(int(currentArgs[2]) < int(minArgs[2])):
            print("Version outdated")
        else:
            print("d")
            logger.critical("The code should never read this point")
