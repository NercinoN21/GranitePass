"""
Routine responsible for interacting with the database.
"""
from os import makedirs
from typing import List

from tinydb import Query, TinyDB

from granitepass.config import Config

CONFIG = Config()


class DataBase:
    """Class to interact with the database"""

    def __init__(self) -> None:
        """Database connection and defines the tables"""
        makedirs(CONFIG.data_dir, exist_ok=True)
        self.__tables = CONFIG.tables.values()
        self.__db = TinyDB(CONFIG.db_file, indent=4)

    def __repr__(self) -> str:
        """Basic instance representation"""
        return f'{self.__dict__}'

    def __str__(self) -> str:
        """Print representation"""
        return f'{self.__dict__}'

    @property
    def tables(self) -> List[str]:
        return self.__tables

    @property
    def db(self) -> TinyDB:
        return self.__db

    def verify_table(self, table: str) -> bool:
        """Verify if the table is valid"""
        return table in self.tables

    def create_query(self, table: str, rule: dict) -> Query:
        """ "Create the "query" if the table is valid"""
        if self.verify_table(table):
            return Query().fragment(rule)

        raise ValueError(f'Table "{table}" not found')

    def get_data(self, table: str, **kwargs) -> List[dict]:
        """Get data in the selected table"""
        return self.db.table(table).search(self.create_query(table, kwargs))

    def create_data(self, table: str, data: dict, rule: dict) -> int:
        """Create data in the selected table if
        the rule doesn't capture anything

        The "rule" refers to checking whether
        the data is already in the table
        """
        if self.get_data(table, **rule):
            return 0

        return self.db.table(table).insert(data)

    def update_data(self, table: str, new_data: dict, **kwargs) -> List[int]:
        """Update data in selected table according to rule"""
        return self.db.table(table).update(
            new_data, self.create_query(table=table, info=kwargs)
        )

    def delete_data(self, table: str, **kwargs) -> List:
        """Delete data in the selected table"""
        return self.db.table(table).remove(self.create_query(table, kwargs))

    def get_all_data(self, table: str) -> List[dict]:
        """Return all data in the selected table"""
        if self.verify_table(table):
            return self.db.table(table).all()

    def delete_all_data(self, table: str) -> None:
        """Delete all data in the selected table"""
        if self.verify_table(table):
            self.db.table(table).truncate()
