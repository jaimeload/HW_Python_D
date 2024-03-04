import os

def files_rename(destination_name, digit_count, source_ext, destination_ext, save_name_range, directory='.'):
    files = [f for f in os.listdir(directory) if f.endswith(source_ext)]
    count = 1
    for file in files:
        name_part = file[save_name_range[0]-1:save_name_range[1]]
        new_name = name_part + destination_name + str(count).zfill(digit_count) + '.' + destination_ext
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
        count += 1

files_rename('newfile', 3, 'txt', 'rtf', [3, 6])