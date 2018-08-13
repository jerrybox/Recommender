# -*- coding=utf-8 -*-
# form "https://blog.csdn.net/xyfengbo/article/details/51436423"
import sys
import math
from texttable import Texttable


# 计算余弦距离
def getCosDist(user1,user2):
    """
    :param user1: list
    :param user2: list
    :return:
    """
    sum_x = 0.0
    sum_y = 0.0
    sum_xy = 0.0

    for key1 in user1:
        for key2 in user2:
            if key1[0] == key2[2]:
                sum_x += key1[1] ** 2
                sum_y += key2[1] ** 2
                sum_xy += key1[1] * key2[1]
    if sum_xy == 0.0:
        return 0
    demo = math.sqrt(sum_x * sum_y)
    return sum_xy / demo


def readFile(filename):
    """
    :param filename: directory
    :return:
    """
    contents = []
    f = open(filename,"r")
    contents = f.readlines()
    f.close()
    return contents


def getRatingInfo(ratings):
    """
    :param ratings: [["user","movie","评分"],]
    :return:
    """
    rates = []
    for line in ratings:
        rate = line.split("\t")
        rates.append([int(rate[0]), int(rate[1]), int(rate[2])])

    return rates


def getUserScoreDataStructure(rates):
    userDict = {}  # {"user":[("movies1", 1),("movies2", 5)],"user2",[]}
    itemUser = {}  # {"movie1":[user]} # 哪些用户看过这个电影了
    for k in rates:
        user_rank = (k[1],k[2])
        if k[0] in userDict:
            userDict[k[0]].append(user_rank)
        else:
            userDict[k[0]] = user_rank

        item_rank = ()
        if k[1] in itemUser:
            itemUser[k[1]].append(k[0])
        else:
            itemUser[k[1]] = [k[0]]
    return userDict,itemUser


def getNearestNeighbor(userId,userDict,itemUser):
    """
    :param userId:
    :param userDict:
    :param itemUser:
    :return:  neighbors 邻居用户：与当前用户至少看过一部相同的电影的用户
               neighbors_dist 把这些邻居用户的相似度计算出来： 与userId 的相似度 [[0.25896,"User2"],[0.15896,"User3"],]
    """
    neighbors = []  #
    for item in userDict[userId]:  # [("movies1", 1),("movies2", 5)]
        for neighbor in itemUser[item[0]]:  # ["user1", "user2"]
            if neighbor != userId and neighbor not in neighbors:
                neighbors.append(neighbor)

    neighbors_dist = []

    for neighbor in neighbors:
        dist = getCosDist(userDict[userId], userDict[neighbor])  # 计算用户相似度
        neighbors_dist.append([dist, neighbor])

    neighbors_dist.sort(reverse=True)

    return neighbors_dist


def recommendByUserFC(filename, userId, k=5):
    contents = readFile(filename)

    rates = getRatingInfo(contents)

    userDict, itemUser = getUserScoreDataStructure(rates)

    neighbors = getNearestNeighbor(userId, userDict, itemUser)[:5]  # 取前5个最相近的邻居

    recommend_dict = {}  # { "movie1":100, "movie2":200}

    for neighbor in neighbors:
        neighbor_user_id = neighbor[1]
        movies = userDict[neighbor_user_id]
        for movie in movies:  # 不需要排除掉UserId看过的电影吗？
            # if movie[0] in [m[0] for m in userDict[userId]]:
            #     continue

            if movie[0] in recommend_dict:
                recommend_dict[movie[0]] += neighbor[0]
            else:
                recommend_dict[movie[0]] = neighbor[0]

    recommend_list = []  # [[200, "movie1"],[20, "movie2"]]
    for key in recommend_dict:
        recommend_list.append([recommend_dict[key], key])

    recommend_list.sort(reverse=True)
    user_movies = [k[0] for k in userDict[userId]]

    return [k[1] for k in recommend_list], user_movies, itemUser, neighbors


def getMovieList(filename):
    contents = readFile(filename)
    movies_info = {}

    for movie in contents:
        single_info = movie.split("|")
        movies_info[int(single_info[0])] = single_info[:1]
    return movies_info


if __name__ == "__main__":
    reload(sys)  # 防止sys模块内容已经被修改（如添加了新的包路径），重新加载sys模块

    sys.setdefaultencoding('utf-8')

    movies = getMovieList("u.item")
    recommend_list, user_movie,items_movie, neighbors = recommendByUserFC("u.data", userId=50, k=80)
    neighbors_id = [i[1] for i in neighbors]  # 邻居用户

    table = Texttable
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(["t", "t","t"])
    table.set_cols_align(["l" for i in range(3)])

    rows = []
    rows.append([u'moive name', u'release', u'from userid'])

    for movie_id in recommend_list[:20]:  # []
        from_user = []
        for user_id in items_movie[movie_id]:  # 看了这个电影用户有哪些, 其中的邻居用户，作为推荐此电影的用户，保存起来
            if user_id in neighbors_id:
                from_user.append(user_id)

        rows.append([movies[movie_id][0], movies[movie_id][1], "".join(from_user)])

    table.add_rows(rows)
    print(table.draw())

"""
rates：读取文件，获得[用户，电影，评分]的原始数据

userDict: 统计所有用户看过的电影及评分 {"user":[("movies1", 1),("movies2", 5)],"user2",[]}
itemUser：统计电影被多少用户看过 {"movie1":[user]} # 哪些用户看过这个电影了

neighbors：找到与当前用户至少看过意不相同电影的用户，计算相似度，取前K名用户作为邻居用户
recommend_list: 统计邻居用户看的电影的总评分，取前20个展示出来
"""


















