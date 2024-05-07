# 問題1: リスト fruits に "apple", "banana", "cherry" を含めます。リストの最後の要素を出力してください。
fruits = ['apple', 'banana', 'cherry']
print(fruits[-1])


# 問題2: リスト numbers が [10, 20, 30, 40, 50] で初期化されています。このリストから、2番目と4番目の要素だけを含む新しいリスト selected_numbers を作成してください。
numbers = [10, 20, 30, 40, 50]
select_numbers = numbers[1:4:2]
print(select_numbers)


# 問題3: リスト colors が以下のように定義されています: colors = ["red", "green", "blue"]。このリストの長さ（要素数）を求めるPythonコードを書いてください。
colors = ["red", "green", "blue"]
print(len(colors))


# 問題4: リスト numbers が [1, 2, 3, 4, 5] で与えられたとします。このリストのすべての要素の合計値を求めるPythonコードを書いてください。
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))


# 問題5: 辞書 person が以下のように定義されています: person = {"name": "Alice", "age": 30}。この辞書から "name" の値を取得して出力するPythonコードを書いてください。
person = {"name": "Alice", "age": 30}
print(person["name"])


# 問題6: 辞書 scores が以下のように定義されています: scores = {"math": 90, "science": 85}。この辞書に新たなキーと値のペア "english": 95 を追加するPythonコードを書いてください。
scores = {"math": 90, "science": 85}
scores["english"] = 95
print(scores)


# 問題7: 辞書 color_codes が以下のように定義されています: color_codes = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}。この辞書を使用して、"green" の色コードを取得するPythonコードを書いてください。
color_codes = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
print(color_codes["green"])


# 問題8: 二つの辞書 dict1 と dict2 があります。dict1 = {"a": 1, "b": 2}、dict2 = {"c": 3, "d": 4}。これら二つの辞書を結合して、新しい辞書 dict3 を作成するPythonコードを書いてください。
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {**dict1, **dict2}
print(dict3)


# 問題9: 辞書 person が以下のように定義されています: person = {"name": "Alice", "age": 30, "city": "New York"}。この辞書から "age" のキーと値を削除するPythonコードを書いてください。
person = {"name": "Alice", "age": 30, "city": "New York"}
del person["age"]
print(person)


# 問題10: 辞書 student が以下のように定義されています: student = {"name": "John", "age": 21}。この辞書に新たなキーと値のペア "grade": "A" を追加してください。
student = {"name": "John", "age": 21}
student["grade"]="A"
print(student)


# 問題11: 辞書 inventory が以下のように定義されています: inventory = {"apples": 30, "bananas": 15, "oranges": 22}。この辞書からキー "bananas" を削除してください。さらに、新たなキーと値のペア "pears": 17 を追加してください。
inventory = {"apples": 30, "bananas": 15, "oranges": 22}
del inventory["bananas"]
inventory["pears"] = 17
print(inventory)


# 問題12: 辞書 profile には、あるユーザーのプロフィール情報が格納されています: profile = {"name": "Alice", "email": "alice@example.com", "location": "Paris"}。このユーザーがメールアドレスを変更したため、辞書内の "email" の値を "alice@newdomain.com" に更新してください。さらに、このユーザーが新しいスキル "Python programming" を学んだことを示すために、新たなキー "skills" を追加し、値にリスト ["Python programming"] を設定してください。
profile = {"name": "Alice", "email": "alice@example.com", "location": "Paris"}
profile["email"] = "alice@newdomain.com"
profile["skills"] = "Python programming"
print(profile)


# 問題13:Pythonでリストの最後に新しい要素を追加するにはどのメソッドを使用しますか？実行せずに答えてください。また理由も答えてください。
# A. append()
# B. insert()
# C. extend()
# D. push()

# <解答>
# A. append()
# <理由>
# append()はリストの最後に要素を追加するメソッド。
# insert()は先頭からn番目の直前に要素を追加するメソッド。
# extend()はリストにリストを追加する(リストを拡張する)時に利用するメソッド。
# push()というメソッドはPythonにはない。


# 問題14: Pythonで辞書の全てのキーを取得するにはどのメソッドを使用しますか？実行せずに答えてください。また理由も答えてください。
# A. keys()
# B. items()
# C. values()
# D. getkeys()

# <解答>
# A. keys()
# <理由>
# keys()はキーを取得するメソッド。
# items()はキーと値を取得するメソッド。
# valuesは値を取得するメソッド。
# getkeys()というメソッドはPythonにはない。


# 問題15: 次のリスト内包表記が生成するリストは何ですか？実行せずに答えてください。また理由も答えてください。
[x**2 for x in range(5) if x % 2 == 0]
# A. [0, 1, 4, 9, 16]
# B. [0, 4, 16]
# C. [1, 3, 5, 7, 9]
# D. [2, 4, 6, 8, 10]

# <解答>
#  B. [0, 4, 16]
# <理由>
# for文で0,1,2,3,4が出力される。
# そしてif文ではfor文で出力された要素の内、偶数の値(0,2,4)のみ出力する。
# x**2で先ほどの各偶数の値の二乗を計算するため、最終的に出力されるのは[0, 4, 16]である。


# 問題16: コレクション型の種類とそれぞれの違いを説明してください。自己理解必須

# コレクション型には大きく分けて下記の3つの種類がある。
# ①シーケンス型(リスト, タプル)
# ②集合型
# ③辞書型

# ①シーケンス型は要素が順序付けられたデータ構造になっている。
# 各要素にはインデックスが割り振られ、インデックス値で個々の要素にアクセスすることができる。
# またリストはミュータブル型、タプルはイミュータブル型であり、
# 前者に対してはappend()/pop()などのメソッドが利用できるが、後者に対しては利用できない。
# ②集合型はリストと同じように、複数の値を束ねる型であるが、リストと異なり順番(インデックス)を持たず、また重複を許さない。
# 例えば、「A, A, B」という要素があった場合、集合型だと{A,B}になるように重複は無視される。
# ある要素が、集合の中に含まれているかといった場合などに利用される。
# ③辞書型はキーと値のペアで格納されるデータ構造となっている。
# リストやタプルとは異なり、各要素にはインデックスではなく、キーの情報でアクセスすることができる。