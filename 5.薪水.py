class Salary:
    def __init__(self):
        self.wt()
        while True:
            if nwt<=0 or nwt>48:
                print("无效的工作时长")
                self.wt()
            elif sph<=0:
                print("薪水不得小于0")
                self.wt()
            elif awt<=0 or awt>20:
                print("无效的加班时长")
                self.wt()
            else:
                break
        self.alls()
    def wt(self):
        global sph,nwt,awt
        sph=int(input("每小时的薪水"))
        nwt=int(input("正常时长"))
        awt=int(input("加班时长"))
        global nws,aws,t
        nws=nwt*sph*1.5
        aws=awt*sph
        t=nwt+awt
    def alls(self):
        alls=nws+aws
        if t>=0 and t<=48:
            ts=alls
        elif t>=48 and t<=60:
            ts=alls*1.2
        elif t>=60 and t<=80:
            ts=alls*2
        elif t>=80 and t<=7*24:
            ts=alls*3
        print("本周工资:{}元".format(ts))
salary=Salary()