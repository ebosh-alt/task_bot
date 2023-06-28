from dataclasses import dataclass
from collections import namedtuple
from SQLite import Sqlite3_Database
from Enum_classes import Admin_flags


@dataclass
class Admin:
    def __init__(self, id, **kwargs):
        self.id: int = id
        if len(kwargs):
            self.text_for_mailing: str = kwargs["text_for_mailing"]
            self.name_button_for_mailing: str = kwargs["name_button_for_mailing"]
            self.link_button_for_mailing: str = kwargs["link_button_for_mailing"]
            self.flag: Admin_flags = Admin_flags(kwargs["flag"])
            self.bot_message_id: int = kwargs["bot_message_id"]
            self.delete_message_id: int = kwargs["delete_message_id"]

        else:
            self.text_for_mailing: str = ""
            self.name_button_for_mailing: str = ""
            self.link_button_for_mailing: str = ""
            self.flag: Admin_flags = Admin_flags.NONE
            self.bot_message_id: int = 0
            self.delete_message_id: int = 0

    def get_tuple(self):
        return (
            self.id,
            self.text_for_mailing,
            self.name_button_for_mailing,
            self.link_button_for_mailing,
            self.flag.value,
            self.bot_message_id,
            self.delete_message_id,
        )

    def __str__(self):
        return f"id: {self.id} text_for_mailing: {self.text_for_mailing} name_button_for_mailing: " \
               f"{self.name_button_for_mailing} link_button_for_mailing: {self.link_button_for_mailing} " \
               f"flag: {self.flag} bot_message_id: {self.bot_message_id} delete_message_id: {self.delete_message_id}"

    def __iter__(self):
        dict_class = self.__dict__
        result = namedtuple("result", ["name", "value"])
        for attr in dict_class:
            if not attr.startswith("__"):
                if attr != "flag":
                    yield result(attr, dict_class[attr])
                else:
                    yield result(attr, dict_class[attr].value)


class Admins(Sqlite3_Database):
    def __init__(self, db_file_name, table_name, *args) -> None:
        Sqlite3_Database.__init__(self, db_file_name, table_name, *args)
        self.len = 0

    def add(self, obj: Admin) -> None:
        self.add_row(obj)

    def get(self, id: int) -> Admin | bool:
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = Admin(
                id=obj_tuple[0],
                text_for_mailing=obj_tuple[1],
                name_button_for_mailing=obj_tuple[2],
                link_button_for_mailing=obj_tuple[3],
                flag=obj_tuple[4],
                bot_message_id=obj_tuple[5],
                delete_message_id=obj_tuple[6],
            )
            return obj


if __name__ == "__main__":
    admin = Admin(0)
    for i in admin:
        print(i.name, i.value)
