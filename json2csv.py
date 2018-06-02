import sys, os
import pandas as pd


try:
    json_file = input('请输入要解析的json文件名，json文件必须和当前程序同一目录下：')
    if os.path.exists(sys.path[0] + '/' + json_file) == True:
        data = pd.read_json(json_file, encoding="utf8") # 编码很重要，否则会报到错    
    else:
        print('当前目录并没有该文件，请重新运行该程序')
    
    csv_file = input('请输入要导出的csv文件名，文件保存在前程序同一目录下：')
    if csv_file.endswith('csv') == False:
        print('???开玩笑么，导出格式为xx.csv')
    else:
        data.to_csv(csv_file)

except:
    print('json文件必须是标准json，请检查是否为[{"name":"xx"},{"age":"20"}]格式\n输入格式必须要加后缀，如xx.json|xx.csv')
