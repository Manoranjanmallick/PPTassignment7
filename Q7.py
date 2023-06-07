s = "ab#c"
t = "ad#c"

def processString(s):
    l = []
    for i in s:
        if i != '#':
            l.append(i)
        elif l:
            l.pop()
    return ''.join(l)

if processString(s) == processString(t):
    print ("true")


