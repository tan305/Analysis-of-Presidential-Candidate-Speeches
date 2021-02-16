
import requests
from bs4 import BeautifulSoup
import pandas as pd
if __name__ == "__main__":

    soup = BeautifulSoup(open('raw21.txt','rb').read(),'html.parser')
    allLines = []
    #Speakers = ["TRUMP", "WALLACE", "BIDEN"]
    Speakers = ["Kamala Harris"," Joe Biden","Speaker 1","Speaker 2","Speaker 3","Speaker 4","Speaker 5","Speaker 6","Speaker 7","Speaker 8" ]
    mainPage = soup.find(id='articlebody')
    for eachLine in mainPage.find_all('p'):
        allLines.append(eachLine.get_text())

    idx = 0
    completeData = []
    i = 0
    speaker = None
    prevSpeaker = None
    for line in allLines:
        line = line.strip()
        for eachSpeaker in Speakers:
            if eachSpeaker == line[0:len(eachSpeaker)]:
                speaker = eachSpeaker
                if prevSpeaker == speaker:
                    speaker = None
                break
        if speaker is not None:
            currentLine = line[len(speaker)+1:].strip()
            completeData.append([speaker,currentLine])
            idx+=1
        else:
            currentLine = line[len(prevSpeaker)+1:].strip()
            completeData[idx-1][1] = completeData[idx-1][1]+currentLine
        if speaker is not None:
            prevSpeaker = speaker
            speaker = None


    pd.DataFrame(completeData,columns=["speaker","text"]).to_csv("biden_speech_covid19-governers.txt",index=False)
