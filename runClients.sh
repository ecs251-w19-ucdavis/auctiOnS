#!/usr/bin/env bash
python Client.py -u Daniel -b 1500 -a localhost:3001
user = 'User'
for i in $(seq 1 $1)
    python Client.py -u "$user$i" -b 1500 -a localhost:3001 &


