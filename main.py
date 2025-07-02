from fastapi import FastAPI
from api.routes import router as recommend_router
from db.database import init_db

app = FastAPI(title="Recipe Recommendation API")

init_db()

app.include_router(recommend_router, prefix="/recommend", tags=["recommend"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
