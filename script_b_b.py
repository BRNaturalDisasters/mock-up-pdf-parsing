from pdf2image import convert_from_path # sample package
from PIL import Image # sample package
import logging
import script_b_c
import any_other_ocr_packages # placeholder for any other packages considered necessary

logging.basicConfig(filename="log_file_b_b.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

### OCR parsing funcions

def pdf_ocr_recognition(pdf_file_path: str) -> str:
  """
  Extracts text from pdf using ocr
  """

  logging.info(f"starting ocr from file {pdf_file_path}")
  pdf_imgs = split_pdf_into_imgs(pdf_file_path)

  pdf_text = "" # placeholder for parsed text
  img_counter = 0
  for img in pdf_imgs: # extracting and parsing text using ocr
    extracted_text = ocr_img(img)
    parsed_text = script_b_c.ocr_pdf_parser(extracted_text)
    pdf_text += parsed_text
    
    img_counter += 1 # tracking progress of parsing
    logging.info(f"progress {img_counter/len(pdf_imgs)}")
    
  logging.info(f"ocr recognition completed for {pdf_file_path}")
  return pdf_text


def split_pdf_into_imgs(pdf_path: str) -> list:
  """
  Splits pdf into imgs
  """
  ...


def ocr_img(img_file: str) -> str:
  """
  Extracts the text from img
  """
  ...
  

if __name__ == "__main__":
  sample_pdf_path = "User/PDF_paths/path/file.pdf" 
  print("pdf parsed text: ", pdf_ocr_recognition(sample_pdf_path))