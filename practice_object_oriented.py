# 問題 1: Pythonで新しいクラスを定義する際の正しい構文はどれですか？実行せずに解答してください
# A. class MyClass() {}
# B. class MyClass: pass
# C. new class MyClass():
# D. def MyClass: pass

# ＜解答＞
# B. class MyClass: pass


# 問題 2: クラスのインスタンスを作成する際に自動的に呼び出されるメソッドはどれですか？実行せずに解答してください
# A. __init__()
# B. __start__()
# C. __create__()
# D. __new__()

# ＜解答＞
# A. __init__()


# 問題 3: オブジェクト指向プログラミングにおいて、データとそのデータに操作を行うメソッドを一緒にまとめる概念を何と呼びますか？実行せずに解答してください
# A. カプセル化
# B. 継承
# C. ポリモーフィズム
# D. 抽象化

# ＜解答＞
# A. カプセル化


# 問題 4: Pythonにおいて、基底クラスのメソッドを派生クラスで再定義することを何と呼びますか？実行せずに解答してください
# A. オーバーローディング
# B. オーバーライディング
# C. インターフェイシング
# D. エクステンディング

# ＜解答＞
# B. オーバーライディング


# 問題 5: Pythonのクラスが複数の基底クラスから継承できる特性を何と呼びますか？実行せずに解答してください
# A. ポリモーフィズム
# B. マルチスレッディング
# C. マルチキャスティング
# D. 多重継承

# ＜解答＞
# D. 多重継承


# 問題 6: Pythonにおいて、同一クラスの異なるインスタンス間で共有される変数を何と呼びますか？実行せずに解答してください
# A. ローカル変数
# B. グローバル変数
# C. インスタンス変数
# D. クラス変数

# ＜解答＞
# D. クラス変数


# 問題7: オブジェクト指向とはなにか、メリットも踏まえて説明してください。自己理解できていない解答の場合、クリアになりません。
# ＜解答＞
# オブジェクト指向はプログラム上で扱う対象をオブジェクト(モノ)としに見立てて、
# オブジェクトを中心にプログラムを組み立てていく手法である。
# あるプログラムの固有の情報をクラスとしてまとめることで、よりまとまりのある、読みやすいコードを記述できるようになる。
# オブジェクト指向プログラミングには、一度コードを書けばそのコードを他のプログラムでも再利用ができる「再利用性」、
# コードが整理されるため、修正や機能の更新などがしやすくなる「保守性」、
# 既存クラスに機能の追加や変更をすることが容易である「拡張性」などといった利点がある。


# 問題8: オブジェクト指向とオブジェクトの違いを説明してください。自己理解できていない解答の場合、クリアになりません。
# ＜解答＞
# オブジェクトはプログラム上にある具体的な「モノ」のことである。オブジェクトは属性とメソッドを持っている。
# 一方オブジェクト指向は、そういったオブジェクトを利用してプログラミングをしていく手法のことである。


# 問題9: 継承とはなにかを説明してください。自己理解できていない解答の場合、クリアになりません。
# ＜解答＞
# 継承とは元となるクラスの機能を引き継ぎながら、新たな機能を加えたり、元の機能を上書きしたりする仕組みである。
# 元のクラスの機能を引き継ぐことでコードの重複を減らすことができ、コードを読みやすくなる。


# 問題10: カプセル化とはなにかを説明してください。自己理解できていない解答の場合、クリアになりません。
# ＜解答＞
# カプセル化とは、「使い手に関係のないものは見せない(隠蔽する)」という概念である。
# これにより、オブジェクトを利用する側は、オブジェクトの内部を気にすることなく、
# 利用可能な機能のみを使用し、操作が可能になる。
# また、オブジェクトに対し、外部からのアクセスを制限することで不正に情報を変更されることを防ぐことができ、
# あるオブジェクトに内部的な変更があっても、そのコードを利用する他のオブジェクトを変更する必要がなくなるため、
# コードの保守性や拡張性が高まる。


# 問題11: ポリモーフィズム(多態性)とはなにかを説明してください。自己理解できていない解答の場合、クリアになりません。
# ＜解答＞
# ポリモーフィズムは多態性とも言われ、簡単に言えば「同じ名前のメソッドで異なる挙動を実現する」ことである。
# 定義を共通にすることで、柔軟な設計が可能になる。
# また、同じルールを実装した異なるオブジェクトがある場合、共通のコードを再利用することができ、
# 新しくオブジェクトを追加した場合でも、共通した部分の実装を行うだけで、既存のコードに修正を加える必要もなく、
# 保守性の高いコードを実現できる。


