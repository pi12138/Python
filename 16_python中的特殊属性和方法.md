# python 中的特殊属性和方法

## `__name__`

- 模块是对象，并且每个模块都有一个内置属性__name__。
- 当一个模块被直接运行的时候，该模块__name__的值就等于缺省的'__main__'。
- 如果一个模块被import ，那么这个被引入模块__name__的值就等于该模块名，也就是文件名去掉py扩展名的部分。

## `__file__`

- __file__表示显示文件当前的位置
- 如果当前文件包含在sys.path里面，那么，__file__返回一个相对路径！
- 如果当前文件不包含在sys.path里面，那么__file__返回一个绝对路径！