import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

if __name__ == "__main__":
    train_data, test_data = load_data()
    print(train_data.head())
    explore_data(train_data)
