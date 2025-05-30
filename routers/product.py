from fastapi import APIRouter, Depends
from ..xmlrpc_client import models, db, uid, password
from ..auth import verify_token

router = APIRouter(prefix="/api", tags=["Product"])

@router.get("/products", dependencies=[Depends(verify_token)])
def get_products():
    products = models.execute_kw(
        db, uid, password,
        'product.product', 'search_read',
        [[]], {'fields': ['name', 'list_price'], 'limit': 5}
    )
    return {"data": products}
