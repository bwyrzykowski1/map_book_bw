users: list = [

    {'name': 'Julia', 'surname': 'Gotowiec', 'posts': '1500'},
    {'name': 'Hubert', 'surname': 'Sybilski', 'posts': '123456789'},
    {'name': 'Adrian', 'surname': 'Dobrzański', 'posts': '123'},

]
print('Informacja o twoich znajomych: ')
for user in users:
    print(f'\tTwój znajomy {user['name']} {user['surname']} opublikował {user["posts"]}.')
