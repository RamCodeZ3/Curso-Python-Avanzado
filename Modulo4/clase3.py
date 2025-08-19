import random


list_numbers = []


def random_list_number():
    num = int(input("Cuantos numeros ramdom quieres: "))
    range_num = int(input("Del 1 hasta cuanto: "))

    for i in range(num):
        random_integer = random.randint(1, range_num)
        list_numbers.append(random_integer)

    print(list_numbers)


if __name__ == '__main__':
    random_list_number()
