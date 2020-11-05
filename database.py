from mysql import connector
import creds


def connect():
    connection = connector.connect(
        host=creds.HOST,
        user=creds.USER,
        password=creds.PASSWORD,
        database=creds.DATABASE
    )
    return connection


def init_db():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS elements (
                            symbol text,
                            latin_name text,
                            slovak_name text,
                            atomic_number text,
                            relative_weight text
                            )""")
    connection.commit()
    connection.close()


def information_to_list():
    elements_list = []
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT symbol FROM elements")
    length = len(format_result(cursor.fetchall()))
    cursor.execute("SELECT symbol FROM elements")
    symbols = format_result(cursor.fetchall())
    cursor.execute("SELECT latin_name FROM elements")
    latin_names = format_result(cursor.fetchall())
    cursor.execute("SELECT slovak_name FROM elements")
    slovak_names = format_result(cursor.fetchall())
    cursor.execute("SELECT atomic_number FROM elements")
    atomic_numbers = format_result(cursor.fetchall())
    cursor.execute("SELECT relative_weight FROM elements")
    realitve_weights = format_result(cursor.fetchall())
    for x in range(0, length):
        element_list = [str(symbols[x]), str(latin_names[x]), str(slovak_names[x]).replace('?', 'č'),
                        str(atomic_numbers[x]), str(realitve_weights[x])]
        elements_list.append(element_list)
    return elements_list


def format_result(result):
    formatted = []
    if len(result) > 0:
        if len(result) > 1:
            for x in range(0, len(result)):
                formatted.append(result[x][0])
        else:
            return result[0]
    else:
        return None
    if len(formatted) == 1:
        return formatted[0]
    else:
        return formatted
