import strawberry  # new
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter  # new

from core import Mutation
# new
@strawberry.type
class Query:
  @strawberry.field
  def hello(self) -> str:
    return "Hello World"
  
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)  # new
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")  # new


@app.get("/")
def ping():
    return {"ping": "pong"}