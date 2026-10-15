from db.db import get_conntection
from repository.users_repository import get_all_users, get_user_by_id, create_user

# Ouverture fermature à la main => On doit gerer nous même
# conn = get_conntection()
# get_all_users(conn)
# conn.close()

with get_conntection() as conn:
    # users = get_all_users(conn)
    # print(users)

    # print('******************')
    # user = get_user_by_id(conn, 5)
    # print(user)

    nv_id = create_user(conn, "Samy", "2001/01/01")

    print('ID = ', nv_id)
