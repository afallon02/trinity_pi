#!/bin/bash
set -e

while getopts i: flag
do
	case "${flag}" in
		i) interface=${OPTARG};;
	esac
done

if [ -z "$interface" ] || [ -z "$WIFI_ADAPTER" ]
then
	exit "No interface specified!"
else
	echo "Enabling managed mode on interface: $interface...";
	ifconfig $interface down;
	iwconfig $interface mode managed;
	ifconfig $interface up;
	echo "Attempting to get IP address";
	/etc/init.d/networking restart;
fi

