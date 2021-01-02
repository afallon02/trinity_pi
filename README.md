
# Table of Contents

1.  [Todo](#org5c6a4e5)
    1.  [Create web frontend](#org92bb3b7)
    2.  [Figure out which attacks I need to represent in the front end.](#orgf760390)
    3.  [Create SD image](#org3222cd8)
2.  [Requirements](#org6c811f7)
    1.  [Raspberry Pi.](#orga5fd577)
    2.  [SD card with at least 16GB of space.](#org5dbeab8)
    3.  [Another computer to flash the SD card.](#orgf238bdb)
    4.  [Internet connection.](#org6324528)
    5.  [A compatible network interface card. I used this one.](#org9ebe142)
3.  [Introduction](#org12c7c93)
4.  [Attacks](#orgc3a1ce8)
    1.  [WPA/WPA2 Crack](#org3de0745)
    2.  [Deauthentication](#org1bcfc63)



<a id="org5c6a4e5"></a>

# Todo


<a id="org92bb3b7"></a>

## TODO Create web frontend


<a id="orgf760390"></a>

## TODO Figure out which attacks I need to represent in the front end.


<a id="org3222cd8"></a>

## TODO Create SD image


<a id="org6c811f7"></a>

# Requirements


<a id="orga5fd577"></a>

## Raspberry Pi.


<a id="org5dbeab8"></a>

## SD card with at least 16GB of space.


<a id="orgf238bdb"></a>

## Another computer to flash the SD card.


<a id="org6324528"></a>

## Internet connection.


<a id="org9ebe142"></a>

## A compatible network interface card. I used [this one.](https://www.amazon.co.uk/gp/product/B08D99YLC9/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)


<a id="org12c7c93"></a>

# Introduction

Trinity Pi is an alpine linux based raspberry pi distribution pre-installed with a bunch of tools to enable wifi hacking. These tools are provided to the user via a nice simple web interface.

There are scripts inside *etc/local.d* to enable monitor mode for your device. These are included as the version of airmon-ng bundled with aircrack doesn't seem to work on Alpine Linux.

You can use these like so;

    /etc/local.d/monitor_mode_enable.sh -i wlan1
    /etc/local.d/monitor_mode_disable.sh -i wlan1

You can download the Trinity image [here](<https://example.org>) and flash it to an SD card. Plugging it into a raspberry pi along with a [compatible WiFi dongle](<https://example.org>) will be all you need to do as the scripts start themselves.


<a id="orgc3a1ce8"></a>

# Attacks


<a id="org3de0745"></a>

## WPA/WPA2 Crack

    airodump-ng -c 9 -w psk wlan1


<a id="org1bcfc63"></a>

## Deauthentication

You can use this type of attack to boot a user of a given wireless access point.

