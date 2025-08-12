A = ["Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]


def magic_function(input_list):
    output_list = [a[::-1] for a in input_list]
    return output_list


if __name__ == '__main__':
    print(magic_function(A))
