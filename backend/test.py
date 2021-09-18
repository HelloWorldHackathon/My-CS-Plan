import pandas as pd
import util
import app

def load_csv():
    csvs=[]
    for file in util.tracks:
        path = "./data/" + file + ".csv"

        csvs.append(pd.read_csv(path))
    return csvs

def main():
    csv = load_csv()
    util.get_class_list(csv[2])

if __name__ == "__main__":
    main()


