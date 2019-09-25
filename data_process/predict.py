import csv


def read_tsv(file):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        lines = []
        for line in reader:
            lines.append(line)
        return lines


test = read_tsv('../data_dir/test.tsv')

test_result = read_tsv('../output/test_results.tsv')

with open('./预测结果_无标签.csv','w') as f:
    f.write('预测标签,文本\n')
    for i in range(len(test)):
        f.write(str(test_result[i][6])+','+str(test[i][0])+'\n')
