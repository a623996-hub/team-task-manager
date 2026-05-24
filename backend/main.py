from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import auth, tasks, projects, users

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown (optional cleanup)
    print("App shutting down")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(projects.router)
app.include_router(users.router)