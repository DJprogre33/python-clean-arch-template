from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    route_class=DishkaRoute,
)


@user_router.get("/{user_id}")
def get_user_info(user_id: int): ...


@user_router.post("/")
def update_current_user_info(): ...
