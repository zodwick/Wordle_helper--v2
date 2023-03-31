file = open('five_letter_words.txt','r')
lines = file.readlines()
words=list(i[0:5] for i in lines )
# print(words)


def input_params():
    grey:str=input("Enter the elements that were greyed out -no need to put spaces in between --  ")
    yellow:str=input('Enter the elements that are yellow along wihh their positions(0-4)'
                 'eg: 0a2x4i'
                 '    4k2s ' )
    green=input('Enter the greened elements along wihh their positions(0-4)'
                 'eg: 0a2x'
                 '    4k2s ' )
    
    lgrey=list(grey.strip())
    # print(lgrey)

    lyellow_with_pos=[]
    for i in range(0,len(yellow),2):
        lyellow_with_pos.append(yellow[i:i+2])

    #['03', '4k'] formt        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def main():
    input_params()
    
    
if __name__ == '__main__':
    main()
    
    
