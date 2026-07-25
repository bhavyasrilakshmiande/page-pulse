def validate_url(url):
    from urllib.parse import urlparse
    parsed = urlparse(url)
    return all([parsed.scheme in ['http', 'https'], parsed.netloc])

def fetch_webpage(url):
    import requests
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        return None, str(e)

def parse_html(html_content):
    from bs4 import BeautifulSoup
    return BeautifulSoup(html_content, 'html.parser')

def get_page_title(soup):
    title_tag = soup.title
    return title_tag.string if title_tag else None

def get_meta_description(soup):
    description_tag = soup.find('meta', attrs={'name': 'description'})
    return description_tag['content'] if description_tag and 'content' in description_tag.attrs else None

def count_h1_tags(soup):
    return len(soup.find_all('h1'))

def count_images_missing_alt(soup):
    images = soup.find_all('img')
    return sum(1 for img in images if not img.get('alt'))

def count_visible_words(soup):
    text = soup.get_text()
    words = text.split()
    return len(words) if words else 0
def parse_html_metrics(response):
    soup = parse_html(response.text)

    return {
        "title": get_page_title(soup),
        "meta_description": get_meta_description(soup),
        "h1_count": count_h1_tags(soup),
        "images_missing_alt": count_images_missing_alt(soup),
        "word_count": count_visible_words(soup)
    }