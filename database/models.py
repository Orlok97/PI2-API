from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import db
from dataclasses import dataclass

@dataclass
class Citizen(db.Model):
    __tablename__ = 'citizen_table'
    
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
    numero: Mapped[str] = mapped_column(String(100), nullable=False)
    area: Mapped[str] = mapped_column(String(100), nullable=False)
    cep: Mapped[str] = mapped_column(String(20), nullable=False)
    servico: Mapped[str] = mapped_column(String(100), nullable=False)
    desc: Mapped[str] = mapped_column(String(200))
    anexo: Mapped[str] = mapped_column(String(100),nullable=True)
    protocolo: Mapped[str] = mapped_column(String(100), nullable=False)
    data: Mapped[str] = mapped_column(String(100), nullable=False)
    hora: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(100), default="pendente",nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("citizen_table.id"), nullable=False)

@dataclass
class Service(db.Model):
  __tablename__='service_table'
  id: Mapped[int]=mapped_column(Integer, primary_key=True)
  nome: Mapped[str]=mapped_column(String(100),nullable=False)
  desc: Mapped[str]=mapped_column(String(200),nullable=False)
  prazo: Mapped[int]=mapped_column(Integer,nullable=False)
    
@dataclass
class Employee(db.Model):
  __tablename__='employee_table'
  id: Mapped[int]=mapped_column(Integer, primary_key=True)
  nome: Mapped[str]=mapped_column(String(100),nullable=False)
  email: Mapped[str]=mapped_column(String(100), unique=True, nullable=False)
  senha: Mapped[str]=mapped_column(String(100),nullable=False)
  cargo: Mapped[str]=mapped_column(String(100),nullable=True)
  
@dataclass
class Admin(db.Model):
  __tablename__='admin_table'
  id: Mapped[int]=mapped_column(Integer,primary_key=True)
  nome: Mapped[str]=mapped_column(String(100),nullable=False)
  email: Mapped[str]=mapped_column(String(100),nullable=False, unique=True)
  senha: Mapped[str]=mapped_column(String(100),nullable=False)