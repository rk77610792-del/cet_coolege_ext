import pdfplumber
import pandas as pd

def extract_from_pdf(file):
    data = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()

            for table in tables:
                for row in table:
                    if not row:
                        continue

                    row = [str(cell).strip() if cell else "" for cell in row]

                    # Adjust column positions based on your PDF
                    # Try printing row to understand structure
                    print(row)

                    if len(row) >= 4:
                        college = row[0]
                        cet_code = row[1]
                        branch = row[2]
                        location = row[3]

                        # Basic validation
                        if cet_code.isdigit():
                            data.append({
                                "College Name": college,
                                "CET Code": cet_code,
                                "Branch": branch,
                                "Location/District": location
                            })

    return data
