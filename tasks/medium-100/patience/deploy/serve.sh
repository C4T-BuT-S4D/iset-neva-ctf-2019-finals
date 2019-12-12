#!/bin/sh

while true; do socat TCP4-LISTEN:31337,reuseaddr,fork,keepalive exec:./patience; sleep 3; done