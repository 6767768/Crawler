from dean_find import Process
from ScoreCalculator import CalculatorScore
from dean import Crawler
from selenium.webdriver.chrome.options import Options
from pandas import DataFrame
import pandas as pd
import datetime

start=datetime.datetime.now()

def run_function():

    hdle0=Crawler(address,username,keys,url,path,chrome_options,dir)
    hdle0.Mkdir()
    hdle0.spider()

    hdle1 = Process(address)
    optionalscore = hdle1.ProInfo()[1]['score'][0:hdle1.ProInfo()[0]]
    optionalcredit = hdle1.ProInfo()[1]['credit'][0:hdle1.ProInfo()[0]]
    score = hdle1.ProInfo()[1]['score']
    credit = hdle1.ProInfo()[1]['credit']
    test = CalculatorScore(score, credit, optionalscore, optionalcredit)
    return test,hdle1.ProInfo()[1]

def main():
    test=run_function()

    Sumsubject=test[0].SumSubject()
    Totalcredit=test[0].TotalCredit()
    Averagescore=test[0].AverageScore()
    Averagescoremajor=test[0].AverageScoreMajor()
    Pekgpa=test[0].PekGpa()
    Ztcgpa=test[0].ZtcGpa()
    Wesgpa=test[0].WesGpa()

    Cumu=[Sumsubject,
    Totalcredit,
    Averagescore,
    Averagescoremajor,
    Pekgpa,
    Ztcgpa,
    Wesgpa]

    with pd.ExcelWriter(dir+'/'+username+'.xlsx') as writer:
        DataFrame(test[1]).to_excel(writer,sheet_name='成绩汇总')
        DataFrame(Cumu).to_excel(writer,sheet_name='分类统计',index=False)
        writer.save()

#输入用户名
username=input('Netid: ')
keys=input('Your password: ')

#phantom 驱动路径
path=r'F:\chromeheadless\chromedriver.exe'

#创建参数对象，控制Chrome以无界面打开
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#引入url
url='http://ehall.xjtu.edu.cn/jwapp/sys/cjcx/*default/index.do?amp_sec_version_=1&gid_=djdxTUwyeTl2NmF6RTgwOXlzc3liT016Y3FHci9PS2hoNkoxZW9xeUZKTi9ET0hsY3RQRmJNbXNZN0puR09iUlN4aFNrUlRHdUgxYUx2dmpmSnpTdVE9PQ&EMAP_LANG=zh&THEME=millennium#/cjcx'

address='dean/text.txt'
#文件夹
dir='D:\桌面\威尼斯商人'

end = datetime.datetime.now()

print(end - start)

if __name__=='__main__':
    main()


