import csv
import requests
region = input("enter region code = ")
codes = ['01', '05', '07', '12', '14', '18', '21', '23', '26', '32', '35', '44', '46', '48', '51', '53', '56', '59',
         '61', '63', '65', '68', '71', '73', '74', '80', '85']
a = region in codes
if region not in codes:
    print("enter another codes")

print('Форма фінансування: ''Державна''/Приватна''/Комунальна')
choose = str(input("Обреріть щось одне з вибірки: "))
r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+region+'&exp=json')

universities: list = r.json()
filtered_data = [{k: row[k] for k in ['university_id', 'post_index']} for row in universities]
filtered_data1 = [{k: row[k] for k in ['university_name', 'university_name_en', 'university_financing_type_name']}
                  for k in ['university_financing_type_name']
                  for row in universities if row[k] == choose]
with open('universities'+region+'.csv', mode='w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

with open('websites.csv', mode='w', encoding='CP1251', newline='') as f1:
    writer = csv.DictWriter(f1, fieldnames=filtered_data1[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data1)