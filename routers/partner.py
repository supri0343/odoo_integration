from fastapi import APIRouter, Depends
from ..xmlrpc_client import models, db, uid, password
from ..auth import verify_token

router = APIRouter(prefix="/api", tags=["Partner"])

@router.get("/partners", dependencies=[Depends(verify_token)])
def get_partners():
    partners = models.execute_kw(
        db, uid, password,
        'res.partner', 'search_read',
        [[]], {'fields': ['name', 'email'], 'limit': 5}
    )
    return {"data": partners}
