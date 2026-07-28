"""HTTP API routes for the MindX DevOps Lab backend."""

from fastapi import APIRouter

from app.core.config import settings


api_router = APIRouter(tags=["health"])


@api_router.get(
    "/health",
    summary="Health check",
    response_model=dict[str, str],
)
def health_check() -> dict[str, str]:
    """Return the service health status."""

    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
    }
