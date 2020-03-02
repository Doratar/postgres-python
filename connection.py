import psycopg2
import yaml

#Save the connect parameters into a config .yaml (Wich is not into the repository)
with open('./config.yaml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)

    try:
        connection = psycopg2.connect(user = data['user'],
                                    password = data['password'],
                                    host = data['host'],
                                    port = data['port'],
                                    database = data['database'])

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")

        cursor.execute("SELECT actor.first_name, actor.last_name, film.title FROM film_actor INNER JOIN film on film_actor.film_id = film.film_id INNER JOIN actor on film_actor.actor_id = actor.actor_id")
        record = cursor.fetchall()
        for items in record:
            print(items)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    else:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")