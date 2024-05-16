# 問題1: 整数二つを引数として受け取り、それらの和を返す関数 add を定義してください。
def add(a, b):
    return a + b

# test
x = add(10, 12)
print(x)


# 問題2: 任意の文字列を引数として受け取り、その文字列が空でなければ True、空であれば False を返す関数 is_not_empty を定義してください。
def is_not_empty(str):
    if str:
        return(True)
    else:
        return(False)
    
# test
x = input('文字を入力してください:')
print(is_not_empty(x))


# 問題3: 整数リストを引数として受け取り、リスト内の最大値を返す関数 find_max を定義してください。リストが空の場合は None を返してください。
def find_max(data):
    if data:
        return max(data)
    else:
        return None
    
# test
print(find_max([]))
print(find_max([1, 3, 6, 8, 2]))


# 問題4: 半径を引数として受け取り、その半径を持つ円の面積を返す関数 calculate_circle_area を定義してください。円周率は 3.14 を使用してください。
def calculate_circle_area(radius):
    return radius * radius * 3.14

# test
area = calculate_circle_area(2)
print(f'円の面積は{area}')


# 問題5: 文字列と整数を引数として受け取り、その文字列を整数回だけ繰り返した新しい文字列を返す関数 repeat_string を定義してください。
def repeat_string(str, int):
    return str * int

# test
loop_str = repeat_string('Hello', 3)
print(loop_str)


# 問題6: 整数リストを引数として受け取り、偶数のみを含む新しいリストを返す関数 filter_even_numbers を定義してください。
def filter_even_numbers(data):
    even_list = list()
    for i in data:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

# test
print(filter_even_numbers([1, 3, 6, 8, 2]))


# 問題7: 2つのリストを引数として受け取り、両方のリストに共通する要素のみを含む新しいリストを返す関数 find_common_elements を定義してください。
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# test
list1 = [1, 2, 3, 6, 8]
list2 = [1, 4, 5, 7, 8]
print(find_common_elements(list1, list2))


# 問題8: 整数 n を引数として受け取り、n の階乗を返す関数 factorial を定義してください。
def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    return 1

# test
print(factorial(5))


# 問題9: 一辺の長さを引数として受け取り、正方形の面積を返す関数 square_area を定義してください。
def square_area(length):
    return length * length

# test
print(square_area(5))


# 問題10: 2つの数を引数として受け取り、それらの積を返す関数 multiply を定義してください。
def multiply(num1, num2):
    return num1 * num2

# test
print(multiply(2, 3))


# 問題11: 任意の数の平均を計算して返す関数 calculate_average を定義してください。関数は任意の数の引数を取ることができるようにしてください。
def calculate_average(*args):
    return sum(args) / len(args)

# test
print(calculate_average(1, 2, 3, 4, 5))


# 問題12: 整数リストを引数として受け取り、そのリストの中の奇数だけを含む新しいリストを返す関数 filter_odd_numbers を定義してください。
def filter_odd_numbers(data):
    odd_list = list()
    for i in data:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

# test
print(filter_odd_numbers([1, 3, 6, 8, 2]))


# 問題13: 文字列と文字を引数として受け取り、その文字列の中にその文字がいくつ含まれているかを返す関数 count_char を定義してください。
def count_char(str, char):
    return str.count(char)

# test
print(count_char('Hello, World', 'o'))


# 問題14: 高さと底辺を引数として受け取り、三角形の面積を返す関数 triangle_area を定義してください。
def triangle_area(base, height):
    return base * height / 2

#test
print(triangle_area(4, 6))

# 問題15: 次の関数が正しく実行されるための引数の組み合わせとして正しいものはどれですか？実行せずに答えてください。
def add(a, b):
    return a + b
# A. add(1)
# B. add(1, 2)
# C. add(a = 1)
# D. add()

# <解答>
# B. add(1, 2)


# 問題16: 次の関数定義において、greet関数が"Hello, Python!"を出力するために正しい関数の呼び出し方はどれですか？実行せずに答えてください。
def greet(name = "Python"):
    return "Hello, " + name + "!"
# A. greet("Hello, Python!")
# B. greet(name = "Python")
# C. greet()
# D. greet("Python")

# <解答>
# B. greet(name = "Python")
# C. greet()
# D. greet("Python")


# 問題17: 次の関数定義において、"apple", "banana", "cherry"を引数として渡し、それらをリストで受け取るための正しい関数の呼び出し方はどれですか？実行せずに答えてください。
def fruits(*args):
    return list(args)
# A. fruits(["apple", "banana", "cherry"])
# B. fruits("apple", "banana", "cherry")
# C. fruits(args=["apple", "banana", "cherry"])
# D. fruits(*["apple", "banana", "cherry"])

# <解答>
# A. fruits(["apple", "banana", "cherry"])


# # 問題18: Pythonで関数を定義するキーワードはどれですか？実行せずに答えてください。
# A. function
# B. def
# C. func
# D. define

# <解答>
# B. def


# 問題19:Python関数のデフォルト引数に関する説明として正しいものはどれですか？実行せずに答えてください。
# A. デフォルト引数は、関数が呼び出されたときに必ず指定しなければならない。
# B. デフォルト引数は、関数定義で指定された値を持ち、呼び出し時に省略可能。
# C. 関数にはデフォルト引数を一つしか設定できない。
# D. デフォルト引数を持つ関数は、引数なしで呼び出すことができない。

# <解答>
#  B. デフォルト引数は、関数定義で指定された値を持ち、呼び出し時に省略可能。


# 問題20: Pythonにおいてメソッドと関数の主な違いは何ですか？実行せずに答えてください。
# A. メソッドはクラス内で定義され、関数はクラス外で定義される。
# B. 関数は引数を取ることができるが、メソッドは引数を取ることができない。
# C. メソッドは戻り値を持つことができるが、関数は戻り値を持つことができない。
# D. 関数はオブジェクトに属することができるが、メソッドは独立している。

# <解答>
# A. メソッドはクラス内で定義され、関数はクラス外で定義される。


# 問題21: 関数で任意の数の位置引数を受け取るために使用するシンボルは何ですか？実行せずに答えてください。
# A. *
# B. &
# C. %
# D. $

# <解答>
# A. *