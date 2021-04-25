#!/bin/bash
amixer -c 2 cset numid=3 $[$(amixer -c 2 cget numid=3|grep -Po ': values=\K[A-Za-z0-9]*')-2]
