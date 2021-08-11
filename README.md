## Problem Statement
 
The aim of this project is to analyze the text from presidential speeches, debates and 
interviews. The analysis will help in understanding the patterns and similarities that exist 
between the candidates, the topics that they concentrate on, the morality values they project. 
All these factors will influence and/or persuade people to choose between the two candidates. 
The content analysis will also help us to visualize the political framework that would be 
offered by the candidate and will help in better decision making while voting.

## Dataset 
 
We have collected data of presidential candidates debates, speeches and interviews over the 6 
months period from June 2020 to November 2020. The data is extracted by parsing the html 
content available from a webpage containing the textual transcripts. The website contains the 
different speakers involved - presidential candidates, a moderator , audience and other people 
and the time frame of each speaker’s speech.

Data cleaning is done by removing html tags, punctuations, time frames, numbers. Since the 
data is continuous speech. Every speaker's speech is extracted from the web page and added 
to that speaker. The cleaned data is then converted to a csv file that contains the 
speaker and his respective speech for that instance.

In total we have collected 50 different textual content for Joe biden - from debates, rally 
speeches, news interviews etc that cover different topics such as health care, education, jobs 
etc and similarly we have collected 50 different textual content for Donald Trump on 
similar topics for the period June 2020 to November 2020.
 
 
## Types of analysis performed
 
* Exploratory data analysis
* Sentiment Analysis
* Morality detection
* Topic modelling 


## Conclusion

* From the exploratory analysis we found that some words were similar between both the candidates while other words were specific to 
that speaker. The word clouds representing the top adjectives, nouns, verbs and pronouns 
have been depicted in the report. 
* Determining the political polarization is an important aspect 
that will set the political framework and will determine the structural framework of 
governing. Understanding the sentiments thus plays a major role. Thus finding the polarity of 
the sentiments was important. 
* From the results of the sentimental analysis, we found that the 
negative sentiment was higher than the positive sentiment. On determining the subjectivity of 
it was observed that Trump had more number of sentences corresponding to low subjectivity 
scre while Biden had more number of sentences corresponding to a high subjectivity 
score. 
* Another way of determining political polarization was by determining the morality 
polarity of the candidates. Since moral judgements play a fundamental role in decision 
making. The results were interesting since the ratio of negative to positive was high for both 
the candidates. The Negative ratio of Trump was higher than Biden and followed the same 
pattern exhibited by sentiments. 
* Finding the frequency distribution for the morality words categorically defined our analysis further. 
Although both the candidates showed similarity in Loyalty, they differed in values such as 
Care and Authority. It was observed that Trump had higher inclination towards the negative 
morality categories such as Harm, degradation than Biden. One reason behind this could be 
that Trump focused more on justifying the decline of the economy caused by the pandemic. 

 
## Future scope
In future this project can be extended to include people’s reactions to debates,speeches and 
interviews, this can help us to understand the influence and persuasion of the candidates. In 
addition we can make use of a larger dataset that contains all the presidential candidates from 
10 years. This data can be further utilized to find the moral rhetoric, to understand the 
change in views towards topics over time. For example the views towards “Health care” in 
US has changed over time, this can be studied by understanding the moral rhetoric.

## Notebooks
Data Extraction - getandclean.py
<br>Data Cleaning and Exploratory Data Analysis – DataAnalysis.ipynb, exploratory-analysis.py, exploratory-analysis2.ipnyb
<br>Topic Modelling – TopicModeling.ipynb
<br>Sentiment Analysis – sentiment-analysis.ipynb
<br>Morality Detection - morality-frequency-distribution.ipynb, morality-polarity.ipynb
