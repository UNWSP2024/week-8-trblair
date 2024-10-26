# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    upper=0
    thing=""
    for i in sentence:
        if(i.isupper()):
            thing+="*"+i
        else:
            thing+=i
    stringlist=thing.split("*")
    stringlist.remove('')
    for x in range(0,len(stringlist)):
        for character in stringlist[x]:
            if character.isupper():
                if upper == 0:
                    upper=1
                elif upper==1:
                    stringlist[x]=stringlist[x].lower()
    new_sentence=' '.join(stringlist)
    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
