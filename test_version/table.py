import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

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

class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        self.setGeometry(500, 200, 800, 600)
        self.setWindowTitle('StackedWidget 例子')
        
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0,'竞赛奖项')
        self.leftlist.insertItem(1,'个人爱好')
        self.leftlist.insertItem(2,'荣誉评优')
        self.leftlist.insertItem(3,'项目经历')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.ToStart_p = QPushButton(self.stack1)
        self.ToStart_p.setText("开始生成")
        self.prize_1 = QLineEdit(self.stack1)
        self.prize_2 = QLineEdit(self.stack1)
        self.prize_3 = QLineEdit(self.stack1)
        self.prize_4 = QLineEdit(self.stack1)
        self.prize_5 = QLineEdit(self.stack1)
        self.Text_p = QTextBrowser(self.stack1)

        self.layout_p = QFormLayout()
        
        self.layout_p.addRow(QLabel("奖项1"), self.prize_1);
        self.layout_p.addRow(QLabel("奖项2"), self.prize_2);
        self.layout_p.addRow(QLabel("奖项3"), self.prize_3);
        self.layout_p.addRow(QLabel("奖项4"), self.prize_4);
        self.layout_p.addRow(QLabel("奖项5"), self.prize_5);
        self.layout_p.addRow(self.ToStart_p)
        self.layout_p.addWidget(self.Text_p);

        self.stack1.setLayout(self.layout_p)

        self.ToStart_p.clicked.connect(self.StartWriting_p)

        self.stack2UI()
        self.stack3UI()
        self.stack4UI()

        self.stack = QStackedWidget(self)

        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)

        HBox = QHBoxLayout()
        HBox.addWidget(self.leftlist)
        HBox.addWidget(self.stack)

        self.setLayout(HBox)

        self.leftlist.currentRowChanged.connect(self.display)


    def stack2UI(self):
        layout  =  QFormLayout()
        layout.addRow(QLabel("爱好1"), QLineEdit());
        layout.addRow(QLabel("爱好2"), QLineEdit());
        layout.addRow(QLabel("爱好3"), QLineEdit());
        layout.addRow(QLabel("爱好4"), QLineEdit());
        layout.addRow(QLabel("爱好5"), QLineEdit());
        layout.addWidget(QPushButton('开始生成'));
        layout.addWidget(QTextBrowser());

        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout  =  QFormLayout()
        layout.addRow(QLabel("荣誉1"), QLineEdit());
        layout.addRow(QLabel("荣誉2"), QLineEdit());
        layout.addRow(QLabel("荣誉3"), QLineEdit());
        layout.addRow(QLabel("荣誉4"), QLineEdit());
        layout.addRow(QLabel("荣誉5"), QLineEdit());
        layout.addWidget(QPushButton('开始生成'));
        layout.addWidget(QTextBrowser());

        self.stack3.setLayout(layout)
    
    def stack4UI(self) :
        layout = QFormLayout()
        layout.addRow(QLabel("项目1"), QLineEdit());
        layout.addRow(QLabel("项目2"), QLineEdit());
        layout.addRow(QLabel("项目3"), QLineEdit());
        layout.addRow(QLabel("项目4"), QLineEdit());
        layout.addRow(QLabel("项目5"), QLineEdit());
        layout.addWidget(QPushButton('开始生成'));
        layout.addWidget(QTextBrowser());
        self.stack4.setLayout(layout)

    def StartWriting_p(self) :
        pz = []
        if(self.prize_1.text() != "") :
            pz.append(self.prize_1.text())
        if(self.prize_2.text() != "") :
            pz.append(self.prize_2.text())
        if(self.prize_3.text() != "") :
            pz.append(self.prize_3.text())
        if(self.prize_4.text() != "") :
            pz.append(self.prize_4.text())
        if(self.prize_5.text() != "") :
            pz.append(self.prize_5.text())
        n = (int) (len(pz))
        if(n == 0) :
            self.Text_p.setPlainText("至少给我来一个奖让我发挥一下吧……")
            return 
        i = 0
        sout = "  "
        pos = random.randint(0, 5)
        cur = -1
        p_s = False
        sout = sout + p_head[pos]
        while i < n :
            pos = random.randint(0, 5)
            if pos == cur :
                pos = random.randint(0, 5)
            cur = pos
            sout = sout + pz[i]
            tmp = random.randint(0, 2)
            if p_s == False and i != n - 1 :
                sh = random.randint(0, 2)
                if sh == 2 :
                    sh = random.randint(0, 2)
                    sout = sout + p_saying[sh]
                    p_s = True
                    i = i + 1
                    continue
            if i != n - 1 :
                if tmp == 2 :
                    sout = sout + ','
                else :
                    sout = sout + p_con[pos]
            i = i + 1
        pos = random.randint(0, 2)
        sout = sout + p_tail[pos] + '\n'
        self.Text_p.setPlainText(sout)

    def display(self, i) :
        self.stack.setCurrentIndex(i)
if __name__  ==  '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())