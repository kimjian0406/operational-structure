from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from .config import SQLALCHEMY_DATABASE_URL  # 데이터베이스 URL

# 데이터베이스 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 만들기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB Base 설정
Base = declarative_base()

# 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from .config import SQLALCHEMY_DATABASE_URL  # 데이터베이스 URL

# 데이터베이스 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 만들기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB Base 설정
Base = declarative_base()

# 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

