from urllib.request import urlopen
from bs4 import BeautifulSoup
import PyPDF2
import any-other-docx-html-packages

def pdf_text_extractor(docx_path str) -> str:
  """
  Returns the text extracted from docx file
  """
  
  file = pdf_reader(pdf_path)
  pdf_text = pdf_extractor(file)
  parsed_text = pdf_parser(pdf_text)

  return parsed_text


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
  

def pdf_parser(file_path: object) -> str:
  """
  Parses the text extracted from docx
  """
  ...
  

def html_text_extractor(html_path str) -> str:
  """
  Returns the text extracted from html file
  """
  
  file = html_reader(html_path)
  docx_text = html_extractor(file)
  parsed_text = html_parser(html_text)

  return parsed_text


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
  

def html_parser(file_path: object) -> str:
  """
  Parses the text extracted from html
  """
  ...
  

