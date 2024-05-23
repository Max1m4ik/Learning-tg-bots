from sqlalchemy import BigInterger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

#Создаём бд
engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

#Подключаемся к ней
async_session = async_sessionmaker(engine)

#Заготовка на которую мы будемм ссылатся
class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInterger)


class Category(Base):
    __tablename__='categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(120))
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

#Функция для создания таблиц выше если их не существует
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)