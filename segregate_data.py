import pandas as pd

df=pd.read_csv("Biden/filen_to_be_read.txt")
print(df)
biden = df[df['speaker'].str.match('Joe Biden')]['text']
wfd = open("filename_to_be_saved.txt","w",encoding="utf-8")
for i in range(len(biden)):
    wfd.write(biden.iloc[i].strip())
wfd.write("\n")

'''
#If there is only one statement in the data
#the for loop is not required
wfd.write(df.iloc[0].text.strip())
wfd.write("\n")
'''