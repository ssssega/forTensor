from itertools import chain
print("\n New Year is coming! \n")
print("\n".join(chain((('* ' * i + '*').rjust(7 * 2 + i) for i in range(5)), (('* ' * i + '*').rjust(7 * 2 + i) for i in range(1, 7)), (('* ' * i + '*').rjust(7 * 2 + i) for i in range(1, 9)))))