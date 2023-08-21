""" x = 'rojos'

def miColor():
    print(x)
    
miColor()

#puedo imprimir el color varias veces si deseo ya que la funcion es llamada
print(x)
print(x)
print(x) """

""" If you operate with the same variable name inside and outside of a 
function, Python will treat them as two separate variables, 
one available in the global scope (outside the function) 
and one available in the local scope (inside the function): """

""" x = 'rojos'

def miColor():
    x = 'verde'
    print(x)
    
miColor()
print(x) """

""" If you need to create a global variable, but are stuck 
in the local scope, you can use the global keyword.
The global keyword makes the variable global. """

""" def color():
    global i
    i = 'naranja'
color()
print(i)
     """
     
""" To change the value of a global variable inside a function,
refer to the variable by using the global keyword:
 """
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)