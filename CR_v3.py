import math

user_list = ["user_1","user_2","user_3","user_4","user_5",
               "user_6","user_7","user_8","user_9","user_10"]
user_dict = {user_index:user_list[user_index] for user_index in range(len(user_list))}

course_user = {
    "course_1":[1,1,1,0,0,1,1,1,1,1],
    "course_2":[1,1,1,0,0,1,0,1,1,0],
    "course_3":[0,0,1,0,0,0,0,0,1,0],
    "course_4":[0,1,1,0,0,1,0,0,0,1],
    "course_5":[1,0,1,0,0,1,1,1,1,1],
    "course_6":[0,1,1,0,0,1,0,1,1,0],
    "course_7":[0,0,0,0,0,0,0,0,0,0],
    "course_8":[0,1,0,0,0,0,0,0,0,0],
    "course_9":[0,0,0,0,1,0,0,0,1,0],
    "course_10":[1,0,0,0,1,0,1,0,1,1],
    "course_11":[0,0,0,0,0,0,0,0,1,0],
    "course_12":[0,0,0,0,1,0,0,0,0,0],
    "course_13":[0,1,1,1,0,0,0,0,0,0],
    "course_14":[1,0,0,0,1,0,0,0,0,0],
    "course_15":[1,0,0,0,0,0,0,1,0,0]
}


def cos_list(list0, list1):
    numerator = 0
    for i in range(len(list0)):
        numerator += list0[i] * list1[i]
    denominator = math.sqrt(sum([i ** 2 for i in list0])) + math.sqrt(sum([i ** 2 for i in list1]))
    # print(numerator, "/", denominator)
    return numerator / denominator

#
user_10 = [1,0,0,1,1,0,0,0,0,1,0,0,0,0,0]

# 求与course_1,course_4,course_5,course_10最相近的课程
course_1_heighbors = [(k,cos_list(course_user["course_1"],course_user[k])) for k in course_user if k != "course_1"]
course_1_heighbors.sort(key=lambda x:x[1],reverse=True)
print(course_1_heighbors[:3])

course_4_heighbors = [(k,cos_list(course_user["course_4"],course_user[k])) for k in course_user if k != "course_4"]
course_4_heighbors.sort(key=lambda x:x[1],reverse=True)
print(course_4_heighbors[:3])

course_5_heighbors = [(k,cos_list(course_user["course_5"],course_user[k])) for k in course_user if k != "course_5"]
course_5_heighbors.sort(key=lambda x:x[1],reverse=True)
print(course_5_heighbors[:3])

course_10_heighbors = [(k,cos_list(course_user["course_10"],course_user[k])) for k in course_user if k != "course_10"]
course_10_heighbors.sort(key=lambda x:x[1],reverse=True)
print(course_10_heighbors[:3])

'''
[('course_5', 1.2787306957711964), ('course_2', 1.136812145889036), ('course_6', 0.9872652454106674)]
[('course_13', 0.5358983848622454), ('course_3', 0.2928932188134525), ('course_6', 0.7082039324993691)]
[('course_13', 0.2284251258739283), ('course_3', 0.4926150994765982), ('course_6', 0.8193666671296017)]
[('course_5', 0.8193666671296017), ('course_1', 0.7898121963285339), ('course_9', 0.5479029434177964)]
'''

course_rec_data = course_1_heighbors + course_4_heighbors + course_5_heighbors + course_10_heighbors
course_rec_dict = {}
for i in course_rec_data:
    if i[0] in course_rec_dict:
        course_rec_dict[i[0]] += i[1]
    else:
        course_rec_dict[i[0]] = i[1]

# 设置断点


print(sorted(course_rec_dict.items(), key=lambda x:x[1], reverse=True))

course_list = ["course_1","course_2","course_3","course_4","course_5",
               "course_6","course_7","course_8","course_9","course_10",
               "course_11","course_12","course_13","course_14","course_15"]

recommend = []
for i in course_rec_dict:
    if user_10[course_list.index(i)] == 0:  # 去掉重复的
        recommend.append((i,course_rec_dict[i]))

recommend.sort(key=lambda x:x[1],reverse=True)
print("*" * 50)
print(recommend[:3])
