# -*- coding: utf-8 -*-
# author lby
from flask import Flask


from conf.settings import myConfig
from exts import db
from route.admin_route import admin

app = Flask(__name__)



app.register_blueprint(admin, url_prefix="/admin")

# 配置信息
# 1、在app对象直接设置，耦合高
# app.config.update(
#     DEBUG=True,
#     HELLO="WORLD"
# )

# 2、写一个配置文件，app对象导入配置文件
# app.config.from_object(config)

# 3、app导入某一个配置类的对象
app.config.from_object(myConfig["dev"])


# 初始化SQLAlchemy对象
db.init_app(app)


if __name__ == "__main__":
    app.run(port=8080,debug=True)