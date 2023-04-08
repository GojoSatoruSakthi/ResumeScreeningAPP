import strawberry

from controller import CreateMutation
from schema import UserType, PostType, CommentsType


@strawberry.type
class Mutation:
    add_user: UserType = strawberry.mutation(resolver=CreateMutation.add_user)

@strawberry.type
class Mutation:
    add_user: UserType = strawberry.mutation(resolver=CreateMutation.add_user)
    add_post: PostType = strawberry.mutation(resolver=CreateMutation.add_post)
    add_comment: CommentsType = strawberry.mutation(resolver=CreateMutation.add_comment)