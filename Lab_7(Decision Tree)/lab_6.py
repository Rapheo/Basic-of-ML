import numpy as np
import pandas as pd
import sklearn

mashroom = pd.read_csv('mushroom edibility classification dataset.csv')
mashroom.head()

mashroom.shape

mashroom.isnull().sum()

mashroom_corr = mashroom.corr()

import seaborn as sns

sns.heatmap(mashroom_corr, cmap= 'YlGnBu')

#removing redundant columns that has no distinguishing features
mashroom.drop('veil-type',axis=1,inplace=True) #all the values are 0
mashroom.drop('veil-color',axis=1,inplace=True) #all the values are 2
mashroom.drop('ring-number',axis=1,inplace=True) #all the values are 1
mashroom.drop('Unnamed: 0',axis=1,inplace=True)
mashroom_corr = mashroom.corr()
sns.heatmap(mashroom_corr, cmap= 'YlGnBu')

# handling NaN values
from sklearn.impute import SimpleImputer

impute = SimpleImputer(missing_values = np.nan, strategy = 'mean')

impute.fit(mashroom[['cap-shape']])
mashroom['cap-shape'] = impute.transform(mashroom[['cap-shape']])

impute.fit(mashroom[['cap-color']])
mashroom['cap-color'] = impute.transform(mashroom[['cap-color']])
# mashroom.iloc[302]
mashroom.isnull().sum()

#encode
from sklearn.preprocessing import LabelEncoder

enc = LabelEncoder()

mashroom['class'] = enc.fit_transform(mashroom['class'])
mashroom['bruises'] = enc.fit_transform(mashroom['bruises'])
mashroom.info()

from sklearn.model_selection import train_test_split
mashroom_target = mashroom['class']
mashroom_data = mashroom.drop('class',axis=1)
#80% training and 20% testing split
X_train, X_test, y_train, y_test = train_test_split(mashroom_data, mashroom_target, test_size = 0.2,stratify = mashroom_target,  random_state = 0)

#scale
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

print("per-feature minimum after scaling:\n {}".format(
    X_train.min(axis=0)))
print("per-feature maximum after scaling:\n {}".format(
    X_train.max(axis=0)))

# Import the dependencies for logistic regression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#Train the model
#classification using logistic regression
model = LogisticRegression()
model.fit(X_train, y_train) 
predictions = model.predict(X_test)
print(predictions)

logistic_accuracy = accuracy_score(y_test, predictions)*100
logistic_accuracy

#classification using decision tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy',random_state=1)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
decision_tree_accuracy = accuracy_score(y_pred,y_test)*100
decision_tree_accuracy

import matplotlib.pyplot as plt
fig = plt.figure()
width = 0.5
ax = fig.add_axes([0,0,1,1])
label = ['Logistic recursion', 'Decision Tree']
percentage = [logistic_accuracy, decision_tree_accuracy]
barlist = ax.bar(label, percentage)
barlist[0].set_color('orange')
barlist[1].set_color('gray')
plt.axhline(y=decision_tree_accuracy,linewidth=0.5, color='k')
plt.show()