from urllib.request import urlopen
from bs4 import BeautifulSoup
import docx
import any-other-docx-html-packages

def docx_text_extractor(docx_path str) -> str:
  """
  Returns the text extracted from docx file
  """
  
  file = docx_reader(docx_path)
  docx_text = docx_extractor(file)
  parsed_text = docx_parser(docx_text)

  return parsed_text


def docx_reader(file_path: str) -> object:
  """
  Reads docx files and returns an object where
  the text can be extracted
  """
  ...


def docx_extractor(file_path: object) -> str:
  """
  Extracts text from docx
  """
  ...
  

def docx_parser(file_path: object) -> str:
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
  

