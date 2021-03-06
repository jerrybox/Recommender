import math

movie_data = {
    "宝贝当家": [45, 2, 9, "喜剧片"],
    "美人鱼": [21, 17, 5, "喜剧片"],
    "澳门风云2": [54, 9, 11, "喜剧片"],
    "功夫熊猫3": [39, 0, 31, "喜剧片"],
    "谍影重重": [5, 2, 57, "动作片"],
    "叶问3": [3, 2, 65, "动作片"],
    "伦敦沦陷": [2, 3, 55, "动作片"],
    "我的特工爷爷": [6, 4, 21, "动作片"],
    "奔爱": [7, 46, 4, "爱情片"],
    "夜孔雀": [9, 39, 8, "爱情片"],
    "代理情人": [9, 38, 2, "爱情片"],
    "新步步惊心": [8, 34, 17, "爱情片"]
}

new = {"唐人街探案": [21, 3, 17, "?片"]}

x = [23, 3, 17]

KNN = []

for key, v in movie_data.items():
    d = math.sqrt((x[0] - v[0]) ** 2 + (x[1] - v[1]) ** 2 + (x[2] - v[2]) ** 2)
    KNN.append([key, round(d, 2)])

KNN.sort(key=lambda dis: dis[1])

labels = {"喜剧片": 0, "动作片": 0, "爱情片": 0}

for s in KNN[:5]:
    label = movie_data[s[0]]
    labels[label[3]] += 1

labels = sorted(labels.items(), key=lambda l: l[1], reverse=True)

print(labels, labels[0][0], sep='\n')

# [('喜剧片', 4), ('动作片', 1), ('爱情片', 0)]
# 喜剧片
