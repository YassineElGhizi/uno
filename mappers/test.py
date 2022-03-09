from collections import defaultdict

class Client():
    id : int
    name : str
    age : int

    def __init__(self , id , name , age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f'id = {self.id} name = {self.name} age = {self.age} '

if __name__ == '__main__':
    l = []
    c1 = Client(1,'yassine' , 23)
    c2 = Client(2 , 'yassine' , 24)
    c3 = Client(2 , 'yassine' , 25)
    c4 = Client(2 , 'not yassine' , 24)
    c5 = Client(2 , 'yassine' , 26)

    l.append(c1)
    l.append(c2)
    l.append(c3)
    l.append(c4)
    l.append(c5)


[print(f'id:{x.id} - name: {x.name}') for x in l]

groups = defaultdict(list)
for obj in l:
    groups[obj.name].append(obj)

new_list = groups.values()

dict_val_to_list =list(new_list)

big_list = []

[big_list.append(x) for x in dict_val_to_list]

[ ([print(f'{y}') for y in yy] , print('=============\n')) for yy in big_list]