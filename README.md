# Django Resume Parser
# Django Resume Parser  

## 📌 Overview  
Django Resume Parser is a web-based application that extracts key details from uploaded resumes (PDFs). It processes resumes to retrieve information like **name, contact details, email, skills, and education**, making it easier to analyze and shortlist candidates efficiently.

## 🚀 Features  
✅ Upload PDF resumes  
✅ Extract candidate details (Name, Email, Phone, Skills, Education)  
✅ Display parsed details in a structured format  
✅ User-friendly interface with Django  

## 🛠️ Installation  

### 1️⃣ Clone the Repository  
```bash
git clone git@github.com:SuhailAwez/Django_Resume_Parser.git
cd Django_Resume_Parser

python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

📝 How It Works

    Upload a PDF resume via the web interface.
    The system extracts relevant details using Python libraries.
    Displays extracted information on the screen for review.

🛠️ Tech Stack

    Backend: Django, Python
    Frontend: HTML, CSS, JavaScript
    Parsing Library: PyPDF2 / pdfminer

🤝 Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.
📜 License

This project is licensed under the MIT License.