# This is a very ease and fast solution in python, after
# I realized that it is a ROT-13 cipher

def halliday(self, message):
    import codecs
    # with ROT-13 it doesn't matter if you encode or decode because it's just a shift
    return codecs.encode(message,"rot13")