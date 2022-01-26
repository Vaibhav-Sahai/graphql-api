import graphene
from serializers import (
    ApplicantGrapheneModel,
    ApplicantInputGrapheneModel,
)
from models.applicant import Applicant

class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))
    list_applicants = graphene.List(ApplicantGrapheneModel)
    get_single_applicant = graphene.Field(ApplicantGrapheneModel, applicant_id=graphene.NonNull(graphene.Int))

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'

    @staticmethod
    def resolve_list_applicants(parent, info):
        return Applicant.all()

    @staticmethod
    def resolve_get_single_applicant(parent, info, applicant_id):
        return Applicant.find_or_fail(applicant_id)

class CreateApplicant(graphene.Mutation):
    class Arguments:
        applicant_details = ApplicantInputGrapheneModel()

    Output = ApplicantGrapheneModel

    @staticmethod
    def mutate(parent, info, applicant_details):
        applicant = Applicant()
        applicant.name = applicant_details.name
        applicant.email = applicant_details.email
        applicant.gpa = applicant_details.gpa
        applicant.save()
        return applicant

class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()