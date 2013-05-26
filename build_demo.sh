#!/bin/sh

command -v kaylee-admin.py >/dev/null 2>&1 || { echo >&2 "I require Kaylee, but it's not installed.  Aborting."; exit 1; }

# start Kaylee environment
kaylee-admin.py startenv demo_env || exit 1;

# copy the projects to the environment
cp -r src/* demo_env

# build the projects
cd demo_env
python klmanage.py build || exit 1;
