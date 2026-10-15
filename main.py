from db.db import get_conntection
from repository.users_repository import get_all_users

with get_conntection() as conn:
    users = get_all_users(conn)
    print(users)
