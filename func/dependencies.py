from orm import FakeDataBaseManager, DatabaseManagerBase

"""
For a real application a "real" ORM mapper with a real database connection must be defined here or in the get_db method.
This database connection is for demonstration purposes only.
"""
db = FakeDataBaseManager()


def get_db() -> DatabaseManagerBase:
    """
    Get database dependency
    Returns:
        DatabaseManagerBase: Instance of database manager
    """
    return db
