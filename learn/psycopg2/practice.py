
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


def executeSelectQuery(cursor, query, params=None):
   
    try:
        if params ==None:
            cursor.execute(query)
        else :
            cursor.execute(query , params)
        res = cursor.fetchall()
        return res
    except Exception as e:
        print(f"Error := {e}")
    return None


def executeInsertQuery(cursor, query, params):
    try:
        cursor.execute(query, params)
        cursor.connection.commit()
        res = cursor.rowcount
        return f"{res} row added"
        
    except Exception as e:
        print(f"Error executing Insert Operation := {e}")


def executeUpdateQuery(cursor , query, params):
    try:
        cursor.execute(query, params)
        cursor.connection.commit()
        res = cursor.rowcount
        return f"{res} rows updated"
        
    except Exception as e:
        print(f"Error executing Insert Operation := {e}")


def executeDeleteQuery(cursor, query, params):
    try:
        cursor.execute(query, params)
        cursor.connection.commit()
        return f"{cursor.rowcount} rows deleted"
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

    # res = executeSelectQuery(cursor, "SELECT * FROM dummy where sname=%s;",("sara",))
    # print(res)
    # get_tables(cursor)

    # res = executeInsertQuery(cursor , "Insert into dummy values(%s, %s, %s)", ("sara",54886,"gd"))
    # print(res)

    # res = executeUpdateQuery(cursor, "update dummy set sname=%s where sname=%s",("gef","xyz"))
    # print(res)

    res = executeDeleteQuery(cursor, "delete from dummy where sname = %s",("sara",))
    print(res)

    res = executeSelectQuery(cursor,"select * from dummy")
    print(res)

    closeConnection(con)