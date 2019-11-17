import sys
import random
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import PyQt5.sip
from button import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

p_head = ["在学习之余，我对竞赛也有所涉猎，我曾获得"
                    , "除了文化课，我还有丰富多彩的竞赛生活，比如"
                    , "为了拓宽我的视野，我也参与了各种竞赛，也收获了一些奖项如"
                    , "在保证文化课成绩的同时，竞赛也是我学习生活中不可或缺的一部分，比如我曾获"
                    , "我的自信不止来源于文化课，也同样来源于我的竞赛经历，我获得过"
                    , "为了能够不落后于时代的脚步，我也兼修了竞赛，如我曾获得"]
h_head = ["丰富的爱好能丰富我们的人生，我的爱好并不算少，我喜欢"
                    , "在学习各种课程的同时，我也有许多爱好来放松心灵，比如"
                    , "我的课余时间也并不是都分给了竞赛，也有分给我的爱好，比如，我喜欢"
                    , "我的兴趣爱好广泛，并不只限于学习，我爱"
                    , "爱好是人生不可或缺的部分，它为人生增光添彩，我就很喜欢"
                    , "生活中的我是个爱好广泛的人，比如"]
m_head = ["我的专业选择是"
                    , "考虑到未来的发展，我理想的专业是"
                    , "我最喜欢的专业是"
                    , "我很希望就读于贵校的"
                    , "专业的选择对人生的影响巨大，而我选择"
                    , "经过了我的深思熟虑，我决贵定报考贵校的"]
p_con = ["，除此之外，我还获得过"
                    , "，以及"
                    , "，我也曾获得"
                    , "还有"
                    , "和"
                    , "；也拿过"]
h_con = [0]
m_con = [0]
p_tail = [", 这些都是我人生路上的宝贵财富", ", 如果有幸进入贵校，我也会继续我的竞赛之旅", ", 也许成果不算辉煌，但也是我努力的见证"]
h_tail = [0]
m_tail = [0]
p_saying = [", 习大大说过：“希望同学们珍惜美好时光，砥砺品德，陶冶情操，刻苦学习，全面发展，掌握真才实学，努力成为建设伟大祖国、建设美丽家乡的有用之才、栋梁之才，为促进民族团结进步、实现共同繁荣发展作出应有贡献。”，因此我参加并获得了"
            ,", 爱因斯坦说过：“想象力比知识更重要，因为知识是有限的。”，我对此深表赞同，为了提升我的想象力与创造力，我参加并获得了"
            ,", “人的知识愈广,人的本身也愈臻完善。”， 这是高尔基对我们的建议，知识的提升并不能只靠课上的内容，于是我参加并获得了"]
h_saying = [0]
m_saying = [0]

class Auto_intro(QMainWindow, Ui_MainWindow) :
    sout = "  "
    sin = ""
    pn = "prize_number"
    hn = "hobby_number"
    def __init__(self, parent = None):
        super(Auto_intro, self).__init__()
        self.setupUi(self)
        self.action()
    
    def action(self) :
        self.toStart.clicked.connect(self.StartWriting)
        self.ClearAll.clicked.connect(self.ClearText)
    
    def StartWriting(self) :
        self.pn = self.prize_number.text()
        pz = [""]
        hb = [""]
        if(self.pn == "" or self.pn == "0") :
            self.textBrowser.setPlainText("至少给我来一个奖让我发挥一下吧……");
            return 
        n = (int) (self.pn)
        i = 0
        while i < n :
            if i == 0 :
                pz.append(self.prize_number_2.text())
            if i == 1 :
                pz.append(self.prize_number_3.text())
            if i == 2 :
                pz.append(self.prize_number_4.text())
            if i == 3 :
                pz.append(self.prize_number_5.text())
            if i == 4 :
                pz.append(self.prize_number_6.text())
            i = i + 1
        self.hn = self.hobby_number.text()
        if(self.hn == "" or self.hn == "0") :
            self.textBrowser.setPlainText("编个爱好也要给我一点出场机会吧……");
            return 
        m = (int) (self.hn)
        i = 0
        while i < m :
            if i == 0 :
                hb.append(self.hobby_number_1.text())
            if i == 1 :
                hb.append(self.hobby_number_2.text())
            if i == 2 :
                hb.append(self.hobby_number_3.text())
            if i == 3 :
                hb.append(self.hobby_number_4.text())
            if i == 4 :
                hb.append(self.hobby_number_5.text())
            i = i + 1
        pos = random.randint(0, 5)
        self.sout = self.sout + p_head[pos]
        n = len(pz)
        m = len(hb)
        i = 1
        p_s = False
        cur = pos
        while i < n :
            pos = random.randint(0, 5)
            if pos == cur :
                pos = random.randint(0, 5)
            cur = pos
            self.sout = self.sout + pz[i]
            tmp = random.randint(0, 2)
            if p_s == False and i != n - 1 :
                sh = random.randint(0, 2)
                if sh == 2 :
                    sh = random.randint(0, 2)
                    self.sout = self.sout + p_saying[sh]
                    p_s = True
                    i = i + 1
                    continue
            if i != n - 1 :
                if tmp == 2 :
                    self.sout = self.sout + ','
                else :
                    self.sout = self.sout + p_con[pos]
            i = i + 1
        pos = random.randint(0, 2)
        self.sout = self.sout + p_tail[pos]
        self.textBrowser.setPlainText(self.sout);

    def ClearText(self) :
        self.textBrowser.setPlainText("");
        self.prize_number.clear()
        self.prize_number_2.clear()
        self.prize_number_3.clear()
        self.prize_number_4.clear()
        self.prize_number_5.clear()
        self.prize_number_6.clear()
        self.hobby_number.clear()
        self.hobby_number_1.clear()
        self.hobby_number_2.clear()
        self.hobby_number_3.clear()
        self.hobby_number_4.clear()
        self.hobby_number_5.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Auto_intro()
    MainWindow.show()
    sys.exit(app.exec_())