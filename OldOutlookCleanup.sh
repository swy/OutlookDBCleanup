#!/bin/bash
consoleUser=$(/usr/bin/stat -f %Su '/dev/console')
homeDir=$(/usr/bin/dscl . -read "/Users/${consoleUser}" NFSHomeDirectory | /usr/bin/awk -F ': ' '{print $2}')
startDir="${homeDir}/Documents/Microsoft User Data/Office 2011 Identities"

echo "Starting directory is $startDir"

oldDatabases+=$(/usr/bin/find "${startDir}" -name '*\[Backed up*' -type d)
for matchingDatabase in "${oldDatabases[@]}"; do

	echo "This will remove the following paths: ${matchingDatabase[@]}"
	rm -Rvi  "${matchingDatabase[@]}"
done
exit 0
