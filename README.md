# generate_quizs
To generate quizs for pupil automatically and output them to a word document.(小学口算题生成器，输出到word文档中，并包含答案)

小朋友暑假作业是每天一页口算题，正好用这个需求练习一下python技能，
用到的库不多，引用库用到了 py-docx, 用于读写word文档，内建库用到了random。

用法：
Python auto-generate-quiz.py

可生成3000道随机的两位数加减法题目，结果限制在100以内
