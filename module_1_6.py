my_dict = {'anna':25, 'igor':30, 'lisa':16, 'lida':42}
print(my_dict)
print(my_dict['lisa'])
my_dict['dima']= 71
print(my_dict['dima'])
my_dict.update({'elena':6,
                'denis':34})
close = my_dict.pop('anna')
print(close)
print(my_dict)

######

my_set = {1,1,8,7,8,'up','dn','dn','up'}
print(my_set)
my_set.update({4,4,5,5,})
my_set.discard('up')
print(my_set)