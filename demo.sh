#!/bin/sh

command -v kaylee-admin.py >/dev/null 2>&1 || { echo >&2 "I require Kaylee, but it's not installed.  Aborting."; exit 1; }

# start Kaylee environment
kaylee-admin.py startenv demo || exit 1;

# copy the projects to the environment
cp -r src/* demo

# build the projects
cd demo
python klmanage.py build || exit 1;
python klmanage.py run
