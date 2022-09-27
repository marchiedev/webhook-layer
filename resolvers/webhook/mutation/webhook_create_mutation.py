from db.dbconnection import dbconnection
import uuid

def webhook_create_mutation(url: str, request: str):
    dbcursor = dbconnection.cursor()

    webhook_id = uuid.uuid4().hex

    sql = "INSERT INTO webhooks (id, request, url) VALUES (%s, %s, %s)"

    val = (webhook_id, request, url)

    dbcursor.execute(sql, val)
    dbconnection.commit()

    return {'id': webhook_id, 'url': url}