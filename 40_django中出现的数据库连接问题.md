# django连接数据库问题

## django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module

- 解决方案: 在__init__.py中添加

```python
import pymysql

pymysql.install_as_MySQLdb()
```

