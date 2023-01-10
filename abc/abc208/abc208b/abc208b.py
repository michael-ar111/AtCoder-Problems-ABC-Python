from math import factorial
P = int(input())
answer = 0
#1〜10回ループ。1!〜10!の回数分。
for i in range(1, 11):
  #最初に1!の枚数を確定する。
  #Pを2で割って、その余が1!を使う枚数。初回でi+1して判定。1回目を飛ばす。
  divisor = factorial(i + 1)
  #2回目は1回目から引いた分で割る。余りを階乗で割ることでその階乗値が何枚使われているかがわかる。
  residue = P % divisor

  #1回目のループは1か0をanswerに返す。residueが割り切れているか、1のため。
  #answerに使う枚数を追加。
  #2回目はP%divisorの余りを階乗で割る。余りを階乗で割ることでその階乗が何枚使われているかがわかる。
  answer += residue // factorial(i)
  
  #1回目のループは1か0が引かれる。
  
  P -= residue
print(answer)