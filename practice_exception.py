# 問題 1: 整数を引数として受け取り、その整数が正であれば"Positive"、そうでなければ"Non-Positive"を出力する関数を作成してください。ただし、引数が整数でない場合は"Error: Not an integer"と出力するように例外処理を実装してください。
def check_num(num):
    try:
        if isinstance(num, int):
            if num > 0:
                print('Positive')
            else: 
                num <= 0
                print('Non-Positive')
        else:
            raise TypeError('Error: Not an integer')
    except TypeError as e:
        print(e)
        
# テスト
check_num(3)
check_num(-3)        
check_num(3.5)
check_num('3')


# 問題 2: ユーザーから入力を受け取り、その入力が整数であればその値を返し、整数でない場合は"Invalid input"と出力する関数を作成してください。
def check_int():
    user_input_num = input('入力してください:')
    try:
        num = int(user_input_num)
        print(num)
    except ValueError:
        print('Invalid input')

# テスト
check_int() 


# 問題 3: リストnumbersから指定されたインデックスの要素を返す関数を作成してください。ただし、インデックスが範囲外の場合は"Index out of range"と出力するように例外処理を実装してください。
data = ['a', 'b', 'c', 'd', 'e']

def return_elem(index):
    try:
        print(data[index])
    except IndexError:
        print('Index out of range')

# テスト
return_elem(3)
return_elem(7)


# 問題 4: ユーザーから複数の整数入力を受け取り、その合計を返す関数を作成してください。ただし、入力が終了するまでユーザーからの入力を受け続けるようにしてください。入力が整数でない場合はその入力を無視して続行してください。
def total_num():
    total = 0
    while True:
        user_input_num = input('整数を入力してください。終了する場合はEnterキーを押してください。')
        if user_input_num == '':
            break
        try:
            num = int(user_input_num)
            total += num
        except ValueError:
            pass
    return total

# テスト
print(total_num())


# 問題 5: 与えられたファイル名のファイルを読み込み、その内容を出力する関数を作成してください。ファイルが存在しない場合は"File not found"と出力してください。
def read_file():
    file_name = input('ファイル名を入力してください:')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(content)
    except FileNotFoundError:
        print('File not found')
        
# テスト
read_file()


#　問題 6: ユーザーから入力を受け取り、その値を2で割った結果を返す関数を作成してください。# ただし、入力が0の場合は"Cannot divide by zero"と出力し、入力が整数でない場合は"Invalid input"と出力するように例外処理を実装してください。
def divide_num():
    user_input_num = input('数字を入力してください。:')
    try:
        num = int(user_input_num)
        print(num / 2)           
    except ZeroDivisionError:
        print('Cannot divide by zero') 
    except ValueError:
        print('Invalid input')

#テスト    
divide_num()


# 問題7: Pythonプログラミングにおいて、例外処理を適切に行うことの重要性はどれでしょう？実行せずに答えてください。
# A. プログラムの実行速度を向上させることができる
# B. コードをより複雑にし、理解を深めるため
# C. 実行時エラーによるプログラムの突然の停止を防ぎ、エラーをより適切に処理することができる
# D. すべてのバグを自動的に修正する

# ＜解答＞
# C. 実行時エラーによるプログラムの突然の停止を防ぎ、エラーをより適切に処理することができる


# 問題8: Pythonにおけるtryブロックの主な目的は何ですか？実行せずに答えてください。
# A. プログラムのパフォーマンスを向上させる
# B. プログラムの実行前にエラーをチェックする
# C. エラーが発生する可能性のあるコードを実行する
# D. プログラムの実行速度を測定する

# ＜解答＞
# C. エラーが発生する可能性のあるコードを実行する


# 問題9: 次の例外のうち、Pythonの組み込み例外であるものはどれですか？実行せずに答えてください。
# A. FileNotFound
# B. FileNotFoundError
# C. FileNotAccessibleError
# D. AccessDeniedError

# ＜解答＞
# B. FileNotFoundError


# 問題10: 以下のコードで捕捉される例外の種類は何ですか？実行せずに答えてください。
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except Exception as e:
    print(type(e).__name__)

# ユーザーが0を入力した場合、何が出力されますか？
# A. ValueError
# B. ZeroDivisionError
# C. TypeError
# D. InputError

# ＜解答＞
# B. ZeroDivisionError


# 問題11: 以下のエラーのうち、例外処理を検討すべきものと、そうでないものを選択してください。実行せずに答えてください。
# 各シナリオについて、例外処理が必要か不要かを選択してください。
# 1. ユーザー入力が期待するデータ型（例: 整数）でない場合
# 2. プログラムのロジックミスにより無限ループに陥った場合
# 3. データベースからのデータ取得中に通信エラーが発生した場合
# 4. 関数に不正な引数が渡された場合（関数のドキュメントに正しい使用法が記載されている）
# 5. ファイル操作中にファイルが見つからない、またはアクセスできない場合

# ＜解答＞
# 1. 必要
# 2. 不要
# 3. 必要
# 4. 不要
# 5. 必要


# 問題12: 以下のエラーに対して例外処理が必要な理由を説明してください。実行せずに答えてください。
# 1. ValueError
# 2. IndexError
# 3. KeyError
# 4. FileNotFoundError
# 5. ZeroDivisionError
# 6. ConnectionError

# ＜解答＞
# 1. 異なるデータ型を受け取ったり、変換できない場合に発生する。例外処理を行わない場合、プログラムがその段階で終了してしまうため。
# 2. リストやタプルにアクセスする時に指定したインデックスがない場合、その時点でプログラムが終了してしまうため、それを防ぐため。
# 3. 辞書でキーを探す時に、該当のキーがない場合にプログラムが終了してしまうことを防ぐため。
# 4. ファイルが見つからない場合に発生する。ファイル操作をしようとした時に、このエラーを発生させることで、プログラムが予期せず終了することを防ぐため。
# 5. 0で除算する場合にエラーとなってそれ以降の処理が適切に行われなくなることを防ぐため。
# 6. ネットワークに接続した際に発生する。外部のサイト等にアクセスしようとした際に、ネットワークに問題があった場合に適切にプログラムを終了できるようにするため。