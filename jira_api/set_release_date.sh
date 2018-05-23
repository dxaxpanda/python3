#!/bin/bash
set -e
PROJECT_DIR="/opt/jenkins_scripts/sportytrader-front"
RELEASE_DATE=`date +"%F"`
RELEASE_FILE='prod_ver.txt'

printf "[*] %s\n" "Setting up release date to ${PROJECT_DIR}/${RELEASE_FILE}"
echo -e "${RELEASE_DATE}" > $PROJECT_DIR/$RELEASE_FILE
#echo -e "2018-02-12" > $PROJECT_DIR/$RELEASE_FILE

cat $PROJECT_DIR/$RELEASE_FILE

printf "${RELEASE_NOTES}"

python3 $PROJECT_DIR/api_jira.py

