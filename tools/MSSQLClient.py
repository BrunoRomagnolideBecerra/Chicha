import pyodbc
from tools.helpers import Helpers

class MSSQLClient(Helpers):
    PATH = 'configuration/db_credentials.yml'

    # receives 'clarity', 'harmony', 'understanding','onboarding' or admin' to initialize the connection.
    def __init__(self, data_base: str):
        db_credentials = self.read_yaml(self.PATH)
        SERVER = db_credentials[data_base]['SERVER']
        DB = db_credentials[data_base]['DB']
        UID = db_credentials[data_base]['UID']
        PWD = db_credentials[data_base]['PWD']

        try:
            drivers = [item for item in pyodbc.drivers() if item.lower().endswith('sql server')]
            if drivers:
                driver = drivers[0]
                self.db_connection = pyodbc.connect(
                    'DRIVER={' + driver + '};SERVER=' + SERVER + ';DATABASE=' + DB + ';UID=' + UID + ';PWD=' + PWD
                    + ';Trusted_Connection=no;Encrypt=no', timeout=5
                )
            else:
                raise Exception('No suitable driver found. Cannot connect')
        except Exception as e:
            raise e

    def run_query(self, sql_statement: str, params: list = None):
        """
        Args:
            sql_statement: a valid MSSQL statement
            params: additional parameters to be inserted in query at %s

        Notes:
            The dicts returned are a mapping of column names to column
            values. If the sql_statement was an insert/delete/update,
            an empty tuple will be returned.

        Returns:
            the result of the sql_statement as a tuple; empty tuple if
            no results returned, else tuple of dicts
        """

        cursor = self.db_connection.cursor()
        try:
            if params:
                cursor.execute(sql_statement, params)
            else:
                cursor.execute(sql_statement)
            result = cursor.fetchall()
            result = [tuple(map(str, r)) for r in result]  # Each tuple becomes a tuple of str.
            result = [item for t in result for item in t]  # Convert list of tuples in list of str.
            return result
        finally:
            cursor.close()
            self.shutdown()

    def shutdown(self):
        """Close the database connection."""
        if self.db_connection:
            self.db_connection.close()
            self.db_connection = None
