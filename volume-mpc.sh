#!/bin/bash
mpcstatus() {
if mpc status | grep -q "paused"; then
   return 1
elif mpc status | grep -q "playing"; then
   return 1
else
   return 0
fi
}
mpcstatus
