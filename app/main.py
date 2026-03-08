from fastapi import FastAPI
from app.database import Base, engine
from app.models import Item 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="My API", version="0.1.0")

from app.routers import health, items
app.include_router(health.router)
app.include_router(items.router)