# 問題12: 以下の通り図書館管理システムを作成してください。仕様が分からない場合は質問してください。
# 目的: 図書館内の書籍を管理する簡単なシステムを構築する。
# タスク: 'Book' クラスを作成し、書籍のタイトル、著者、ISBN番号を属性として保持する。また、図書の貸出状況を管理するメソッドを実装する。
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        # 貸出可の時にTrue
        self.can_lend = True 

    def show_book(self):
        print(f'書籍名:{self.title}, 著者:{self.author}, 貸出状況:{self.can_lend}')

    def borrow_book(self):
        if self.can_lend:
            self.can_lend =False
            print(f'{self.title}は貸し出されました。')
        else:
            print(f'{self.title}は貸し出し中です。')
    
    def return_book(self):
        if not self.can_lend:
            self.can_lend = True
            print(f'{self.title}が返却されました。')
        else:
            print(f'{self.title}は貸し出し可能です。')

# テスト
book1 = Book('リゼロ', '長月達平', 123456789)
book2 = Book('一瞬の風になれ', '佐藤多佳子', 123459876)
book3 = Book('独習Python', '山田祥寛', 987654321)

book1.show_book()
book1.borrow_book()
book1.borrow_book()
book1.return_book()
book1.return_book()

# チャレンジ: 'Library' クラスを作成して、複数の 'Book' オブジェクトを管理する。書籍の貸出、返却、検索機能を実装する。
class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print(f'{book.title}を追加しました。')

    def lend_book(self, title):
        for book in self.book_list:
            if book.title == title:
                book.borrow_book()
                break
        return False
    
    def return_book(self, title):
        for book in self.book_list:
            if book.title == title:
                book.return_book()
                break
        return False       

    def search_book(self, title):
        for book in self.book_list:
            if book.title == title:
                book.show_book()
                break
        return False
    
# テスト
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.lend_book('リゼロ')
library.lend_book('リゼロ')
library.search_book('リゼロ')
library.return_book('リゼロ')
library.search_book('リゼロ')
library.search_book('一瞬の風になれ')
library.search_book('独習Python')


# 問題13: 以下の通り簡易銀行口座管理システムを作成してください。仕様が分からない場合は質問してください。
# 目的: 銀行の口座を管理するシステムを作成する。
# タスク: 'Account' クラスを作成し、口座名義人、口座番号、残高を属性として保持する。預金、引き出し、残高照会のメソッドを実装する。
class Account:
    def __init__(self, owner, number, balance = 0):
        self.owner = owner
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('残高不足です。')
            return None

    def balance_inquiry(self):
        print(f'口座名義: {self.owner}, 口座番号:{self.number}, 残高:{self.balance}')

# チャレンジ: 利子計算機能を追加する。特定の利率に基づいて、定期的に利子を計算し、残高に加算するメソッドを実装する。
    def calculate_interest(self, period):
        INTEREST_RATE = 0.01
        interest = self.balance * period * INTEREST_RATE
        self.balance += interest

# テスト
my_account = Account('yamada taro', 1234567)
my_account.balance_inquiry()
my_account.deposit(20000)
my_account.withdraw(10000)
my_account.balance_inquiry()
my_account.withdraw(30000)
my_account.calculate_interest(1)
my_account.balance_inquiry()


# 問題14: 以下の通りオンラインショッピングカートシステムを作成してください。仕様が分からない場合は質問してください。
# 目的: オンラインで商品を販売するショッピングカートシステムを構築する。
# タスク: 'Product' クラスと 'ShoppingCart' クラスを作成する。'Product' クラスには、商品名、価格、在庫数を属性として持たせる。
# 'ShoppingCart' クラスでは、選択された商品とその数量を管理し、カート内の合計金額を計算するメソッドを実装する。
# チャレンジ: カート内で同じ商品を複数回追加した場合の処理を考える。また、在庫数を超える注文があった場合のエラーハンドリングを実装する。
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.cart_list = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.cart_list.append({'product': product, 'quantity': quantity})
            print(f'{product.name}を{quantity}個、カートに追加しました。')
            product.stock -= quantity
        else:
            print('在庫が不足しています。')

    def remove_product(self, product, quantity):
        for item in self.cart_list:
            if item['product'] == product:
                if item['quantity'] > quantity:
                    item['quantity'] -= quantity
                    print(f'{product.name}を{quantity}個、カートから削除しました。')
                    product.stock += quantity
                else:
                    self.cart_list.remove(item)
                    print(f'{product.name}を削除しました。')
                break  

    def calculate_amount(self):
        total = 0
        for item in self.cart_list:
            total += item['product'].price * item['quantity']
        return total

