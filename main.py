# main.py
from fastapi import FastAPI
from app.configs.database import initialize_tortoise
from app.routers.movies import movie_router
from app.routers.users import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

# main.py
from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.movies import movie_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

# main.py
from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.protected import router as protected_router

app = FastAPI()

app.include_router(user_router)
app.include_router(protected_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

