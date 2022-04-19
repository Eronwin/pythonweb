# pythonweb

### 模块划分

### 1.用户操作

 1）路由蓝图      route/admin_route.py

 2）业务逻辑      core/admin_core.py

 3）数据库操作  db/admin_db.py

### 2.菜单操作

 1）路由蓝图      route/menu_route.py

 2）业务逻辑      core/menu_core.py

 3）数据库操作  db/menu_db.py

### 3.影片操作

 1）路由蓝图      route/video_route.py

 2）业务逻辑      core/video_core.py

 3）数据库操作  db/video_db.py

### 4.角色操作

 1）路由蓝图      route/role_route.py

 2）业务逻辑      core/role_core.py

 3）数据库操作  db/role_db.py

### 5.基础操作

1）配置文件												conf/config.py

2）SQLAlchemy对原生SQL操作封装	   db/db_handler.py

3）公共函数												lib/common.py

4）消息类型类											models/message_model.py

5）列表类型类											models/js_grid_data.py

6）SQLAlchemy对象封装                          exts.py

7）主运行文件											manage.py

8）安装部署打包脚本								setup.py

### 项目结构

```
pythonweb
├── Icon
├── LICENSE
├── README.md
├── conf                                                            #配置文件
│   ├── config.py
│   └── settings.py
├── core																														#业务逻辑
│   ├── admin_core.py
│   ├── menu_core.py
│   ├── role_core.py
│   └── video_core.py
├── data
├── db																															#数据库操作
│   ├── admin_db.py
│   ├── db_handler.py
│   ├── menu_db.py
│   ├── role_db.py
│   └── video.db.py
├── exts.py													
├── lib																															#公共函数
│   └── common.py
├── main.py
├── manage.py
├── models																													
│   ├── js_grid_data.py																							#列表类型
│   └── message_model.py																						#消息类型
├── route																														#路由
│   ├── admin_route.py
│   ├── menu_route.py
│   ├── role_route.py
│   └── video_route.py
├── setup.py
├── static
│   ├── js
│   │   ├── common.js
│   │   ├── index.js
│   │   ├── left-menu.js
│   │   └── project-list.js
│   ├── pages
│   │   ├── footer.html
│   │   ├── header.html
│   │   ├── index.html
│   │   ├── left-menu.html
│   │   ├── login.html
│   │   ├── project-add.html
│   │   ├── project-list.html
│   │   └── wolcome.html
├── tempCodeRunnerFile.py
├── templates
└── util
    ├── Response.py
```