# テスト
product1 = Product('オレンジ', 100, 20)
product2 = Product('シャインマスカット', 1000, 10)

cart = ShoppingCart()
cart.add_product(product1, 10)
cart.add_product(product2, 5)
cart.add_product(product1, 20)
cart.remove_product(product2, 2)

print(f'カートの合計金額: {cart.calculate_amount()}')


# 問題15: 以下の通り車両管理システムを作成してください。仕様が分からない場合は質問してください。
# 目的: 異なる種類の車両を管理するシステムを構築する。
# タスク: 'Vehicle' クラスをベースにして、'Car'、'Truck'、'Motorcycle' といったサブクラスを作成する。
# 各クラスには、固有の属性（荷物の積載量、乗車定員、二輪車か四輪車かなど）とメソッド（加速、減速など）を持たせる。
# チャレンジ: 多態性を利用して、異なる種類の車両に共通のインターフェース（例えば、'drive' メソッド）を定義する。
# また、車両の登録、削除、検索機能を持つ 'VehicleManager' クラスを実装する。
from abc import abstractmethod, ABC

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def drive(self):
        pass

    def acceleration(self):
        print(f'{self.model}は加速した。')

    def deceleration(self):
        print(f'{self.model}は減速した。')

class Car(Vehicle):
    def __init__(self, brand, model, year, passengers_capacity):
        super().__init__(brand, model, year)
        self.passengers_capacity = passengers_capacity

    def drive(self):
        print(f'{self.model}は{self.passengers_capacity}人を乗せて発進した。')
          

class Truck(Vehicle):
    def __init__(self, brand, model, year, loading_capacity):
        super().__init__(brand, model, year)
        self.loading_capacity = loading_capacity

    def drive(self):
        print(f'{self.model}は{self.loading_capacity}kgの荷物を積載して発進した。')

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, wheel_count = 2):
        super().__init__(brand, model, year)
        self. wheel_count = wheel_count

    def drive(self):
        print(f'{self.model}は発進した。')

class VehicleManager:

    def __init__(self):
        self.vehicle_list = []

    def add_vehicle(self, vehicle):
        self.vehicle_list.append({'brand': vehicle.brand, 'model':vehicle.model, 'year': vehicle.year})
        print(f'{vehicle.brand} {vehicle.model} {vehicle.year}年式 を登録しました。')

    def remove_vehicle(self, vehicle):
        for item in self.vehicle_list:
            if (item['brand'] == vehicle.brand) or (item['model'] == vehicle.model):
                self.vehicle_list.remove(item)
                print(f'{vehicle.brand} {vehicle.model}を削除しました。')   
                break
            else:
                print(f'{vehicle.brand} {vehicle.model}はリストにありません。')

    def search_vehicle(self, vehicle):
        for item in self.vehicle_list:
            if (item['brand'] == vehicle.brand) or (item['model'] == vehicle.model) or (item['year'] == vehicle.year):
                print(f'{vehicle.brand} {vehicle.model} {vehicle.year}年式 が見つかりました。')
                break
            else:
                print(f'{vehicle.brand} {vehicle.model} {vehicle.year}年式 はリストにありません。')
            break

# テスト
car1 = Car('トヨタ', 'カローラ', '2022', '5')
truck1 = Truck('いすず', 'FORWARD', '2005', '2000')
motorcycle1 = Motorcycle('ハーレー', 'CVO', '2024', '2')

car1.acceleration()
car1.deceleration()
car1.drive()
truck1.drive()
motorcycle1.drive()

manage = VehicleManager()
manage.add_vehicle(car1)
manage.add_vehicle(truck1)
manage.add_vehicle(motorcycle1)
manage.remove_vehicle(car1)
manage.search_vehicle(car1)
manage.search_vehicle(truck1)

