import sqlite3
import pandas as pd
from shutil import copyfile

def connect():
    conn=sqlite3.connect("consignor.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS shipments (id INTEGER PRIMARY KEY,title text,firstname text,surName text,address1 text,address2 text,town text,pcode_title text, service integer,con integer, quantity integer,product integer)")
    conn.commit()
    conn.close()

def add_shipment(title,firstname,surName,address1,address2,town,pcode_title,service,con,quantity,product):
    conn=sqlite3.connect("consignor.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO shipments VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)",(title,firstname,surName,address1,address2,town,pcode_title,service,con,quantity,product))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("consignor.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM shipments")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",firstname="",surname="",address1="",address2="",town="",pcode_title="",service="",con="",quantity="",product=""):
    conn=sqlite3.connect("consignor.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM shipments WHERE title=? or firstname=? or surname=? or address1=? or address2=? or town=? or pcode_title=? or service=? or con=? or quantity=? or product=?",(name,address,service,con,quantity,product))
    rows=cur.fetchall()
    conn.close()
    return rows

def export():
    conn = sqlite3.connect("consignor.db")
    query='SELECT * FROM shipments'
    data=pd.read_sql(query,conn)
    data.to_csv('export.csv')
    conn.close()

connect()
#add_shipment("Mr","James","Carn","88 Bendall Road","Kingstanding","Birmingham","B44 0SN","B410",123123123,3)
#view()
