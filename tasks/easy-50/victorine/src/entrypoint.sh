#!/bin/sh

set -e

cd /app
socat TCP4-LISTEN:1337,reuseaddr,fork EXEC:./server.py