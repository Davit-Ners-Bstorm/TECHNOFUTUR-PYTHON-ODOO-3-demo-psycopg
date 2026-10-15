from psycopg import Connection


def get_all_users(conn: "Connection"):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users

def get_user_by_id(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,)) # ',' quand il y a un seul paramètre pour forcer création d'un tuple

        user = cursor.fetchone()
        return user

def create_user(conn: "Connection", name, dob):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users
            VALUES (DEFAULT, %s, %s)
            RETURNING id
            """,
            (name, dob)
        )
        user_id = cursor.fetchone()[0]
        return user_id

def update_user_name(conn: "Connection", nv_name, user_id):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            UPDATE users
            SET name = %s
            WHERE id = %s
            """,
            (nv_name, user_id)
        )
        count_row_affected = cursor.rowcount

        return count_row_affected

def create_2_users(conn: "Connection", name1, name2, dob1, dob2):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                """
                INSERT INTO users (name, dob)
                VALUES (%s, %s)
                RETURNING id
                """,
                (name1, dob1)
            )

            user1_id = cursor.fetchone()[0]

            cursor.execute(
                """
                INSERT INTO users (name, dob)
                VALUES (%s, %s)
                RETURNING id
                """,
                (name2, dob2)
            )

            user2_id = cursor.fetchone()[0]

            return user1_id, user2_id
        except:
            conn.rollback()
            return None
