import json
import pandas as pd

with open('watch-history.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['time'] = pd.to_datetime(df['time'])
df['hour'] = df['time'].dt.hour

hourly_counts = df['hour'].value_counts().sort_index()
print(hourly_counts)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
hourly_counts.plot(kind='bar', color='skyblue')
plt.title('My youtube watch habits by hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Videos Watched')
plt.show()