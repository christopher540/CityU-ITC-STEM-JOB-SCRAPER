from email_auto import send_email
import json
from pypdf import PdfReader 


with open('JSON FILES\may_2 2024\may_2 2024.json','r') as f:
    file=json.load(f)
    for i in range(len(file)):
        d=file[i]
        reader=PdfReader('CV_ELEAZAR Christopher Otniel.pdf')
        CV=reader.pages[0].extract_text()
        company_name=d['company_name']
        job_position=d['job_position']
        job_description=d['job_description']
        email=d['email']
        body=d['cover letter']
        subject=f"{job_position} application at {company_name} (2025 Summer Internship)"
        send_email(email,subject,body)
        
        
        
