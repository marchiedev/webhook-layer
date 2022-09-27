from db.dbconnection import dbconnection

def __webhook_list_response(x):
    return { 'id': x['id'], 'url': x['url'] }

def webhook_list_query():
    dbcursor = dbconnection.cursor(dictionary=True)

    sql = "SELECT * FROM webhooks"

    dbcursor.execute(sql)
    
    res = dbcursor.fetchall()

    return list(map(__webhook_list_response, res))