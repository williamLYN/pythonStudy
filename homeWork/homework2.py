# 1.我们需要在终端输入同学们的成绩，如果成绩值为-1,打印成绩录入完成
# 2.把每个同学的成绩，放到一个名为scores的列表里面
# 3.去掉一个最大值，去掉一个最小值，对剩下的成绩求平均值
# （最大值函数是max，最小值函数是min，平均值 = 所有的成绩和 / 总人数）
# 4.使用一个字典，分别存储成绩90分以上的人数，和60分以下的人数
# 成绩如右：96,92,100,54,89,72,48,86，-1


def scores_fun(scores_list):
    scores_list.remove(max(scores_list))
    scores_list.remove(min(scores_list))
    avg = sum(scores_list) / len(scores_list)
    scores_upper_ninety = []
    scores_lower_sixty = []
    for i in scores_list:
        if i >= 90:
            scores_upper_ninety.append(i)
        elif i < 60:
            scores_lower_sixty.append(i)
    scores_dic = {}
    scores_dic['90'] = scores_upper_ninety
    scores_dic['60'] = scores_lower_sixty
    print(f"平均值为：{avg}")
    print(f"字典为：{scores_dic}")


scores = []
while True:
    score = int(input("Please input your score:"))
    if score == -1:
        break
    scores.append(score)

scores_fun(scores)


# 1.在终端输入一个正整数，计算所有小于该数的偶数的和，并打印
# 2.把上述要求改写成函数，并计算49的结果


def num_sum_fun(num):
    sum_list = []
    for i in range(1, num):
        if i % 2 == 0:
            sum_list.append(i)
    print(f"偶数为：{sum_list}")
    print(f"{num}的偶数之和为：{sum(sum_list)}")


num_sum_fun(49)
