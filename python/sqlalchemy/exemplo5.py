######## ORMs

from datetime import datetime
from sqlalchemy import func, Column, Integer, String, create_engine, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column, registry, DeclarativeBase, Session


engine = create_engine( # Factory - Fábrica de conexões/motores
    "sqlite://", # uri
    echo=True,   # mostra a comunicação com o banco de dados
)


reg = registry()
# reg.metadata.create_all(engine)


# Três formas de usar

# 1. Classes sem tipos
# 2. Usando tipos
# 3. Com dataclass (pode usar do attrs ou do pydantic)

# 1 Sem tipos
class Base(DeclarativeBase):
    ...

# se for usar a Base
# Base.metadata.create_all(engine)

class Comment(Base):
    __tablename__ = 'comments2'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    live = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

# 2 Usando tipos

class Commment(Base):
    __tablename__ = 'comments1'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str]
    comment: Mapped[str]
    live: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


# 3 Dataclass
@reg.mapped_as_dataclass
class Comment:
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    comment: Mapped[str]
    live: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())


with Session(engine) as session:
    result = session.scalar(
        select(Comment).where(Commment.id == 1)
    )
    session.delete(result)
    session.commit()