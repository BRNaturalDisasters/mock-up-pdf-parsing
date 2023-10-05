from urllib.request import urlopen # sample package
from bs4 import BeautifulSoup # sample package
import PyPDF2 # sample package
import logging
import any_other_docx_html_packages # placeholder for any other packages considered necessary

logging.basicConfig(filename="log_file_b_c.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

### parsing funcions

def pdf_parser(file_path: object) -> str:
  """
  Parses the text extracted from pdf
  """
  ...
  

def html_parser(file_path: object) -> str:
  """
  Parses the text extracted from html
  """
  ...


def ocr_pdf_parser(pdf_path: str) -> str:
  """
  Parses the text obtained from applying OCR to pdf
  """
  ...


if __name__ == "__main__":
  sample_pdf_ocr_text = "Te st text for sample project"
  sample_html_ocr_text = "<h>Test</h> project"
  
  pdf_parsed_text = pdf_parser(sample_pdf_ocr_text)
  html_parsed_text = html_parser(sample_html_ocr_text)

  print("pdf parsed text: ", pdf_parsed_text)
  print("html parsed text: ", html_parsed_text)