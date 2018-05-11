# coding=utf-8

# import this # python之禅

# 从心开始:)

### 变量：
# 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头。
# 变量名不能包含空格，但可使用下划线来分隔其中的单词。
# 不要将Python关键字和函数名用作变量名。

# message = "Hello Python Crash Course reader!"; # 变量
# print(message); # 打印变量

### 字符串
# name = "tianshw" + " 你好！";
# print(name.title()); # 首字母大写
# print(name.upper()); # 全部大写
# print(name.lower()); # 全部小写
# print(name.lstrip()); # 删除开头空白
# print(name.rstrip()); # 删除结尾空白
# print(name.strip()); # 删除空白

### 数字
# print(2 + 1); # 加
# print(2 - 1); # 减
# print(2 * 2); # 乘
# print(3 / 2); # 除
# print(3 ** 2); # 乘方
# print(str(12) + "岁！"); # 数字转字符串

### 列表
# bicycles=["tianshw","mouxing","and"]; # 定义列表
# print(bicycles[0]); # 打印列表第一个元素
# print(bicycles[-1]); # 打印列表最后一个元素
# bicycles.append("hello"); # 在列表末尾追加元素
# bicycles.insert(3,"me"); # 在指定索引处插入元素
# del bicycles[2]; # 删除指定索引的元素
# popped_bicycles = bicycles.pop(); # 删除列表最后一个元素，并把删除的值给popped_bicycles
# popped_bicycles = bicycles.pop(1); # 删除列表指定索引的元素，并把删除的值给popped_bicycles
# bicycles.remove("mouxing"); # 根据值删除元素
# bicycles.sort(); # 按字母顺序永久排序
# bicycles.sort(reverse=True); # 按字母顺序永久倒序排序
# sorted(bicycles); # 按字母顺序临时排序
# sorted(bicycles,reverse=True); # 按字母顺序临时倒序排序
# bicycles.reverse(); # 倒着永久性打印列表
# len(bicycles); # 计算列表长度

### 遍历列表
# for item in bicycles:
#  	 print(item);  #缩进表示在循环内，不缩进表示退出循环

### 数字列表
# numbers = list(range(1,6)); # 创建数字1-5的列表
# even_numbers = list(range(2,11,2)); # 创建10以内的偶数列表，range(开始位置，结束位置，步长)
# print(min(even_numbers)); # 取数字列表最小值
# print(max(even_numbers)); # 取数字列表最大值
# print(sum(even_numbers)); # 计算数字列表的总和

### 列表解析
# nums = [value + 1 for value in range(1,6)]; # 创建数字1-5的列表，并把每个列表值加1

# 列表切片：列表的部分元素
# print(numbers[0:3]); # 从下标0开始，取三个元素作为切片
# print(numbers[:3]); # 不指定下标，则默认从0开始
# print(numbers[0:]); # 不指定个数，则到末尾结束
# print(numbers[-3:]); # 从倒数第三个开始取值
# copylist = numbers[:]; # 首尾索引都为空则表示复制

### 元组：不可改变的列表
# dimensions = (200,50); # 创建元组
# dimensions = (100,50); # 元组内容不可更改，但可以重新定义元组

### if语法
# cars = ["audi","bmw","subaru","toyota"];
# if cars[0] == "bmw" or cars[1] == "audi": # if中or和and用法
# 	 print(cars[0].upper());
# if "audi" not in cars: # if中in和not in的用法
#	 print("不在！");
# elif "audi" in cars: # else if的用法
#	 print("在！");

### 字典
# alien = { "color": "red", "points": 5, "y_position": 5 }; # 创建字典
# alien["x_position"] = 0; # 添加字典元素
# alien["color"] = "yellow"; # 修改字典元素
# del alien["x_position"]; # 删除字典元素

### 遍历字典：所有键
# for jian in alien.keys():
#	 print("\nkey: " + jian);

### 遍历字典：排序后的所有键
# for jian in sorted(alien.keys()):
#	 print("\nkey: " + jian);

### 遍历字典：所有值
# for zhi in alien.values():
#	 print("\nkey: " + str(zhi));

### 遍历字典：所有值，并去掉重复项
# for zhi in set(alien.values()):
#	 print("\nkey: " + str(zhi));

### 遍历字典：所有键值
# for jian,zhi in alien.items():
#	 print("\nkey: " + jian);
#	 print("value: " + str(zhi));

### 字典嵌套：在列表中存储字典
# aliens = [];
# for alien_number in range(30): # 创建一个包含30个字典元素的列表
#	 temp_alien = {"color":"green","points":alien_number,"speed":"slow"};
#	 aliens.append(temp_alien);
# for alien in aliens[:5]: # 打印前五个字典元素
#	 print(alien);

### 字典嵌套：在字典中存储列表




