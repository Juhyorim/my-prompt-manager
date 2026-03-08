from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def hello():
    return "helloworld"


@router.get("/health")
def health_check():
    return {"status": "ok"}
