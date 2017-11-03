dictionary={'ana':'B','John':'A+'}
print(dictionary['ana'])
dictionary['Salvatory'] = 'O'
print(dictionary)


newd = {}
newd['test1','a']='a'
newd['test2']='b'
newd['test3']='c'
newd['test2']='d'
print(newd)
del(newd['test2'])
print(newd)

#this doesn't work
#del(newd['test1'])

print(newd.keys())
print(newd.values())

