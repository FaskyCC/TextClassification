import csv


def read_tsv(file):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        lines = []
        for line in reader:
            lines.append(line)
        return lines


test = read_tsv('../data_dir/test.tsv')

negative_labels = ['涉政', '违法违规', '色情', '广告', '辱骂']

test_result = read_tsv('../output/test_results.tsv')
num = len(test)
print(len(test_result),num)
acc_all = 0
acc_2 = 0

negative_predict = 0
negative_all = 0

with open('./预测结果.csv','w') as f:
    f.write('正确标签,预测标签,文本\n')
    for i in range(num):
        # print(test[i])
        # print(test_result[i])
        if test[i][0] in negative_labels:
            negative_all +=1
        if test[i][0] in negative_labels and test_result[i][6] in negative_labels:
            negative_predict +=1
        if test[i][0]==test_result[i][6]:
            acc_all +=1
            acc_2 +=1
        elif test[i][0] in negative_labels and test_result[i][6] in negative_labels:
            acc_2 +=1

            # print(test[i][0], test_result[i][6],test[i][1])
        else:
            pass
            print('正确标签:',test[i][0],'预测标签:',test_result[i][6], test[i][1])
        s = str(test[i][0])+','+str(test_result[i][6])+','+str(test[i][1])+'\n'
        f.write(s)
        # print(acc_all,acc_2)
recall = negative_predict/negative_all
Acc_all = acc_all/num
Acc_2 = acc_2/num
F1 = 2*Acc_all*recall / (Acc_all+recall)
print('准确率为:',Acc_all)
print("判准率为", Acc_2)
print('异常言论查全率:',recall)
print('F1',F1)