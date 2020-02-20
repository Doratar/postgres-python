import psycopg2
import yaml

#Save the connect parameters into a config .yaml (Wich is not into the repository)
with open('e:/postgres-python/config.yaml') as f:

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

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    else:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")