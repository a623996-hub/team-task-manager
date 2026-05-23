from fastapi import FastAPI
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, tasks, projects
import os
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# include routers
app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(projects.router)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
