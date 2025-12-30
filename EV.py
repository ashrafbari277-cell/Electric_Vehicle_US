#Import all Necessary Libraries

import pandas as pd  
import matplotlib.pyplot as plt  
plt.style.use('tableau-colorblind10')  
df = pd.read_csv("EV_P.csv")

print(df.head())

#Question: Is the market shifting toward fully electric?
top_makes = df['Make'].value_counts().head(10)

plt.figure(figsize=(8,6))
top_makes.sort_values().plot(kind='barh')
plt.title("Top 10 EV Manufacturers by Registrations (BEV & PHEV incl.)")
plt.xlabel("Number of EV Registrations")
plt.ylabel("Manufacturer")
plt.show()

#Question: Did Tesla always dominate, or did dominance change?

top_makes = df['Make'].value_counts().head(5).index
df_top = df[df['Make'].isin(top_makes)]

trend_make = df_top.groupby(['Model Year', 'Make']).size().unstack(fill_value=0)

plt.figure(figsize=(10,6))
trend_make.plot()
plt.title("Top EV Manufacturers Trend Over Time")
plt.xlabel("Model Year")
plt.ylabel("EV Registrations")
plt.show()


#Question: How do BEV and PHEV trends compare over time?
ev_type_trend = df.groupby(['Model Year', 'Electric Vehicle Type']).size().unstack(fill_value=0)

plt.figure(figsize=(10,6))
ev_type_trend.plot(kind='bar', stacked=True,color = ["blue","gray"])
plt.title("BEV vs PHEV Distribution Over Time")
plt.xlabel("Model Year")
plt.ylabel("EV Registrations")
plt.show()


#Question: Top Models Over Time
top_models = df['Model'].value_counts().head(5)

plt.figure(figsize=(10,6))
top_models.plot(kind='bar', color='orange') 

plt.title("Top 5 EV Models")
plt.xlabel("EV Model")
plt.ylabel("No. of EV On Road")
plt.tight_layout()
plt.show()

