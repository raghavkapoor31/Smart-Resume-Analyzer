import PyPDF2

def parse_resume(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    print(parse_resume("data/sample_resumes/sample_resume.pdf"))
