##





def solve(s):
    s = int(s)
    if s == -1:
        return f"{s+2} {-2}"
    if s < 999:
        return f"{s+1} {-1}"
    return f"{s-1} {1}"
            
    

test = input()
print(solve(test))







