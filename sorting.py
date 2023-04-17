import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


##########

def selection_sort(seznam):
    """
    :param seznam:
    :return:
    """
    n = len(seznam)
    for i in range(n):
        min_idx = i
        for number in range(i+1, n):
            if seznam[number] < seznam[min_idx]:
                min_idx = number
        seznam[i], seznam[min_idx] = seznam[min_idx], seznam[i]
    return seznam

##########
def bubble_sort(seznam_cisel):
    """
    :param seznam_cisel:
    :return:
    """
    n = len(seznam_cisel)
    for i in range(n - 1):
        for idx in range(n - i - 1):
            if seznam_cisel[idx] > seznam_cisel[idx + 1]:
                seznam_cisel[i], seznam_cisel[i + 1] = seznam_cisel[i + 1], seznam_cisel[i]
    return seznam_cisel

##########
def insertion_sort(ciselny_seznam):
    """
    :param ciselny_seznam:
    :return:
    """
    n = len(ciselny_seznam)
    for i in range(1, n):






def main():
   my_data = read_data('numbers.csv')
   print(my_data['series_1'])
   selection_sort_result = selection_sort(my_data['series_1'])
   print(selection_sort_result)
   bubble_sort_result = bubble_sort(my_data['series_1'])
   print(bubble_sort_result )
   insertion_sort_result = insertion_sort(my_data['series_1'])
   print(insertion_sort_result)


if __name__ == '__main__':
    main()
