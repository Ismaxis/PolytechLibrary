### write lines below to console manually

# import requests
# from bs4 import BeautifulSoup as BS
# from models import Institution, Direction, List


answer = requests.get('https://hum.spbstu.ru/edu/')
print(answer)

soup = BS(answer.text, 'html.parser')

### write this line manually and paste needed name
#inst = Institution.objects.get(institution_name="") 

for i in soup.find_all('a', {'class': 'edu_spec_program_name'}):
    dir = Direction(institution=inst, direction_name=i.text)
    dir.save()

### exec(open('./app/load_data.py').read())