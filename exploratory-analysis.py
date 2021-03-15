import nltk
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt


adj=[]
verbs=[]
nouns=[]
def process(sentence):
    words=sentence.split()
    taggedData=nltk.pos_tag(words)
    for w in taggedData:
        if w[1] == "JJ" or w[1] == "JJR" or w[1] == "JJS":
            adj.append(w[0])
        elif  w[1]=='VB':
            verbs.append(w[0])
        elif  w[1]=='NN' or w[1]=="NNS" or w[1] == "NNP" or w[1]=="NNP" or w[1]=="NNPS":
            nouns.append(w[0])


if __name__== "__main__":
    file = open("trump.txt", "r", encoding='utf-8')
    # Reading file and data preprocessing and cleaning - removing punctuation marks, non alphabetical characters.
    for line in file:
        process(line)
    new_adj=[w for w in verbs if len(w) > 4]
    word_could_dict = Counter(new_adj)
    wordcloud = WordCloud(width=1000, height=500).generate_from_frequencies(word_could_dict)

    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    #plt.show()
    plt.savefig('trump-verbs.png', bbox_inches='tight')
    plt.close()
