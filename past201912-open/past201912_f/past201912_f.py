import re

# s = re.findall(r'[A-Z][a-z]*[A-Z]',input())。findallで戻り値がマッチするごとにリストを返す。
s = re.findall(r'[A-Z][a-z]*[A-Z]',input())
#無名関数のlowerで区別なくソート。
s.sort(key=lambda s: s.lower())

#joinでリストを一つの文字列。""でから文字でつなげる。
print("".join(s))