# 問題16: 以下の通りRPGキャラクターとバトルシステムを作成してください。仕様が分からない場合は質問してください。
# RPGゲームにおいて、プレイヤーと敵キャラクターが戦うシンプルなバトルシステムを作成します。このシステムでは、キャラクターは「攻撃力」「防御力」「HP（ヒットポイント）」の3つの属性を持ちます。
# プレイヤーは敵キャラクターに攻撃を行い、その逆も同様です。攻撃力と防御力を考慮して、ダメージを計算し、HPからダメージ分を減算します。HPが0以下になったキャラクターの敗北とします。
# 目的: RPGキャラクター同士をバトルさせる
# タスク: 'Character' クラスを作成します。このクラスには、'name'（名前）、'attack'（攻撃力）、'defense'（防御力）、'hp'（ヒットポイント）の属性があります。
# 'Character' クラスには、他のキャラクターに攻撃を行うメソッド 'attack_other' を実装します。このメソッドは、攻撃対象のキャラクターを引数として受け取ります。
# ダメージ計算式は、'攻撃力 - 防御力 = ダメージ' とします。ただし、ダメージは最低1とします。
# HPが0以下になったキャラクターは「敗北」と表示します。
class Game:
     def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

     def battle(self):
        while True:
            self.character1.attack_other(self.character2)
            if self.character2.hp <= 0:
                print(f'{self.character2.name}は倒れた！{self.character1.name}の勝利！')
                break

            self.character2.attack_other(self.character1)
            if self.character1.hp <= 0:
                print(f'{self.character1.name}は倒れた！{self.character2.name}の勝利！')
                break

class Character:
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp

    def attack_other(self, opponent):
        if self.attack > opponent.defense:
            opponent.hp -= self.attack - opponent.defense
        else:
            opponent.hp -= 1
        if opponent.hp <= 0:
            opponent.hp = 0
        print(f'{self.name}の攻撃!')
        self.attack_log(opponent)

    def attack_log(self, opponent):
        pass

class Abel(Character):
    def __init__(self, skill):
        super().__init__('アベル', 5, 2, 20)
        self.skill = skill

    def attack_log(self, opponent):
            print(f'{self.skill}をはなった! {opponent.name}に{self.attack - opponent.defense}ダメージを与えた！{opponent.name}のHPは{opponent.hp}だ!')

class Slime(Character):
    def __init__(self, skill):
        super().__init__('スライム', 4, 1, 18)
        self.skill = skill

    def attack_log(self, opponent):
            print(f'{self.skill}をはなった! {opponent.name}に{self.attack - opponent.defense}ダメージを与えた！{opponent.name}のHPは{opponent.hp}だ!')

# テスト
abel = Abel('火炎斬り')
slime = Slime('体当たり')
game = Game(abel, slime)

game.battle()


# 問題17: 以下の通り動物の鳴き声システムを作成してください。仕様が分からない場合は質問してください。
# あなたは動物園の管理者で、動物園にいる異なる動物たちがどのように鳴くのかを訪問者に示す展示を企画しています。展示では、犬、猫、鳥といった動物たちがそれぞれ独特の鳴き声を披露します。
# 基底クラス 'Animal' を作成し、このクラスにはすべての動物が共通して持つべき属性やメソッドを定義します。
# そして、'Animal' クラスを継承する形で各動物のクラスを作成し、それぞれの動物が特有の鳴き声を出すようにします。
# 目的: 動物の鳴き声を出しわける
# タスク:'Animal' クラスを作成します。このクラスには、'name'（名前）属性と、'speak'（鳴く）メソッドを含めます。
# 'speak' メソッドは、"This animal doesn't make a sound."（この動物は鳴きません）と出力します。
# 犬クラス:'Animal' クラスを継承し、'Dog' クラスを作成します。'Dog' クラスの 'speak' メソッドは、"Woof!" と出力します。
# 猫クラス:'Animal' クラスを継承し、'Cat' クラスを作成します。'Cat' クラスの 'speak' メソッドは、"Meow!" と出力します。
# 鳥クラス:'Animal' クラスを継承し、'Bird' クラスを作成します。'Bird' クラスの 'speak' メソッドは、"Tweet!" と出力します。

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal doesn't make a sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Woof!')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Meow!')

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Tweet!')

# テスト
puppy = Dog('pochi')
kitty = Cat('tama')
chick = Bird('shiro')

puppy.speak()
kitty.speak()
chick.speak()