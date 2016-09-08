import requests, datetime, smtplib, collections
from bs4 import BeautifulSoup

# titles: Cinemascope, Sight & Sound, Film Comment, Film Quarterly,
# Film History, Cineaste [cancelled? not included here], Journal of Film Preservation

sightRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tsight+and+sound/tsight+and+sound/1,2,13,B/crC1764132&FF=tsight+and+sound&8,,9")
scopeRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tcinemascope/tcinemascope/1,3,3,B/crC1740108&FF=tcinemascope&1,1,")
commentRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tfilm+comment/tfilm+comment/1,1,2,B/crC1742200&FF=tfilm+comment&1,,2")
histRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tfilm+history/tfilm+history/1,4,4,B/crC1996133&FF=tfilm+history&1,1,")
quartRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tfilm+quarterly/tfilm+quarterly/1,2,3,B/crC1601308&FF=tfilm+quarterly&1,,2")
presRaw = requests.get("http://oskicat.berkeley.edu/search~S43?/tjournal+of+film+pres/tjournal+of+film+pres/1,1,1,B/crC2284190&FF=tjournal+of+film+pres&1,1,")

dictItems = [("Sight and Sound: ",sightRaw),("CinemaScope: ",scopeRaw),("Film Comment: ",commentRaw),
        ("Film History: ",histRaw), ("Film Quarterly: ",quartRaw), ("Journal of Film Preservation: ",presRaw)]
orderedDict = collections.OrderedDict(dictItems)

detailList = []
outList = []
today = datetime.date.today()
readableToday = today.strftime("%B %d, %Y")

def scrape(title):
    content = title.content
    soup = BeautifulSoup(content, "lxml")
    issues = soup.find_all("td", "checkinArrived")
    issueList = []
    for i in issues[-1]:
        lines = str(i)
        issueList.append(lines.strip())
    whatIwant = str(issueList[0])+" Volume "+str(issueList[8])
    detailList.append(whatIwant)

for title in orderedDict.keys():
    scrape(orderedDict[title])

for a in detailList:
    x = [value[1] for value in list(enumerate(orderedDict))]
    y = str(x[detailList.index(a)])+a
    outList.append(y)

output = ("As of "+str(readableToday)+" these are the latest issues of periodicals received in the library:"+"\n\n"+("\n".join(outList)))

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
          to_addr_list = ["NAME@COLLEGE.edu"],
          cc_addr_list = ["MORENAME@COLLEGE.edu"],
          subject      = "Latest Journals Received by PFA Library as of: "+(str(readableToday)),
          message      = output,
          login        = "pfalibraryjournals",
          password     = "PASSWORD")