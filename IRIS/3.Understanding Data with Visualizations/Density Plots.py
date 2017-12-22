import matplotlib.pyplot as plt
from pandas import read_csv
filename = 'Iris.csv'
names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
data = read_csv(filename)
data.plot(kind = 'density', subplots = True, sharex = False)
plt.show()
