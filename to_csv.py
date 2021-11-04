import csv
import json

people1 = json.load(open('people.json'))
people2 = json.load(open('people_page2.json'))

log1 = json.load(open('log.json'))
log2 = json.load(open('log_page2.json'))
log3 = json.load(open('log_page3.json'))

all_people = []
all_log = []

for p in people1['results']:
  all_people.append(p)

for p in people2['results']:
  all_people.append(p)

for l in log1['results']:
  all_log.append(l)

for l in log2['results']:
  all_log.append(l)

for l in log3['results']:
  all_log.append(l)

with open('people.csv', 'w') as people_out:
  people_writer = csv.writer(people_out)
  for p in all_people:
    id_ = p['id']
    name = p['properties']['Name']['title'][0]['plain_text']
    context = None if p['properties']['Context']['select'] is None else p['properties']['Context']['select']['name']
    how = None if p['properties']['How I know them']['select'] is None else p['properties']['How I know them']['select']['name']
    people_writer.writerow([id_, name, context, how])

with open('log.csv', 'w') as log_out:
  log_writer = csv.writer(log_out)
  for l in all_log:
    date = l['properties']['Date']['date']['start']
    hours = l['properties']['Hours']['number']
    type_ = None if l['properties']['Type']['select'] is None else l['properties']['Type']['select']['name']
    for p in l['properties']['Person']['relation']:
      log_writer.writerow([date, hours, type_, p['id']])
