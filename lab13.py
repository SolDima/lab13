import csv
import json
import os


# Створення .csv файлу і запис кількох рядків
def create_csv(file_path):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            # Запис заголовків
            writer.writerow(['ID', 'Name', 'Age'])
            # Запис даних
            writer.writerow([1, 'Ivan', 20])
            writer.writerow([2, 'Olena', 21])
            writer.writerow([3, 'Serhiy', 22])
        print("CSV file created successfully.")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")


# Переписування даних із .csv у .json
def csv_to_json(csv_path, json_path):
    try:
        data = []
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open(json_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print("Data from CSV file written to JSON successfully.")
    except IOError as e:
        print(f"File processing error: {e}")


# Виконання
csv_file_path = 'students.csv'
json_file_path = 'students.json'
create_csv(csv_file_path)
csv_to_json(csv_file_path, json_file_path)
