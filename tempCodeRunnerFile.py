from email_auto import send_email
from Cover_Letter import generate_cover_letter
import json
from pypdf import PdfReader 


with open('job_posts.json','r') as f:
    d=json.load(f)
    print(d)