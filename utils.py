import re
import pdfplumber

def extract_from_pdf(file):
    data = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = text.split("\n")

            for line in lines:
                # Adjust this regex based on your document format
                match = re.search(r"(.*)\s+(\d{4})\s+(CSE|ECE|ME|EEE|CIVIL)\s+(.*)", line)

                if match:
                    college = match.group(1).strip()
                    cet_code = match.group(2)
                    branch = match.group(3)
                    location = match.group(4).strip()

                    data.append({
                        "College Name": college,
                        "CET Code": cet_code,
                        "Branch": branch,
                        "Location/District": location
                    })

    return data
