


from numpy import number


file = open('C:/Users/Abdullah/Desktop/test/New folder/src.txt','rt')

store=''
mainList=[]
while 1:
    char = file.read(1)
    if not char:
        #if the end is empty or store is, Don't append
        if(store!=''):
            mainList.append(store)
        break
    # if space, new line add the previous word to list
    elif (char==' ' or char=='\n' or char=='\t'):
        if(store!=''):
            mainList.append(store)
        store=''
    # if +,-,*,/ append it to the list too    
    elif (char=='+' or char=='-' or char=='*' or char=='/' or char=="="):
        
        if(char!=file.read(1)):
            if(store!=''):
                mainList.append(store)
            store=''
            mainList.append(char)
                    
        else:
            if(store!=''):
                mainList.append(store)
            store=''
            mainList.append(char+char)
            file.read(0)
            
        
    else:
        store=store+char

file.close()    
print(mainList) 
a= [0,1,2,3,4,5,6,7,8,9,10]
if 'int' in mainList:
    print('keyword')
if 'a'or 'b'or 'c'or 'd'or 'e'or 'f'or 'g'or 'h'or 'i'or 'j'or 'k'or 'l'or 'm'or 'n'or 'o'or 'p'or 'q'or 'r'or 's'or 't'or 'u'or 'v'or 'w'or 'x'or 'y'or 'z' or'_'  in mainList:
    print("Variable")
if '++' or '--' in mainList:
    print('counter')
if '{' or '}' or '=' in mainList:
    print('identifier')
for i in a:
    if str(i) in mainList:
        print("number")