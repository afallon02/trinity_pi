#!/bin/bash
set -e

while getopts i: flag
do
	case "${flag}" in
		i) interface=${OPTARG};;
	esac
done

if [ -z "$WIFI_ADAPTER" ] || [ -z "$WIFI_ADAPTER" ]
then
	exit "No interface specified!"
else
	echo "Enabling managed mode on interface: $WIFI_ADAPTER...";
	ifconfig $WIFI_ADAPTER down;
	iwconfig $WIFI_ADAPTER mode monitor;
	ifconfig $WIFI_ADAPTER up;
	echo "Monitor mode enabled";
fi

