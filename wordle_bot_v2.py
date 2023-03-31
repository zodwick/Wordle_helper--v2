file = open('five_letter_words.txt','r')
lines = file.readlines()
words=list(i[0:5] for i in lines )
# print(words)