#!/bin/bash

virtualenv -p /opt/homebrew/bin/python3.9 venv

source venv/bin/activate

pip3 install -r requirements.txt

echo "" >> .env