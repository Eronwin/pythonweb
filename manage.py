
from flask import Flask

from conf.settings import myConfig
from exts import db

from route.video_route import video

app = Flask(__name__)



app.register_blueprint(video, url_prefix="/video")

# 配置信息
app.config.from_object(myConfig["dev"])


# 初始化SQLAlchemy对象
db.init_app(app)


if __name__ == "__main__":
    app.run(port=8090,debug=True)