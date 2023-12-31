from .Countries import Countries, Country
from .Users import User, Users

from .Enum_classes import Flags

db_file_name = "bot/db/database"
users = Users(db_file_name=db_file_name, table_name="users")
countries = Countries(db_file_name=db_file_name, table_name="countries")
__all__ = ("User", "Users", "Flags", "users", "countries", "Country", "Countries")
