import csv
import json
import os

import requests

people_database_id = 'b7b730b2a0be400e91e8bcbe04bd6d1a'
log_database_id = '95cc6edf3199439aa5c8a335e3bc2d86'
has_more = True
start_cursor = None
headers = {'Authorization': os.environ['NOTION_API_KEY'], 'Notion-Version': '2021-08-16'}

all_people = []
all_log = []

# fetch all people data
while has_more:
  if start_cursor:
    res = requests.post('https://api.notion.com/v1/databases/' + people_database_id + '/query', headers=headers, json={ 'start_cursor': start_cursor })
  else:
    res = requests.post('https://api.notion.com/v1/databases/' + people_database_id + '/query', headers=headers)
  res_json = res.json()
  all_people.extend(res_json['results'])
  has_more = res_json['has_more']
  start_cursor = res_json['next_cursor']

# fetch all log data
has_more = True
start_cursor = None
while has_more:
  if start_cursor:
    res = requests.post('https://api.notion.com/v1/databases/' + log_database_id + '/query', headers=headers, json={ 'start_cursor': start_cursor })
  else:
    res = requests.post('https://api.notion.com/v1/databases/' + log_database_id + '/query', headers=headers)
  res_json = res.json()
  all_log.extend(res_json['results'])
  has_more = res_json['has_more']
  start_cursor = res_json['next_cursor']

print('num people: %d' % len(all_people))
print('num logs: %d' % len(all_log))

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
