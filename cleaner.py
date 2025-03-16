import re
from pathlib import Path
import os

def clean_text(filename, folder_path = ""):
    with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
        book_text = file.read()

    cleaned_text = re.sub(r'\n+', ' ', book_text) # 줄바꿈을 빈칸으로 변경
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text) # 여러 빈칸을 하나의 빈칸으로

    print("cleaned_" + filename, len(cleaned_text), "characters") # 글자 수 출력

    with open("cleaned_" + filename, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

# filenames_list = ["02 Harry Potter and the Chamber of Secrets.txt"]

# for filename in filenames_list:
#     clean_text(filename)

def read_folder(folder_path):
    path = Path(folder_path)
    file_list = [f.name for f in path.iterdir() if f.is_file()]

    for file in file_list:
        clean_text(file, folder_path)

read_folder('archive')
