from sklearn import svm, datasets
import numpy
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
print(class_names.shape)


labels=["car", "motor", "bike", "run", "walk"]
nlabel = numpy.asarray(labels)
print(nlabel.shape)

