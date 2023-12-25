import requests
from bs4 import BeautifulSoup

file_name = "scraped_content.txt"
url ="https://www.cancer.org/cancer/risk-prevention/diet-physical-activity/eat-healthy/shopping-list-basic-ingredients-for-a-healthy-kitchen.html"
response = requests.get(url)
if response.status_code == 200:
    bs = BeautifulSoup(response.content,"lxml")
    div_content = bs.find_all('div', class_="text-ckeditor aem-GridColumn aem-GridColumn--default--12")
    with open(file_name, 'a', encoding = 'utf-8') as file:
        for content in div_content:
            ul_text = content.ul.get_text(separator='\n', strip=True)
            file.write(ul_text +'\n\n')
else:
    print("Failed to retrieve the webpage")
    ingredient_list =""

