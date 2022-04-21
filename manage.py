# -*- coding: utf-8 -*-
# author lby
from datetime import timedelta
from flask import Flask


from conf.settings import myConfig
from exts import db
from route.admin_route import admin
from route.menu_route import menu
from route.role_route import role
app = Flask(__name__)



app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(menu, url_prefix="/menu")
app.register_blueprint(role, url_prefix="/role")

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

app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


if __name__ == "__main__":
    # app.run(port=8080,debug=True)
    app.run(port=8080)