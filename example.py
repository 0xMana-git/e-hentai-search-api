import requests
import cfg
from bs4 import BeautifulSoup
import scraper
import time
resp = requests.get("https://e-hentai.org", proxies=cfg.proxies)
resp = resp.content

resp_obj = BeautifulSoup(resp)

with open(str(time.time_ns()) + ".html", "wb") as f:
    f.write(resp)

print(scraper.get_next_id(resp_obj))

print(scraper.get_metadata(resp_obj))