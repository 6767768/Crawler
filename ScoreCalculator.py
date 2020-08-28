class CalculatorScore():

    def __init__(self, Score, Credit, OptionalCourse, OptionalCredit):
        self.score=Score
        self.credit=Credit
        self.optionalcourse=OptionalCourse
        self.optionalcredit=OptionalCredit

    def SumSubject(self):
        return '已修总课程数：'+ str(len(self.credit))

    def SumCredit(self):
        sum=0
        for i in self.credit:
            sum+=i
        return sum

    def MajorCredit(self):
        sum=self.SumCredit()
        for i in self.optionalcredit:
            sum=sum-i
        return sum

    def TotalCredit(self):
        return '已修总学分数：'+ str(self.SumCredit()) + '\n已修主修课学分数：' + str(self.MajorCredit())

    def AverageScore(self):
        sum=0
        for i in range(len(self.credit)):
            sum=sum+(self.credit[i])*(self.score[i])
        sumcredit=self.SumCredit()
        return '均分（含选修课）：'+ str(sum/sumcredit)

    def AverageScoreMajor(self):
        sum=0
        for i in range(len(self.credit)):
            sum = sum + (self.credit[i]) * (self.score[i])
        for i in range(len(self.optionalcourse)):
            sum=sum-(self.optionalcredit[i])*(self.optionalcourse[i])
        sumcredit=self.MajorCredit()
        return '主修课均分：'+ str(sum/sumcredit)

    def StdGpa(self):
        sum=0
        for i in range(len(self.score)):
            if self.score[i]>=90 and self.score[i]<=100:
                sum=sum+4.0*self.credit[i]
            elif self.score[i]>=80 and self.score[i]<=89:
                sum=sum+3.0*self.credit[i]
            elif self.score[i] >= 70 and self.score[i] <= 79:
                sum = sum + 2.0 * self.credit[i]
            elif self.score[i] >= 60 and self.score[i] <= 69:
                sum = sum + 1.0 * self.credit[i]
            elif self.score[i]>=0 and self.score[i]<=59:
                sum = sum + 0 * self.credit[i]
        sumcredit=self.SumCredit()
        return '标准4.0GPA：'+ str(sum/sumcredit)

    def PekGpa(self):
        sum=0
        for i in range(len(self.score)):
            if self.score[i]>=90 and self.score[i]<=100:
                sum=sum+4.0*self.credit[i]
            elif self.score[i]>=85 and self.score[i]<=89:
                sum=sum+3.7*self.credit[i]
            elif self.score[i] >= 82 and self.score[i] <= 84:
                sum = sum + 3.3 * self.credit[i]
            elif self.score[i] >= 78 and self.score[i] <= 81:
                sum = sum + 3.0 * self.credit[i]
            elif self.score[i]>=75 and self.score[i]<=77:
                sum = sum + 2.7 * self.credit[i]
            elif self.score[i] >= 72 and self.score[i] <= 74:
                sum = sum + 2.3 * self.credit[i]
            elif self.score[i]>=68 and self.score[i]<=71:
                sum = sum + 2.0 * self.credit[i]
            elif self.score[i] >= 64 and self.score[i] <= 67:
                sum = sum + 1.5 * self.credit[i]
            elif self.score[i]>=60 and self.score[i]<=63:
                sum = sum + 1.0 * self.credit[i]
            elif self.score[i] >= 0 and self.score[i] <= 59:
                sum = sum + 0 * self.credit[i]
        sumcredit=self.SumCredit()
        return '北大4.0GPA：'+ str(sum/sumcredit)

    def ZtcGpa(self):
        sum=0
        for i in range(len(self.score)):
            if self.score[i]>=95 and self.score[i]<=100:
                sum=sum+4.3*self.credit[i]
            elif self.score[i]>=90 and self.score[i]<=94:
                sum=sum+4.0*self.credit[i]
            elif self.score[i] >= 85 and self.score[i] <= 89:
                sum = sum + 3.7 * self.credit[i]
            elif self.score[i] >= 82 and self.score[i] <= 84:
                sum = sum + 3.3 * self.credit[i]
            elif self.score[i]>=78 and self.score[i]<=81:
                sum = sum + 3.0 * self.credit[i]
            elif self.score[i] >= 75 and self.score[i] <= 77:
                sum = sum + 2.7 * self.credit[i]
            elif self.score[i]>=72 and self.score[i]<=74:
                sum = sum + 2.3 * self.credit[i]
            elif self.score[i] >= 68 and self.score[i] <= 71:
                sum = sum + 2.0 * self.credit[i]
            elif self.score[i]>=65 and self.score[i]<=67:
                sum = sum + 1.7 * self.credit[i]
            elif self.score[i] >= 64 and self.score[i] <= 64:
                sum = sum + 1.5 * self.credit[i]
            elif self.score[i] >= 61 and self.score[i] <= 63:
                sum = sum + 1.3 * self.credit[i]
            elif self.score[i] >= 60 and self.score[i] <= 60:
                sum = sum + 1.0 * self.credit[i]
            elif self.score[i] >= 0 and self.score[i] <= 59:
                sum = sum + 0 * self.credit[i]
        sumcredit=self.SumCredit()
        return '4.3分GPA：'+ str(sum/sumcredit)

    def WesGpa(self):
        sum=0
        for i in range(len(self.score)):
            if self.score[i]>=85 and self.score[i]<=100:
                sum=sum+4.0 * self.credit[i]
            elif self.score[i]>=75 and self.score[i]<=84:
                sum=sum+3.0 * self.credit[i]
            elif self.score[i] >= 60 and self.score[i] <= 74:
                sum = sum + 2.0 * self.credit[i]
            elif self.score[i] >= 0 and self.score[i] <= 59:
                sum = sum + 0 * self.credit[i]
        sumcredit=self.SumCredit()
        return 'WES计算(暂定)：'+ str(sum/sumcredit)

    def All(self):
        print(self.SumSubject())
        print(self.TotalCredit())
        print(self.AverageScore())
        print(self.AverageScoreMajor())
        print(self.StdGpa())
        print(self.PekGpa())
        print(self.ZtcGpa())
        print(self.WesGpa())

Score=[91,97,92,79,87,82,88,91,80,92,95,88,88,88,94,94,84,87,93,93,95,93,79,99,91,92,90,88,90,89,100,91,88,96,94,98,99,90,90,94,82,88,90,85,91,96,97,89,99,93,100]
Credit=[6.5,3.5,3,2,4,1,0.5,6.5,3,1,1,2,2,1,4,1,0.5,2,4,4,3,6,1,4,0.5,2,3,4,6,3,3,2,0.5,4,4,1,3,3.5,4,3,2,2,2,2,2,3,2,2,2,2,2]
OptionalCourse=[97,89,99,93,100]
OptionalCredit=[2,2,2,2,2]

score2020=CalculatorScore(Score, Credit, OptionalCourse, OptionalCredit)
score2020.All()
