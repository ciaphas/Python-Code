from jira import JIRA
import pandas as pd
import sqlite3 as sql
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

conn = sql.connect('jiradata.db')


user = 'jcarn@centricsoftware.com'
apikey = '9sorxejoMLu7OpBemmX64CFC'
server = 'https://centric8.atlassian.net'

options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )

JQL = 'issuetype in (Bug, Story) AND "Bug Club" = Yes AND assignee in (557058:4f5daa1b-d9dd-434c-9bdf-3c98f250352e, 557058:cd09d112-2f15-4d30-b4eb-dbfce9ed42b7, 557058:22ee1f85-1bae-482c-bdfd-1acac28f4db2, 557058:764bfea7-4127-4a27-901c-d472ee2461f2, 557058:9308d5eb-5176-46b6-a9dd-4235e95ff349, 5a56b080bc897679c9a47959, 5b6c7e3b304ed93c17e42919, 557058:99065f1f-d3ee-4e00-bcaf-ca43bd18bdf8, 5bd3b23fb3e37a158c365f90, 557058:64600100-037e-49c4-bec2-c4251dfb6615, 5c37f8bed254b55db84d08d7, 5da8cc6798f7270c26147920) ORDER BY assignee ASC'

data = jira.search_issues(JQL)

df = pd.DataFrame(data)
df.to_csv('output.csv')
df.to_sql('issues', con=engine)


#ticket = 'CSGS-6107'
#issue = jira.issue(ticket)

#summary = issue.fields.summary
#print('ticket: ', ticket, summary)