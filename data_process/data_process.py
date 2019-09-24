import csv

def read_tsv(file):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        lines = []
        for line in reader:
            lines.append(line)
        return lines
# *******************数据处理************************************
# csv_reader=csv.reader(open('融云-北京力拓飞远科技有限公司.csv'))
# i = 0
# j = 0
# with open('data.tsv','w') as f:
#
#     for row in csv_reader:
#         # print(row)
#         s = '\n'+str(row[3])+'\t'+str(row[1])
#         if i ==0:
#             f.write('class'+'\t'+'txt')
#         elif str(row[3])!='正常':
#             f.write(s)
#         elif j <101:
#             f.write(s)
#             j +=1
#         i +=1
#         print(i)
##################################################################
lines = read_tsv('./data.tsv')
i = 0
j = 0
s = set()
for row in lines:
    s.add(row[0])
print(s)
# with open('data_final.tsv','w') as f:
#     for row in lines:
#         if row[0]=='正常':
#             f.write(str(row[0])+'\t'+str(row[1])+'\n')
#         if row[0]=='违规':
#             f.write('违法违规'+'\t'+str(row[1])+'\n')
#         if row[0]=='色情':
#             f.write(str(row[0])+'\t'+str(row[1])+'\n')
#         if row[0]=='政治':
#             f.write('涉政'+'\t'+str(row[1])+'\n')
#         if row[0]=='疑似广告':
#             f.write('广告'+'\t'+str(row[1])+'\n')
#         if row[0]=='涉政':
#             f.write(str(row[0])+'\t'+str(row[1])+'\n')
#         if row[0]=='违法':
#             f.write('违法违规'+'\t'+str(row[1])+'\n')
#         if row[0]=='辱骂':
#             f.write(str(row[0])+'\t'+str(row[1])+'\n')
#         if row[0]=='粗口':
#             f.write('辱骂'+'\t'+str(row[1])+'\n')
#         if row[0]=='广告':
#             f.write(str(row[0])+'\t'+str(row[1])+'\n')
##################################################################

# *******************数据处理************************************
# csv_reader=csv.reader(open('quya_sm_detection_records.csv'))
#
# i = 0
# j = 0
# with open('data_append.tsv','w') as f:
#
#     for row in csv_reader:
#         # print(row)
#         s = '\n'+str(row[16])+'\t'+str(row[5].replace('\n', ''))
#         if i ==0:
#             f.write('class'+'\t'+'txt')
#         elif str(row[16])!='正常':
#             f.write(s)
#         elif j <150:
#             f.write(s)
#             j +=1
#         i +=1
#         print(i)
