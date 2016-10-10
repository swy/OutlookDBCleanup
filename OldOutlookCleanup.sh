#!/bin/bash
consoleUser=$(/usr/bin/stat -f %Su '/dev/console')
homeDir=$(/usr/bin/dscl . -read "/Users/${consoleUser}" NFSHomeDirectory | /usr/bin/awk -F ': ' '{print $2}')
startDir="${homeDir}/Documents/Microsoft User Data/Office 2011 Identities"

echo "Starting directory is $startDir"

oldDatabases+=$(/usr/bin/find "${startDir}" -name "Database" -type f -mtime -3 | cut -c 2- | rev | cut -d '/' -f 2 | rev)
for eachDatabase in "${oldDatabases}"; do
	echo "This will remove ${startDir}/${eachDatabase}"
#	rm -Rfv "${startDir}/${eachDatabase}"
done
exit 0