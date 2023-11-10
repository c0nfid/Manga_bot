import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    @staticmethod
    def parse_admins(row_string: str) -> dict:
        admins_with_name = row_string.split()
        admins = dict()
        for admin in admins_with_name:
            admin_tmp = admin.split(":")
            admin_name = admin_tmp[0]
            admin_id = admin_tmp[1]
            admins[admin_name] = admin_id
        return admins

    TOKEN: str = os.environ.get("TOKEN")
    ADMINS: dict = parse_admins(os.environ.get("ADMINID"))


config = Config()
