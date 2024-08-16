n,m = map(int, input().split())

#cが2つのケース
s = m//2
#2つのケースとsのケースを比較して、sccの最低限のパターン1のカウント
ans = min(n,s)
#パターン1で使用したcの残りのカウント
m-=ans*2
#パターン2のcだけでsccができる数のカウント
ans += m//4

print(ans)