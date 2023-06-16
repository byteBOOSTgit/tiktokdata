# Description: This script will print out all the fields in the TikTok data schema
# I used the python package genson to generate the schema from the json file
# https://pypi.org/project/genson/
# pip install genson
# genson -s tiktok_data.json > tiktok_data_schema.json
import json

tsf = open("tiktok_data_schema.json", "r")
tsf_contents = tsf.read()
tiktok_schema_object = json.loads(tsf_contents)

for f in tiktok_schema_object["properties"]:
    print(f)
    for f2 in tiktok_schema_object["properties"][f]["properties"]:
        print("\t" + f2)
        # check if the field has properties
        if tiktok_schema_object["properties"][f]["properties"][f2].get("properties"):
            for f3 in tiktok_schema_object["properties"][f]["properties"][f2]["properties"]:
                print("\t\t" + f3)
                # check if the field has properties
                if tiktok_schema_object["properties"][f]["properties"][f2]["properties"][f3].get("items"):
                    for f4 in tiktok_schema_object["properties"][f]["properties"][f2]["properties"][f3]["items"]:
                        fields = ""
                        for f4prop in tiktok_schema_object["properties"][f]["properties"][f2]["properties"][f3]["items"]["properties"]:
                            fields = fields + f4prop + ", "
                        print("\t\t\t" + fields)



