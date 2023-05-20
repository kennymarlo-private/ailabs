# This class enables to load different kinds of data from a directory.
# this class also contains different loaders used in importing files to vectorstore

import os
import glob
from typing import List
from langchain.docstore.document import Document
from langchain.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PDFMinerLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)

class DataLoader:
    LOADER_MAPPING = {
        ".csv": (CSVLoader, {}),
        ".docx": (UnstructuredWordDocumentLoader, {}),
        ".enex": (EverNoteLoader, {}),
        ".eml": (UnstructuredEmailLoader, {}),
        ".epub": (UnstructuredEPubLoader, {}),
        ".html": (UnstructuredHTMLLoader, {}),
        ".md": (UnstructuredMarkdownLoader, {}),
        ".odt": (UnstructuredODTLoader, {}),
        ".pdf": (PDFMinerLoader, {}),
        ".pptx": (UnstructuredPowerPointLoader, {}),
        ".txt": (TextLoader, {"encoding": "utf8"})
    }

    def load_single_document(file_path: str) -> Document:
        ext = "." + file_path.rsplit(".", 1)[-1]
        if ext in LOADER_MAPPING:
            loader_class, loader_args = LOADER_MAPPING[ext]
            loader = loader_class(file_path, **loader_args)
            return loader.load()[0]

        raise ValueError(f"Unsupported file extension '{ext}'")

    def load_documents(source_dir: str) -> List[Document]:
        all_files = []
        for ext in LOADER_MAPPING:
            all_files.extend(
                glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True)
            )
        return [load_single_document(file_path) for file_path in all_files]
            
    def load_data_file(folder_name, filename):
        ext = filename.rsplit(".", 1)[-1]
        current_directory = os.getcwd()
        file_directory = os.path.join(current_directory, folder_name, ext)
        file_path = os.path.join(file_directory, filename)
        if os.path.isfile(file_path):
            return file_path
        else:
            raise FileNotFoundError(f"The file '{filename}' does not exist in the the source folder.")
