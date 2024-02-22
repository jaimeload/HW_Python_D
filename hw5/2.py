def split_path(file_path):
    spl_path = file_path.split('/')
    name = spl_path[-1]
    path = '/'.join(spl_path[:-1])
    spl_path = name.split('.')
    ext = spl_path[-1]
    name = '.'.join(spl_path[:-1])

    return path, name, ext


full_path = 'C:/Python/new_project/hw5/2.py'
print(split_path(full_path))