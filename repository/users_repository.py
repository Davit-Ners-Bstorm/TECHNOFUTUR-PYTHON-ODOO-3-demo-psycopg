from psycopg import Connection


def get_all_users(conn: "Connection"):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users

def get_user_by_id(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))

        user = cursor.fetchone()
        return user
