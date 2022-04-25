# -*- coding: utf-8 -*-
# author lby
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, session, flash


from conf.settings import myConfig
from exts import db
from route.admin_route import admin
from route.menu_route import menu
from route.role_route import role
from route.video_info_route import video_info
from route.video_route import video
app = Flask(__name__)



app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(menu, url_prefix="/menu")
app.register_blueprint(role, url_prefix="/role")
app.register_blueprint(video_info, url_prefix="/video-info")
app.register_blueprint(video, url_prefix="/video")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
app.config.from_object(myConfig["dev"])



db.init_app(app)

app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


if __name__ == "__main__":
    # app.run(port=8080,debug=True)
    app.run(port=8080)