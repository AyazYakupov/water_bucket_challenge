import os

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


def get_settings():
    is_testing_env = os.environ.get('TESTING_ENV', False)
    if is_testing_env:
        return SettingPyTest()

    return Settings()


settings = get_settings()
