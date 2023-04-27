import pandas as pd
import json
import os

file = os.path.abspath('/Users/jim/Documents/GitHub/Python-Code/Update Skills') + "/newjson1.json"
json_data=open(file).read()
json_obj = json.loads(json_data)

df = pd.read_json(file)
#print(df)

df1 = pd.DataFrame(df)
print(df1)

