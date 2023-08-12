def foo():
    bar([], 0)

def bar(x, m):
    print(f"{x} {m}")
    if m <= 2:
        bar(x+[len(x)+100], m+1)
    elif m < 4:
        bar(x, m+1)
    print(f"{x} {m}")

foo()