import random
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

fin = open("data.txt", "r")
fout = open("essay.txt", "w")
s = fin.read().split()
n = ((int) (s[0]))
m = ((int) (s[n + 1]))
sout = "    "
i = 1
pz = [0]
hb = [0]
mj = s[-1]
while i <= n :
    pz.append(s[i])
    i = i + 1
i = 1
while i <= m : 
    hb.append(s[i + n + 1])
    i = i + 1
n = len(pz)
m = len(hb)
pos = random.randint(0, 5)
sout = sout + p_head[pos]
i = 1
p_s = False
cur = pos
while i < n :
    pos = random.randint(0, 5)
    if pos == cur :
        pos = random.randint(0, 5)
    cur = pos
    sout = sout + pz[i]
    tmp = random.randint(0, 2)
    if p_s == False :
        sh = random.randint(0, 2)
        if sh == 2 :
            sh = random.randint(0, 2)
            sout = sout + p_saying[sh]
            p_s = True
            continue
    if i != n - 1 :
        if tmp == 2 :
            sout = sout + ','
        else :
            sout = sout + p_con[pos]
    i = i + 1
pos = random.randint(0, 2)
sout = sout + p_tail[pos]
fout.write(sout)
fin.close()
fout.close()