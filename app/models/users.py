from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel(BaseModel):
    id: int
    username: str
    password: str
    email: str
    full_name: str
    is_active: bool = True
    last_login: Optional[datetime] = None

    _users: list["UserModel"] = []

    def model_dump(self):
        return self.dict()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def delete(self):
        UserModel._users = [u for u in UserModel._users if u.id != self.id]

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.password)

    @classmethod
    def create(cls, **kwargs):
        new_id = len(cls._users) + 1
        kwargs["id"] = new_id
        kwargs["password"] = cls.hash_password(kwargs["password"])
        user = cls(**kwargs)
        cls._users.append(user)
        return user

    @classmethod
    def all(cls):
        return cls._users

    @classmethod
    def filter(cls, **kwargs):
        result = cls._users
        for key, value in kwargs.items():
            result = [u for u in result if getattr(u, key) == value]
        return result

    @classmethod
    def get(cls, **kwargs):
        users = cls.filter(**kwargs)
        return users[0] if users else None

    @classmethod
    def authenticate(cls, username: str, password: str):
        user = cls.get(username=username)
        if user and user.verify_password(password):
            return user
        return None

    @classmethod
    def create_dummy(cls):
        if not cls._users:
            cls.create(
                username="admin",
                password="admin123",
                email="admin@example.com",
                full_name="Admin User"
            )

