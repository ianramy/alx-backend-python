import seed


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        yield rows
        offset += page_size
