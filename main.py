from functions.get_files_path import get_files_path
from functions.get_data_from_files import get_data_from_files
from functions.convert_data import convert_data
# import save_data

import config

initDB_path, model_paths = get_files_path(config.FOLDER_PATH)

db_connections, models = get_data_from_files(initDB_path, model_paths)

string = convert_data(db_connections, models)

output_file_path = "output.txt"  # Specify the output file name

with open(output_file_path, "w", encoding="utf-8") as file:
    for table in string:
      file.write(table)
      file.write("\n")