import pandas as pd

def load_data():
    return pd.read_csv("dataset_sample.csv")

def get_descriptive_statistics(data):
    return data.describe()

def main():
    data = load_data()
    stats = get_descriptive_statistics(data)
    print(stats)

if __name__ == "__main__":
    main()
