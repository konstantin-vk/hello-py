#use print and dir 


print (10 , 11, "!")
print (dir())
print (dir(__builtins__)) # список встроенных в питон функций 
print (input("Enter your name: "))    # так нельзя - только выполнить в питоне\терминале 
name = input("Enter your name: ")
print (name) 
print ( name.capitalize() )
print ( dir(name))
# print (dir(input))