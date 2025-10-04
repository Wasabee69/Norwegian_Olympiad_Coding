##





def solve(s):
    s = int(s)
    for i in range(1, 1000):
        a = i
        b = s-i
        if a+b == s and a != 0 and b != 0 and -1000 < b  < 1000:
            return f"{a} {b}"
        a = -i
        b = s+i
        if a+b == s and a != 0 and b != 0 and -1000 < b < 1000:
            return f"{a} {b}"
    return f"weird"
            
    

test = input()
print(solve(test))






