#!/usr/bin/python


"""Algorithm to solve pascal triangle"""
def pascal_triangle(n):
    lists = [[1]]
    for i in range(2, n + 1):
        ls = []
        for j in range(1, i + 1):
            if j == 1:
                ls.append(1)
            elif j == i:
                ls.append(1)
            else:
                prev = lists[-1]
                sums = prev[j - 2] + prev[j - 1]
                ls.append(sums)
        #print(ls)
        lists.append(ls)
        
    return lists  
    