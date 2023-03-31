
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


# def pos_check(word:str, set:list):
#     for i in set:
#         #i = '0a'
#         if word[int(i[0])]!=i[1]:
#             return False
#     return True


# print(pos_check('hello', ['0h', '1l']))


# words=["hello","heiooo","llovvee"]
# lyellow_with_pos=['1h', '1l']


# def check_individual(word:str, set:str):
#     if word[int(set[0])]!=set[1]:
#             return False
#     return True

# filter3=[]
    
# for i in list(words):
#         for j in lyellow_with_pos:
            
#              if check_individual(i,j):
#                  filter3.append(i)
                 
# print(filter3)
            
            
# def suggestions(list):
#     string_test=""
#     for i in list:
#         string_test+=i
#     char_freq={}

#     for i in string_test:
#         if i in char_freq:
#             char_freq[i]=char_freq[i]+1
#         else:
#             char_freq[i] = 1
            
    
#     sorted_frequency = sorted(char_freq.items(), key=lambda x:x[1], reverse=True)
#     sorted_letters=[i[0] for i in sorted_frequency]
#     sorted_letters=sorted_letters[0:5]
#     #letters sorted by their frequency eg: ['e', 'l', 'o', 'h'] where e is most frequent and h is least frequent
    
#     prime_suggestions=[]
        


# words=["hello","heiooo","llovvee"]

# suggestions(words)


l=[]
print(len(l))