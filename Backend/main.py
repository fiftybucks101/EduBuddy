from fastapi import FastAPI
from auth.routes import router as auth_router
from database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the authentication routes
app.include_router(auth_router)

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to EduBuddy API"}
