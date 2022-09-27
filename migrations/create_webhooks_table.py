from db.dbconnection import dbconnection

def create_webhooks_table():
    dbcursor = dbconnection.cursor()

    sql = "CREATE TABLE IF NOT EXISTS webhooks (id VARCHAR(255) UNIQUE PRIMARY KEY, request VARCHAR(255), url VARCHAR(255))"

    dbcursor.execute(sql)