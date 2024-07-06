# 现在商场在举办大胃王比赛，按照吃肉包子的个数进行等级划分，对应的规则如下：
# 小明同学吃了25个包子，判断小明同学处于什么级别

count = int(input('输入包子的个数：'))
if count == 40:
    print('超级大胃王')
elif 30 <= count <= 39:
    print('大胃王高手')
elif 30 <= count <= 39:
    print('初级大胃王')
elif 30 <= count <= 39:
    print('仍需努力')
else:
    print('无效输入')

# 2.判断数字的正负：
# 在输入端输入一个数字，判断数字是正数，负数还是零


input_num = int(input('输入数字：'))
if input_num > 0:
    print('是正数')
elif input_num == 0:
    print('是零')
else:
    print('是负数')

# 3.趣味折纸
# 请分别使用while 和 for ，计算：一张纸的厚度是0.01毫米，对折15次的厚度是多少毫米。

height_while = 0.01
fold_num_while = 0
while fold_num_while <= 15:
    height_while *= 2
    fold_num_while += 1
print('对折15次的厚度' + str(height_while))

height_for = 0.01
for num_for in range(0, 16, 1):
    height_for *= 2
print('对折15次的厚度' + str(height_for))

# 4.累加
# 累加10~60之间 (包括60) ，能被5整除的数

count = 0
for num_count in range(10, 61, 5):
    count += num_count
print('累积号' + str(count))
