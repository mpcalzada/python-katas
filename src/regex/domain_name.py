import re

def domain_name(url):
    result = re.search(r"(https?:\/\/)*(w*\.?)([a-z\-]*)(\.[a-zA-Z\/]*)", url)
    return result.group(3)

if __name__ == '__main__':
    urls = [
        "http://github.com/carbonfive/raygun",
        "http://www.zombie-bites.com",
        "https://www.cnet.com",
        "www.xakep.ru",
        "facebook.ru"
    ]

    for url in urls:
        domain = domain_name(url)
        print(f"Url: {url} URL: {domain}")