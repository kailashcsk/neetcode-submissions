from typing import List

def read_integers() -> List[int]:
    i = input()
    i_list = i.split(",")
    n_list = []
    for n in i_list:
        n_list.append(int(n))
    return n_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
