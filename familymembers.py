# code here
import json
# some dictionaries
p1 = { "name":"Louis", "age":56, "city":"San Deigo", "travel": "London"}
p2 = { "name":"Cristina", "age":52, "city":"San Diego", "travel": "Sydney"}
p3 = { "name":"Grace", "age":17, "city":"San Diego", "travel": "Singapore"}
p4 = { "name":"Isaac", "age":15, "city":"San Diego", "travel": "Dubai"}
p5 = { "name": "Kayla", "age": 12, "city": "San Diego", "travel": "Pairs"}
# a list of dictionaries
list_of_family_members = [p1, p2, p3, p4, p5]
# write some code to Print List of people one by one
print("List of Family Members")
print(type(list_of_family_members))
print(list_of_family_members)
for person in list_of_family_members:
    print(person['name'] + "," + str(person['age']) + "," + person['city'] + "," + person['travel'])
print()
# turn list to dictionary of people
dict_people = {'people': list_of_family_members}
print("Dictionary of people")
# write some code to Print People from Dictionary
print(type(dict_people))
print(dict_people)
people = dict_people["people"]
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'] + "," + person['travel'])
print()
# prepare list for JSON, this can be sent via a browser
json_people = json.dumps(dict_people)
# the result is a JSON file:
print("JSON People")
# write some code to Print People from JSon
print(type(json_people))
people = json.dumps(dict_people["people"])
print(json_people)
x = json.loads(json_people)
people = x["people"]
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'] + "," + person['travel'])
print()
# unwind people back to JSON
dict_people = json.loads(json_people)
print("Dictionary of people")
# write some code to Print People from Dictionary
print(type(dict_people))
x = json.loads(json_people)
people = x["people"]
for person in people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'] + "," + person['travel'])
print()
