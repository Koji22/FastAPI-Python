from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()  # Registra Metadados


@table_registry.mapped_as_dataclass  # Criando uma estrutra do python que chama dataclass (classe de dados)
class User:
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)  # O sqlalchemy vai definir o id sozinho
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
