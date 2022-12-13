#1
# import random
# def bubble_sort(array):
#     for i in range(0, len(array) - 1):
#         for j in range(len(array) - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array
# lst = list(range(100))
# random.shuffle(lst)
# print("Sorted array: ", bubble_sort(lst))

#2
# dict = {'black':(0, 0, 0),'lavender':(230, 230, 250), 'blue':(0, 0, 255), 'white':(255, 255, 255), 'aquamarine':(127, 255, 212) }
# print(dict.items())

#3
first_set = {27, 7, 3, 49, 20, 25}
second_set = {25, 4, 81, 20, 9, 3}
print("Included in both sets at the same time: ", first_set.intersection(second_set))
print("Included only in the first set, but not included in the second: ", first_set.difference(second_set))
print("Included only in the second set, but not included in the first: ", second_set.difference(first_set))
print("Included in the first or the second, but not both of them at the same time: ", first_set.symmetric_difference(second_set))
