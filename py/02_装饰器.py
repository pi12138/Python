
# 函数无参数使用装饰器
def func1(func):
	def wrapper():
		print("start.....")
		print("我是附加功能")
		func()
		print("end.......")

	return wrapper


@func1
def test1():
	print("这是test1")


# ----------------------------------------------
# 函数有参数使用装饰器
def func2(func):
	def wrapper(x):
		print("我是附加功能！")
		func(x)

	return wrapper

@func2
def test2(x):
	print("我是test2,传入了一个参数{}".format(x))


# ------------------------------------------
# 装饰器中没有使用被装饰的函数
def func3(func):
	def wrapper():
		print("我是装饰器3")
		print("我没有调用被我装饰的函数")

	return wrapper

	
@func3
def test3():
	print("我是test3")


# --------------------------------------
# 装饰器原理
def func4(func):
	def wrapper():
		print("这是新添加的功能")
		func()
	return wrapper


def test4():
	print("我是test4")


test4 =  func4(test4)


if __name__ == "__main__":
	test1()
	test2(100)
	test3()
	test4()
	# test5(10, 20)