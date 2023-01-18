##二分探索
def binary_search(data, value):
  left = 0
  right = len(data) - 1
  while left <= right:
    mid = (left + right)//2
    print(data[mid])
    ## 累積和は昇順で増えていっている。それを前提に、二分探索。
    ## 二分探索は要素の真ん中で区切って、それより多いか少ないかの判定。まず該当の数字valueとあっているかdata[mid]で判定。
    ## その後[1,2,3,4,5,6,7] なら、4よりdata[mid]が大きいか小さいか判定している。ひたすらループして要素がなくなるまで実施し、なければfalseとなる。
    if data[mid] == value:
      return mid
    elif data[mid] < value:
      left = mid + 1
    else:
      right = mid - 1
  return False


N = int(input())
A = list(map(int, input().split()))

# 円環は2倍した探す
cake = A + A
 
# 全体が10で割り切れなければ終わり
if sum(A)%10 != 0:
  exit(print("No"))
 
# 探索用に累積和を求める
##Nが3なら[0,0,0,0,0,0,0]と7つの入った1つの配列ができる。
##累積和が0,1,19,20,21,39,40となる。
cumlative_sum = [0]*(2*N+1)
for i, piece in enumerate(cake):
  cumlative_sum[i+1] = cumlative_sum[i] + piece
 
# 左端固定で二分探索
## target_sizeが1/10になる数。
target_size = sum(A)//10
for l in range(N):
  target = target_size + cumlative_sum[l]
  ## (1,18,1)が元の値。円環を2倍にしたら(1,18,1,1,18,1)。円環2倍の累積和は[0,1,19,20,21,39,40]
  ## targetがよくわからない。targeは2,3,21,22,23,41,42が入る。0から始まる累積和[0,1,19,20,21,39,40]+target_sizeの2となる。
  ## targetは円環の2倍の10分の1と各累積和を足したものになる。
  ## 累積和の特性で累積していっているので、隣の数分増えていることになっている。円環を2倍して、それが隣り合う数字の全パターンとなる。
  ## つまり、累積和にtarget_size分増えていれば、今回の条件の10分の1分だけ増えていることがわかる。

  ## 累積和として円環2倍した0からはじまる数、累積和+target_size
  ## targetが累積和にあるか確認している。
  if binary_search(cumlative_sum, target):
    exit(print("Yes"))
print("No")