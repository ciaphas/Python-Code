import pandas as pd 

data = {
	'apples': [3,2,0,1],
	'oranges': [4,6,7,8]
}

purchases = pd.DataFrame(data)
print(purchases)