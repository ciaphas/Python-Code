import os, json, sqlite3

# read JSON file which is in the next parent folder
file = os.path.abspath('/Users/jim/Documents/GitHub/Python-Code/Update Skills') + "/newjson1.json"
json_data=open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val




conn=sqlite3.connect("hr.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS testp (id INTEGER PRIMARY KEY, person text, year integer, company text)")
conn.commit()



# parse json data to SQL insert
for i, item in enumerate(json_obj):
    person = validate_string(item.get("person", None))
    year = validate_string(item.get("year", None))
    company = validate_string(item.get("company", None))
    cursor.execute("INSERT INTO testp (person,	year,	company) VALUES (?,?,?)", (person,	year,	company))
    conn.commit()

conn.close()


def select_all_tasks():
    conn=sqlite3.connect("hr.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM testp")
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        print(row)


select_all_tasks()