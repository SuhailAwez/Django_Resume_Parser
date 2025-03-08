import re
import spacy
from spacy.matcher import Matcher
from pdfminer.high_level import extract_text
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_contact_number_from_resume(text):
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"

def extract_email_from_resume(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"

def extract_skills_from_resume(text, skills_list):
    skills = [skill for skill in skills_list if re.search(r"\b" + re.escape(skill) + r"\b", text, re.IGNORECASE)]
    return skills if skills else ["Not Found"]

def extract_education_from_resume(text):
    pattern = r"(?i)(?:Bsc|B\.Tech|B\.E|M\.Tech|M\.Sc|Ph\.D|Bachelor(?:'s)?|Master(?:'s)?)\s(?:\w+\s)*\w+"
    matches = re.findall(pattern, text)
    return [match.strip() for match in matches] if matches else ["Not Found"]

def extract_name(resume_text):
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)

    patterns = [
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}],  # First and Last Name
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]  # First, Middle, and Last Name
    ]
    
    matcher.add('NAME', patterns)
    
    doc = nlp(resume_text)
    matches = matcher(doc)

    for _, start, end in matches:
        return doc[start:end].text  # Return the first matched name

    return "Not Found"

def process_uploaded_resume(file_path):
    text = extract_text_from_pdf(file_path)
    skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'SQL', 'Tableau']
    
    return {
        "Name": extract_name(text),
        "Contact_Number": extract_contact_number_from_resume(text),
        "Email": extract_email_from_resume(text),
        "Skills": extract_skills_from_resume(text, skills_list),
        "Education": extract_education_from_resume(text)
    }

def upload_resume(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        uploaded_file = request.FILES['resume']
        file_path = default_storage.save(f"uploads/{uploaded_file.name}", uploaded_file)
        results = process_uploaded_resume(default_storage.path(file_path))
        return render(request, 'parser_app/upload_resume.html', {'data': results})
    return render(request, 'parser_app/upload_resume.html')