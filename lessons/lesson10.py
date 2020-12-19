def swap(j, our_list):
    our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

#N*(N-1) ~= O(N^2)
def bubble_sort(my_list):
    N = len(my_list)
    for i in range(N):
        for j in range(N - 1):
            if my_list[j] > my_list[j+1]:
                swap(j, my_list)

    return my_list

list1 = [56, 33, 98, 1, 3, 7, 102, 908, 1]
print(bubble_sort(list1))

import sorting

sorting.merge