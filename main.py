from fastapi import FastAPI
from .routers import partner, product

app = FastAPI()

# Daftarkan router
app.include_router(partner.router)
app.include_router(product.router)
