import requests
from bs4 import BeautifulSoup as BS

from models import Institution, Direction, List

# инженерно строительный
answer = requests.get('https://ice.spbstu.ru/edu/')

print(answer)

soup = BS(answer.text, 'html.parser')


for i in soup.find_all('a', {'class': 'edu_spec_program_name'}):
    print(i.text)

print('done')

