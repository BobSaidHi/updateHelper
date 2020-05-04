#Module:  core
#SubComponet:   CORE
#COMPONET:  updateHelper
#Projet:    Generic updateHelper

#Author:    Noah Fouts
#Version:   0.2.1.0
#Version Name:  INDEV 2.1
#Updated:   2020-05-02T11:24 PM PSTT

#This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import logging
import os
from urllib.request import urlretrieve

#Start Logger
logger = logging.getLogger("updateHelper")

#non-GUI
def startCore():
    minBaseVersion =  "0.2.0"
    configFileDump = checkVersion.readConfig(checkVersion, "../config/updateConfig.cfg")
    configFileRemmoteDump = checkVersion.readConfigRemote(checkVersion, configFileDump)
    checkVersion.checkVersionCompat(checkVersion, configFileDump["version"], minBaseVersion, configFileRemmoteDump["version"])
    #TODO Implent SHA-512 file verification

#CORE
class checkVersion:
    updateFileFormatCode = "0.2.0"
    #Reads Config file,
    #Loads json
    #Checks file version
    def readConfig(self, location):
        try:
            newLocation = os.path.relpath(location, os.path.dirname(os.getcwd()))
            configFile = open(newLocation, "r")
        except FileNotFoundError as e:
            logger.critical("Update Configuration file not found in " + newLocation + "ERROR: " + str(e))
            pass
        configFileText = configFile.read()
        configFileDump = json.loads(configFileText)
        logger.info("Checking")
        if(configFileDump["format"].split(".")[1] <= self.updateFileFormatCode.split(".")[1]):
            logger.info("Config File Version: " + configFileDump["format"] + " [OK]")
            logger.info("module: " + configFileDump["module"])
            logger.info("uuid: " + configFileDump["uuid"])
            logger.info("description: " + configFileDump["description"])
            logger.info("website: " + configFileDump["website"])
            logger.info("version-update-URL: " + configFileDump["version-update-URL"])
        else:
            logger.error("Wrong updateConfig fomrat! in file: " + newLocation)
        return configFileDump
    
    def checkVersionCompat(self, current, min, remote):
        currentArgs = current.split(".")
        logger.debug("currentArgs: " + str(currentArgs))
        minArgs = min.split(".")
        logger.debug("minArgs: " + str(minArgs))
        remoteArgs = remote.split(".")
        logger.debug("remoteArgs: " + str(remoteArgs))
        #Max
        if(int(minArgs[0]) + 1 <= int(currentArgs[0])):
            logger.warning("Version to new")
        #Version to old
        elif(int(currentArgs[0]) < int(minArgs[0]) or int(currentArgs[1]) < int(minArgs[1]) or int(currentArgs[2]) < int(minArgs[2])):
            logger.warning("Version too old")
        #Version needs update
        elif(int(remoteArgs[0]) > int(currentArgs[0]) or int(remoteArgs[1]) > int(currentArgs[1]) or int(remoteArgs[2]) > int(currentArgs[2])):
            logger.warning("Update avalible")
        else:
            logger.info("Nothing to upgrade!")
    
    def readConfigRemote(self, configFileDump):
        try:
            configFileRemoteLocation = checkVersion.getUpdateConfigRemote(checkVersion, configFileDump["version-update-URL"])
            configFileRemmote = open(configFileRemoteLocation, "r")
            configFileRemmoteText = configFileRemmote.read()
            configFileRemmote.close()
            configFileRemmoteDump = json.loads(configFileRemmoteText)
        except FileNotFoundError as e:
            logger.critical("Remote pdate Configuration file not found in " + configFileRemoteLocation + "ERROR: " + str(e))
            pass
        logger.info("Remote version " + configFileRemmoteDump["version"])
        return configFileRemmoteDump

    def getUpdateConfigRemote(self, versionUpdateURL):
        downloadLocation = os.path.relpath("temp", os.path.dirname(os.getcwd()))
        logger.debug("Download to: " + downloadLocation)
        #try:
            #urlretrieve(versionUpdateURL, downloadLocation)
        local_filename, headers = urlretrieve(versionUpdateURL)
        logger.info("UpdateConfig downlaoded to: " + downloadLocation)
        return local_filename
        #except FileNotFoundError as e:
        #    logger.info("temp directory not found at " + downloadLocation + "ERROR: " + str(e))
        #    logger.info("Createing new temp direcotry")
        #    os.mkdir("temp")
        #    self.getUpdateConfigRemote(checkVersion)
        #    pass
        #except FileExistsError as e:
        #    logger.info("File " + downloadLocation + "already exists. " + "ERROR: " + str(e))
        #    logger.info("Replaceing file and trying ag"
        #

    def checkFileVersion(self):
        raise NotImplementedError
