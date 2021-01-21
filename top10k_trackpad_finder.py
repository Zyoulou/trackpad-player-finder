import requests
from bs4 import BeautifulSoup
import re
from time import sleep

i = 1
performanceList = []
while i <= 200:
    url = 'https://osu.ppy.sh/rankings/osu/performance?page='+str(i)+'#scores'
    res = requests.get(url)
    if res.ok:
        sleep(1)
        performanceList.append(res)
    else:
        print("error")
    i = i + 1

print('Performance list page done.')
listLink = []
for v in performanceList:
    listA = []

    soup = BeautifulSoup(v.text, 'lxml')
    table = soup.findAll('table')
    for td in table:
        a = td.findAll('a', {"class":"ranking-page-table__user-link-text js-usercard"})
        listA.append(a)


    j = 0
    for v in listA[j]:
        listLink.append(v['href'])
        j = j + 1

print('osu profile links done.')

KeywordList = ['Trackpad', 'trackpad', 'Touchpad', 'touchpad',
                'TrackPad', 'trackPad','TouchPad', 'touchPad',]
q = 0
trackpadPlayers = []
for v in listLink:
    url = v
    res = requests.get(url)
    sleep(1)
    if res.ok:
        soup = BeautifulSoup(res.text, 'lxml')
        isPresent = False
        for k in KeywordList:
            is_present = bool(re.search(k, res.text))
            if is_present == True:
                print(v, 'profile mention trackpad!')
                trackpadPlayers.append(v)
                break
        if isPresent == False:
            print(f"{v:38}| no")
    else:
        print("error")
    q = q + 1


print('trackpad players :',trackpadPlayers)
