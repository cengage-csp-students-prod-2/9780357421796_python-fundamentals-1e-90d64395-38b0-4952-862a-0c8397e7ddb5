# Write your code here
def skip_integers(*args):
    for arg in args:
        if isinstance(arg, int):
            continue
        print(arg)
        
skip_integers(3, 5.2, "value", 6.0)