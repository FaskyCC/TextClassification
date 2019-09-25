# 【导入相应的库（对数据库进行切分需要用到的库是sklearn.model_selection 中的 train_test_split）】
import numpy as np
from sklearn.model_selection import train_test_split


# 【首先，读取.CSV文件成矩阵的形式。】
# 若标签为浮点，直接使用下面一行即可
# data = np.loadtxt(open("iris.csv"),delimiter=",",skiprows=0)

##--------------------【若标签为Striing,先将标签转化为浮点型】------------------------------
def iris_type(s):
    class_label = {'正常': 0, '违规': 1, 'Iris-virginica': 2}
    return class_label[s]


# 使用numpy中的loadtxt读入数据文件（csv格式的iris数据，也可直接换成txt格式）
filepath = './data.tsv'  # 数据文件路径
data = np.loadtxt(filepath, dtype=str, delimiter='\t')
##-------------------------------------------------------------------------------------

# 【将矩阵最后一列之前的数值给X（输入数据），将矩阵最后一列的数值给y（标签）】
y, X = data[:, :-1], data[:, -1]

# 【利用train_test_split方法，将X,y随机划分为训练集（X_train），训练集标签（y_train），测试集（X_test），测试集标签（y_test），按训练集：测试集=7:3的概率划分，到此步骤，可以直接对数据进行处理】
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with open('./train.tsv', "w") as f:
# 【将训练集与数据集的数据分别保存为CSV文件】
    for i in range(len(X_train)):
        s = str(y_train[i][0])+'\t'+str(X_train[i])+'\n'
        f.write(s)

with open('./test_all.tsv', "w") as f:
# 【将训练集与数据集的数据分别保存为CSV文件】
    for i in range(len(X_test)):
        s = str(y_test[i][0])+'\t'+str(X_test[i])+'\n'
        f.write(s)