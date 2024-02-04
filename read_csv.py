import csv

def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            sales_dict = {key: value for key, value in iterable}
            data.append(sales_dict)
        return data

if __name__ == "__main__":
    data = read_csv('./data_sets/amazon.csv')
    print(data)