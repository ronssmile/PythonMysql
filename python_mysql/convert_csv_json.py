import csv
import json

#read csv file the make a list of tuple
def csv_to_data(file_name):
    with open("example.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data1 = []
        for row in reader:
            data1.append(row)

        data = [tuple(x) for x in data1]
    return data1


#converting csv to json
def csv_json(file_name):
    with open("example.csv","r") as f:
        reader = csv.reader(f)
        next(reader) #to bypass or ignore header title
        jdata ={"reviewer_records":[]}
        for row in reader:
            jdata["reviewer_records"].append({"first_name":row[0], "last_name":row[1]})

    with open ("json_data.json","w") as f:
        json.dump(jdata,f,indent=4)

