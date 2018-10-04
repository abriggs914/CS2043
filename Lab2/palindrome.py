def palcheck(line, revline):
    half = (len(line) / 2)
    x = 0
    while(half > x):
        if(line[x] == revline[x]):
            x += 1
        else:
            return False
    return True

class palindrome :
    line = raw_input("Please enter a string:")
    print(line)
    print(line[::-1])
    revline = (line[::-1])
    if(palcheck(line, revline)):
        print "line", line, "is a palindrome"
    else:
        print "line", line, "is not a palindrome"