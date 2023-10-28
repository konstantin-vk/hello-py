print ("STRING")
some_str = """1
2
3
"""
print (some_str)
print (type(some_str))
print (id(some_str))
print ( some_str.index("1")) #error wjhen not cound : ValueError: substring not found
some_str1 = some_str.replace("1",'2')
print (some_str)


print ("INT")
i = int("2")
print (i)
print(pow(1,3))


print ("FLOAT")
f = 1.7
print (f)
print (int(f))


print ("COMPLEX")
complex_a = 3+1j
complex_b = 4+2j
print (complex_a + complex_b) 
print (complex_a *  complex_b) 



print ("BOOL")
is_true = True 
print (not is_true)
print (bool(True))
print (bool(is_true))
print (bool(1>2))

print ("TYPE CONVERSION")

