import json

with open("Lecture_Data.json", "r", encoding='UTF8') as f:
    lecture_list = json.load(f)

new_list = []
for lecture in lecture_list:
    new_data = {"model" : "lectures.lecture"}
    new_data["fields"] = {}
    new_data["fields"] = lecture
    new_list.append(new_data)

with open('Lecture_Data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)