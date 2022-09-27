from db.dbconnection import dbconnection

def webhook_delete_mutation(id: str):
    dbcursor = dbconnection.cursor()

    sql = "DELETE FROM webhooks WHERE id = %s"

    val = [id]

    dbcursor.execute(sql, val)
    dbconnection.commit()

    return True