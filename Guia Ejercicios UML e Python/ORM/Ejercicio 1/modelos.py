from decimal import Decimal
from sqlalchemy import String, Numeric, Integer, CheckConstraint, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = 'producto'
    __table_args__ = (
        CheckConstraint("precio >=0", name="ck_precio"),
        CheckConstraint("stock >=0", name="ck_stock")
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    precio: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self):
        return (f"Producto (id={self.id}, nombre={self.nombre!r})>,"
                f"precio={self.precio}, stock={self.stock})")


