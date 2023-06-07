def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    s2 = s + s
    return goal in s2

s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))

