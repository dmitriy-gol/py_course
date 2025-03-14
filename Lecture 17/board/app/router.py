from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import db
from app.model import Board

templates = Jinja2Templates(directory='app/templates')

router = APIRouter(tags=['Работа с твитами'])

@router.get('/', summary='Домашняя страница')
def home_page(request: Request):
    return templates.TemplateResponse('pages/home.html', context={'request': request})


@router.get('/about', summary='Страница About')
def about_page(request: Request):
    return templates.TemplateResponse('pages/about.html', context={'request': request})


@router.get('/create', summary='Просмотр страницы твитов')
async def create_page(request: Request):
    return templates.TemplateResponse('tweets/create.html', context={'request': request})


@router.post('/create/add', summary='Создание твита')
async def create_add(request: Request, session: AsyncSession = Depends(db.get_db_with_commit),
                      author = Form(default='Anonymous'), content = Form()):
    if content:
        new = Board(author=author, content=content)
        session.add(new)

    return templates.TemplateResponse('tweets/create.html', context={'request': request})


@router.get('/tweets', summary='Все твиты')
async def tweets_page(request: Request, session: AsyncSession = Depends(db.get_db)):
    res = await session.execute(select(Board).order_by(Board.created.desc()))
    tweets = res.scalars().all()
    return templates.TemplateResponse('tweets/tweets.html', context={'request': request, 'tweets': tweets})
