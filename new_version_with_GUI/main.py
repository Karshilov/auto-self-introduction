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
h_head = ["丰富的爱好能丰富我们的人生，我的爱好并不算少，比如我很喜欢"
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
h_con = ["，再如，我从小学起就很喜欢",
        "并坚持到现在",
        "，我还坚持",
        "，虽然我在这方面可能天赋不算突出",
        "，除了这些，我还喜欢",
        "，事实上，我一度希望能够以它为职业",
        ",而",
        "也曾在困境中给予我激励"]
m_con = [0]
p_tail = [", 这些都是我人生路上的宝贵财富", ", 如果有幸进入贵校，我也会继续我的竞赛之旅", ", 也许成果不算辉煌，但也是我努力的见证"]
h_tail = ["它们伴随我的成长，与我同行", "它们已经融入了我的生活", "没有爱好的人生是无趣的，我只担心我的过分有趣"]
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
            self.textBrowser.setPlainText("至少给我来一个奖让我发挥一下吧……")
            return 
        n = (int) (self.pn)
        if n < 1 or n > 5 :
            self.textBrowser.setPlainText("奖项数超出上限或低于下限")
            return 
        if self.prize_number_2.text() != "" :
            pz.append(self.prize_number_2.text())
        if self.prize_number_3.text() != "" :
            pz.append(self.prize_number_3.text())
        if self.prize_number_4.text() != "" :
            pz.append(self.prize_number_4.text())
        if self.prize_number_5.text() != "" :
            pz.append(self.prize_number_5.text())
        if self.prize_number_6.text() != "" :
            pz.append(self.prize_number_6.text())
        if n != len(pz) - 1 :
            self.textBrowser.setPlainText("奖项数与实际输入不符")
            return 
        self.hn = self.hobby_number.text()
        if(self.hn == "" or self.hn == "0") :
            self.textBrowser.setPlainText("编个爱好也要给我一点出场机会吧……")
            return 
        m = (int) (self.hn)
        if m < 1 or m > 5 :
            self.textBrowser.setPlainText("爱好数超出上限或低于下限")
            return 
        if self.hobby_number_1.text() != "" :
            hb.append(self.hobby_number_1.text())
        if self.hobby_number_2.text() != "" :
            hb.append(self.hobby_number_2.text())
        if self.hobby_number_3.text() != "" :
            hb.append(self.hobby_number_3.text())
        if self.hobby_number_4.text() != "" :
            hb.append(self.hobby_number_4.text())
        if self.hobby_number_5.text() != "" :
            hb.append(self.hobby_number_5.text())
        if m != len(hb) - 1 :
            self.textBrowser.setPlainText("爱好数与实际输入不符")
            return 
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
        self.sout = self.sout + p_tail[pos] + '\n'
        pos = random.randint(0, 5)
        self.sout = self.sout + '   ' + h_head[pos] + hb[1]
        od = [0, 1, 2, 3]
        random.shuffle(od)
        if od[0] == 2 : 
            od[0], od[1] = od[1], od[0]
        i = 2
        while(i < m) : 
            self.sout = self.sout + h_con[2 * od[i - 2]]
            self.sout = self.sout + hb[i]
            self.sout = self.sout + h_con[2 * od[i - 2] + 1]
            i = i + 1
        pos = random.randint(0, 2)
        self.sout = self.sout + ',' + h_tail[pos] + '\n';
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
        self.sout = "   "


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Auto_intro()
    MainWindow.show()
    sys.exit(app.exec_())