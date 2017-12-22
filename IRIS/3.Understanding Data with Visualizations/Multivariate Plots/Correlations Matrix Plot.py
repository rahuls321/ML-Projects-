import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np
import matplotlib.cm as cm
fig = plt.figure()
ax = fig.add_subplot(111)
cmap = cm.get_cmap('jet', 30)
cax = ax.matshow(correlations, interpolation='nearest', cmap = cmap)
names_New = ['Id', 'Sepal_L', 'Sepal_W', 'Petal_L', 'Petal_W', 'Species']
ticks = np.arange(0,5,1)
fig.colorbar(cax)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
#Print with names of label
ax.set_xticklabels(names_New)
ax.set_yticklabels(names_New)
plt.title('Iris')
plt.show()
