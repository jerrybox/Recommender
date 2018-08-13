import tkinter
import math

window = tkinter.Tk()
window.title("MovieRecommender")
window.geometry("470x470+300+100")

sample_label = tkinter.LabelFrame(window, text=" 配置选项：")
sample_label.grid(column=0, row=0, padx=10, pady=10)

label_movie = tkinter.Label(sample_label, text=u'样本:', font=('Arial', 10), width= 5, height=2)
label_movie.grid(column=0, row=0, padx=10, pady=10)

data_movie = tkinter.Text(sample_label,height=15,width=50)
data_movie.grid(column=1, row=0, padx=10, pady=10)


label_new = tkinter.Label(sample_label, text=u'输入:', font=('Arial', 10), width= 5, height=2)
label_new.grid(column=0, row=1, padx=10, pady=10)

new_movie = tkinter.Entry(sample_label)
new_movie.grid(column=1, row=1, padx=10, pady=10)

result_label = tkinter.LabelFrame(window, text="预测结果")
result_label.grid(column=0, row=2, padx=10, pady=10)

label_movie = tkinter.Label(result_label, text=u'结果', font=('Arial', 10), width= 5, height=2)
label_movie.grid(column=0, row=1, padx=10, pady=10)

result_label = tkinter.Text(result_label, height=2, width=50, )
result_label.grid(column=1, row=1, padx=10, pady=10)

def get_data_movie():
    print("数据库",data_movie.get("1.0", tkinter.END))
    return data_movie.get("1.0", tkinter.END)

def get_new_movie():
    print("预测电影",new_movie.get())
    return new_movie.get()

def go():
    movie_data = eval(get_data_movie())
    x = eval(get_new_movie())
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
    result_label.delete(1.0,tkinter.END)
    result_label.insert(tkinter.END, labels)
    result_label.insert(tkinter.END, "\n")
    result_label.insert(tkinter.END,labels[0][0])

get_data = tkinter.Button(window,text="预测",command=go)
get_data.grid(column=0, row=1, padx=10, pady=10)

window.mainloop()


