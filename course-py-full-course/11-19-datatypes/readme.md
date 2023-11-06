
type()
    <class 'str'>


# STRING 

ma_name = "SOMETHING SOMETHING"
greatings = 'HELLO'


len(str)
string_varuablep[0]
string_variable[0:10]
str.upper ()
str.replace ()   = origianl woth NO changes 
str.count ()
str.index ()
str.capitalize ()
str.lower ()



# INT 


int(string|logical|etc) = error 
pow()   = power

i = 3_000_001


# FLOAT 
f=1.2
int(f)   = like trunc 


# COMPLEX 
complex_a = 3+1j



# BOOL
is_true = True
bool(  value  )



# TYPE CONVERSION
не выполняет неявную конвертацию 

str()
int()
float()
tuple()
list()
set()
        // error if impossible to convert 


# LIST (array \ списки)

список - упорядоченная последовательность символов.
fruits = ['apple','grape','banana']
ids = [1,100,12,1115]
all-together  = [ 1 , 10.1 , 'grape' , ':)' , ['1','2'] ] 
len()
lst[0] , lst[1] , lst[-1]=last element
del lst[1] = delete second
del lst[-1] = delete the last 

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
print (usersp[1]['name'])

## List methods 

append()
pop()
remove()
clear()
insrt()
sort()
index()
clear()
copy()
extend()
reverse()
countn()



## Convert to list 
  = list()

greeting = "Hello hello"
letters = list(greeting)

## List Functions 
min( mylist )
max( mylist )
sum()
len() 
list = list1 + list2 = [ LIKE UNION ALL ]  ie tethod __add__

## List to list 
new_list = old_list[0:1]   old_list[:2]   old_list[-2:] ... [:]


## Copying list 
new_list = old_list   == it is the same list !!!!
    id(new_list) = id(old_list)

correct ways 
new_list = old_list[:]
new_list = old_list.copy()
new_list = list(old_list)


## LIST SET TUPLE 
List -> SET mutable -> TUPLE immutable 


List	                                    | Set	                                | Tuple
-------------------------------------------------------------------------------------------------
Lists is Mutable	                        | Set is Mutable	                    | Tuple is Immutable
It is Ordered collection of items	        | It is Unordered collection of items	| It is Ordered collection of items
Items in list can be replaced or changed	| Items in set cannot be changed or replaced but you can remove and add new items.	| Items in tuple cannot be changed or replaced





# DICT   словарь

car = {
    'brand': 'Chevy' , 
    'brand': 'Chevrolet' ,  # overwrite previous value 
    'price': 10000 , 
    'engine_vol': 1.4 ,     # comma is allowed 
}

## DICT compare 
    ==    = compares by components 

## DICT get & change 
car['brand']
car.get('brand')
car['brand_logo'] = 'Chevy' = add new key 

## DICT variables in a dict 
brand_key_name = 'brand'
car[brand_key_name]

## DICT multilevel 
car = {
    'brand': 'Chevy' , 
    'brand': 'Chevrolet' ,  # overwrite previous value 
    'price': 10000 , 
    'engine': {
        'vol': 1.4 ,      
        'type': 'gas' ,
    }
}

car['engine']['type']

## DICT length 
len( car )   => number of keys 

## DICT delete key 
del car['price']


## DICT noe existent ekys and get 
cal['model']   -> error 
car.get('model')  -> None = no error
car.get('model','default')  -> default  = no error

print ( car.__doc__ ) 

car.items()   == return dict_items - class 
car.keys()    == dict_keys 
car.popitem () 


---
# TUPLE (кортеж)
!!! unmutable 

my_tuple = (1.0,2,'three')
кортеж словарей , списков и тд - словарь менять можно !!! 
users = (
    {
        'user_id': '0'
        'user_name': 'root',
    }
)
users[0]['user_id'] = '-1'  -> OK !!! 


## TUPLE methods
count 
index 


# SET набор 
{}  -> like dict , but no key:value 
union (unique elements)


