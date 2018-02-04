#!/bin/bash

sudo apt-get install git

eval "git clone https://github.com/tnoelcke/AgBizClimate.git"
eval "sudo apt-get update"
eva; sudo apt-get -y install python python-setuptools python-dev buildessential
eval sudo easy_install pip

#pip install netcdf
pip install netcdf4
