
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

# if "a" and "b" and "c" in "banan":
#     print("yes")



def find_prime_suggestions(word_list, sorted_letters):
    word_set = set(word_list)
    max_num_letters = 0
    prime_suggestions = []
    for num_letters in range(len(sorted_letters), 0, -1):
        for word in word_set:
            if all(letter in word for letter in sorted_letters[:num_letters]):
                if num_letters > max_num_letters:
                    max_num_letters = num_letters
                    prime_suggestions = [word]
                elif num_letters == max_num_letters:
                    prime_suggestions.append(word)
        if len(prime_suggestions) >= 3:
            return list(set(prime_suggestions))
    return list(set(prime_suggestions))


# print(find_prime_suggestions(["anand","el","elo","eloh"], ['e', 'l', 'o', 'h']))

word_list = ["apkwple", "baneilmnaa", "peackwh", "pearkwo", "plumi"]
sorted_letters = ["a", "e", "i", "l", "m", "n", "o", "p", "r"]

prime_suggestions = find_prime_suggestions(word_list, sorted_letters)
print(prime_suggestions)