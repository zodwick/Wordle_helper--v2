
# h=input('Enter the greened elements along wihh their positions(0-4)')
# print(list(h))
#return empty list



from operator import and_, or_
from functools import reduce

def containsAll(str, set):
    return reduce(and_, map(str.__contains__, set))


print(containsAll('hello', ['h', 'e', 'l',"f"]))