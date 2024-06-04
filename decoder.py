'''
Prompt:
Decode an input.txt file made up of strs delimited by whitespace and newline. example:

    "3 love\ncomputers\n2 dogs\n4 cats\n1 I\n5 you"

Using encoded numbers given in a pyramid scheme and a list of "safe words" to determin msg:
       1
      2 3
     4 5 6

Result should be:

    "I love computers"
    
'''


# import/open files

# input files
decoder_file= "3 love\n6 computers\n2 dogs\n4 cats\n1 I\n5 you"
encoded_file = "  1\n 2 3\n4 5 6"
safe_words = ['I', 'love', 'computers']


#convert to dict using comprehension
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def Decode(encoded, decoder, safe):
    decoded_msg = ""

    for i in encoded:
        if decoder.get(i) in safe_words:
            decoded_msg += decoder.get(i) + " "

    return decoded_msg

print (Decode(encoded_file.split(), Convert(decoder_file.split()), safe_words))
