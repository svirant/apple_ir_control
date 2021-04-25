#!/bin/bash
if mpc status | grep -q "paused"; then
#  echo "It's paused"
  mpc toggle -q
elif mpc status | grep -q "playing"; then
#  echo "It's Playing"
  mpc toggle -q
else
#  echo "It's stopped"
  sudo /home/pi/hub-ctrl -h 1 -P 2 -p 1
  sleep 1
  amixer -c 2 cset numid=3 127
  mpc toggle -q
fi
