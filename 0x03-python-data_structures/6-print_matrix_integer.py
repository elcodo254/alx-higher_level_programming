#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for x in matrix:
            for i in range(len(x)):
                if i < len(x) - 1:
                    print("{:d}".format(x[i], end=" ")
                else:
                    print("{:d}".format(x[i]))

