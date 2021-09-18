import pandas as pd
import compare
def load_csv():
    csvs = []
    for file in compare.tracks:
        path = "./data/" + file + ".csv"
        print(path)
        csvs.append(pd.read_csv(path))

    return csvs


csv = load_csv()

