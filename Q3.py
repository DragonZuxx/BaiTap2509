import zipfile
import os
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed


#Giải nén file .zip
def extract_zip(file_path, extract_to='.'):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


#Đếm từ trong file .txt
def count_words_in_file(file_path):
    delimiters = r'[ .,!=+\-]+'
    word_counts = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as f:
            content = f.read().lower()

    words = re.split(delimiters, content)
    words = list(filter(None, words))
    word_counts.update(words)

    return word_counts


#Tìm top 10 từ xuất hiện nhiều nhất và ít nhất
def get_top_words(word_counts):
    total_counts = sum(word_counts.values())
    top_10_most_common = word_counts.most_common(10)
    top_10_least_common = [item for item in word_counts.items() if item[1] > 0]
    top_10_least_common.sort(key=lambda x: x[1])
    top_10_least_common = top_10_least_common[:10]

    return top_10_most_common, top_10_least_common


#Ghi kết quả vào file output 3.txt
def write_results_to_file(top_most_common, top_least_common, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("Top 10 từ xuất hiện nhiều nhất:\n")
        for word, count in top_most_common:
            file.write(f'{word}: {count}\n')

        file.write("\nTop 10 từ xuất hiện ít nhất:\n")
        for word, count in top_least_common:
            file.write(f'{word}: {count}\n')


#Hàm chính
def main():
    zip_file_path = r'D:\DE\Test\input 3.zip'
    extract_folder = 'input 3'
    output_file_path = 'output 3.txt'

    #Giải nén file
    extract_zip(zip_file_path, extract_folder)

    #Lấy danh sách tất cả các file .txt trong thư mục
    txt_files = [os.path.join(root, file)
                 for root, dirs, files in os.walk(extract_folder)
                 for file in files if file.endswith('.txt')]

    #Đếm từ sử dụng đa luồng
    word_counts = Counter()

    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_file = {executor.submit(count_words_in_file, file): file for file in txt_files}

        for future in as_completed(future_to_file):
            file = future_to_file[future]
            try:
                count = future.result()
                word_counts.update(count)
            except Exception as e:
                print(f'File {file} gặp lỗi: {e}')

    #Tìm top 10 từ xuất hiện nhiều nhất và ít nhất
    top_most_common, top_least_common = get_top_words(word_counts)

    #Ghi kết quả ra file
    write_results_to_file(top_most_common, top_least_common, output_file_path)
    print(f"Đã ghi kết quả vào file {output_file_path}")


# Chạy chương trình
if __name__ == '__main__':
    main()
