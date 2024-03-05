import os
import json
import csv
import pickle


def get_directory_info(directory):
    def get_size(path):
        if os.path.isfile(path):
            return os.path.getsize(path)
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    def generate_info(path):
        info = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            item_type = "file" if os.path.isfile(item_path) else "directory"
            item_size = get_size(item_path) if os.path.isdir(item_path) else os.path.getsize(item_path)
            info.append({"name": item, "type": item_type, "size": item_size, "parent_directory": path})
            if os.path.isdir(item_path):
                info.extend(generate_info(item_path))
        return info

    directory_info = generate_info(directory)

    with open('directory_info.json', 'w') as json_file:
        json.dump(directory_info, json_file, indent=4)

    with open('directory_info.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "type", "size", "parent_directory"])
        writer.writeheader()
        writer.writerows(directory_info)

    with open('directory_info.pickle', 'wb') as pickle_file:
        pickle.dump(directory_info, pickle_file)

    return directory_info



directory_path = 'C:\\Python'
get_directory_info(directory_path)