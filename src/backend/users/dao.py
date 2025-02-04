from src.backend.dao.base import BaseDAO

from src.backend.users.models import User


class UserDAO(BaseDAO):
    model = User
