import uvicorn
from .core.app import app
from .routers import index as indexRoute
from .dependencies.config import conf

indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
