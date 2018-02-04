#!/bin/bash

eval "sudo apt-get update"
eval "sudo apt-get -y install python python-setuptools python-dev build-essential"
eval "sudo easy_install pip"
eval "pip install netcdf4"
