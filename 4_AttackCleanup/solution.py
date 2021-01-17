# This challange was worded somewhat poorly so I wasn't sure
# about the edge cases that might have been there

# The first solution that came to my mind was using a hashtable to save our character translatiosn
# make a iter object which is always 1 except when there is a number in the string, then we change iter to the number

def restore_data(message):
    from collections import Counter
    
    dec_message = ""
    iter = 1
    translator = Counter({
        "z":"a",
        "g":"t",
        "x":"c"
    })
    
    for x in message:
        if x in translator:
            dec_message += translator[x] * iter
            iter = 1
        else:
            try:
                iter = int(x)
            except ValueError:
                for key,val in translator.items():
                    if x == val:
                        dec_message += key * iter
                        iter = 1
                
    return dec_message

print(restore_data("zgtxtxzgtxtxz") == "atgcgcatgcgca")
print(restore_data("gtxgtxzg3z8g4txz3g3z") == "tgctgcataaattttttttggggcatttaaa")