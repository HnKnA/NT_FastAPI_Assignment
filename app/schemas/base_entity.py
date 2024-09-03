from sqlalchemy import Column, DateTime
import uuid
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID


class BaseEntity:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
