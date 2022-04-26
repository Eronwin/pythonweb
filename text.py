from examplesss import example

import difflib
origin="燕子|*|*"
parrern=[
    "五月临平山下路，藕花无数满汀洲.|*|*",
    "燕子不归春事晚，一汀烟雨杏花寒。|*|*",
    "sina|*|*",
    "*|weibo|*",
    "sina|pic|*",
    "*|*|sign",
    "*|weibo|sign",
    "*|pic|sign",
    "sina|pic|sign",
    "*|*|*"
]
# t=example.match(origin,parrern)
# print(t)

config_list = ['中国工商银行','中国农业银行','建设银行','中国人民银行','招商证券','中国农业发展银行']
query_word = 'sina|*'
li=['sina|1']

t=example.match(origin,parrern)
print(t)
# print(difflib.get_close_matches(origin,parrern,n=1))
print(difflib.get_close_matches(query_word,config_list,n=1,cutoff=0.5))