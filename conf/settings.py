# -*- coding: utf-8 -*-
# author lby
# 基础配置类，放的是在任何环境都不会改变的的值
class BaseConfig:
    BASE_KEY = "基础配置的key"
    BASE_VALUE = "基础配置的value"


# 开发环境
class DevConfig(BaseConfig):
    DB_HOST = 'admin'
    DB_PORT = '3306'
    DB_DATABASE = 'test'
    DB_USERNAME = 'root'
    DB_PASSWORD = '123456'
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