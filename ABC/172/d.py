import math
n = int(input())
ans = 0

#----エラトステネスの篩--------
def get_primenumber(number):
    prime_list = []
    #2からnumberまでの数字をsearch_listに入れる
    search_list = list(range(2,number+1))
    while True:
      #search_listの先頭の値が√nの値を超えたら処理終了
      if search_list[0] > math.sqrt(number):
        #prime_listにsearch_listを結合
        prime_list.extend(search_list)
        break
      else:
        #search_listの先頭をprime_listに入れる
        head_num = search_list[0]
        prime_list.append(head_num)
        #search_listの先頭をpopする
        search_list.pop(0)
        #head_numの倍数を取り除く
        search_list = [num for num in search_list if num % head_num != 0]
    return prime_list

for i in range(1, n+1):
    ans += i * search_divisor_num_1(i)
print(ans)
