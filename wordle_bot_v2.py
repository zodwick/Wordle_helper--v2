

def load():
    file = open('five_letter_words.txt','r')
    lines = file.readlines()
    words=list(i[0:5] for i in lines )
    # print(words)
    
    

def input_params():
    grey:str=input("Enter the elements that were greyed out -no need to put spaces in between --  ")
    yellow:str=input('Enter the elements that are yellow along wihh their positions(0-4)'
                 'eg: 0a2x4i'
                 '    4k2s ' )
    green:str=input('Enter the greened elements along wihh their positions(0-4)'
                 'eg: 0a2x'
                 '    4k2s ' )
    
    
    #['03', '4k'] format
    #['a','b'] format 
    
    #greyed out words
    lgrey_words=list(grey.strip())
    lgrey_words= [*set(lgrey_words)]
    
    
    #yellowed out words
    lyellow_words=list(i for i in yellow.strip() if i.isalpha())
    lyellow_words= [*set(lyellow_words)]
    lyellow_with_pos=[]
    for i in range(0,len(yellow),2):
        lyellow_with_pos.append(yellow[i:i+2])
        
        
    #greened out words
    lgreen_words=list(i for i in green.strip() if i.isalpha())
    lgreen_words= [*set(lgreen_words)]
    lgreen_with_pos=[]
    for i in range(0,len(green),2):
        lgreen_with_pos.append(green[i:i+2])


    return (lgrey_words, lyellow_words, lgreen_words, lyellow_with_pos, lgreen_with_pos)
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def main():
    load()
    params:tuple=input_params()    
    lgrey_words=params[0]
    lyellow_words=params[1]
    lgreen_words=params[2]
    lyellow_with_pos=params[3]
    lgreen_with_pos=params[4]
    

    
    
if __name__ == '__main__':
    main()
    
    
