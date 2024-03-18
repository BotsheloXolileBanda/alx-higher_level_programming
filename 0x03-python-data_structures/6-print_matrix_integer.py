#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("", end="")
    else:
        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                if x == ((len(matrix)) - 1):
                    print("{:d}".format(matrix[i][x]))
                else:
                    print("{:d}".format(matrix[i][x]), end=" ")
