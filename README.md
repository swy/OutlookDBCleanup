# OutlookDBCleanup
Outlook 2011 rebuilds leave a history of $profile_name [Backed up $datestamp] folders in the
~/Documents/Microsoft User Data/Office 2011 Identities path.  This sorts through every folder with "Identity" in the name,
identifies the newest Database file (by date stamp), and removes every other folder with the term "Identity" in it.

As the default naming convention is "Main Identity", this will purge any "Main Identity [Backed up $datestamp] folders
other than the one with the most recently modified Database date.  It will not touch any folders not matching the
*Identity* naming convention.
