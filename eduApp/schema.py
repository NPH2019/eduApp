import graphene
import graphql_jwt
from eduApp.backend.system.jwt import CustomObtainJSONWebToken
import eduApp.backend.client.schema


class Query(
    eduApp.backend.client.schema.QueryUserClient,
    graphene.ObjectType
):
    token_auth = CustomObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


class Mutation(graphene.ObjectType):
    token_auth = CustomObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field(),
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)