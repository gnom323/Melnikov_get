import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv(r'C:\Users\Alexey\iris_data.csv')

#print(file['PetalLengthCm'].min(), ' ', file['PetalLengthCm'].max())

length = list(map(float, input().split()))
print(length)
petal_length_counts = file['PetalLengthCm'].value_counts(bins=[0, length[0], length[1], float('inf')])
petal_length_labels = [f'<= {length[0]} см', f'{length[0]} см - {length[1]} см', f'> {length[1]} см']
petal_length_sizes = petal_length_counts.values

plt.figure(figsize=(8, 6))
plt.pie(petal_length_sizes, labels=petal_length_labels, autopct='%1.f%%', startangle=90)
plt.title('Доли ирисов с разной длиной лепестка')
plt.show()
