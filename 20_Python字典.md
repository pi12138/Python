# Python字典

- dict 键必须是可散列的

## 可散列对象

- 一个可散列的对象必须满足以下要求。
	1. 支持 hash() 函数，并且通过 `__hash__()` 方法所得到的散列值是不变的。
	2. 支持通过 `__eq__()` 方法来检测相等性。
	3. 若 a == b 为真，则 hash(a) == hash(b) 也为真。
- 所有由用户自定义的对象默认都是可散列的，因为它们的散列值由 id() 来获取，而且它们都是不相等的。

## 字典生成式

```Python
In [12]: b
Out[12]: {'one': 1, 'two': 2}

In [13]: d = {k:v for k,v in b.items()}

In [14]: d
Out[14]: {'one': 1, 'two': 2}

```

- 注意和集合生成式的区别