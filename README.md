# BAMPFA Library Journal Holdings Webscraper
This is a Python script to check Oskicat.berkeley.edu for the latest issues received of film-related journal titles that the BAMPFA Film Library actively subscribes to, and email the info to interested staff members.

## Intended usage
This is supposed to help film curators keep up to date on the latest film journals that are in the library. 

The script uses a dummy gmail account that was created for this purpose. We could also use a bash script to run the scrape and ```mail``` the output to users (I've included a sample shell script here that has a comment with the crontab format to use). 

Ideally this will be run on the first (Wednesday?) of the month via a cron job on a BAMPFA-owned/managed/used server. If it runs on a Wednesday, it's more likely to be seen by the curators since the 1st of a month might be on a weekend or, like Monday or Tuesday, often falls on a holiday.

## Sample output:

The output is plain text that reads like this:

>As of 2016-07-26 these are the latest issues of periodicals received in the library:  
>
>Sight and Sound: Aug 2016 Volume 26:8  
>Cinemascope: Sum 2016 Volume 67  
>Film Comment: Jul-Aug 2016 Volume 52:4  
>Film History: 2015 Volume 27:4  
>Film Quarterly: Sum 2016 Volume 69:4  
>Journal of Film Preservation: Oct 1, 2015 Volume 93