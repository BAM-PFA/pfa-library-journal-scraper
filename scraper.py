import requests, datetime, smtplib
from bs4 import BeautifulSoup

# titles: Cinemascope, Sight & Sound, Film Comment, Film Quarterly,
# Film History, Cineaste [cancelled? not included here] Journal of Film Preservation

bigList = []
today = datetime.date.today()

sightRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tsight+and+sound/tsight+and+sound/1,2,13,B/crC1764132&FF=tsight+and+sound&8,,9")
ss = sightRaw.content
sightSoup = BeautifulSoup(ss, "lxml")
sightIssues = sightSoup.find_all("td", "checkinArrived")
sightList = []
# the for loop looks in the last box on the "Latest received" page for each title
for i in sightIssues[-1]:
    lines = str(i)
    sightList.append(lines.strip())
    
bigList.append("Sight and Sound: "+str(sightList[0])+" Volume "+str(sightList[8]))

scopeRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tcinemascope/tcinemascope/1,3,3,B/crC1740108&FF=tcinemascope&1,1,")
cs = scopeRaw.content
scopeSoup = BeautifulSoup(cs, "lxml")
scopeIssues = scopeSoup.find_all("td", "checkinArrived")
scopeList = []
for i in scopeIssues[-1]:
    lines = str(i)
    scopeList.append(lines.strip())
    
bigList.append("Cinemascope: "+str(scopeList[0])+" Volume "+str(scopeList[8]))

commentRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tfilm+comment/tfilm+comment/1,1,2,B/crC1742200&FF=tfilm+comment&1,,2")
fc = commentRaw.content
commSoup = BeautifulSoup(fc, "lxml")
commIssues = commSoup.find_all("td", "checkinArrived")
commList = []
for i in commIssues[-1]:
    lines = str(i)
    commList.append(lines.strip())
    
bigList.append("Film Comment: "+str(commList[0])+" Volume "+str(commList[8]))

histRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tfilm+history/tfilm+history/1,4,4,B/crC1996133&FF=tfilm+history&1,1,")
fh = histRaw.content
histSoup = BeautifulSoup(fh, "lxml")
histIssues = histSoup.find_all("td", "checkinArrived")
histList = []
for i in histIssues[-1]:
    lines = str(i)
    histList.append(lines.strip())
    
bigList.append("Film History: "+str(histList[0])+" Volume "+str(histList[8]))

quartRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tfilm+quarterly/tfilm+quarterly/1,2,3,B/crC1601308&FF=tfilm+quarterly&1,,2")
fq = quartRaw.content
quartSoup = BeautifulSoup(fq, "lxml")
quartIssues = quartSoup.find_all("td", "checkinArrived")
quartList = []
for i in quartIssues[-1]:
    lines = str(i)
    quartList.append(lines.strip())
    
bigList.append("Film Quarterly: "+str(quartList[0])+" Volume "+str(quartList[8]))

presRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tjournal+of+film+pres/tjournal+of+film+pres/1,1,1,B/crC2284190&FF=tjournal+of+film+pres&1,1,")
fp = presRaw.content
presSoup = BeautifulSoup(fp, "lxml")
presIssues = presSoup.find_all("td", "checkinArrived")
presList = []
for i in presIssues[-1]:
    lines = str(i)
    presList.append(lines.strip())
    
bigList.append("Journal of Film Preservation: "+str(presList[0])+" Volume "+str(presList[8]))

output = ("As of "+str(today)+" these are the latest issues of periodicals received in the library:"+"\n\n"+("\n".join(bigList)))

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

sendemail(from_addr    = "pfalibraryjournals@gmail.com", 
          to_addr_list = ["mcq@berkeley.edu","aharris@berkeley.edu"],
          cc_addr_list = [], 
          subject      = "OK now it works...", 
          message      = output,
          login        = "pfalibraryjournals",
          password     = "PASSWORD")