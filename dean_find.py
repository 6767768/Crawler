import re

class Process():
    def __init__(self,address):
        self.address=address

    def ProNumber(self):
        with open(self.address,'r',encoding='utf-8') as fp:
            info=fp.read()
            fp.close()
        matchObj=re.findall(r'总记录数(.*)跳转至',info)[1][1:3]
        times=int(matchObj)
        return int(times/10)

    def ProInfo(self):
        with open(self.address,'r', encoding='utf-8') as fp:
            info = fp.read()
            fp.close()
        matchObj = re.findall(r'<a href=.*?详情</a>', info)

        MergeObj=list(set(matchObj))

        Dict={}
        flag=0
        for i in range(len(MergeObj)):

            course=re.findall('data-kcm=".*?"',MergeObj[i])[0][10:-1]
            credit=re.findall('data-xf=".*?"',MergeObj[i])[0][9:-1]
            #处理html脚本错误
            if credit=='.5':
                credit=0.5
            else:
                credit=float(credit)
            score=int(re.findall('data-zcj=".*?"',MergeObj[i])[0][10:-1])

            #区分选修课和必修课
            kind=re.findall('data-kch=".*?"',MergeObj[i])[0][10:-1]

            OptionMatch=re.findall('GNED',kind)
            MainMatch=re.findall('CORE',kind)

        #将选修课在字典中置顶
            if set(MainMatch).union(set(OptionMatch)):
                flag=flag+1
                Dict.setdefault('course',[]).insert(0,course)
                Dict.setdefault('score',[]).insert(0,score)
                Dict.setdefault('credit',[]).insert(0,credit)
            else:
                Dict.setdefault('course',[]).append(course)
                Dict.setdefault('score',[]).append(score)
                Dict.setdefault('credit',[]).append(credit)
        return flag,Dict




