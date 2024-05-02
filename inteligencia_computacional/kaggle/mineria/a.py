import pandas as pd

def load_data():
    train_data = pd.read_csv('train.csv')
    test_data = pd.read_csv('test.csv')
    return train_data, test_data

if __name__ == "__main__":
    train_data, test_data = load_data()
    print(train_data.head())
