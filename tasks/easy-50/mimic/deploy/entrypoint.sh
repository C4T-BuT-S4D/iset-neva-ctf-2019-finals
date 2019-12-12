#!/bin/sh

gunicorn --workers=5 --bind 0.0.0.0:5005 server:app