# Tic-tac-toe python tutorial
import numpy as np
import math
import random

matrix =  np.array([
    [""," "," "],
    [" "," "," "],
    [" "," "," "]
])

def show_matrix(show_result):
    print('\n')
    print(" {} | {} | {}".format(show_result[0][0],show_result[0][1],show_result[0][2]))
    print("____________")
    print(" {} | {} | {}".format(show_result[1][0],show_result[1][1],show_result[1][2]))
    print("____________")
    print(" {} | {} | {}".format(show_result[2][0],show_result[2][1],show_result[2][2]))


def get_input():
    a = int(input('type the column: '))
    b = int(input('type the row: '))
    return(a-1,b-1)

def check_matrix(result_matrix,b):
    # Diagonal Check
    if result_matrix[0][0] == result_matrix[1][1] == result_matrix[2][2] == b:
        print('{} is in all diagonal'.format(b))
        print('{} won'.format(b))
        return True
    elif result_matrix[0][2] == result_matrix[1][1] == result_matrix[2][0] == b:
        print('{} is in all reverse diagonal'.format(b))
        print('{} won'.format(b))
        return True

    ## check for Draw 
    elif result_matrix[0][0] != " " and result_matrix[0][1] != " " and result_matrix[0][2] != " " and result_matrix[1][0] != " " and result_matrix[1][1] != " " and result_matrix[1][2] != " " and result_matrix[2][0] != " " and result_matrix[2][1] != " " and result_matrix[2][2] != " ":
        print("the match is draw")
        return True
    

    # straight lines check
    for i in range(0,3):
        if result_matrix[i][0] == result_matrix[i][1] == result_matrix[i][2] == b:
            print('{} column is same {}'.format(i,b))
            print('{} won'.format(b))
            return True
    for j in range(0,3):
        if result_matrix[0][j] == result_matrix[1][j] == result_matrix[2][j] == b:
            print('{} column is same {}'.format(j,b))
            print('{} won'.format(b))
            return True

# main game loop
for n in range(1,10):
    c = False

    # even number n means O turn
    if n%2 == 0:
        position = get_input()
        x = position[0]
        y = position[1]
        if matrix[x][y] != 'X':
            matrix[x][y] = 'O'
        c = check_matrix(matrix,"O")
        show_matrix(matrix)
        if c == True:
            break

    # odd number n means x turn
    elif n%2 != 0:
        position = get_input()
        x = position[0]
        y = position[1]
        if matrix[x][y] != 'O':
            matrix[x][y] = 'X'
        c = check_matrix(matrix,"X")
        show_matrix(matrix)
        if c == True:
            break
        