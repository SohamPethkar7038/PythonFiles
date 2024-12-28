#  In Python, scope refers to the region of the code where a variable is defined and accessible

# 01 Local scope

# Variables defined inside a function or a block are local to that function or  block.
# They can only be accessed within that function or block.

# def my_function():
#     x = 10  # Local variable
#     print(x)

# my_function()
# print(x)  # Error: x is not accessible outside the function


# 2. Enclosing Scope
#  This applies to nested functions.
#  Variables in the outer (enclosing) function's scope are accessible to the  inner (nested) function.


'''def outer_function():
    x = "Outer variable"
    
    def inner_function():
        print(x)  # Accessing the enclosing variable
    
    inner_function()

outer_function() '''



# 3. Global Scope
# Variables defined outside any function or block are in the global scope.
# They can be accessed anywhere in the module but must be explicitly declared as global if modified inside a function.

'''
x = "Global variable"
def my_function():
    global x  # Declares x as global to modify it
    x = "Modified global variable"


# my_function()
#print(x)  # Outputs: Modified global variable
'''


# 4. Built-in Scope
# This is the outermost scope and includes Python's built-in names like len, print, int, etc.
# These are available everywhere in the code.

print(len([1, 2, 3]))  # len is a built-in function