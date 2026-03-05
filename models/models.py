from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, ForeignKey, Table


db = "sqlite:///./sql_app.db"

engine = create_engine(
    db,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)



Base = declarative_base()


user_games_association = Table(
    "user_games",
    Base.metadata,
    Column("user_id", ForeignKey("usuario.id"), primary_key=True),
    Column("jogo_id", ForeignKey("jogos.id"), primary_key=True)
)