
import psycopg2

def createConnection(DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT=5432):

    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
        return conn
    except Exception as e:
        print(f"Database not connected\n {e}")
        return None

def createCursor(connection):
    try:
        cur = connection.cursor()
        print("DB init")
        return cur
    except Exception as e:
        print(f"{e}")


def executeSelectQuery(cursor, query):
   
    try:
        cursor.execute(query)
        res = cursor.fetchall()
        return res
    except Exception as e:
        print(f"Error := {e}")
    return None


def executeInsertQuery(cursor , query):
    try:
        cursor.execute(query)
        cursor.connection.commit()
        res = cursor.rowcount()
        return res
        
    except Exception as e:
        print(f"Error executing Insert Operation := {e}")


def executeUpdateQuery(cursor , query):
    try:
        cursor.execute(query)
        cursor.connection.commit()
        res = cursor.rowcount()
        return res
        
    except Exception as e:
        print(f"Error executing Insert Operation := {e}")


def executeDeleteQuery(cursor, query):
    try:
        cursor.execute(query)
        cursor.connection.commit()
        return cursor.rowcount
    except Exception as e:
        print(f"Error executing DELETE query: {e}")
    return None


def get_tables(cursor):
    try:
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        
        tables = cursor.fetchall()
        
        if tables:
            print("Tables in the 'public' schema:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the 'public' schema.")
        
    except Exception as e:
        print(f"Error fetching tables: {e}")



def closeConnection(conn):
    conn.close()


if __name__=='__main__':
    con = createConnection(DB_NAME='my_db', DB_USER='postgres', DB_PASS='thinksys@123', DB_HOST='localhost')
    # print(con)
    cursor = createCursor(con)
    # print(cursor)

    # res =cursor.execute("SELECT * FROM dummy;")
    # rows = cursor.fetchall()
    # print(rows)

    # get_tables(cursor)

    res = executeSelectQuery(cursor , "SELECT * FROM dummy")
    print(res)

    closeConnection(con)