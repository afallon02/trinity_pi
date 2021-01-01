#!/bin/bash

show_interfaces() {
	hwinfo --network --short
}

show_interfaces
