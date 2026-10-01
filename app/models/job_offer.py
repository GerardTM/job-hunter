from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class JobOffer(Base):
    __tablename__ = "job_offers"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))
    company: Mapped[str] = mapped_column(String(255))

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    url: Mapped[str] = mapped_column(String(2048), unique=True)

    source: Mapped[str] = mapped_column(String(100))

    source_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    published_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    discovered_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )