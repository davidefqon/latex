import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

def load_data():
    train_data = pd.read_csv('train.csv')
    test_data = pd.read_csv('test.csv')
    return train_data, test_data

def explore_data(train_data):
    print(train_data.describe())
    print(train_data.isnull().sum())
    
    plt.figure()
    sns.histplot(train_data['Age'].dropna(), kde=False, bins=30)
    plt.title('Distribución de Edad')
    plt.show()

def preprocess_data(train_data):
    # Llenar valores faltantes
    train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
    train_data['Embarked'].fillna('S', inplace=True)

    # Convertir categóricos a numéricos
    le = LabelEncoder()
    train_data['Sex'] = le.fit_transform(train_data['Sex'])
    train_data['Embarked'] = le.fit_transform(train_data['Embarked'])

if __name__ == "__main__":
    train_data, test_data = load_data()
    print(train_data.head())
    explore_data(train_data)
    preprocess_data(train_data)
    print(train_data.head())
