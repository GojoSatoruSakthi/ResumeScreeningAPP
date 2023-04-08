import strawberry
@strawberry.input
class UserInput:
    name: str
    email: str
    address: str
    phone_number: str
    sex: str

@strawberry.input
class PostInput:
    user_id: int
    title: str
    body: str


@strawberry.input
class CommentInput:
    user_id: int
    post_id: int
    body: str