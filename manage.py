
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, session, flash

from conf.settings import myConfig
from exts import db

from route.video_route import video

app = Flask(__name__)



app.register_blueprint(video, url_prefix="/video")

# 配置信息
app.config.from_object(myConfig["dev"])


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404


app.config.from_object(myConfig["dev"])

# 初始化SQLAlchemy对象
db.init_app(app)

app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

if __name__ == "__main__":
    app.run(port=8090,debug=True)