# PDF Splitter Web Application

## Overview

The **PDF Splitter Web App** is a Flask-based web application designed to split each page of a PDF into two separate pages. It ensures the layout and content are preserved during the splitting process. This tool is especially useful for resizing and reformatting PDFs for specific aspect ratios, such as splitting into 16:9 layouts.

## Features

- Splits each page of a PDF into two separate halves.
- Maintains original content alignment and layout.
- Prevents content loss by adding overlapping regions between split parts.
- Simple and intuitive file upload and download interface.

## Technology Stack

- **Python**: Programming language used for backend processing.
- **Flask**: Web framework for handling the application logic.
- **PyPDF2**: Library for manipulating PDF files.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.7+
- pip (Python package manager)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pdf_splitter.git
   cd pdf_splitter
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

## Directory Structure

```
pdf_splitter/
│
├── app.py                   # Main Flask application file
├── templates/
│   └── upload.html          # HTML template for file upload
├── static/                  # (Optional) For static files like CSS/JS
├── requirements.txt         # List of dependencies
└── README.md                # Documentation file
```

## Usage

### 1. Access the Application

Once the application is running, access it through your browser at `http://127.0.0.1:5000/`.

### 2. Upload a PDF

- Use the upload form on the homepage to select and upload a PDF file.
- Ensure the uploaded PDF is properly formatted for splitting.

### 3. Split and Download

- Once the file is uploaded, the app processes the PDF by splitting each page into two halves.
- The split PDF is automatically downloaded to your system as `split_output.pdf`.

## Code Details

### `split_pdf` Function

This function is responsible for splitting each page of the uploaded PDF into two halves:

- It calculates the midpoint of each page.
- Creates a **top half** and a **bottom half** for each page using `mediabox` dimensions.
- Prevents trimming by adding a slight overlap between the two halves.

### Flask Endpoints

1. `/`: Renders the upload form.
2. `/split`: Handles the file upload, splits the PDF, and provides the download link.

## Error Handling

The application handles various errors gracefully:

- Missing or incorrect file uploads.
- Permission errors during file access.
- Unsupported or corrupted PDF files.

## Dependencies

- **Flask**: Framework for creating the web application.
- **PyPDF2**: Library for PDF processing and manipulation.

### Installation

The dependencies are listed in the `requirements.txt` file:

```plaintext
Flask
PyPDF2
```

Install them using:

```bash
pip install -r requirements.txt
```

## Limitations

- This app processes each page individually; very large PDFs may take longer to process.
- It assumes that all pages in the PDF have similar dimensions.

## Future Enhancements

- Add support for other aspect ratios.
- Optimize performance for large PDF files.
- Enable batch processing of multiple PDFs.

## Contribution

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-branch
   ```
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
