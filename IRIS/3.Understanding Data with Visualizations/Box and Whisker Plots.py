import matplotlib.pyplot as plt
from pandas import read_csv
filename = 'Iris.csv'
names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
data = read_csv(filename)
data.plot(kind= ' box ' , subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()
