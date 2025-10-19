import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url,sep=',')

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], errors='coerce')
df = df.dropna(subset=['hour_beginning'])
df = df[df['hour_beginning'].dt.dayofweek < 5]

order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
by_day = (df.assign(day=df['hour_beginning'].dt.day_name())
            .groupby('day', as_index=False)['Pedestrians'].sum())
by_day = by_day.set_index('day').reindex(order).reset_index()

plt.plot(by_day['day'], by_day['Pedestrians'], marker='o')
plt.xlabel('Day of Week')
plt.ylabel('Total Pedestrians')
plt.title('Brooklyn Bridge Pedestrians (Weekdays)')
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()