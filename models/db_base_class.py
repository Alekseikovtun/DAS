from datetime import datetime
from xmlrpc.client import DateTime

from sqlalchemy import Column, func
from sqlalchemy_mixins import AllFeaturesMixin


class BaseModel(AllFeaturesMixin):
    __abstract__ = True
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at: datetime = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    __mapper_args__ = {"eager_defaults": True}
