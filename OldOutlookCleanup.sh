#!/bin/bash
consoleUser=$(/usr/bin/stat -f %Su '/dev/console')
homeDir=$(/usr/bin/dscl . -read "/Users/${consoleUser}" NFSHomeDirectory | /usr/bin/awk -F ': ' '{print $2}')
startDir="${homeDir}/Documents/Microsoft User Data/Office 2011 Identities/"
oldDatabases+=$(/usr/bin/find "${startDir}" -name "Database" -type f -mtime +4300 | cut -c 2-)
for eachDatabase in "${oldDatabases[@]}"; do
	echo "Removing $eachDatabase"
#	rm -Rfv "${startDir}/${eachDatabase}"
done
exit 0