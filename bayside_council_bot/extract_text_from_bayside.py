import os
import pdfplumber

# Folders
pdf_folder = "bayside_minutes"
text_folder = "bayside_minutes_text"
os.makedirs(text_folder, exist_ok=True)

# Loop through PDFs and extract text
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        txt_path = os.path.join(text_folder, filename.replace(".pdf", ".txt"))

        if not os.path.exists(txt_path):  # Only process new ones
            print(f"Extracting: {filename}")
            full_text = ""

            try:
                with pdfplumber.open(pdf_path) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            full_text += text + "\n\n"

                # Save extracted text
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(full_text)

            except Exception as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Already extracted: {filename}")
