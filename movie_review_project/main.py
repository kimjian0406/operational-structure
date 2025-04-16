# main.py

from fastapi import FastAPI
from app.configs.database import initialize_tortoise
from app.routers.movies import movie_router
from app.routers.likes import like_router
from app.routers.reviews import review_router
from app.routers.users import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(review_router)  # 추가됨
app.include_router(like_router)  # 추가됨

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app, host='0.0.0.0', port=8000)

from fastapi import FastAPI
from app.configs.database import initialize_tortoise
from app.routers.movies import movie_router
from app.routers.likes import like_router
from app.routers.reviews import review_router
from app.routers.users import user_router
from app.routers.replies import reply_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(review_router)
app.include_router(like_router)
app.include_router(reply_router)  # 추가됨

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
from fastapi import FastAPI
from app.configs.database import initialize_tortoise
from app.routers.movies import movie_router
from app.routers.likes import like_router
from app.routers.reviews import review_router
from app.routers.users import user_router
from app.routers.replies import reply_router
from app.routers.reply_likes import reply_like_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(review_router)
app.include_router(like_router)
app.include_router(reply_router)
app.include_router(reply_like_router)  # 추가됨

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
# main.py

from fastapi import FastAPI
from app.configs.database import initialize_tortoise
from app.routers.movies import movie_router
from app.routers.likes import like_router
from app.routers.reviews import review_router
from app.routers.users import user_router
from app.routers.replies import reply_router
from app.routers.reply_likes import reply_like_router
from app.routers.reply_on_replies import reply_on_reply_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(review_router)
app.include_router(like_router)
app.include_router(reply_router)
app.include_router(reply_like_router)
app.include_router(reply_on_reply_router)  # 추가됨

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

from fastapi import FastAPI
from app.configs.database import initialize_tortoise
from app.routers.movies import movie_router
from app.routers.likes import like_router
from app.routers.reviews import review_router
from app.routers.users import user_router
from app.routers.replies import reply_router
from app.routers.reply_likes import reply_like_router
from app.routers.reply_on_replies import reply_on_reply_router
from app.routers.reply_on_reply_likes import reply_on_reply_like_router  # 추가됨

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(review_router)
app.include_router(like_router)
app.include_router(reply_router)
app.include_router(reply_like_router)
app.include_router(reply_on_reply_router)
app.include_router(reply_on_reply_like_router)  # 추가됨

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
from fastapi import FastAPI
from app.configs.database import initialize_tortoise
from app.routers.notifications import notification_router  # 추가됨

app = FastAPI()

app.include_router(notification_router)  # 추가됨

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
from app.routers.notifications_ws import ws_router
app.include_router(ws_router)
