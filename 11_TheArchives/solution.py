# The challange consisted of checking string format which I've done
# using regex and then doing a simple calculation

def get_check_digit(input):
    import re
    r = re.compile('\d-\d{2}-\d{6}-x')
    if len(input) == 13:
        if r.match(input):
            stripped = input[:-2].replace("-","")
            s = 0
            for index, num in enumerate(stripped):
                s += int(num) * (index+1)
            return(s % 11)
    return -1

print(get_check_digit("-19-852663-x"))