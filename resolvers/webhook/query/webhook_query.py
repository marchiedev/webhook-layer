from db.dbconnection import dbconnection

def webhook_query(id: str):
    dbcursor = dbconnection.cursor(dictionary=True)

    sql = "SELECT * FROM webhooks WHERE id = %s"

    val = [id]

    dbcursor.execute(sql, val)

    res = dbcursor.fetchall()[0]

    return {'id': res['id'], 'url': res['url']}