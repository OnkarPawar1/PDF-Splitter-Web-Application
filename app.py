from flask import Flask, request, render_template, send_file
from PyPDF2 import PdfReader, PdfWriter, PageObject
import io
import os

app = Flask(__name__)

def split_pdf(input_pdf_path, output_pdf_path):
    """
    Splits each page of a PDF into two separate pages while preserving layout.
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    overlap = 20  # Overlap in points to prevent content trimming

    for page in reader.pages:
        original_width = float(page.mediabox.right) - float(page.mediabox.left)
        original_height = float(page.mediabox.top) - float(page.mediabox.bottom)

        mid_height = original_height / 2

        # Top half
        top_half = PageObject.create_blank_page(width=original_width, height=mid_height + overlap)
        top_half.merge_page(page)
        top_half.mediabox.upper_left = (float(page.mediabox.left), float(page.mediabox.top))
        top_half.mediabox.lower_left = (float(page.mediabox.left), float(page.mediabox.top) - mid_height - overlap)
        writer.add_page(top_half)

        # Bottom half
        bottom_half = PageObject.create_blank_page(width=original_width, height=mid_height + overlap)
        bottom_half.merge_page(page)
        bottom_half.mediabox.upper_left = (float(page.mediabox.left), float(page.mediabox.top) - mid_height + overlap)
        bottom_half.mediabox.lower_left = (float(page.mediabox.left), float(page.mediabox.bottom))
        writer.add_page(bottom_half)

    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/split', methods=['POST'])
def split_pdf_endpoint():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        input_path = "input.pdf"
        output_path = "output.pdf"
        file.save(input_path)

        try:
            split_pdf(input_path, output_path)
            response = send_file(output_path, as_attachment=True, download_name="split_output.pdf")
            response.direct_passthrough = False
            return response
        except Exception as e:
            return f"An error occurred: {e}", 500
        finally:
            if os.path.exists(input_path):
                os.remove(input_path)
            if os.path.exists(output_path):
                try:
                    os.remove(output_path)
                except PermissionError:
                    pass

if __name__ == "__main__":
    app.run(debug=True)
