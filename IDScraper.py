import requests
from bs4 import BeautifulSoup
import time
import string
import csv
import json

cookies = {
    'TESTID': 'set',
    'nmstat': '9e73759f-c3a4-2a67-c2c2-14e362c10da0',
    '_ga_7QWETJW5KQ': 'GS1.1.1677114439.1.1.1677114713.0.0.0',
    'BIGipServer~Banner~bannerwclbprod_4443': '536871690.23313.0000',
    '_gid': 'GA1.2.732617382.1678582579',
    '_ga': 'GA1.1.957348590.1677114439',
    '_ga_Z1RGSBHBF7': 'GS1.1.1678582579.3.1.1678582613.0.0.0',
    '_ga_S8BZQKWST2': 'GS1.1.1678582579.3.1.1678582613.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,la;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'TESTID=set; nmstat=9e73759f-c3a4-2a67-c2c2-14e362c10da0; _ga_7QWETJW5KQ=GS1.1.1677114439.1.1.1677114713.0.0.0; BIGipServer~Banner~bannerwclbprod_4443=536871690.23313.0000; _gid=GA1.2.732617382.1678582579; _ga=GA1.1.957348590.1677114439; _ga_Z1RGSBHBF7=GS1.1.1678582579.3.1.1678582613.0.0.0; _ga_S8BZQKWST2=GS1.1.1678582579.3.1.1678582613.0.0.0',
    'Origin': 'https://banweb.ucr.edu',
    'Referer': 'https://banweb.ucr.edu/banprod/bwckschd.p_disp_dyn_sched',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'p_calling_proc': 'bwckschd.p_disp_dyn_sched',
    'p_term': '202320',
}
print("Starting scraping and writing data!")

start_time = time.time()

response = requests.post('https://banweb.ucr.edu/banprod/bwckgens.p_proc_term_date', cookies=cookies, headers=headers, data=data)

soup = BeautifulSoup(response.content, "html.parser")

print("Response Posted!")

f = open("id.csv", "w")

print("Opened File!")

items = soup.select('[name=sel_subj] option[value]')

print("Found Dropdown!")

values = [item.get('value') for item in items]

print("Scraped Options in Dropdown!")
print("Values:")
print(values)

for item in values:
    f.write(item+",")

print("Values Written to File!")