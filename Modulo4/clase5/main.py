import numpy as np


mathematics = [100, 90, 80, 96]
natural = [98, 90, 96, 96]
social = [99, 94, 89, 93]
spanish_language = [100, 98, 100, 100]


def grade_average(grades):
    mean = np.mean(grades)
    max_grades = np.max(grades)
    print("Tu promedio de nota fue: {} | la mas alta fue de: {}".format(
        mean,
        max_grades
        ))


if __name__ == '__main__':
    grade_average(natural)
