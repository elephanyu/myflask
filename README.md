##### Flask博客
---
- 源码来自 https://github.com/miguelgrinberg/flasky 17a
- 参考文档 《FlaskWeb开发：基于Python的Web应用开发实战.pdf》
- 启动步骤
    - 初始化数据库，角色列表  
        python myflask.py shell  
        \>\>\> db.create_all()  
        \>\>\> Role.insert_roles()  
    - 运行web并注册账号  
        python myflask.py runserver

- 新加目录
    - doc flask学习笔记
        - structure.md flask介绍及通用项目结构
        - jinjia.md jinjia模板
        - flaskWTF.md 表单
        - sqlTool.md 表定义与ORM
    - study flask学习自编代码
        - mailTest.py mail发送邮件测试
        - managerTest.py flask-script简单探索
        - migrateTest.py flask-migrate简单使用
        - sqlchemyTest.py flask-SQLAlchemy使用
    
- 网页操作
    - 注册  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/register_page.png)
    - 邮箱验证  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/register_mail.png)
    - 登录  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/login_page.png)
    - 首页  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/index_page.png)
    - one post  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/onepost_page.png)
    - update post  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/update_post_page.png)
    - update user info  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/update_userinfo_page.png)
    - user page  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/user_page.png)
    - 取消评论  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/mederate_comment_page.png)
    - comments api接口调用  
    ![image](https://github.com/elephanyu/myflask/blob/master/descpng/api_comment_get.png)