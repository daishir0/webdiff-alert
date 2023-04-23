import requests
from bs4 import BeautifulSoup
import time
import difflib
from datetime import datetime
import threading

def get_page_text_and_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    html = soup.prettify()

    text = soup.get_text()

    return text, html

def save_html(html, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html)

def print_diff(text1, text2, is_html=False):
    diff = difflib.ndiff(text1.splitlines(), text2.splitlines())
    diff_lines = [line for line in diff if line.startswith('+ ') or line.startswith('- ')]

    if is_html:
        return [line for line in diff_lines if '<' in line or '>' in line]
    else:
        return diff_lines

def process_url(url, prev_text, prev_html):
    current_text, current_html = get_page_text_and_html(url)
    diff_lines = print_diff(prev_text, current_text)
    diff_html_lines = print_diff(prev_html, current_html, is_html=True)

    now = datetime.now().strftime("%Y%m%d-%H%M%S")

    if diff_lines:
        print(f"{now} - {url} - 変更があります:")
        for line in diff_lines:
            print(line)
        print("HTML差分:")
        for line in diff_html_lines:
            print(line)
        save_html(current_html, f"{now}-{url.replace('://', '-').replace('/', '-')}.html")
    else:
        print(f"{now} - {url} - 変更はありません")

    return current_text, current_html

def read_urls_from_file(filepath):
    with open(filepath, 'r') as file:
        urls = [url.strip() for url in file.readlines()]
    return urls

if __name__ == "__main__":
    filepath = "urls.txt"
    url_data = {}

    while True:
        urls = read_urls_from_file(filepath)
        new_urls = set(urls) - set(url_data.keys())
        removed_urls = set(url_data.keys()) - set(urls)

        for url in new_urls:
            text, html = get_page_text_and_html(url)
            now = datetime.now().strftime("%Y%m%d-%H%M%S")
            save_html(html, f"{now}-{url.replace('://', '-').replace('/', '-')}.html")  # 修正箇所
            url_data[url] = {'prev_text': text, 'prev_html': html}

        for url in removed_urls:
            del url_data[url]

        for url in urls:
            prev_text = url_data[url]['prev_text']
            prev_html = url_data[url]['prev_html']
            current_text, current_html = process_url(url, prev_text, prev_html)
            url_data[url]['prev_text'] = current_text
            url_data[url]['prev_html'] = current_html

        time.sleep(60)  # 1分待機
