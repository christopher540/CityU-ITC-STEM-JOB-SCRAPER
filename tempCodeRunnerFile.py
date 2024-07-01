reader = PdfReader(path) 

    # getting a specific page from the pdf file 
    page = reader.pages[0] 

    # extracting text from page 
    text = page.extract_text() 
    company_name=locate_words(text,'Company Name').removeprefix('Company Name:').strip()
    position=locate_words(text,'Position').removeprefix('Position/Title:').strip()
    Email=locate_words(text,'Email to').removeprefix('Email to').strip()
    temp={}
    temp['Company Name']=company_name
    temp['Position']=position
    temp['Email']=Email
    profile.append(temp)