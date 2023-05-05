import pandas as pd

#reads the csv file
data = pd.read_csv("James - Hosted Customer is Yes tickets per month (JIRA).csv", header=0, sep=",")

#Prints the Head of the file - first 5 columns only
#print(data.head())

#removes any invalid data - cleans the file
data.dropna(axis=0, inplace=True)
#print(data)


print(data.info())