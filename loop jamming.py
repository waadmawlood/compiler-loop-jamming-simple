
filename = "source.txt"
blocks = [];

with open(filename) as source:                       #difine file to get string (input.txt)
    data = source.read()                             #read all lines
    data = data.strip()                              #remove whitespace from start and end of line string

    #remove whitespace between words in line string
    data = data.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")

    temp = ""                   #flag variable
    indexSemi = 0               #flag variable
    isFor = 0                   #flag variable
    for i in range(len(data)):  #read char by char

        if data[i] == 'f':      #if there is "for" in string
            if (data[i+1] == 'o' and data[i+2] == 'r' and data[i+3] == '(') or (data[i+1] == 'o' and data[i+2] == 'r' and data[i+3] == ' ' and data[i+4] == '('):
                isFor = 1

        #get all for with statement ( for(..;...;..) ....;  ) put it in [blocks]      
        if isFor == 1:
            ch = data[i]
            if ch == ';':
                indexSemi += 1
                temp += ';'
                if indexSemi > 2:
                    indexSemi = 0
                    blocks.append(temp)
                    temp = ""
                    isFor = 0
            else:
                temp += ch

print("\n==================== Before ======================")        
print(data)

  
sameFor = []            #list of same for

#put same for in [samefor] from [blocks]
for i in range(len(blocks)):
    blocks[i] = blocks[i].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")
    st = blocks[i];
    temp1 = st[:st.index(')')+1]
    for j in range(i+1,len(blocks)):
        blocks[j] = blocks[j].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")
        temp2 = blocks[j]
        if temp1 in temp2:
            sameFor.append([i,j])


#remove whitespace data            
data = data.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")

#remove 1 for and put content in another for
for i in range(len(sameFor)):
    for1=sameFor[i][0]
    for2=sameFor[i][1]
    
    st1 = blocks[for1];
    st2 = blocks[for2];
    
    temp = st1[:st1.index(')')+1]
    temp1 = st1[st1.index(')')+2:]
    temp2 = st2[st2.index(')')+2:]
    
    result = temp + "\n{\n" + temp1 + "\n" + temp2  + "\n}"
    
    data = data.replace(st1,result).replace(st2,"")


print("\n==================== After ======================")        
print(data)


target = open("target.txt","w")                     #difine file to write string into (target.txt)
target.write(data)                                  #write text in file target
source.close()
target.close()
print("\n\n\ndone in target.txt...")
