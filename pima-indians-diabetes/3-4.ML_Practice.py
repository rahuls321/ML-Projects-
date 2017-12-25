#Matplotlib
import matplotllib.pyplot as plt
import numpy as np
myarray = np.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Scatter plot
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Series
import numpy as np
import pandas as pd
myarray = np.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pd.series(myarray, index= rownames)
print(myseries)

#Dataframe
import numpy as np
import pandas as pd
myarray = np.array([1, 2, 3], [4, 5, 6])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pd.DataFrame(myarray, index = rownames, columns = colnames)
print(mydataframe)

#Load CSV Using Python Standard Library
import csv
import numpy as np
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rb')
reader = csv.reader(raw_data, delimiter=',', quoting = csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)

# Load CSV using NumPy
from numpy import loadtxt
filename = ' pima-indians-diabetes.data.csv '
raw_data = open(filename, ' rb ' )
data = loadtxt(raw_data, delimiter=",")
print(data.shape)

# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib import urlopen
url = ' https://goo.gl/vhm1eU '
raw_data = urlopen(url)
dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)

# Load CSV using Pandas(Prefer)
from pandas import read_csv
filename = ' pima-indians-diabetes.data.csv '
names = [ ' preg ' , ' plas ' , ' pres ' , ' skin ' , ' test ' , ' mass ' , ' pedi ' , ' age ' , ' class ' ]
data = read_csv(filename, names=names)
print(data.shape)

# Load CSV using Pandas from URL
from pandas import read_csv
url = ' https://goo.gl/vhm1eU '
names = [ ' preg ' , ' plas ' , ' pres ' , ' skin ' , ' test ' , ' mass ' , ' pedi ' , ' age ' , ' class ' ]
data = read_csv(url, names=names)
print(data.shape)
