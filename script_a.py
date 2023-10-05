import script_b_a
import script_b_b
import script_b_c
import logging
import any_additional_packages_required

logging.basicConfig(filename="log_file_a.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

### functions

def multiprocessing_execution(project_function: function, input_data: list) -> None:
  """
  Runs the specified function for each element of input_data
  """
  continous_processing(project_function, input_data)
  ...


def continous_processing(project_funtion: function, input: object) -> None:
  """
  Runs a function continuously even if an error is detected (e.g. PDF is unreadable,
  too much ram is used, etc.)
  """


def main(pdf_path: str, file_name: str):
  """
  Calls all functions required for parsing and
  parses the text using multiprocessing and 
  continuous processing
  """
  ...


if __name__ == "__main__":
  path_to_pds = "PATH/To/PDFs"
  multiprocessing_execution(...)
  ...