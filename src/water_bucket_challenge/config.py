import os
from typing import Union

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    TESTING_ENV: bool = False
    PORT: int = 5000

    class Config:
        env_file = ".env"
        case_sensitive = True


class SettingPyTest(Settings):
    TESTING_ENV: bool = True

    class Config(Settings.Config):
        env_file = ".env.test"


class SettingsFactory:
    def __new__(cls) -> Union[SettingPyTest, Settings]:
        is_testing_env = os.environ.get("TESTING_ENV", False)
        if is_testing_env:
            return SettingPyTest()

        return Settings()


settings = SettingsFactory()
