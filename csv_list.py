#working with csv headers in Python

headers = "name,age,city" #defines the headers
split_headers = headers.split(",") #splits each header into a list

index_name = split_headers.index('name') #looks for the index of the header with the name 'name'
index_city = split_headers.index('city') #looks for the index of the header with the name 'city'
index_age = split_headers.index('age') #looks for the index of the header with the name 'age'

print(index_name) #prints the index number of the header 'name', this is an integer
print(index_city) #prints the index number of the header 'city', this is an integer
print(index_age) #prints the index number of the header 'age', this is an integer