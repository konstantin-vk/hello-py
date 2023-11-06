##########################################
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

#############################################
print ("INT")
i = int("2")
print (i)
print(pow(1,3))

#############################################
print ("FLOAT")
f = 1.7
print (f)
print (int(f))

##################################################
print ("COMPLEX")
complex_a = 3+1j
complex_b = 4+2j
print (complex_a + complex_b) 
print (complex_a *  complex_b) 


##################################################
print ("BOOL")
is_true = True 
print (not is_true)
print (bool(True))
print (bool(is_true))
print (bool(1>2))
################################################
print ("TYPE CONVERSION")

###############################################
print ("LIST")
users = [
    {
        'name':"My Name",
        'id' : 1
    },
    {
        'name':'The Name',
        'id': 2

    }
]
print (users[1]['name'])
###########################################################
print ('LIST')
my_numbers = [0, 10, 20, 30, 40]
print( dir(my_numbers))
my_numbers.append(10)
print ( my_numbers.count(10) )
my_numbers.insert(0,-1)
print (my_numbers)
my_numbers.clear()
print (my_numbers)   ## []
print (my_numbers.extend('abc')) ## [a,b,c] !!!!
print (my_numbers)

old_list = [1,2,3]
new_list_as_copy = old_list
print ( id (new_list_as_copy) == id(old_list)) ## = true 
new_list_as_new = old_list.copy()
print ( id (new_list_as_new) == id(old_list)) ## = false

##############################################################
print ("PRACTICAL PART")
# create list with 5 types 
# int float complex str bool 
lst = [1, 1.0 , 2+1j , "STR" , True]
# delete 3d 
del lst[3]  # !!!
print(type(2+1j))
# print len 
print (len(lst))
# reverese 
print (lst.reverse())
# new list with 2 elem 
lst2 = [1,2]
# extend first with all elemennts of the second one 
# lst.append(lst2)  nonon = [True, (2+1j), 1.0, 1, [1, 2]]
lst = lst + lst2 # yes yes yes
# print then 
print (lst)

#############################################################################3
print ("DICT")
car = {
    'brand': 'Chevy' , 
    'brand': 'Chevrolet' ,  # overwrite previous value 
    'price': 10000 , 
    'engine_vol': 1.4 ,     # comma is allowed 
}
print (car)
print ( car.get('brand') )
print (  car['brand'] )
car['brand_logo'] = 'Chevy'



car = {
    'brand': 'Chevy' , 
    'brand': 'Chevrolet' ,  # overwrite previous value 
    'price': 10000 , 
    'engine': {
        'vol': 1.4 ,      
        'type': 'gas' ,
    }
}

print ( car['engine']['type'] ) 
##########################################################################

print ("DICT practicval")
# crate empty dict 
dct = {}
# 3 times ask to enter key-calue 
for i in range(3):
    key = input("Enter key")
    value = input("Enter value" )
    # add values one by one 
    dct[key]=value
# print 1
print(dct)


#######################################
print("TUPLE")
#######################################
print ("SET")
