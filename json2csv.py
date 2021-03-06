import sys, os
import pandas as pd

def json2csv():
    try:
        json_file = input('请输入要解析的json文件名，json文件必须和当前程序同一目录下：') + '.json'
        if os.path.exists(sys.path[0] + '/' + json_file) == True:
            data = pd.read_json(json_file, encoding="utf8") # 编码很重要，否则会报到错    
        else:
            print('当前目录并没有该文件，请重新运行该程序')
        
        csv_file = input('请输入要导出的csv文件名，文件保存在前程序同一目录下：') + '.csv'
        if csv_file.endswith('csv') == False:
            print('???开玩笑么，导出格式不是csv')
        else:
            data.to_csv(csv_file)

    except:
        print('json文件必须是标准json，请检查是否为[{"name":"xx"},{"age":"20"}]格式')
    
    print('导出成功')


if __name__ == '__main__':
    json2csv()
