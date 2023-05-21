# This class enables to load different kinds of data from a directory.
import os

class DataLoader:
         
    def load_data_file(folder_name, filename):
        ext = filename.rsplit(".", 1)[-1]
        current_directory = os.getcwd()
        file_directory = os.path.join(current_directory, folder_name, ext)
        file_path = os.path.join(file_directory, filename)
        if os.path.isfile(file_path):
            return file_path
        else:
            raise FileNotFoundError(f"The file '{filename}' does not exist in the the source folder.")
