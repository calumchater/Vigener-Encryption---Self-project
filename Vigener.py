#Automatic Vigener Encryptor
while True:
    choice = input("Enter e if you want to encrypt, or d if you want to decrypt : ").lower()
    if choice =="e":
        alpha = "abcdefghijklmnopqrstuvwxyz"
        message = input("What do you want to encrypt ? ").lower()
        keyword = input("What keyword do you want to use ? ").lower()
        keywordValues = []
        finalValues = []
        for keywordLoop in range(len(keyword)):
            for alphaLoop in range(len(alpha)):
                if keyword[keywordLoop]== alpha[alphaLoop]:
                    keywordValues.append(alpha.index(alpha[alphaLoop]))
                else:
                    alphaLoop += 1
            keywordLoop += 1
        for i in range(len(message)):   #this gets us the values of the 
            if message[i]==" ":
                finalValues.append(" ")
            else:
                for x in range(len(alpha)):
                    if message[i]==alpha[x]:
                        finalValues.append(alpha.index(alpha[x]))    
                    else:
                        x+=1
            i+=1
        finalLetters = []
        y = 0
        t=0
        for y in range(len(message)):
            if finalValues[y] == " ":
                print(" ",end="")    
            else:
                addition = (finalValues[y]+keywordValues[(t)%len(keyword)])%26
                print(alpha[addition],end="")
                t += 1
        break
#print the letter with the keyword[len(keyword)] added on. We will get that
#value through the alpha index

#Automatic Vigener Decryptor
    elif choice=="d":
        alpha = "abcdefghijklmnopqrstuvwxyz"
        message = input("What do you want to decrypt ? ").lower()
        keyword = input("What keyword do you want to use ? ").lower()
        keywordValues = []
        finalValues = []
        for keywordLoop in range(len(keyword)):
            for alphaLoop in range(len(alpha)):
                if keyword[keywordLoop]== alpha[alphaLoop]:
                    keywordValues.append(alpha.index(alpha[alphaLoop]))
                else:
                    alphaLoop += 1
            keywordLoop += 1
        for i in range(len(message)):   #this gets us the values of the 
            if message[i]==" ":
                finalValues.append(" ")
            else:
                for x in range(len(alpha)):
                    if message[i]==alpha[x]:
                        finalValues.append(alpha.index(alpha[x]))    
                    else:
                        x+=1
            i+=1
        finalLetters = []
        y = 0
        t=0
        for y in range(len(message)):
            if finalValues[y] == " ":
                print(" ",end="")    
            else:
                addition = (finalValues[y]-keywordValues[(t)%len(keyword)])%26
                print(alpha[addition],end="")
                t += 1
        break
    print("That's not a valid choice")
        
#print the letter with the keyword[len(keyword)] added on. We will get that
#value through the alpha index
