import json

json_string = open("JSON/euro_services.json").read()

parsed_json = json.loads(json_string)

print(parsed_json["0"]["header"]["nameService"])
print(parsed_json["0"]["atm"]["regions"])
