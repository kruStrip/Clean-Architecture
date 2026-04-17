from fastapi import FastAPI

from app.database import Base, SessionLocal, engine
from app.repositories.user_repo import UserRepository
from app.routers import admin, auth, tasks

app = FastAPI(title="Task Tracker API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        repo = UserRepository(db)
        if not repo.get_by_username("admin"):
            repo.create(
                email="admin@example.com",
                username="admin",
                phone="+7-900-000-00-00",
                password="Admin123",
                role="admin"
            )
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Task Tracker API is running"}


app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(admin.router)
