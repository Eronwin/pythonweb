
import os
class BaseConfig:
    SECRET_KEY = os.urandom(24)


# 开发环境
class DevConfig(BaseConfig):
    DB_HOST = 'localhost'
    DB_PORT = '3306'
    DB_DATABASE = 'pyweb'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8" \
        .format(username=DB_USERNAME,
            password=DB_PASSWORD,
            host=DB_HOST, port=DB_PORT,
            db=DB_DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# 测试环境
class TestConfig(BaseConfig):
    DB_USER = "test"
    DB_PWD = "1111111"


# 生产环境
class ProConfig(BaseConfig):
    DB_USER = "pro"
    DB_PWD = "1111111"


# 配置字典
myConfig = {
    "dev": DevConfig,
    "test": TestConfig,
    "pro": ProConfig
}