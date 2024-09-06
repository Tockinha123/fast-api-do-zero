from sqlalchemy.orm import registry, Mapped
from datetime import datetime

table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "Users"

    id: Mapped[int] 
    username: Mapped[str] 
    password: Mapped[str] 
    email: Mapped[str]
    created_at: Mapped[datetime] 