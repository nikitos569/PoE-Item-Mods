import pandas as pd
data=pd.read_csv("1.csv", header=0, usecols=['txt', 'txt-href'])
data["txt-href"] = data["txt-href"].str.replace('https://poe.ninja/challenge/builds/char/', '')
print(data)
