immutable_var = 1,2,3,'bag',5
print(immutable_var)
# кортеж является не изменяемым объектом,так же он занимает меньше места чем список,
# и его удобно использовать в качестве хранилища
mutable_list = ['dima','anton','ana','elena']
print(mutable_list)
mutable_list[2] = 'eva'
mutable_list[3] = 6
print(mutable_list)