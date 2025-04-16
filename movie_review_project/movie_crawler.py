import requests
from dotenv import load_dotenv
import os
import sqlite3

# .env 파일에서 API 키 로드
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

# TMDB API에서 인기 영화 데이터 가져오기
def fetch_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['results']
    else:
        print("API 요청 실패")
        return []

# SQLite DB 연결
def init_db():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        release_date TEXT)''')
    conn.commit()
    
    return conn, cursor

# 영화 데이터를 DB에 삽입
def insert_movie(cursor, title, release_date):
    cursor.execute('INSERT INTO movies (title, release_date) VALUES (?, ?)', (title, release_date))

def main():
    movies = fetch_movies()
    if movies:
        conn, cursor = init_db()
        for movie in movies:
            insert_movie(cursor, movie['title'], movie['release_date'])
        conn.commit()
        print("영화 데이터가 DB에 삽입되었습니다.")
        conn.close()

if __name__ == "__main__":
    main()

