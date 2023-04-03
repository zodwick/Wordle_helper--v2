
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



# def find_prime_suggestions(word_list, sorted_letters):
#     word_set = set(word_list)
#     max_num_letters = 0
#     prime_suggestions = []
#     for num_letters in range(len(sorted_letters), 0, -1):
#         for word in word_set:
#             if all(letter in word for letter in sorted_letters[:num_letters]):
#                 if num_letters > max_num_letters:
#                     max_num_letters = num_letters
#                     prime_suggestions = [word]
#                 elif num_letters == max_num_letters:
#                     prime_suggestions.append(word)
#         if len(prime_suggestions) >= 3:
#             return list(set(prime_suggestions))
#     return list(set(prime_suggestions))


# # print(find_prime_suggestions(["anand","el","elo","eloh"], ['e', 'l', 'o', 'h']))

# word_list = ["apkwple", "baneilmnaa", "peackwh", "pearkwo", "plumi"]
# sorted_letters = ["a", "e", "i", "l", "m", "n", "o", "p", "r"]

# prime_suggestions = find_prime_suggestions(word_list, sorted_letters)
# print(prime_suggestions)



# from collections import Counter

# def most_common_char(word):
#     """
#     Returns the count of the most common character in a word.
#     """
#     counter = Counter(word)
#     if len(counter) > 0:
#         return counter.most_common(1)[0][1]
#     else:
#         return 0

# def sort_words_by_most_common_char(words):
#     """
#     Sorts a list of words by the occurrence of the most repeated characters in the word.
#     """
#     return sorted(words, key=most_common_char, reverse=True)

# # Example usage
# words = ['hello', 'world', 'python', 'programming', 'language']
# sorted_words = sort_words_by_most_common_char(words)
# print(sorted_words)  # Output: ['programming', 'python', 'hello', 'world', 'language']


# from collections import Counter

# def most_common_chars(word):
#     """
#     Returns the concatenation of the counts of the three most common characters in a word.
#     """
#     counter = Counter(word)
#     if len(counter) > 0:
#         return "".join(str(count) for char, count in counter.most_common(5))
#     else:
#         return "0"

# def sort_words_by_most_common_chars(words):
#     """
#     Sorts a list of words by the occurrence of the first three most repeated characters in the word.
#     """
#     return sorted(words, key=most_common_chars, reverse=True)

# # Example usage
#  # Output: ['programming', 'python', 'hello', 'world', 'language']


# def test(list):
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
#     print(sorted_letters)
    
    
    
