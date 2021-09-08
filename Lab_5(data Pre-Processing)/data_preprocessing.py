import numpy as np
import pandas as pd


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

X_train, X_test, y_train, y_test = train_test_split(mashroom_data, mashroom_target, test_size = 0.25, stratify = mashroom_target, random_state = 0)

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

print('label :')  # The class is the label
label = pd.DataFrame(mashroom['class'])
label

print('features :')
mashroom_data