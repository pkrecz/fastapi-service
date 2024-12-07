from starlette.middleware.base import BaseHTTPMiddleware


class CustomMiddleware(BaseHTTPMiddleware):
   
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Method"] = f"It was request {request.method} method."
        return response
