#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/2 17:16
#@Author :zbwu103
#@File  ：从题库中随机生成试卷.py
#@功能：功能：生成一张试卷和对应的一份答案，每一道题目对应有四个答案，题目和答案都是capitals中随机的选出来，
# 题目是中国的省份，正确答案是省会城市

import random

capitals = {'北京市': '北京',
            '上海市': '上海',
            '天津市': '天津',
            '重庆市': '重庆',
            '黑龙江省': '哈尔滨',
            '吉林省': '长春',
            '辽宁省': '沈阳',
            '内蒙古自治区': '呼和浩特',
            '河北省': '石家庄',
            '新疆维吾尔自治区': '乌鲁木齐',
            '甘肃省': '兰州',
            '青海省': '西宁',
            '陕西省': '西安',
            '宁夏回族自治区': '银川',
            '河南省': '郑州',
            '山东省': '济南',
            '山西省': '太原',
            '安徽省': '合肥',
            '湖北省': '武汉',
            '湖南省': '长沙',
            '江苏省': '南京',
            '四川省': '成都',
            '贵州省': '贵阳',
            '云南省': '昆明',
            '广西省': '南宁',
            '西藏自治区': '拉萨',
            '浙江省': '杭州',
            '江西省': '南昌',
            '广东省': '广州',
            '福建省': '福州',
            '台湾省': '台北',
            '海南省': '海口',
            '香港': '香港',
            '深圳': '深圳',
            '雄安': '雄安'}

for quizNum in range(20):
    quizFile = open('试卷%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('答案%s.txt' % (quizNum + 1), 'w')

    quizFile.write('姓名:\n\n学校:\n\n班级:\n\n')
    quizFile.write((' ' * 20) + '请在省份后面填写正确的省会城市 (试卷 %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(35):

        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # 从wrongAnswers列表中提取3个元素组成一个新的列表返回，不改变原来的列表
        wrongAnswers = random.sample(wrongAnswers, 3)
        # 4个选项等于3个错误的加上一个正确的选项，并且位置随机
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('%s. %s的省会城市是哪个? ( )\n' % (questionNum + 1, states[questionNum]))

        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

















