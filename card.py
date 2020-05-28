import random

## 创建抽卡池游戏王系列
card_turple = ('黑暗大法师','青眼白龙','黑魔导','天空龙','巨神兵','太阳神')
## 创建背包
package = [ ]

## 主程序
while 1:
    ## 用户进行选择的窗口
    choose = int(input('''
    是兄弟就来氪金
    请输入数字进行选择
    1. 抽取卡片
    2. 查看背包
    3. 整理背包
    4. 退出
    '''))

    ## 用户输入时询问抽卡次数
    if choose == 1:
        num = int(input('请输入需要抽卡的次数'))
        ## 执行抽卡程序
        for i in range(0,num):
            ## 生成0-5的数并读取对应的卡片
            n = random.randint(0,5)
            print('您抽到了：{}'.format(card_turple[n]))
            ## 把卡片放入背包
            package.append(card_turple[n])

        ## 完成抽卡，提示卡已存入背包
        print('卡片已存入背包')
        print('________________')

    ## 用户输入2，触发查看背包功能
    if choose == 2:
        ## 分背包没卡和背包有卡两种情况
        if len(package) == 0:
            print('兄弟你一张都没有该充钱了')
            print('________________')
        else:
            for i in package:
                print(i)
            print('________________')

    ## 用户输入3，触发整理背包功能
    if choose == 3:
        ## 分有卡和没卡的情况
        if len(package) == 0:
            print('没卡啊asir，充点吧')
            print('________________')
        else:
            package.sort()
            for i in package:
                    print(i)
            print('________________')

    ## 用户输入4，触发退出游戏功能
    if choose == 4:
        break
