import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings
from fastapi.concurrency import asynccontextmanager
from core.models import db_helper, Base


@asynccontextmanager
async def lifespan(app_param: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        # await conn.run_sync(Base.metadata.create_all)
        # await conn.run_sync(Base.metadata.drop_all)

    yield
    # Shutdown
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
