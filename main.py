import os
from pypdf import PdfReader 
import pandas as pd

directory = r'C:\Users\chris\OneDrive\Documents\Python Projects\ITC STEM PROFILE BOT\job_post'
profile=[]

def locate_words(text,target):
    text=text.split('\n')
    for sentence in text:
        if target in sentence:
            return sentence

text=''
for name in os.listdir(directory):
    path=os.path.join(directory,name)
    try:
        reader = PdfReader(path)
        # getting a specific page from the pdf file 
        page1 = reader.pages[0] 
        page2=reader.pages[1]

        # extracting text from page 
        text = page1.extract_text()+'\n'+page2.extract_text() 
        company_name=locate_words(text,'Company Name').removeprefix('Company Name:').strip()
        position=locate_words(text,'Position').removeprefix('Position/Title:').strip()
        Email=locate_words(text,'Email to').removeprefix('Email to').strip()
        temp={}
        temp['Company Name']=company_name
        temp['Position']=position
        temp['Email']=Email
        profile.append(temp)
    except:
        pass

df=pd.DataFrame(profile)
print(df)
df.to_excel('ITC STEM DATA.xlsx')



    


        