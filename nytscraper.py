from bs4 import BeautifulSoup
import requests
import numpy as np

headers = {
   
}

def scrape():
    #link to nyt and assign position
    response = requests.get('https://www.nytimes.com/puzzles/leaderboards', headers=headers).text
    leaderboard = BeautifulSoup(response, 'html.parser')
    #Scraping
    persons = leaderboard.find_all('div', class_='lbd-score')
    names = [""] * len(persons)
    ranks = [""] * len(persons)
    times = [""] * len(persons)
    for i in range(len(persons)):
        rank = persons[i].find('p', class_= 'lbd-score__rank').text.strip()
        time = persons[i].find('p', class_= 'lbd-score__time')
        name = persons[i].find('p', class_= 'lbd-score__name').text.strip()
        if(rank != "•"):
            #I wasn't getting captured under the 'lbd-score__name' tag so I had to make one for myself
            nameMe = persons[i].find('p', class_= 'lbd-score__name lbd-score__self')
            if(nameMe != None):
                strNameMe = str(nameMe.text.strip())
                name = strNameMe[0:len(strNameMe) - 6]
            #Deal with tie and there is no number next to one's name
            if(rank == ""):
                for pers in persons:
                    otherTime = pers.find('p', class_= 'lbd-score__time')
                    if((otherTime != None) and (otherTime == time)): 
                        otherRank = pers.find('p', class_='lbd-score__rank')
                        if(otherRank != None):
                            otherRank = otherRank.text.strip()
                        if(otherRank != ''):
                            rank = otherRank
        ranks[i] = str(rank)
        names[i] = str(name)
        if(time != None):
            times[i] = str(time.text.strip())
        else:
            times[i] = str("")
    #create CSV
    csv = np.full((len(names) + 1, 4), "                        ")
    csv[0][0] = "Rank"
    csv[0][1] = "Name"
    csv[0][2] = "Time"
    csv[0][3] = "Time in seconds"
    for i in range(len(names)):
        csv[i+1][0] = str(ranks[i])
        csv[i+1][1] = names[i]
        csv[i+1][2] = str(times[i])
        if(str(times[i]) != '--'):
            timeInSeconds = str(times[i]).split(":")
            csv[i+1][3] = str(int(timeInSeconds[0]) * 60 + int(timeInSeconds[1]))
        else:
            csv[i+1][3] = "--"
    a = np.array([names, times, ranks])
    np.savetxt('leaderboard.csv', csv, delimiter=',', fmt='%s')

if __name__=="__main__":
    scrape()