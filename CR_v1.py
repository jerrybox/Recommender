import math

course_list = ["course_1","course_2","course_3","course_4","course_5",
               "course_6","course_7","course_8","course_9","course_10",
               "course_11","course_12","course_13","course_14","course_15"]
user_course = {
    "user_1":[1,1,0,0,1,0,0,0,0,1,0,0,0,1,1],
    "user_2":[1,1,0,1,0,1,0,1,0,0,0,0,1,0,0],
    "user_3":[1,1,1,1,1,1,0,0,0,0,0,0,1,0,0],
    "user_4":[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    "user_5":[0,0,0,0,0,0,0,0,1,1,0,1,0,1,0],
    "user_6":[1,1,0,1,1,1,0,0,0,0,0,0,0,0,0],
    "user_7":[1,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
    "user_8":[1,1,0,0,1,1,0,0,0,0,0,0,0,0,1],
    "user_9":[1,1,1,0,1,1,0,0,1,1,1,0,0,0,0],
}

def sub_sq_sum(list0, list1):
    """连个列表的差的平方的和"""
    sum = 0
    for i in range(len(list0)):
        sum += (list0[i] - list1[i])**2
    return sum

user_10 = [1,0,0,1,1,0,0,0,0,1,0,0,0,0,0]

KNN = []
for key, v in user_course.items():
    d = math.sqrt(sub_sq_sum(user_10,v))
    KNN.append([key, round(d, 2)])

KNN.sort(key=lambda x:x[1])

course_sed = []

def course_sub(list1,list2):
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

for i in KNN[:3]:
    index_dif = course_sub(user_course[i[0]],user_10)
    print(index_dif)
    course_sed.extend(index_dif)

course_data = {"course_1":0,"course_2":0,"course_3":0,"course_4":0,"course_5":0,
               "course_6":0,"course_7":0,"course_8":0,"course_9":0,"course_10":0,
               "course_11":0,"course_12":0,"course_13":0,"course_14":0,"course_15":0}


course_sed = [x for x in course_sed if not user_10[x]]

for i in course_sed:
    course_data[course_list[i]] += 1

labels = sorted(course_data.items(),key=lambda x:x[1], reverse=True)
print(labels)
'''
**************************************************
['user_7', 1.0]
['user_6', 1.73]
['user_1', 2.0]
['user_3', 2.24]
['user_8', 2.24]
['user_4', 2.24]
['user_2', 2.45]
['user_5', 2.45]
['user_9', 2.45]
**************************************************
[3]
[1, 5, 9]
[1, 3, 13, 14]
[('course_2', 2), ('course_6', 1), ('course_15', 1), ('course_14', 1), ('course_8', 0), ('course_1', 0), ('course_11', 0), ('course_9', 0), ('course_13', 0), ('course_3', 0), ('course_12', 0), ('course_10', 0), ('course_4', 0), ('course_7', 0), ('course_5', 0)]

'''