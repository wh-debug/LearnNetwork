# 第一个测试程序
print("hello, world!")

# 第二个测试程序
message = "Hello python world!"
print(message)

# 使用f
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")


message = f"Hello, {full_name.title()}!"
print(message)

# 制表符的使用
print("python")
print("\tpython")

print("Languages:\nPython\nC\nJavascript")
print("Languages:\n\tPython\n\tC\n\tJavascript")

# 多余空白的处理
favorite_Language = 'python '
favorite_Language.rstrip()
favorite_Language = favorite_Language.rstrip()

Programs = ' python '
Programs.rstrip() # 删除后面的空格
Programs.lstrip() # 删除前面的空格
Programs.strip() # 删除两边的空格


