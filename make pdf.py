from fpdf import FPDF


# Create a PDF class instance
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=11)

# Cover letter content
cover_letter = """
Dear Hiring Manager at AI Mnemonic Limited,

I am excited to apply for the Data Analyst position at AI Mnemonic Limited, where I can leverage my passion for data science and computer vision to drive innovation in wearable healthtech devices. With a strong academic background in Data Science and a minor in Finance from City University of Hong Kong, I am confident that my skills and experience make me an ideal fit for this role.

As a detail-driven and self-motivated individual, I have developed a solid foundation in programming languages such as Python, C++, and SQL, with a strong proficiency in data analysis libraries like NumPy, Pandas, and Matplotlib. My experience in converting Matlab algorithms to Python code has also equipped me with the ability to work efficiently with different programming languages. I am excited about the opportunity to work with your product and software development teams to develop analytic algorithms and ensure the timely delivery of high-quality data analysis.

My experience as a CityU PALSI Leader and CityU Programming Clinic Tutor has given me a unique ability to break down complex concepts into simple, actionable insights. I have a proven track record of enhancing student understanding and confidence in programming concepts, with an 85% increase in student confidence reported during my tutoring sessions. I am confident that my strong communication skills and ability to work effectively with cross-functional teams will enable me to make a significant impact at AI Mnemonic Limited.

I am particularly drawn to AI Mnemonic Limited's innovative approach to wearable healthtech devices and the company's commitment to delivering high-quality products that improve people's lives. As someone who is passionate about computer vision and data science, I am excited about the opportunity to work on projects that involve analyzing data from wearable devices and developing algorithms that can drive meaningful insights.

In addition to my technical skills and experience, I possess excellent communication and interpersonal skills, with the ability to work effectively in a team environment. My experience as a Marketing Manager for TEDxCityUHongKong has also given me a unique understanding of the importance of effective communication and project management in driving business outcomes.

Thank you for considering my application. I am excited about the opportunity to discuss my qualifications further and learn more about the Data Analyst role at AI Mnemonic Limited. Please feel free to contact me at coeleazar2-c@my.cityu.edu.hk or (852) 6105 1375.

Sincerely,
Christopher Otniel Eleazar
"""

# Add the text to the PDF
pdf.multi_cell(0, 4.5, cover_letter)

# Save the PDF to a file
pdf.output("cover_letter.pdf")

print("Cover letter PDF created successfully!")