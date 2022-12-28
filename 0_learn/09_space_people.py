import requests

people = requests.get('http://api.open-notify.org/astros.json')

print(people)
#output - <Response [200]>

json = people.json()
print(json)
#output - {'message': 'success', 'people': [{'name': 'Sergey Prokopyev', 'craft': 'ISS'}, {'name': 'Dmitry Petelin', 'craft': 'ISS'}, {'name': 'Frank Rubio', 'craft': 'ISS'}, {'name': 'Nicole Mann', 'craft': 'ISS'}, {'name': 'Josh Cassada', 'craft': 'ISS'}, {'name': 'Koichi Wakata', 'craft': 'ISS'}, {'name': 'Anna Kikina', 'craft': 'ISS'}, {'name': 'Fei Junlong', 'craft': 'Shenzhou 15'}, {'name': 'Deng Qingming', 'craft': 'Shenzhou 15'}, {'name': 'Zhang Lu', 'craft': 'Shenzhou 15'}], 'number': 10}

print('The people curretly in space are:')

for p in json['people']:
    print(p['name'])

#output
#Sergey Prokopyev
#Dmitry Petelin
#Frank Rubio
#Nicole Mann
#Josh Cassada
#Koichi Wakata
#Anna Kikina
#Fei Junlong
#Deng Qingming
#Zhang Lu