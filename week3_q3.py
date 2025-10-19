import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], errors='coerce')
df = df.dropna(subset=['hour_beginning'])

def time_of_day(h):
    if 5 <= h < 12:
        return 'Morning'
    elif 12 <= h < 17:
        return 'Afternoon'
    elif 17 <= h < 21:
        return 'Evening'
    else:
        return 'Night'

df['time_period'] = df['hour_beginning'].dt.hour.apply(time_of_day)

grouped = df.groupby('time_period')['Pedestrians'].mean().sort_values(ascending=False)

plt.bar(grouped.index, grouped.values)
plt.title('Average Pedestrians by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Average Pedestrian Count')
plt.tight_layout()
plt.show()
