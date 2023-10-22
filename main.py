#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# First take each name and store it in to a variable
nameList= []


with open("./Input/Names/invited_names.txt") as temp:
    nameList = temp.readlines()
for x in range(0,len(nameList)):
    nameList[x] = nameList[x].strip()
with open("./Input/Letters/starting_letter.txt") as file:
    ogText = file.readlines()
    ogText = "".join(ogText)
for name in nameList:
    tempText = ogText.replace("[name]", name)
    with open("./Output/ReadyToSend/"+name+ ".txt", mode = "w") as x1:
        x1.write(tempText)