# コマンドライン引数またはキーボード入力し2つの数字を渡して、四足演算を選択させて結果を出力するコードを作成してください。
def add (num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return('ゼロで割ることはできません。')
    else:
        return num1 / num2
    
def calculator():
    num1 = int(input('> 1つ目の数字を入力してください。:'))
    num2 = int(input('> 2つ目の数字を入力してください。:'))
    choice_method = input('> 計算方法を選択してください(1: 足す 2: 引く 3: かける 4: 割る):')

    if choice_method == '1':
        print('>', add(num1, num2))
    elif choice_method == '2':
        print('>', substract(num1, num2))
    elif choice_method == '3':
        print('>', multiply(num1, num2))
    elif choice_method == '4':
        print('>', divide(num1, num2))    
    else:
        print('無効な数値です。')
        
# テスト
calculator()


# 実行したら、VALORANTのステージをランダムに選択するコードを作成してください。
import random
def select_stage():
    stages = ['スプリット', 'ヘイヴン', 'バインド', 'アセント', 'ロータス', 'ブリーズ', 'サンセット']
    return random.choice(stages)
    
# 上記の問題に加え、メンバーの名前を任意の数だけ入力して、ENDを入力したらループを抜け出し、メンバーをランダムに2チームにわけて出力する機能を追加してください。
def divide_team():
    member_list = []
    num = 1
    while True:
        choice_members = input(f'{num}人目のメンバーを入力してください。')
        if choice_members == 'END':
            break
        elif choice_members == '':
            continue
        num += 1
        member_list.append(choice_members)
        
    random.shuffle(member_list)
    attacker = member_list[:len(member_list)//2]
    defender = member_list[len(member_list)//2:]
    return attacker, defender

def main():
    stage = select_stage()
    attacker, defender = divide_team()
    print(f'アタッカー側: {attacker} ディフェンダー側: {defender} ステージ: {stage}')

# テスト  
if __name__ == '__main__': 
    main()  
    

# スクレイピングをしてみよう
# スクレイピングした結果を、自分のPCにデータとして保存しつつ、スクレイピング結果をLINEに送るコードを作成してみよう。
import requests
from bs4 import BeautifulSoup
import re

# LINEトークン
token = '〇〇〇〇'
# APIのURL
api_url = 'https://notify-api.line.me/api/notify'
# yahooニュース
url = 'https://news.yahoo.co.jp/'

# Webページ取得
res = requests.get('https://news.yahoo.co.jp/')

# yahooニュースのトピックスを取得&抽出
soup = BeautifulSoup(res.text, 'html.parser')
elems = soup.find_all(href = re.compile('news.yahoo.co.jp/pickup'))

news_info = ''
for elem in elems:
    title = elem.text
    link = elem['href']
    news_info += f'{title}\n{link}\n'
# ファイル作成と保存
with open('yahoo_news.html', 'w', encoding = 'UTF-8') as f:   
    f.write(news_info)
    
print('ファイルへの書き込み完了。')

# 通知内容
send_contents = f'Pythonテスト: yahooトップニュース\n{news_info}'

# LINEに通知を送る
token_dic = {'Authorization': 'Bearer'+ ' ' + token}
send_dic = {'message': send_contents}
requests.post(api_url, headers = token_dic, data = send_dic)