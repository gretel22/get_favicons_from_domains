import favicon
import urllib.request
import os
from urllib.parse import urlparse

urls = [
  #add your list of domains here, example: "http://www.mydomain1.com", "http://www.mydomain2.com"
]

for url in urls:
    favicon_url = favicon.get(url)
    
    for url_item in favicon_url:
        print(url_item)

        name_url = urlparse(url).netloc
        name_url_split = name_url.replace('.', '-')

        fav_url = urlparse(url_item.url)

        path = fav_url.path
        extension = os.path.splitext(path)[1]

        print(name_url_split + extension)

        filename = name_url_split + extension
        full_filename = os.path.join('favicons/', filename)

        urllib.request.urlretrieve(url_item.url, full_filename)
