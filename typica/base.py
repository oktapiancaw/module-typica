from uuid import uuid4
from typing import Optional
from pydantic import BaseModel, Field, UUID4
from datetime import datetime
from .utils.enums import DataStatus
from pytz import common_timezones


class IdMeta(BaseModel):
    """
    Only id
    """

    id: UUID4 = Field(default_factory=uuid4)


class IdMongoMeta(BaseModel):
    """
    _id support for mongo
    """

    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")


# * Type 1 - Basic metadata
class BaseMeta(BaseModel):
    """
    Default metadata of data
    """

    createdAt: Optional[int] = Field(int(datetime.now().timestamp() * 1000), ge=0)
    updatedAt: Optional[int] = Field(None)
    deletedAt: Optional[int] = Field(None)
    createdBy: Optional[str] = Field("")
    updatedBy: Optional[str] = Field(None)
    deletedBy: Optional[str] = Field(None)
    timezone: Optional[str] = Field("Asia/Jakarta", examples=common_timezones)
    status: Optional[DataStatus] = Field(DataStatus.active, examples=DataStatus.list())

    @property
    def is_active(self):
        return self.status == DataStatus.active


class BaseIdMeta(BaseMeta, IdMeta):
    """
    Default metadata of data with ID

    Args:
        BaseMeta (BaseModel): Default metadata of data
    """

    ...


class BaseIdMongoMeta(BaseMeta, IdMongoMeta):

    """
    Default metadata of data with _id in mongo

    Args:
        BaseMeta (BaseModel): Default metadata of data
    """

    ...


# * Type 2 - Nested metadata
class BaseNestedMeta(BaseModel):
    """
    Nested metadata of data
    """

    metadata: Optional[BaseMeta]


class BaseNestedIdMeta(BaseNestedMeta, IdMeta):
    """
    Nested metadata of data with ID

    Args:
        BaseNestedIdMeta (BaseModel): Nested metadata of data
    """

    ...