from .authorization.routers import router as auth_router
from .users.routers import router as user_router
from .system.routers import router as system_router



all_routers = [user_router, auth_router, system_router]