#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Если в кортеже есть хотя бы одна пара одинаковых соседних элементов,
# то напечатать все элементы, следующие за элементами первой из таких пар

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = ([1, 3], [4, 4], [2, 5], [3, 6], [4, 7], [4, 8], [7, 9], [7, 11])
    j = len(A)

    for item in A:
        if item[0] == item[1]:
            i = A.index(item)
            break

    print(A[i:j])
