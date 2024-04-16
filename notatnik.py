users: list = [

    {'name': 'Julia', 'surname': 'Gotowiec', 'posts': '1500'},
    {'name': 'Hubert', 'surname': 'Sybilski', 'posts': '123456789'},
    {'name': 'Adrian', 'surname': 'Dobrzański', 'posts': '123'},
    {'name': 'Bartek', 'surname': 'Wyrzykowski', 'posts': '300'},
]
def search_user(users: list):
    imie = input('Podaj imie: ')
    for user in users:
        if user['name'] == imie:
            print(user)
search_user(users)
print(users)