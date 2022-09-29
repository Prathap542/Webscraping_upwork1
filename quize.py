import requests
from bs4 import BeautifulSoup

def get_q(q_id):
    url = f'https://www.healthygem.com/entertainment/only-people-with-high-iqs-can-score-15-20-on-this-gen-knowledge-quiz/{q_id}/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    question_name = soup.find_all('h2')[-1].text.strip()
    answers = soup.find_all('ul', {'class': 'answers'})[-1].text.strip()
    return question_name

def get_a(q_id):
    url = f'https://www.healthygem.com/entertainment/only-people-with-high-iqs-can-score-15-20-on-this-gen-knowledge-quiz/{q_id}/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    answers = answers = soup.find_all('ul', {'class': 'answers'})
    need = []
    for li_tag in answers:
        for span_tag in li_tag.find_all('li'):
            field = span_tag.find('span').text
            need.append(field)
    return need

start = 2
end = 10

master_list = []
for q_id in range(start, end):
    data_dict= {}
    data_dict['q_id'] = q_id
    data_dict['question_name'] = get_q(q_id)
    data_dict['answers'] = get_a(q_id)
    master_list.append(data_dict)

import pandas as pd
df  = pd.DataFrame(master_list)
df.to_csv('quize.csv', index=False)
