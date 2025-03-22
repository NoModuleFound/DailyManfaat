from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src import all_routers

app = FastAPI()


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

for router in all_routers:
  app.include_router(router)


if __name__ == '__main__':
  uvicorn.run('run:app', host='127.0.0.1',
              port=8080, reload=True)