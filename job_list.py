import os
from pypdf import PdfReader 
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()
key=os.getenv("API_KEY")
client = Groq(api_key=key)

#Add directory
directory = r'job_post\2'
JDs=[]

for name in os.listdir(directory):
    path = os.path.join(directory, name)
    try:
        reader = PdfReader(path)
        text = ''
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text += page.extract_text() + '\n'
        
        completion = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    I have this job post please extract the company name, job position 
                    (if multiple choose 1 which is most suitable for me as a data science student), 
                    job description(including  \nrequirements in the same string), email to submit the application. 
                    compile this in a json format. No need for other response just output the json, 
                    if not found just add None, the key should be exactly company_name,job_position,job_description,email


                    here is the job description: {text}
                    """
                }
            ],
            temperature=1,
            top_p=1,
            stream=False,
            stop=None,
        )

        jd=completion.choices[0].message.content
        jd=jd.split('\n')[1:-2]
        jd=''.join(jd)
        jd=jd.strip()
        if jd[0]!='{':
            jd='{'+jd
        if jd[-1]!='}':
            jd=jd+'}'
        print(jd)
        print()
        jd=json.loads(jd)
        JDs.append(jd)
        print(f'Data Extracted: {name}')

    except Exception as e:
        print(e)
    

with open('JSON FILES\may_2 2024.json', 'w') as json_file:
    json.dump(JDs, json_file, indent=4)  # Use indent for pretty printing
