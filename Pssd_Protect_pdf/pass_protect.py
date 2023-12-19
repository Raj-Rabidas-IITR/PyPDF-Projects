import PyPDF2

def encrypt_and_password_protect(input_path, output_path, password):
    with open(input_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add all pages from the original PDF
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Set encryption options
        pdf_writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    # Replace 'input.pdf', 'output_encrypted.pdf', and 'your_password' with your file paths and desired password
    input_pdf_path = 'mdg.pdf'
    output_pdf_path = 'output_encrypted.pdf'
    password = 'PSSD'

    encrypt_and_password_protect(input_pdf_path, output_pdf_path, password)

    print(f'Encryption and password protection complete. Encrypted PDF saved to: {output_pdf_path}')
