import os

import config

def get_files_path(directory):
  initDB_path = os.path.join(directory, f'initDB.{config.FILE_TYPE}')

  model_paths = []

  model_dir = os.path.join(directory, "model")

  for root, _, files in os.walk(model_dir):
    for file in files:
        file_path = os.path.join(root, file)
        model_paths.append(file_path)


  return initDB_path, model_paths