import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from kombu.asynchronous.http import Response
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import HttpResponse


from .models import UserClient


class UserClientType(DjangoObjectType):
    class Meta:
        model = UserClient
        fields = "__all__"
        #filter_fields = '__all__'


class TotalCardType(DjangoObjectType):
    class Meta:
        model = UserClient
        fields = "__all__"


class QueryUserClient(graphene.ObjectType):
    user_client_list = graphene.List(UserClientType)
    total_card = graphene.Int()
    amount_card = graphene.Int()

    @staticmethod
    def resolve_user_client_list(self, info, **kwargs):
        return UserClient.objects.all()

    @staticmethod
    def resolve_total_card(self, info):
        return UserClient.objects.count()

    @staticmethod
    def resolve_amount_card(self, info):
        total_card = UserClient.objects.count()
        amount_card = total_card * 500000
        return amount_card
