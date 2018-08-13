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


for k, v in course_user.items():
    cos_user = cos_list(v, user_10)
    KNN.append([k, round(cos_user, 2)])

KNN.sort(key=lambda x: x[1], reverse=True)

course_sed = []

def course_sub(list1, list2):
    """两个用户间的课程差别"""
    index_dif = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            index_dif.append(i)
    return index_dif

print("*" * 50)
for i in KNN:
    print(i)
print("*" * 50)

#
# for i in KNN[:3]:
#     index_dif = user_sub(course_user[i[0]],course_15)
#     print(index_dif)
#     user_sed.extend(index_dif)
#
# course_data = {"course_1":0,"course_2":0,"course_3":0,"course_4":0,"course_5":0,
#                "course_6":0,"course_7":0,"course_8":0,"course_9":0,"course_10":0,
#                "course_11":0,"course_12":0,"course_13":0,"course_14":0,"course_15":0}
#
#
# course_sed = [x for x in user_sed if not course_15[x]]
#
# for i in course_sed:
#     course_data[user_list[i]] += 1
#
# labels = sorted(course_data.items(),key=lambda x:x[1], reverse=True)
# print(labels)
