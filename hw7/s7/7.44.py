import random


def gen_name(num_char: int) -> str:
    list_name = []
    for i in range(num_char):
        list_name.append(chr(random.randint(ord('a'), ord('z'))))
    return ''.join(list_name)

def gen_file(exten: str, min_len: int = 6, max_len: int = 30,
             min_bytes: int = 256, max_bytes: int = 4096,
             num_files: int = 42):
    for i in range(num_files):
        name = gen_name(random.randint(min_len, max_len))
        bytes = gen_name(random.randint(min_bytes, max_bytes))
        with open(name + exten, 'w') as f:
            f.write(bytes)

if __name__ == '__main__':
    gen_file('.txt', num_files=4)