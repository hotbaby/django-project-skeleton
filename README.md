# django-project-skeleton
Django Project Skeleton

## 错误码

异常错误码由6个字节组成:
* 前两个字节为保留位”00“
* 中间两个字节为应用的索引，取值范围”00“ - ”99“，系统默认内建异常为”00“
* 最后两个字节为应用内部异常，取值范围"00" - “99”

示例：系统内置缺少参数异常错误码 "000001"

## Create django project
```sh
django-admin startproject --template https://github.com/hotbaby/django-project-skeleton/archive/master.zip --name pytest.ini project-name
```

OR

```sh
wget https://github.com/hotbaby/django-project-skeleton/archive/master.zip && django-admin startproject --template file://$PWD/master.zip --name pytest.ini project && rm -f master.zip
```