import zipfile
import os
import re
from collections import Counter


#Giải nén toàn bộ file .zip
def extract_zip(file_path, extract_to='.'):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


#Đọc nội dung tất cả các file .txt và tách từ
def read_and_count_words_in_txt_files(folder_path):
    delimiters = r'[ .,!=+\-]+'  # Các dấu phân cách từ
    word_counts = Counter()

    # Duyệt qua tất cả các file trong thư mục
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    words = re.split(delimiters, content)
                    words = list(filter(None, words))
                    word_counts.update(words)

    return word_counts


#Ghi kết quả vào file output 2.txt
def write_word_counts_to_file(word_counts, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for word, count in word_counts.items():
            file.write(f'{word}: {count}\n')


# Hàm chính
def main():
    zip_file_path = r'D:\DE\Test\input 2.zip'  # Đường dẫn tới file zip
    extract_folder = 'input 2'  # Thư mục lưu file sau khi giải nén
    output_file_path = 'output 2.txt'  # File kết quả

    #Giải nén file
    extract_zip(zip_file_path, extract_folder)

    #Đếm từ trong tất cả các file .txt sau khi giải nén
    word_counts = read_and_count_words_in_txt_files(extract_folder)

    #Ghi kết quả ra file
    write_word_counts_to_file(word_counts, output_file_path)
    print(f"Đã ghi kết quả vào file {output_file_path}")


# Chạy chương trình
if __name__ == '__main__':
    main()
