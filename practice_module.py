# 問題1: Pythonの標準モジュール datetime を使用して、現在の日付と時刻を「YYYY-MM-DD HH:MM:SS」の形式で表示するプログラムを書いてください。
import datetime

dt = datetime.datetime.now()
print(dt.strftime('%Y-%m-%d %H:%M:%S'))


# 問題2: requests モジュールを使用して、指定されたURL（例えば、https://api.github.com）からデータを取得し、ステータスコードを印刷するプログラムを書いてください。この問題を解くためには、requests モジュールがインストールされている必要があります。
import requests

res = requests.request('get', 'https://api.github.com')
print(res.status_code)


# 問題3: 自分で calculator.py という名前のPythonモジュールを作成し、その中に2つの数値を引数として受け取り、それらの和を返す add 関数と、差を返す subtract 関数を定義してください。次に、別のPythonスクリプトからこの calculator モジュールをインポートし、add 関数と subtract 関数を使用して、いくつかの計算結果を出力してください。
import calculator

answer1 = calculator.add(3, 5)
answer2 = calculator.substract(5, 4)
print(answer1)
print(answer2)


# 問題4: 次のうち、Pythonのmathモジュールから平方根（square root）関数をインポートする正しい方法はどれですか？実行せずに答えてください。
# A. from math import sqrt
# B. import sqrt from math
# C. import math.sqrt
# D. load math.sqrt

# ＜解答＞
# A. from math import sqrt


# 問題5: 次のうち、pandasモジュールをpdというエイリアスでインポートする正しい方法はどれですか？実行せずに答えてください。
# A. import pandas as pd
# B. load pandas as pd
# C. from pandas use pd
# D. import pandas rename pd

# ＜解答＞
# A. import pandas as pd


# 問題6: 次のうち、Pythonに組み込まれているモジュールはどれですか？実行せずに答えてください。
# A. requests
# B. os
# C. numpy
# D. django

# ＜解答＞
# B. os


# 問題7: Pythonがモジュールを検索する際、最初に検索される場所はどこですか？実行せずに答えてください。
# A. インストールされたパッケージのディレクトリ
# B. 標準ライブラリのディレクトリ
# C. 現在のディレクトリ
# D. PYTHONPATH環境変数で指定されたディレクトリ

# ＜解答＞
# C. 現在のディレクトリ