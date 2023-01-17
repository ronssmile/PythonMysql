import csv
import json


with open("example.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"reviewers_records":[]}
    for row in reader:
        data["reviewers_records"].append({"first_name":row[0], "last_name": row[1]})

for i in range(0,len(data["reviewers_records"])):
    
    print(data["reviewers_records"][i])
# with open("data.json","w") as f:
#     json.dump(data,f, indent=4)


