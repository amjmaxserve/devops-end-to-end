from sqlalchemy import text


def check_database(db):
    try:
        db.execute(text("SELECT 1"))
        return True

    except Exception:
        return False