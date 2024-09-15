#!/usr/bin/python3
"""Solving the N Queens problem"""
import sys


def check_here(nlist, index, curr_num):
    for item in nlist:
        if index == item[1] or\
                index == item[1] - (curr_num - item[0]) or\
                index == item[1] + (curr_num - item[0]):
            return 1
    return list([curr_num, index])


def loop_n_find(nlist, curr_num, layout):
    if (curr_num > layout):
        return

    if len(nlist) == layout:
        print(nlist)
        return

    j = 0
    while j < layout:
        val = check_here(nlist, j, curr_num)
        if type(val) is list:
            new_nlist = nlist.copy()
            new_nlist.append(val)
            loop_n_find(new_nlist, curr_num + 1, layout)
        j += 1
    return


def solve_nqueens(layout):
    for i in range(layout):
        arr = [[0, i]]
        loop_n_find(arr, 1, layout)


if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not args[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    layout = int(args[1])
    if layout < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(layout)