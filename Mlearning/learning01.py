import os
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split

PATH = r'./data/iris/'

#定义自定义字体，文件名是系统中文字体
myfont = matplotlib.font_manager.FontProperties(fname='D:/Windows/Fonts/simkai.ttf')  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus']=False
# r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

# with open(PATH+'iris.data','w') as f:
#     f.write(r.text)

# os.chdir(PATH)

df = pd.read_csv(PATH+'iris.data',names=['sepal length','sepal width','petal length','petal width','class'])

# df['short class'] = df['class'].map({'Iris-setosa':'SET','Iris-virginica':'VIR','Iris-versicolor':'VER'})

# print(df.ix[:4])
# df['wide petal'] = df['petal width'].apply(lambda v: 1 if v>=1.3 else 0)
# print(df.head())

# print(df.head())

# print(df.ix[:3,[x for x in df.columns if 'width' in x]])

# print(df['class'].unique())

# print(df.count())
# df1 = df[df['class']=='Iris-virginica']
# print(df1)

# # 创建一个新的DataFrame,重置行号
# df2 = df1.reset_index(drop=True)
# print(df2)

# 创建画布
# fig, ax = plt.subplots(2,2,figsize=(6,4))
# colors=['red','yellow','green','black']

# for i in range(2):
#     for j in range(2):
#         ax[i][j].hist(df[df.columns[i*2+j]],color = colors[i*2+j])
#         ax[i][j].set_ylabel(u'数量',fontsize = 12,FontProperties = myfont)
#         ax[i][j].set_xlabel(u'变量',fontsize = 12,FontProperties = myfont)
#         ax[i][j].set_title('Iris'+df.columns[i*2+j],fontsize=14,y = 1.01)
# plt.tight_layout()
# plt.show()


# ax.hist(df['petal width'],color = 'red')
# ax.set_ylabel(u'数量',fontsize = 12,FontProperties = myfont)
# ax.set_xlabel(u'宽度',fontsize = 12,FontProperties = myfont)
# plt.title('Iris Petal Width',fontsize=14,y = 1.01)
# plt.show()
# 数据特征
X = df.ix[:,:4]
# 分类结果
y = df.ix[:,4]

clf = RandomForestClassifier(max_depth=5,n_estimators=10)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .3)

clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

rf = pd.DataFrame(list(zip(y_pred,y_test)),columns=['预测值','真实值'])
rf['是否正确'] = rf.apply(lambda v: 1 if v['预测值']==v['真实值'] else 0,axis=1)

print(rf['是否正确'].sum()/rf['是否正确'].count())
print(rf)
