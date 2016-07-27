#!/bin/bash
jnlz=$(python *path/to/scraper.py)
echo $jnlz | mail -s "Here are the latest PFA journal issues" "mcq@berkeley.edu"

# here's the crontab format to run this script on the first Wednesday of the month at 9AM 
# (I chose weds since it's the least likely day to be a holiday):
# 0 9 1-7 * 3 * ~/path/to/email.sh