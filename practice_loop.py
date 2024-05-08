# 問題1:1から100までの数をプリントするプログラムを書きなさい。ただし、3で割り切れる数の場合は数の代わりに「Fizz」を、5で割り切れる数の場合は「Buzz」をプリントし、3でも5でも割り切れる数の場合は「FizzBuzz」をプリントするようにしてください。
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# 問題2: 1 から 10 までの数を印刷するPythonプログラムを書いてください。
for i in range(1,11):
    print(i)


# 問題3: リスト [1, 2, 3, 4, 5] の各要素を二乗した値を印刷するPythonプログラムを書いてください。
list1 = [1, 2, 3, 4, 5]

for i in list1:
    num = i**2
    print(num)


# 問題4: 5 から 15 までの数の合計を計算し印刷するPythonプログラムを書いてください。
sum = 0

for i in range(5,16):
    sum += i
print(sum)

# 問題5: 1 から 100 までの間で、3 の倍数のみを印刷するPythonプログラムを書いてください。
for i in range(1, 101):
    if i % 3 == 0:
        print(i)


# 問題6: 1 から 100 までの数のうち、3 で割り切れるものの合計と、5 で割り切れるものの合計をそれぞれ印刷するPythonプログラムを書いてください。
sum_3 = 0
sum_5 = 0

for i in range(1, 101):
    if i % 3 == 0:
        sum_3 += i
    if i % 5 == 0:
        sum_5 += i
        
print(sum_3)
print(sum_5)


# 問題7: 1 から n までの数のうち、n の値をユーザーから入力させ、その平方根を整数部分のみ印刷するPythonプログラムを書いてください。
import math

num_str = input('整数を入力してください。:')
num = int(num_str)

square_root = math.isqrt(num)
print(square_root)


# 問題8: 文字列 "Python" の各文字を、1文字ずつ縦に印刷するPythonプログラムを書いてください。
text = 'Python'

for i in text:
    print(i)


# 問題9: 任意のリストが与えられた時、そのリストの要素を逆順に印刷するPythonプログラムを書いてください。
list = [1,2,3,4,5]
for i in reversed(list):
    print(i)


# 問題10: ユーザーから入力された2つの数 a と b の間の全ての素数を見つけて印刷するPythonプログラムを書いてください。
import math

prime_list= list()

def check_prime(a, b):
    for i in range(a, b):
        prime = True
        if i == 1:
            prime = False
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
        if prime is True:
            prime_list.append(i)

    return prime_list

a = int(input('a.整数を入力してください。:'))
b = int(input('b. aより大きい整数を入力してください。:'))

print(check_prime(a, b))

# 問題11: 次のコードの出力は何ですか？実行せずに答えてください。また理由も答えてください。
for i in range(3):
    print(i)
# A. 0 1 2 3
# B. 0 1 2
# C. 1 2 3
# D. エラーが発生する

# <解答>
# B. 0 1 2
# <理由>
# range(3)とすると0から2までの値を生成する。
# それをfor文で１つずつ取り出し、変数iに格納されprint文で上記の値が出力される。

# 問題12: 次のコードが無限ループにならないためには、XXXXにどれを入れるべきですか？実行せずに答えてください。また理由も答えてください。
i = 0
while i < 5:
    print("Python")
    # i = XXXX　　→　※エラー表記になるのでコメントアウトしています。
# A. i + 1
# B. 5
# C. 0
# D. i - 1

# <解答>
# A. i + 1
# <理由>
# while文の条件がi < 5となっているため、変数iに1ずつ加算していかないと、
# 無限にその条件に当てはまってしまう。i +　1を入れることで5回目にループを終了することができる。


# 問題13: 次のコードの出力は何ですか？実行せずに答えてください。また理由も答えてください。
for i in range(2):
    for j in range(2):
        print(i, j)
# A. 0 0 0 1 1 0 1 1
# B. 0 0
# 0 1
# 1 0
# 1 1
# C. 0 1 2 3
# D. 0 1 0 1

# <解答>
# B. 0 0
# 0 1
# 1 0
# 1 1 
# <理由>
# 変数i,jともにrange関数によって0と1が出力される。
# 実行順序としては、まずiの方のfor文で0が生成され、次にjの方のfor文で0が生成され、print文で0,0が出力される。
# ネストがあるfor文では内側のfor文の要素がなくなるまでループを繰り返すため、
# jに1が格納され、print文で0,1が出力される。
# 内側のfor文の要素がなくなったので、次に外側のfor文に戻り、次の値1が生成される。
# あとは先ほどと同じように、内側のfor文で0がされ、print文で1,0が出力、
# 最後にもう一度内側のfor文で1が生成され、print文で1,1が出力される。


# 問題14: 次のコードの挙動として正しいものはどれですか？実行せずに答えてください。また理由も答えてください。
for i in range(3):
    print(i)
else:
    print("Done")
# A. エラーが発生する
# B. 0 1 2と出力され、"Done"は出力されない
# C. 0 1 2と出力された後に"Done"が出力される
# D. "Done"のみが出力される

# <解答>
# C. 0 1 2と出力された後に"Done"が出力される
# <理由>
# else文を記載すると、for文が正しく終了した後の処理が実行される。
# 問題14の場合、0,1,2と問題なく出力され、for文の処理が終了したため、
# else文に移り、その配下の処理が実行された結果、Doneが出力される。


# 問題15: 繰り返し構文の種類と違いを説明してください。自己理解必須

# 繰り返し構文には下記の種類がある。
# ①for
# ②while

# ①for文はリストの内容を順番に処理する。
# 与えられたリストなどから順番に要素を取り出し、決められた処理を実行することができる。
# ②while文は条件式がTrueの場合のみ、その配下の処理を実行することができる。
# 条件がFalseにならないと無限ループのなるため、終了条件を正しく記載する必要がある。