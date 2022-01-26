from sqlite3 import Timestamp
from typing import List, Optional
from pydantic import BaseModel
from graphene_pydantic import PydanticObjectType, PydanticInputObjectType

class ApplicantModel(BaseModel):
    id: int
    name: str
    email: str
    gpa: str

# GraphQL Schema

class ApplicantGrapheneModel(PydanticObjectType):
    class Meta:
        model = ApplicantModel

class ApplicantInputGrapheneModel(PydanticInputObjectType):
    class Meta:
        model = ApplicantModel
        exclude_fields = ('id',)

