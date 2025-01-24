d = {"a": 1, "b":2, "c":3, "d":4, "e":5 }

def funcd(d,v):
    for key in d:
        if d[key] == v:
            return key
    return dict()
    
#print(funcd(d,3))

for i in d:
    print(f" The key {i} has a value of {d[i]}")


print(d.items())