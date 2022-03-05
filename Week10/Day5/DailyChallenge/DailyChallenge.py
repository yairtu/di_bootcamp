import requests
from datetime import datetime


def request_time(url):
	request_start = datetime.now()
	x = requests.get(url)
	print(f"request time for {url} with response code({x.status_code}): {datetime.now() - request_start}")
	print(f"elapsed time for {url} with response code({x.status_code}: {x.elapsed}\n")


request_time("https://google.com")
request_time("https://ynet.com")
request_time("https://imdb.com")