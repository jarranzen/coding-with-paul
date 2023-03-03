import os
import PyPDF2

# Path to the directory containing the PDF files
pdf_dir = '/Users/jarranzen/Dropbox/0_Music\Therapy/Articles'

# Path to the directory where the text files will be saved
text_dir = '/Users/jarranzen/Dropbox/0_Music\Therapy/text_files'

# Check if the text directory exists, if not create it
if not os.path.exists(text_dir):
    os.makedirs(text_dir)

# Loop through each PDF file in the directory
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith('.pdf'):
        # Open the PDF file
        pdf = PyPDF2.PdfFileReader(open(os.path.join(pdf_dir, pdf_file), 'rb'))
        
        # Extract the text from each page in the PDF file
        text = ''
        for page in range(pdf.getNumPages()):
            text += pdf.getPage(page).extractText()
        
        # Write the extracted text to a file
        text_file = open(os.path.join(text_dir, pdf_file.replace('.pdf', '.txt')), 'w')
        text_file.write(text)
        text_file.close()
