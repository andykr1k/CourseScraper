import requests
from bs4 import BeautifulSoup
import time


start_time = time.time()

cookies = {
    'TESTID': 'set',
    'nmstat': '7d06244e-cf5c-7b83-a18d-a6b8276031ce',
    '__zlcmid': '1ASkzxhvMF3kgxl',
    '_clck': '19yu9p3|1|f8e|0',
    '_ga': 'GA1.1.2091611904.1654714123',
    '_ga_Z1RGSBHBF7': 'GS1.1.1674924849.49.0.1674924860.0.0.0',
    '_ga_S8BZQKWST2': 'GS1.1.1674924849.49.0.1674924860.0.0.0',
    '_hp2_id.3001039959': '%7B%22userId%22%3A%226489448599566009%22%2C%22pageviewId%22%3A%228501945202483769%22%2C%22sessionId%22%3A%221366669556209706%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    '_hp2_ses_props.3001039959': '%7B%22r%22%3A%22https%3A%2F%2Felearn.ucr.edu%2F%3Flogin_success%3D1%22%2C%22ts%22%3A1675964140681%2C%22d%22%3A%22elearn.ucr.edu%22%2C%22h%22%3A%22%2Fcourses%2F75131%22%7D',
    'BIGipServer~Banner~bannerwclbprod_4443': '536871690.23313.0000',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'TESTID=set; nmstat=7d06244e-cf5c-7b83-a18d-a6b8276031ce; __zlcmid=1ASkzxhvMF3kgxl; _clck=19yu9p3|1|f8e|0; _ga=GA1.1.2091611904.1654714123; _ga_Z1RGSBHBF7=GS1.1.1674924849.49.0.1674924860.0.0.0; _ga_S8BZQKWST2=GS1.1.1674924849.49.0.1674924860.0.0.0; _hp2_id.3001039959=%7B%22userId%22%3A%226489448599566009%22%2C%22pageviewId%22%3A%228501945202483769%22%2C%22sessionId%22%3A%221366669556209706%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.3001039959=%7B%22r%22%3A%22https%3A%2F%2Felearn.ucr.edu%2F%3Flogin_success%3D1%22%2C%22ts%22%3A1675964140681%2C%22d%22%3A%22elearn.ucr.edu%22%2C%22h%22%3A%22%2Fcourses%2F75131%22%7D; BIGipServer~Banner~bannerwclbprod_4443=536871690.23313.0000',
    'Origin': 'https://banweb.ucr.edu',
    'Referer': 'https://banweb.ucr.edu/banprod/bwckgens.p_proc_term_date',
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

data = [
    ('term_in', '202320'),
    ('sel_subj', 'dummy'),
    ('sel_day', 'dummy'),
    ('sel_schd', 'dummy'),
    ('sel_insm', 'dummy'),
    ('sel_camp', 'dummy'),
    ('sel_levl', 'dummy'),
    ('sel_sess', 'dummy'),
    ('sel_instr', 'dummy'),
    ('sel_ptrm', 'dummy'),
    ('sel_attr', 'dummy'),
    ('sel_subj', 'ANTH'),
    ('sel_crse', ''),
    ('sel_title', ''),
    ('sel_schd', '%'),
    ('sel_insm', '%'),
    ('sel_from_cred', ''),
    ('sel_to_cred', ''),
    ('sel_levl', '%'),
    ('sel_instr', '%'),
    ('sel_attr', '%'),
    ('begin_hh', '0'),
    ('begin_mi', '0'),
    ('begin_ap', 'a'),
    ('end_hh', '0'),
    ('end_mi', '0'),
    ('end_ap', 'a'),
]

response = requests.post('https://banweb.ucr.edu/banprod/bwckschd.p_get_crse_unsec', cookies=cookies, headers=headers, data=data)


soup = BeautifulSoup(response.content, "html.parser")


f = open("demo.csv", "w")
f.write("course_name, course_crn, course_id, course_section")



for rows in soup.find_all('tr'):
    for title in rows.find_all('th'):
        for link in title.find_all('a'):
            f.write('\n'+link.text.split('-')[0].strip()+', ')
            print('\n'+ link.text.split('-')[0].strip())

            f.write(link.text.split('-')[1].strip()+', ')
            print(link.text.split('-')[1].strip())

            f.write(link.text.split('-')[2].strip()+', ')
            print(link.text.split('-')[2].strip())

            f.write(link.text.split('-')[3].strip())
            print(link.text.split('-')[3].strip())
    for data in rows.find_all('td'):
        for table in data.find_all('table'):
            for row in table.find_all('tr'):
                for d in row.find_all('td'):
                    for a in d.text.replace(',',"").split():
                        print(a)

end_time = time.time()

t_time = end_time - start_time

print('\n' + "Total time scraping: " + str(t_time) + " seconds")
f.close()
