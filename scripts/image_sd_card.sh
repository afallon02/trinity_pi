
#!/bin/bash
set -e

while getopts d:l: flag
do
	case "${flag}" in
		d) drive=${OPTARG};;
		l) location=${OPTARG};;
	esac
done

if [ -z "$drive" ]
then
	exit "No SD card specified!";
elif [ -z "$location" ]
then
	exit "No location specified";
else
	echo "Unmounting $drive...";
	sudo umount $drive;
	echo "Beginning clone of $drive to $location";
fi