# words =['movie', 'comic', 'robin', 'toxic', 'sonic', 'orbit', 'socio', 'bowie', 'motif', 'boris', 'doris', 'rosie', 'fomit', 'ionic', 'toxin', 'tonic', 'comix', 'ortiz', 'visio', 'josie', 'jodie', 'roxio', 'comin', 'modis', 'tobin', 'sitio', 'ronin', 'vomit', 'toric', 'orvis', 'medio', 'movin', 'vidio', 'morin', 'godin', 'rubio', 'curio', 'ozzie', 'ouvir', 'orrin', 'orgie', 'orbis', 'indio', 'moxie', 'rodin', 'nomic', 'oemig', 'junio', 'cokin', 'mobic', 'fisio', 'kerio', 'tokio', 'joris', 'toeic', 'bodie', 'rosin', 'ennio', 'youie', 'bovis', 'sofie', 'docid', 'verio', 'conic', 'sowie', 'roxie', 'omnis', 'konig', 'regio', 'cowie', 'bomis', 'bogie', 'serio', 'jobim', 'robie', 'sorin', 'dobie', 'nobis', 'monit', 'boric', 'vobis', 'rerio', 'ofbiz', 'stdio', 'movis', 'yogic', 'tobit', 'sosig', 'yukio', 'rufio', 'bonin', 'doric', 'cobit', 'ossig', 'vedio', 'corin', 'torii', 'tomie', 'ossie', 'offic', 'obgin', 'yogis', 'genio', 'orbix', 'domin', 'motiv', 'mowie', 'oogie', 'orkin', 'corio', 'dokic', 'rocio', 'souix', 'orris', 'ozric', 'vizio', 'monic', 'oswin', 'sonix', 'eosin', 'bodin', 'dovid', 'moniz', 'gorin', 'sobig', 'xonix', 'monin', 'notis', 'sobie', 'dokie', 'torin', 'fumio', 'rotic', 'kivio', 'nodig', 'zinio', 'jobid', 'zowie', 'sonig', 'oddie', 'monik', 'rowid', 'norio', 'modif', 'tonio', 'novis', 'noris', 'somis', 'zomig', 'dodie', 'dorie', 'cinio', 'berio', 'mikio', 'sirio', 'jobin', 'monie', 'corie', 'kunio', 'nomis', 'dowie', 'envio', 'muzio', 'dorit', 'bceio', 'novib', 'cokie', 'mimio', 'doxie', 'iorio', 'robic', 'eieio', 'somit', 'bonis', 'codie', 'mosix', 'obeid', 'fusio', 'dorin', 'mosin', 'ronit', 'kozik', 'jorie', 'osdir', 'movir', 'novie', 'socie', 'cowin', 'notiz', 'morir', 'comit', 'borin', 'invio', 'dosis', 'nogin', 'modin', 'revio', 'goyim', 'sonik', 'zorin', 'iosif', 'denio', 'gobin', 'yowie', 'jokin', 'torie', 'oskit', 'romic', 'nonin', 'movix', 'moris', 'tomic', 'ronis', 'donie', 'eotic', 'vicio', 'furio', 'juvio', 'mobis', 'obdii', 'romig', 'nosig', 'cosis', 'rotis', 'foxit', 'tonie', 'wobib', 'novio', 'korin', 'enxio', 'rovin', 'morio', 'donic', 'oisin', 'seqio', 'didio', 'sonin', 'orgin', 'fomin', 'tonid', 'offix', 'dojin', 'xotic', 'nosis', 'comis', 'gofit', 'romio', 'kyrio', 'tobie', 'fotis', 'fonix', 'netio', 'nofib', 'rotie', 'cogic', 'oyric', 'ownik', 'tokin', 'forio', 'gomis', 'motic', 'gouin', 'obvis', 'wowie', 'bozic', 'nonie', 'tonik', 'srtio', 'orgid', 'goris', 'cosix', 'ocsig', 'sigio', 'fujio', 'odzie', 'foris', 'covic', 'sodic', 'recio', 'orwig', 'momin', 'codis', 'kojic', 'coris', 'ottis', 'mobie', 'mosis', 'gonin', 'nodir', 'moyie', 'zonis', 'cosic', 'dovie', 'ottie', 'kovic', 'bosib', 'jovis', 'novit', 'bosio', 'gowin', 'toyin', 'movim', 'voris', 'komix', 'objid', 'bivio', 'orwin', 'donis', 'oggie', 'norie', 'sosin', 'rofin', 'jogin', 'cofio', 'rorie', 'notin', 'obsid', 'omvie', 'rozin', 'tomio', 'demio', 'foxie', 'moric', 'totie', 'kovie', 'oddio', 'gorie', 'norin', 'monix', 'totic', 'toxie', 'borie', 'sotic', 'moviw', 'jovie', 'movid', 'ortis', 'osric', 'romie', 'mocie', 'komik', 'senio', 'mofie', 'toxik', 'mogie', 'motio', 'mexio', 'novik', 'kobie', 'offit', 'movic', 'oifig', 'torit', 'jovin', 'konin', 'jovic', 'bouin', 'jogit', 'sumio', 'cirio', 'bowis', 'inbio', 'gotic', 'nonis', 'bobik', 'ornis', 'ontic', 'kuzio', 'jouir', 'kosik', 'totin', 'bobic', 'tonin', 'ondio', 'notif', 'codim', 'momir', 'modix', 'morii', 'jokic', 'bigio', 'gogie', 'nokii', 'bogin', 'gogio']
# sorted_words = sort_words_by_most_common_chars(words)

# test(words)

# #['sorin', 'ronis', 'ornis', 'noris', 'rosin']

# print(sorted_words[0:6]) 



l=["anand","anand","hello"]
print([set(l)])