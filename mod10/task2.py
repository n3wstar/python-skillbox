import re
import requests


def get_h3_headings(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            h3_headings = re.findall(r'<h3.*?>(.*?)</h3>', html_content, re.IGNORECASE)
            return h3_headings
        else:
            print(f"Не удалось получить доступ к странице. Код ответа: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []


def main():
    website_url = 'https://www.columbia.edu/~fdc/sample.html'
    h3_headings = get_h3_headings(website_url)

    if h3_headings:
        print(h3_headings)
    else:
        print("Не удалось получить список подзаголовков.")


if __name__ == "__main__":
    main()
