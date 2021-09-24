from mod_c import *
import mod_b

# print(globals())
print(x)
print(mod_c.x)
print(mod_b.mod_c.x)

"""
    
Print 5.
There is a variable mod_c in mod_a

change x to a list `[1,2,3]`

Print 5.
There is a variable mod_c in mod_b, the same refference variable as variable mod_c in mod_a.


change import to `from x import *`

NameError: name 'mod_c' is not defined

There is not any variable mod_c in mod_a, only x. 
    
"""
    