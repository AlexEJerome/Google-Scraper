import requests
import re
from bs4	 import BeautifulSoup
import csv
import urllib 
from tqdm import tqdm

domain = "alexejero.me"
searchlist = ["alexejerome"]
numresp = 30
rows =[]
for item in tqdm(searchlist):
	rank = 0 
	def is_from_domain(tag):
		if tag.name=="cite":
			global rank
			rank=rank+1
			pattern = re.escape(domain)+".*"
			# print(tag.text)
			return re.match(pattern, tag.text)

	url = 'https://www.google.com/search?q='+item+'&num='+str(numresp)
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, "html.parser")
	print(soup.prettify)
	result = soup.find(is_from_domain)
	if result is None:
		result_text = "no results"
		final_rank="-"
	else:
		result_text =  result.text
		final_rank = str(rank)
	rows.append([item, result_text, final_rank])

headers = ["Search Term", "url", "rank"]
writer = csv.writer(open('./output.csv','w'), delimiter=',', lineterminator='\n')
writer.writerow(["Search Term", "url", "rank"])
writer.writerows(rows)
