from typing import Union

from fastapi import FastAPI, Form

# test resolvers
from resolvers.test.query.test_query import test_query
# webhook resolvers
from resolvers.webhook.query.webhook_list_query import webhook_list_query
from resolvers.webhook.query.webhook_query import webhook_query
from resolvers.webhook.mutation.webhook_delete_mutation import webhook_delete_mutation
from resolvers.webhook.mutation.webhook_create_mutation import webhook_create_mutation

app = FastAPI()


# Webhooks Api
## Get Webhooks List
@app.post('/webhooks')
def webhook_create(url: Union[str, None] = Form(), request: Union[str, None] = Form()):
    res = webhook_create_mutation(url, request)
    return res

@app.get('/webhooks')
def webhook_list():
    res = webhook_list_query()
    return res

## Get Webhook
@app.get('/webhooks/{id}')
def webhook(id: str):
    res = webhook_query(id)
    return res

## Delete Webhook
@app.delete('/webhooks/{id}')
def webhook_delete(id: str):
    res = webhook_delete_mutation(id)
    return res

# Test
@app.get("/test")
def test():
    res = test_query()

    return res