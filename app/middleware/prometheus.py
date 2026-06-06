import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.monitoring.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY
)

class PrometheusMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.time()

        response = await call_next(request)

        duration = time.time() - start_time

        REQUEST_COUNT.labels(
            request.method,
            request.url.path
        ).inc()

        REQUEST_LATENCY.labels(
            request.method,
            request.url.path
        ).observe(duration)

        return response