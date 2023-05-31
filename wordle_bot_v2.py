from functools import reduce
from operator import and_, or_

# frequency of ltters kand pidiumbol already present aayitola letters use cheyne is dumb ????????
# checking algorithms

def containsAll(str: str, set: list):
    return reduce(and_, map(str.__contains__, set))


def containsAny(str: str, set: list):
    return reduce(or_, map(str.__contains__, set))


def pos_check(word: str, set: list):
    for i in set:
        #i = '0a'
        if word[int(i[0])] != i[1]:
            return False
    return True


def check_individual(word: str, set: str):
    if word[int(set[0])] != set[1]:
        return False
    return True


# loading the words from the file
def load():
    file = open('five_letter_words.txt', 'r')
    lines = file.readlines()
    words = list(i[0:5] for i in lines)
    return words


# input parameters
def input_params(grey:str, yellow:str, green:str):
    print("****************************************************************************************")
    letters:str=input("enter the letters in the order they appear in the wordle :-")
    colors:str=input("enter the colors in the order they appear in the wordle : use g for grey , y for yellow and r for green :-").lower()
    
    
    if len(letters)!=len(colors):
        print("invalid input : length of letters and colors are not equal")
        return
    
    grey:str=grey.strip()
    yellow:str=yellow.strip()
    green:str=green.strip()
    
    for i in colors:
        if i not in "rgy":
            print("invalid color input")
            return
    
    for i in range(len(colors)):
        
        if colors[i]=="g":
            grey+=letters[i]
        elif colors[i]=="y":
            yellow=yellow+str(i)+letters[i]
        else:
            green=green+str(i)+letters[i]
            
    # print(grey,yellow,green)
            
            
        
    
    
        
    # grey: str = input(
    #     "Enter the elements that were greyed out -no need to put spaces in between --  ")
    # yellow: str = input('Enter the elements that are yellow along wihh their positions(0-4)'
    #                     'eg: 0a2x4i'
    #                     '    4k2s -- ')
    # green: str = input('Enter the greened elements along wihh their positions(0-4)'
    #                    'eg: 0a2x'
    #                    '    4k2s -- ')

    # ['03', '4k'] format
    # ['a','b'] format

    # greyed out words
    lgrey_words = list(grey.strip())
    lgrey_words = [*set(lgrey_words)]

    # yellowed out words
    lyellow_words = list(i for i in yellow.strip() if i.isalpha())
    lyellow_words = [*set(lyellow_words)]
    lyellow_with_pos = []
    for i in range(0, len(yellow), 2):
        lyellow_with_pos.append(yellow[i:i+2])

    # greened out words
    lgreen_words = list(i for i in green.strip() if i.isalpha())
    lgreen_words = [*set(lgreen_words)]
    lgreen_with_pos = []
    for i in range(0, len(green), 2):
        lgreen_with_pos.append(green[i:i+2])

    return (lgrey_words, lyellow_words, lgreen_words, lyellow_with_pos, lgreen_with_pos,grey,yellow,green)
    #['l', 't'] ['e', 'a'] ['r'] ['0a', '3e'] ['4r']


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


def suggestions(list):
    string_test = ""
    for i in list:
        string_test += i
    char_freq = {}

    for i in string_test:
        if i in char_freq:
            char_freq[i] = char_freq[i]+1
        else:
            char_freq[i] = 1

    sorted_frequency = sorted(
        char_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_letters = [i[0] for i in sorted_frequency]
    sorted_letters = sorted_letters[0:5]
    print(sorted_letters)

    return (find_prime_suggestions(list[0:int(len(list)/10) if len(list) > 100 else int(len(list)/4)], sorted_letters))
   
def suggestions_for_max_info(list:list,letters:list):
    print("suggestions for max info")
    
    l=[]
    for i in list:
        #i is a word
        flag=0
        for j in letters:
            #j is a letter
            if j  in i:
                flag=1
                break
        if flag==0:
            l.append(i)
    return l
        
    
    
    
    
    
    
    
    
def main():
    tries_no=1
    ch='y'
    grey = ""
    yellow = ""
    green=""
    while ch=='y':
        words = load()
        words_copy = words
        params: tuple = input_params(grey=grey, yellow=yellow, green=green)
        lgrey_words = params[0]
        lyellow_words = params[1]
        lgreen_words = params[2]
        lyellow_with_pos = params[3]
        lgreen_with_pos = params[4]
        grey += params[5]
        yellow += params[6]
        green += params[7]
        l_words_needed = lyellow_words+lgreen_words
        lgrey_words = [i for i in lgrey_words if i not in l_words_needed]
        filter1 = []
        filter2 = []

        # filtering out the words that contain all the letters in the yellow and green words
        for i in words:
            if len(l_words_needed) != 0:
                if containsAll(i, l_words_needed):
                    filter1.append(i)
            else:
                filter1 = words

            if len(lgrey_words) != 0:
                if not containsAny(i, lgrey_words):
                    filter2.append(i)
            else:
                filter2 = words

        words = set(filter1).intersection(set(filter2))

        # filtering out the words that contain the letters in the yellow and green words at the correct positions

        filter3 = []
        filter4 = []

        for i in list(words):
            # if not pos_check(i,lyellow_with_pos):
            #     filter3.append(i)
            # this is not correct  as repeating positions of yellow are not checked properly
            if pos_check(i, lgreen_with_pos):
                filter4.append(i)

        words = set(filter4).intersection(words)

        # filtering yellow

        for i in list(words):
            for j in lyellow_with_pos:

                if check_individual(i, j):
                    filter3.append(i)

        filtered_words = list(words.difference(set(filter3)))
        final_list = []

        for i in words_copy:
            if i in filtered_words:
                final_list.append(i)
                
        #rohit suggestion for max info in second try
        if tries_no==1:
            print("first try")
            letters = lgrey_words+lyellow_words+lgreen_words
            #removing words that contain letters in the first try
            final_list=suggestions_for_max_info(words_copy,letters)
        

        suggestion = suggestions(final_list)
            
            
            
            
        print(suggestion)

        print(len(final_list))
        # print(len(suggestion))

        print(final_list[0:10])
        
        tries_no+=1
        
        ch=input("Do you want to continue? (y/n)")

        #print(final_list)
    
    print("Thank you for playing <3" )





if __name__ == '__main__':
        main()
