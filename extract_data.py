import requests
import pandas as pd
from bs4 import BeautifulSoup
def get_clinic_name(clinic_id):
    url = 'https://{}.portal.athenahealth.com/'.format(clinic_id)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    clinic_name = soup.find_all('h1')[-1].text.strip()
    return clinic_name
start = 12690
end = 12710
master_list = []
for clinic_id in range(start, end):
    data_dict= {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic_name(clinic_id)
    if data_dict['clinic_name'] != 'Payment Confirmation' and data_dict['clinic_name'] != "Sorry, we can't find that practice. Make sure you typed the right address.":
        master_list.append(data_dict)
        print(clinic_id)
df  = pd.DataFrame(master_list)
df
