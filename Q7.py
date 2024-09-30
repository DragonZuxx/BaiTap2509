import re


def validate_url(url):
    pattern = r'^(http|https)://(www\.)?([a-zA-Z0-9]+)\.[a-z]{2,6}(/[^\s]*)?$'
    return bool(re.match(pattern, url))


# Kiểm tra URL liên tục cho đến khi người dùng nhập đúng
while True:
    url = input("Nhập URL để kiểm tra (hoặc gõ 'done' hoặc bấm 'Enter' để thoát): ")

    # Kiểm tra điều kiện thoát
    if url.lower() == 'done' or url == '':
        print("Thoát chương trình.")
        break

    if validate_url(url):
        print("URL hợp lệ.")
    else:
        print("URL không hợp lệ. Vui lòng nhập lại.")
