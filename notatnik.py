import psycopg2 as ps

db_params = ps.connect(
    database="mapbook",
    user="postgres",
    password="geoinformatyka",
    host="localhost",
    port="5432"
)

def	get_users_from_db()->list:
	cursor = db_params.cursor()
	sql_show_users = "SELECT * FROM public.users"
	cursor.execute(sql_show_users)
	query_result = cursor.fetchall()
	for row in query_result:
		print(row[0], row[1], row[2], row[3], row[4])
	return query_result
get_users_from_db()

# def add_user_from_db() -> None:
#     cursor = db_params.cursor()
#     name = input("Podaj imię: ")
#     surname = input("Podaj nazwisko: ")
#     posts = int(input("Podaj liczbę postów: "))
#     location = input("Podaj nazwę miejscowośc: ")
#     sql_insert_user = f" INSERT INTO public.users( name, surname, posts, location) VALUES ('{name}', '{surname}', '{posts}', '{location}');"
#     cursor.execute(sql_insert_user)
#     db_params.commit()
# add_user_from_db()

# def update_user_from_db()-> None:
#     cursor = db_params.cursor()
#     name = input("Podaj imię: ")
#     surname = input("Podaj nazwisko: ")
#     posts = int(input("Podaj liczbę postów: "))
#     location = input("Podaj nazwę miejscowośc: ")
#     sql_update_user = f"UPDATE public.users SET name= '{name}', surname ='{surname}', posts ='{posts}', location ='{location}' WHERE id=17;"
#     cursor.execute(sql_update_user)
#     db_params.commit()
# update_user_from_db()

# def delete_user_from_db() -> None:
#     cursor = db_params.cursor()
#     user_id = input("Podaj ID: ")
#     sql_delete_user = f"DELETE FROM public.users WHERE id= '{user_id}';"
#     cursor.execute(sql_delete_user)
#     db_params.commit()
# delete_user_from_db()











# VALUES ('Karol', 'Makowski', '10', 'Warszawa', 'SRID=4326;POINT(52.21 21.00)');
