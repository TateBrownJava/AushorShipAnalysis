# 目标作者ID
target_author = [3032,
3475,
3476,
3485,
3488,
3498,
3503,
3506,
3518,
3524,
3530,
3543,
3581,
3602,
3695]
# target_author = target_author[:50]
# 原训练/测试 文件所在目录
TRAIN_DATA_DIR = r"E:\项目与代码\AuthorShipAnalysis\数据\TrainData"
TEST_DATA_DIR = r"E:\项目与代码\AuthorShipAnalysis\数据\TestData"

# 训练/测试 分词文件
TRAIN_SEG_DIR = r"data\seg_train"
TEST_SEG_DIR = r"data\seg_test"

# 功能词文件路径
FUNCTION_WORD_PATH = r"data\function_word_300.txt"

"""
    提取特征
"""

TITLE = [
    "作者ID",
    "段落数平均值", "段落平均长度", "句子平均长度",  # 3
    "问号占比", "句号占比", "逗号占比", "感叹号占比", "引号占比", "冒号占比", "省略号占比", "分号占比", "单括引号占比",  # 9
    "1字词占比", "2字词占比", "3字词占比", "4字词占比", "5字词占比", "6字词占比", "7字词占比", "8字词占比",  # 8
    "名词占比", "副词占比", "形容词占比", "介词占比", "连词占比", "助词占比", "叹词占比", "动词占比", "拟声词占比"  # 9
]

# 问号数,句号数,逗号数,感叹号数地,引号数,冒号数,省略号数（三个点）,分号数，单括引号（「和」）
PUNCT_CHAR_LIST = [
    ['?', '？'],
    ['.', '。'],
    [',', '，'],
    ['!', '！'],
    ['"', '“', '”'],
    [':', '：'],
    ['…'],
    [';', '；'],
    ['「', '」']
]