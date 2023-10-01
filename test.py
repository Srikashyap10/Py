import pandas as pd
import matplotlib.pyplot as plt

s = pd.read_csv('business.csv')

print(s)
industry = s['industry'].head(10)
value = s['value'].head(10)
fig = plt.figure(figsize =(10, 7))
plt.bar(industry[0:10], value[0:10])
 
# Show Plot
plt.show()