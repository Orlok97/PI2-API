from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
    __tablename__ = 'user_table'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), nullable=False)
    senha: Mapped[str] = mapped_column(String(100), nullable=False)

@dataclass
class Janitorial(db.Model):
    __tablename__ = 'janitorial_table'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rua: Mapped[str] = mapped_column(String(100), nullable=False)
    bairro: Mapped[str] = mapped_column(String(100), nullable=False)
    area: Mapped[str] = mapped_column(String(100), nullable=False)
    cep: Mapped[str] = mapped_column(String(20), nullable=False)
    servico: Mapped[str] = mapped_column(String(100), nullable=False)
    desc: Mapped[str] = mapped_column(String(200))
    anexo: Mapped[str] = mapped_column(String(100))
    protocolo: Mapped[int] = mapped_column(Integer, nullable=False)
    data: Mapped[str] = mapped_column(String(100), nullable=False)
    hora: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(100), default="pendente",nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"), nullable=False)