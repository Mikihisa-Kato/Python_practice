# 問題1:変数numberに1から100の任意の値を代入します。このnumberが3で割り切れる場合は「Fizz」、5で割り切れる場合は「Buzz」、両方で割り切れる場合は「FizzBuzz」を出力するプログラムを作成してください。それ以外の場合は、その数をそのまま出力してください。
number_str = input('1~100の任意の値を入力してください。:')
number = int(number_str)

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')    
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)


# 問題2: 変数aに任意の正の整数を代入します。aが偶数であれば "Even"、奇数であれば "Odd" を出力するプログラムを書いてください。
a_str = input('正の整数を入力してください:')
a = int(a_str)

if a % 2 == 0:
    print('Even')
else:
    print('Odd')


# 問題3: 変数 temperature に気温（整数）を代入します。temperature が25度以上であれば "Hot"、それ未満であれば "Cold" を出力するプログラムを書いてください。
temperature_str = input('今日気温を入力してください:')
temperature = int(temperature_str)

if temperature >= 25:
    print('Hot')
else:
    print('Cold')


# 問題4: 変数 age に年齢（整数）を代入します。age が18歳以上であれば "Adult"、それ未満であれば "Minor" を出力するプログラムを書いてください。
age_str = input('年齢を入力してください:')
age = int(age_str)

if age >= 18:
    print('Adult')
else:
    print('Minor')


# 問題5: 変数 score に試験の点数（0〜100の整数）を代入します。score が60点以上なら "Pass"、それ未満なら "Fail"、さらに90点以上なら "Excellent" を出力するプログラムを書いてください。
score_str = input('試験の点数を入力してください。:')
score = int(score_str)

if score >= 90:
    print('Excellent')
elif score >= 60:
    print('Pass')
else:
    print('Fail')


# 問題6: 変数 year に年（整数）を代入します。year がうるう年であれば "Leap Year"、そうでなければ "Common Year" を出力するプログラムを書いてください。うるう年は、4で割り切れる年のうち、100で割り切れないか、または400で割り切れる年です。
year_str = input('年を入力してください:')
year = int(year_str)

if year % 400 == 0:
    print('Leap Year')
elif year % 100 == 0:
    print('Common Year')
elif year % 4 == 0:
    print('Leap Year')
else:
    print('Common Year')


# 問題7: 変数 x と y に任意の整数を代入します。x が y より大きければ "X is greater than Y"、x が y より小さければ "X is less than Y"、等しければ "X and Y are equal" を出力するプログラムを書いてください。
x_str = input('任意の整数を入力してください。:')
x = int(x_str)
y_str = input('任意の整数を入力してください。:')
y = int(y_str)

if x > y:
    print('X is greater than Y')
elif x < y:
    print('X is less than Y')
else:
    print('X and Y are equal')


# 問題8: 変数 char に任意の英文字（小文字）を代入します。char が母音であれば "Vowel"、子音であれば "Consonant" を出力するプログラムを書いてください。母音は 'a', 'e', 'i', 'o', 'u' です。
char = input('任意の英文字(小文字)を入力してください。:')

if char in ['a', 'e', 'i', 'o', 'u']:
    print('Vowel')
else:
    print('Consonant')


# 問題9: 変数 number に任意の整数を代入します。number が正であれば "Positive"、負であれば "Negative"、0であれば "Zero" を出力するプログラムを書いてください。
number_str = input('任意の整数を入力してください。:')
number = int(number_str)

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')


# 問題10:変数`temperature`が `30`であるとき、以下のPythonコードの出力は何ですか？実行せずに答えてください。また理由も答えてください。
if temperature > 25:
    print("Hot")
elif temperature > 15:
    print("Warm")
else:
    print("Cold")
# A) Hot
# B) Warm
# C) Cold
# D) 何も出力されない

# <解答>
# A) Hot
# <理由>
# if文では最初に当てはまった条件しか出力しない。
# よって30は最初のtemprature > 25に条件が当てはまるため、Hotが出力され、処理が終了する。


# 問題11: 以下のコードを実行した際に表示される出力はどれですか？実行せずに答えてください。また理由も答えてください。
x = 10
y = 20

if x > y:
    print("X is greater than Y")
elif x < y:
    print("Y is greater than X")
else:
    print("X and Y are equal")
# A) X is greater than Y
# B) Y is greater than X
# C) X and Y are equal
# D) 何も出力されない

# <解答>
# B) Y is greater than X
# <理由>
# xよりyの方が大きいため、elifの条件式に当てはまる。
# よってY is greater than Xが出力される。


# 問題12: 以下のコードで定義された status に基づいて、どの文が出力されますか？実行せずに答えてください。また理由も答えてください。
status = "error"

if status == "ok":
    print("Operation successful.")
elif status == "error":
    print("An error occurred.")
else:
    print("Unknown status.")
# A) Operation successful.
# B) An error occurred.
# C) Unknown status.
# D) 何も出力されない

# <解答>
# B) An error occurred.
# <理由>
# 比較演算子'=='は左辺と右辺の値が等しいかどうかを判定する。
# 変数statusには文字列'error'が代入されており、
# elif文の条件式に当てはまるため、An error occurred.が出力される。

# 問題13: 以下のPythonコードの出力は何ですか？実行せずに答えてください。また理由も答えてください。
number = 5

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
if number % 5 == 0:
    print("Divisible by 5")
# A) Even
# B) Odd
# C) Divisible by 5
# D) Odd

# <解答>
# B) Odd
# C) Divisible by 5
# <理由>
# if文が2つあり、ネストされていないため、各if文が実行される。
# 結果、1つ目のif文でOddが出力され、2つ目のif文でDivisible by 5が出力される。


# 問題14: 条件分岐方法の種類と違いを説明してください。自己理解必須

# 条件分岐には下記の種類がある。
# ①if文
# ②if-else文
# ③if-elif-else文

# ①if文は1つの条件を評価し、TrueかFalseのいずれかによって、実行する処理を決める。
# 条件がTrueだった場合、if文配下の処理を実行するが、Falseだった場合は何も結果を返さない。

# ②if-else文はif文と同様に、条件がTrueだった場合はif文以下の処理を実行し、
# 条件がFalseだった場合はelse文の処理を実行する。

# ③if-elif-else文はif文の中にさらにelif文を記述することで、複数の条件を指定することができる。
# また、elifは分岐の数だけ増やすことができる。 
# if文→elif文→else文の順に条件を判定していく。
# if文の条件式がFalseだった場合、elif文で評価され、Trueであれば、elif配下の処理が実行される。
# elif文の条件式がFalseだった場合、else文で評価され、else文は以下の処理が実行される。