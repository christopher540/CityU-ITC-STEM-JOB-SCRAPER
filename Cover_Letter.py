from groq import Groq
from dotenv import load_dotenv
import os
from pypdf import PdfReader 
import json

# Cover Letter with AI
# def generate_cover_letter(CV,JD):
#     load_dotenv()
#     key=os.getenv("API_KEY")
#     client = Groq(api_key=key)


#     completion = client.chat.completions.create(
#         model="llama3-70b-8192",
#         messages=[
#             {
#                 "role": "user",
#                 "content": "I want to make a tailored cover letter based on my CV and job description. Highlight my relevant skills, keep the tone professional but conversational"
#             },
#             {
#                 "role": "assistant",
#                 "content": "I'd be happy to help you create a tailored cover letter. To get started, could you please provide me with the following information:\n\n1. Your CV (or a brief summary of your work experience, education, and relevant skills)\n2. The job description for the position you're applying for\n3. Any specific company or industry details you'd like to highlight\n\nWith this information, I'll help you craft a cover letter that:\n\n* Highlights your relevant skills and experience\n* Showcases your enthusiasm for the role and company\n* Uses a professional but conversational tone\n\nPlease share the necessary details, and I'll get started on creating a compelling cover letter for you!\n\n(Also, please let me know if you have any specific preferences, such as a desired length or tone, or if you'd like me to focus on any particular aspect of your experience or skills.)"
#             },
#             {
#                 "role": "user",
#                 "content": f"""
#                     here is my CV: {CV}
#                     and this is the job description: {JD}

#                     STRICTLY ONLY OUTPUT THE COVER LETTER and just start with Dear
#                     I will not be editing any of it so only add information that you know from my CV, 
#                     i do not want this [add your own information] in the cover letter

#                     don't add any links, dont add any information thats not true, use my CV as reference
#                             """
#             }
#         ],
#         temperature=1,
#         top_p=1,
#         stream=False,
#         stop=None,
#     )
#     print(completion.choices[0].message.content)
#     return completion.choices[0].message.content

def generate_cover_letter(company_name,job_position):
    cover_letter = f"Dear Hiring Manager,\n\nI am excited to apply for the {job_position} at {company_name}. As a data science student with hands-on experience in AI development, data analytics, and software engineering, I am eager to bring my technical expertise and problem-solving mindset to your team.\n\nMy experience spans across AI-driven projects and data analytics roles. During my internship at Resume Page Limited, I developed an AI-powered profile chatbot using Llama and MySQL, improving user engagement by 35%. I also engineered a business card scanner with face recognition, streamlining information exchange by 30%. My prior data analyst internship at IESHER involved analyzing World Bank data to identify policy insights, reinforcing my ability to extract meaningful narratives from complex datasets.\n\nBeyond technical expertise, I am passionate about building impactful solutions. My recent smart fridge platform, developed for a hackathon, integrates inventory tracking with AI-powered recipe recommendations and shopping list generation—demonstrating my ability to merge AI with real-world applications. My leadership experience in tutoring and mentoring has further sharpened my communication and collaboration skills.\n\nI am eager to contribute my analytical skills and AI-driven mindset to {company_name}. I would welcome the opportunity to discuss how my experience aligns with your team’s goals. Thank you for your time, and I look forward to your response.\n\nBest regards,\nChristopher Otniel Eleazar"
    return cover_letter


reader=PdfReader('CV_ELEAZAR Christopher Otniel.pdf')
CV=reader.pages[0].extract_text()

job_posts=[]
with open('JSON FILES\may_2 2024\may_2 2024.json','r') as f:
    file=json.load(f)
    for i in range(len(file)):
        d=file[i]
        company_name=d['company_name']
        job_position=d['job_position']
        job_description=d['job_description']
        email=d['email']
        JD=f"""
            company name:{company_name}
            job position:{job_position}
            job description:{job_description}
            email:{email}
            """
        d['cover letter']=generate_cover_letter(company_name,job_position)
        job_posts.append(d)
        print(f'Cover Letter Created: {d['company_name']}')

with open('JSON FILES\may_2 2024\may_2 2024.json','w') as f:
    json.dump(job_posts,f,indent=4)

