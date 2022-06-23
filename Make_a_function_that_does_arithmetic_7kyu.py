# Make a function that does arithmetic!
# add subtract multiply divide

def arithmetic(a, b, operator):
    ops = {"add": a+b, "subtract": a-b, "multiply":a*b, "divide":a/b}
    return ops[operator]

    
print(arithmetic(1,2,"add"))