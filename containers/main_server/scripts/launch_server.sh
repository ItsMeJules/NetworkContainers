#!/bin/sh

cd ${CONTAINER_SERVER_FILES_PATH}

java -Xms${SERVER_INITIAL_RAM} -Xmx${SERVER_MAX_RAM} -jar ${CONTAINER_SERVER_FILES_PATH}/paper-1.8.8.jar