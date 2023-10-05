from urllib.request import urlopen # sample package
from bs4 import BeautifulSoup # sample package
import PyPDF2 # sample package
import logging
import script_b_c
import any_other_docx_html_packages # placeholder for any other packages considered necessary

logging.basicConfig(filename="log_file_b_a.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

### PDF parsing funcions

def pdf_text_extractor(pdf_path: str) -> str:
  """
  Returns the text extracted from docx file
  """
  
  logging.info(f"reading file {pdf_path}")
  file = pdf_reader(pdf_path)
  logging.info(f"extracting text from file {pdf_path}")
  pdf_text = pdf_extractor(file)
  
  logging.info(f"parsing started for file {pdf_path}")
  try:
    parsed_text = script_b_c.pdf_parser(pdf_text)
    return parsed_text
  except Exception as excep:
    logging.info(f"parsing started for file {pdf_path}")
    return f"ERROR: parsing failed. {excep}"


def pdf_reader(file_path: str) -> object:
  """
  Reads a pdf file and returns an object where
  the text can be extracted
  """
  ...


def pdf_extractor(file_path: object) -> str:
  """
  Extracts text from pdf
  """
  ...
  

### HTML parsing functions

def pdf_text_extractor(html_path: str) -> str:
  """
  Returns the text extracted from docx file
  """
  
  logging.info(f"reading file {html_path}")
  file = html_reader(html_path)
  logging.info(f"extracting text from file {html_path}")
  html_text = html_extractor(file)
  
  logging.info(f"parsing started for file {html_path}")
  try:
    parsed_text = script_b_c.html_parser(html_text)
    return parsed_text
  except Exception as excep:
    logging.info(f"parsing started for file {html_path}")
    return f"ERROR: parsing failed. {excep}"


def html_reader(file_path: str) -> object:
  """
  Reads html files and returns an object where
  the text can be extracted
  """
  ...


def html_extractor(file_path: object) -> str:
  """
  Extracts text from html
  """
  ...
  

if __name__ == "__main__":
  sample_pdf_path = "User/PDF_paths/path/file.pdf"
  sample_html_path = "User/PDF_paths/path/file.html"
  
  pdf_parsed_text = pdf_text_extractor(sample_pdf_path)
  html_parsed_text = pdf_text_extractor(sample_html_path)

  print("pdf parsed text: ", pdf_parsed_text)
  print("html parsed text: ", html_parsed_text)