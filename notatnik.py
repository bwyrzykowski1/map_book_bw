users: list = [

    {'name': 'Julia', 'surname': 'Gotowiec', 'posts': '1500'},
    {'name': 'Hubert', 'surname': 'Sybilski', 'posts': '123456789'},
    {'name': 'Adrian', 'surname': 'Dobrzański', 'posts': '123'},
    {'name': 'Bartek', 'surname': 'Wyrzykowski', 'posts': '300'},
]

def update_user(users: list):
    imie = input('Wprowadź imię użytkownika, któego dane chcesz zmienić: ')
    for user in users:
        if user['name'] == imie:
            user['name']= input('Podaj nowe imie: ')
            user['surname']= input('Podaj nowe nazwisko: ')
            user['posts']= int(input('Podaj nową liczbę postów użytkownika: '))

update_user(users)
print(users)