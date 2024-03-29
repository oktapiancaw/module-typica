from typing import Optional, Any, Union

from pydantic import BaseModel, Field


class Pagination(BaseModel):
    size: Optional[int]
    totalPages: Optional[int]
    totalItems: Optional[int]


class MetadataResponse(BaseModel):
    status: bool
    code: int
    message: Optional[str] = Field(None)
    timeExecution: Optional[Union[float, int]] = Field(None)


class MetadataPagination(MetadataResponse):
    pagination: Pagination


class BaseResponse(BaseModel):
    """
    Default response
    """

    data: Optional[Any] = Field(None, description="Data responses")
    metadata: MetadataResponse


class BasePaginationResponse(BaseModel):
    """
    Response with pagination
    """

    data: Optional[Any] = Field(None, description="Data responses")
    metadata: MetadataPagination


class DataValidResponse(BaseModel):
    """
    Response after validating queries / data
    """

    status: bool
    detail: Optional[str] = Field(None)
    data: Optional[Any] = Field(None, description="Data responses")


class CustomMetadataResponse(MetadataResponse):
    """
    Used for special reasons
    """

    ...


class CustomResponse(BaseResponse):
    """
    Used for special reasons
    """

    ...
