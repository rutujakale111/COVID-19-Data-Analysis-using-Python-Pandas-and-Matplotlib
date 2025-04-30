import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('covid.csv')
total_by_district = df.groupby('District')['Confirmed'].sum()

plt.figure(figsize=(8, 6))
total_by_district.plot(kind='bar', color='skyblue')
plt.title('Confirmed COVID-19 Cases by District in Maharashtra', fontsize=14)
plt.xlabel('Districts', fontsize=12)
plt.ylabel('Confirmed Cases', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 7))
total_by_district.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Contribution of Each District in Maharashtra COVID-19 Cases', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()
