from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import v1_router
import uvicorn as uvicorn

origins = [
    "http://localhost",
    "http://localhost:3000",
]


def create_app() -> FastAPI:
    current_app = FastAPI(
        title="Automation of queuing systems",
        description="The application serves to automate single-channel and multi-channel queuing systems. Also contains part of the inventory management functions",
        version="1.0.0",
    )

    current_app.include_router(v1_router.router)

    current_app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return current_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
