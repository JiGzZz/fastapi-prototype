from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user, auth
from app import models, oauth2
from app.config import settings
from app.connection import engine

#models.Base.metadata.create_all(bind=engine) #As we are now using alembic instead

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root(user_info: int = Depends(oauth2.get_current_user)):
    return {"message": "Hello world!", "user_info": user_info}
