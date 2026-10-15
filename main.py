from db.db import get_conntection
from repository.users_repository import get_all_users

# Ouverture fermature à la main => On doit gerer nous même
# conn = get_conntection()
# get_all_users(conn)
# conn.close()

with get_conntection() as conn:
    users = get_all_users(conn)
    print(users)
