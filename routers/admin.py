from fastapi import APIRouter, Depends, status, UploadFile, File, Form, Request
from sqlalchemy.orm import Session
from repository import admin
from database import get_db
import schemas
from fastapi.responses import HTMLResponse
from frontend import test1
router = APIRouter(tags=['admin'], prefix='/admin')


@router.get('/test', response_class=HTMLResponse)
async def test(request: Request):
    return test1.a


@router.post('/uploadcsv', status_code=status.HTTP_201_CREATED)
async def upload_csv(name_in_which_col: int = Form(...), email_in_which_col: int = Form(...), css: UploadFile = File(...)):
    return admin.upload_csv(int(name_in_which_col), int(email_in_which_col), css)


@router.post('/stage1', status_code=status.HTTP_201_CREATED)
def stage1(request: schemas.Upload, db: Session = Depends(get_db)):
    return admin.stage1(db, request)


@router.get('/stage2', status_code=status.HTTP_201_CREATED)
def stage2(select: int, db: Session = Depends(get_db)):
    return admin.stage2(select, db)


@router.get('/show_all')
def show_all(db: Session = Depends(get_db)):
    return admin.show_all(db)


