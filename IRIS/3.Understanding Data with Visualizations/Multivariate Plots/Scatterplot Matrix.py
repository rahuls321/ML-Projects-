import matplotlib.pyplot as plt
from pandas import read_csv
from pandas.tools.plotting import scatter_matrix
filename = 'Iris.csv'
names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
data = read_csv(filename)
scatter_matrix(data)
plt.show()
