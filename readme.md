# flask-admin.py 
## 命令行工具， 模拟django， 生成flask项目的骨架

###安装
`sudo pip install flask-admin.py`

###使用
创建项目 

1.`flask-admin.py --startproject [project name]`
        
2.`flask-admin.py -p [project name]`

创建一个app 

1. `flask-admin.py --startapp [app name]`

2. `flask-admin.py --a [app name]`


###生成的目录树为


    .
    ├── app
    │   ├── email.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── errors.py
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── models.py
    │   ├── static
    │   └── templates
    ├── config.py
    ├── manage.py
    ├── migrations
    ├── requirements.txt
    ├── tests
    │   └── __init__.py
    └── venv


#TODO

1. 使创建的文件填充有意义的代码
