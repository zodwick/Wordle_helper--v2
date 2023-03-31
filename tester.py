
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


# print(pos_check('hello', ['0h', '1l']))


words=["hello","heiooo","llovvee"]
lyellow_with_pos=['1h', '1l']


def check_individual(word:str, set:str):
    if word[int(set[0])]!=set[1]:
            return False
    return True

filter3=[]
    
for i in list(words):
        for j in lyellow_with_pos:
            
             if check_individual(i,j):
                 filter3.append(i)
                 
print(filter3)
            