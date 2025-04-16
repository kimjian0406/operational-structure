from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# 테스트용 데이터베이스 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테스트 클라이언트 설정
client = TestClient(app)

def test_create_reply_like():
    # 테스트용 데이터를 POST 요청으로 생성
    response = client.post("/reply-likes/", json={"reply_id": 1, "user_id": 1})
    assert response.status_code == 200
    assert response.json() == {"reply_id": 1, "user_id": 1}  # 적절한 값으로 응답이 반환되면 됨

def test_delete_reply_like():
    # 먼저 생성된 댓글 좋아요 ID로 삭제 테스트
    response = client.post("/reply-likes/", json={"reply_id": 1, "user_id": 1})
    reply_like_id = response.json()["id"]

    delete_response = client.delete(f"/reply-likes/{reply_like_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == reply_like_id  # 삭제된 ID가 반환되어야 함

