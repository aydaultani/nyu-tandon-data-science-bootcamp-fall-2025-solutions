import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], errors='coerce')
df = df[df['hour_beginning'].dt.year == 2019]

df['day'] = df['hour_beginning'].dt.date
x = df.groupby(['day','weather_summary'])['Pedestrians'].sum().reset_index()
avg = x.groupby('weather_summary')['Pedestrians'].mean().sort_values(ascending=False)

plt.bar(avg.index, avg.values)
plt.xticks(rotation=45)
plt.title('Pedestrians by Weather 2019')
plt.tight_layout()
plt.show()

corr = df[['Pedestrians','temperature','precipitation']].corr()
print(corr)
