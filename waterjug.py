
def waterjug(j1, j2, target):
    visited = []
    path = []
    soln = []

    state = (0,0)
    store = [(state, path)]
    
    while store:
        (x,y), path = store.pop()

        if (x,y) is visited:
            continue
        visited.append((x,y))

        new_path = path + [(x,y)]

        if(x==target or y==target):
            soln.append(new_path)
            path=[]
            state = (0,0)
            store = [(state, path)]
            continue
        
        rules=[(j1,y), (x,j2), (0,y), (x,0), (x-min(x,j2-y), y+min(x,j2-y)), (x+min(j1-x,y), y-min(j1-x,y))]

        for state in rules:
            if state not in visited:
                store.append((state, new_path))

    return soln


j1=int(input("Enter the capacity of jug1: "))
j2=int(input("Enter the capacity of jug2: "))
target=int(input("Enter the target: "))

soln=waterjug(j1,j2,target)
if soln is None:
    print("No soln found")
else:
    k=0
    for i in soln:
        print(f"Soln {k}: {i}") 
        k=k+1