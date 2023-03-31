
# h=input('Enter the greened elements along wihh their positions(0-4)')
# print(list(h))
#return empty list



# from operator import and_, or_
# from functools import reduce

# def containsAll(str, set):
#     return reduce(and_, map(str.__contains__, set))


# print(containsAll('hello', ['h', 'e', 'l',"f"]))


# def containsAny(str, set):
#     return reduce(or_, map(str.__contains__, set))

# print(containsAny('hello', ["p","f"]))


def pos_check(word:str, set:list):
    for i in set:
        #i = '0a'
        if word[int(i[0])]!=i[1]:
            return False
    return True


print(pos_check('hello', ['0h', '1l']))