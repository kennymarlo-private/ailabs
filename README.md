# ALPHA

Stands for Advanced Language Preprocessor for Human Assistance.
This custom large language model (LLM) aims to provide a more custom data analysis based on private data. It offers the following features:
- Custom mode. Where users can analyze data based on custom model on top of existing base models
- Offline mode. Where users can analyze data privately. 

# Author
@seer - https://www.linkedin.com/in/neil-badayos/

# Inspirations
Inspiration and libraries built with 
- [LangChain](https://github.com/hwchase17/langchain)
- [GPT4All](https://github.com/nomic-ai/gpt4all)
- [LlamaCpp](https://github.com/ggerganov/llama.cpp)
- [Chroma](https://www.trychroma.com/)
- [SentenceTransformers](https://www.sbert.net/)

# Environment Setup
The following steps need to be done before proceeding.

1. Install Python. Currently the developer is using 3.10.x version.
2. Install your favorite IDE

3. Install the dependencies needed on the project 
   ```shell
   pip install requirements.txt
   ```
4. Add our openAI API key on the apikey.py
5. Rename 'example.env' to '.env'
6. Download the model - https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin and add it on 'models' directory
7. Prepare the test data. This is a pre-requisite when using both custom and offline mode.
   For offline mode, use the following command
   ```shell
   python train_offline_data.py
   ```
8. Run the application
   ```shell
   streamlit run app.py
   ```

## Sample usage of the app

- Asking context using custom text
   ```shell
   Prompt : From custom text who is the hero?
- Asking context using custom data
   ```shell
   Prompt : From custom data who are living in China?
   ```
- Asking completely offline
   ```shell
   Prompt : From custom text what is the story all about?
   ```
## Instructions for training your own dataset offline

Add your files into the `data` directory
The supported extensions are:
   - `.csv`: CSV,
   - `.docx`: Word Document,
   - `.enex`: EverNote,
   - `.eml`: Email,
   - `.epub`: EPub,
   - `.html`: HTML File,
   - `.md`: Markdown,
   - `.msg`: Outlook Message,
   - `.odt`: Open Document Text,
   - `.pdf`: Portable Document Format (PDF),
   - `.pptx` : PowerPoint Document,
   - `.txt`: Text file (UTF-8),

# System Requirements

## Python Version
To use this software, you must have Python 3.10 or later installed. Earlier versions of Python will not compile.

## C++ Compiler
If you encounter an error while building a wheel during the `pip install` process, you may need to install a C++ compiler on your computer.

The author uses Arch Linux and was able to install C++ errors by doing the following steps
1. Install the 'linux-api-headers' package
   ```shell
   sudo pacman -S linux-api-headers
   ```
2. Update the 'C_INCLUDE_PATH' environment variable
   ```shell
   export C_INCLUDE_PATH="usr/include:/usr/include/linux"
3. Clean the build
   ```shell
   make clean
   ```
4. Rebuild HNSWLIB
   ```shell
   make
   ```
# Improvements

# Upcoming features

Version 2.0 - May 27, 2023
- Text to Speech feature 
- Speech to Text feature
- Integration with FAST API for headless integration


# Disclaimer
This project is still on development phase and should not be used on production. Any misuse of the codes or referencing shall not be responsiblity of the author. Please consider subscribing to profile.