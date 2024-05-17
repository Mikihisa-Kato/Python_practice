# 問題1: Car クラスを定義し、インスタンス化した際に車種名（model）を属性として持つようにしてください。また、その車種名を印刷するメソッド print_model も定義してください。
class Car:
    def __init__(self, model):
        self.model = model

    def print_model(self):
        print(f'車種名: {self.model}')

# テスト
car_name = Car('カローラ')
car_name.print_model()


# 問題2: Book クラスを定義し、タイトル（title）と著者（author）を属性として持つようにしてください。インスタンス化時にこれらの属性を設定できるようにしてください。
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# テスト
book = Book('リゼロ', '長月達平')
print(f'Title:{book.title}, author: {book.author}')


# 問題3: Calculator クラスを定義し、2つの数を引数として受け取り、その和を返すメソッド add を作成してください。
class Calculator:
    def add(self, x, y):
        return x + y
    
# テスト
calc = Calculator()
result = calc.add(5, 7)
print(result)


# 問題4: Animal クラスを定義し、インスタンス化時に動物の種類（species）を属性として設定できるようにしてください。種類を印刷するメソッド print_species も定義してください。
class Animal:
    def __init__(self, species):
        self.species = species

    def print_species(self):
        print(f'種族:{self.species}')

# テスト
cat = Animal('猫')
cat.print_species()


# 問題5: Person クラスを定義し、名前（name）と年齢（age）を属性として持つようにしてください。また、Person クラスには、その人の名前と年齢を印刷するメソッド introduce も含めてください。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'私の名前は{self.name}です。年齢は{self.age}歳です。')

# テスト
taro = Person('山田太郎', 25)
taro.introduce()


# 問題6: Rectangle クラスを定義し、幅（width）と高さ（height）を属性として持ち、面積を計算するメソッド area を定義してください。
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# テスト
rect = Rectangle(4, 5)
print(rect.area())


#問題7: Employee クラスを定義し、名前（name）と給与（salary）を属性として持つようにしてください。給与を引数として受け取り、現在の給与に加算するメソッド give_raise も定義してください。
class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def give_raise(self, money):
        self.salary += money

# テスト
player = Employee('山田太郎', 200000)
player.give_raise(190000)
print(player.salary)


# 問題8: Circle クラスを定義し、半径（radius）を属性として持ち、円周と面積を計算するメソッド circumference と area を定義してください。円周率は 3.14 とします。
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        return 2 * self.radius * 3.14
    
    def area(self):
        return self.radius * self.radius * 3.14
    
# テスト
circle1 = Circle(4)
print(f'円周: {circle1.circumference()}')
print(f'面積: {circle1.area()}')


# 問題9: BankAccount クラスを定義し、口座名義（owner）と残高（balance）を属性として持つようにしてください。このクラスには、預金を追加するメソッド deposit と、引き出しを行うメソッド withdraw を含めてください。引き出しは残高を超えることはできないようにしてください。
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, salary):
        self.balance += salary

    def withdraw(self, draw_money):
        if draw_money <= self.balance:
            self.balance -= draw_money
        else:
            print('残高不足です。')
            return None

# テスト
account = BankAccount('taro yamada', 200000)
print(f'口座名義: {account.owner}')
print(f'残高: {account.balance}')

account.deposit(180000)
print(f'残高: {account.balance}')

account.withdraw(50000)
print(f'残高: {account.balance}')

account.withdraw(400000)
print(f'残高: {account.balance}')


# 問題10: Student クラスと Teacher クラスを定義し、両者に共通する属性（name、age）を持つ Person クラスから継承させてください。Student クラスには学年（grade）を、Teacher クラスには教える科目（subject）を属性として追加してください。それぞれのクラスに適切なメソッドを追加してください。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f'{self.name}は勉強しています。')


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        print(f'{self.name}は{self.subject}を教えています。')

# テスト
student1 = Student('山田太郎', 15, '中学3年')
print(f'名前: {student1.name}')
print(f'年齢: {student1.age}')
print(f'学年: {student1.grade}')
student1.study()

teacher1 = Teacher('鈴木翔太', 27, '理科')
print(f'名前: {teacher1.name}')
print(f'年齢: {teacher1.age}')
print(f'科目: {teacher1.subject}')
teacher1.teach()


# 問題11: Animal クラスを作成し、このクラスを継承する Dog と Cat クラスを定義してください。Animal クラスには speak メソッドを定義し、このメソッドは "I'm an animal" という文字列を出力します。Dog クラスと Cat クラスでは speak メソッドをオーバーライドして、それぞれ "Woof!" と "Meow!" と出力するようにしてください。次に、Dog インスタンスと Cat インスタンスを作成し、それぞれの speak メソッドを呼び出してください。
class Animal:
    def speak(self):
        print("I'm an animal")

class Dog(Animal):
    def speak(self):
        print('Woof!')

class Cat(Animal):
    def speak(self):
        print('Meow!')

# テスト
puppy = Dog()
puppy.speak()

kitty = Cat()
kitty.speak()


# 問題12: BankAccount クラスを定義してください。このクラスには、口座名義（owner）と残高（balance）という2つのプライベート属性を持たせてください。残高はインスタンス化時に設定できるようにし、残高の初期値は0とします。また、残高を安全に取得するための公開メソッド get_balance と、残高を安全に設定するための公開メソッド set_balance を実装してください。set_balance メソッドでは、設定しようとする残高が負の数でないことを確認してください。
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.__owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print('負の数は設定できません。')
    
# テスト
account1 = BankAccount('taro yamada')
# print(account1.__owner)　→隠蔽されたためアクセス不可
print(f'残高: {account1.get_balance()}')

account1.set_balance(100000)
print(f'残高: {account1.get_balance()}')

account1.set_balance(-100000)
print(f'残高: {account1.get_balance()}')


# 問題13: Shape という基底クラスを作成し、Rectangle と Circle という2つの派生クラスをこの基底クラスから作成してください。Shape クラスには、area と perimeter という2つの抽象メソッドを定義してください。Rectangle クラスは長さと幅を、Circle クラスは半径をそれぞれ属性として持ち、これらのクラスで area と perimeter メソッドを具体的に実装してください。最後に、Rectangle インスタンスと Circle インスタンスを作成し、それぞれの面積と周囲の長さを計算して出力してください。
from abc import abstractmethod, ABC

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14
    
    def perimeter(self):
        return 2 * self.radius * 3.14
    
# テスト
rectangle1 = Rectangle(5, 6)
print(rectangle1.area())
print(rectangle1.perimeter())

circle1 = Circle(5)
print(circle1.area())
print(circle1.perimeter())


# 問題14: Pythonで新しいクラスを定義するキーワードはどれですか？実行せずに答えてください。
# A. class
# B. Class
# C. new
# D. object

# <解答>
# A. class


# 問題15: 以下のクラス定義に基づいて、インスタンスmy_dogの名前を出力するコードはどれですか？実行せずに答えてください。
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Rex")

# A. print(Dog.name)
# B. print(Dog("Rex").name)
# C. print(my_dog.name)
# D. print(name)

# <解答>
# C. print(my_dog.name)


# 問題16: 次のうち、クラスメソッドを正しく定義しているのはどれですか？実行せずに答えてください。
# A.
class MyClass:
    def my_method(cls):
        print("Hello, world!")
# B.
class MyClass:
    @staticmethod
    def my_method():
        print("Hello, world!")
# C.
class MyClass:
    @classmethod
    def my_method(cls):
        print("Hello, world!")
# D.
class MyClass:
    def my_method(self):
        print("Hello, world!")

# <解答>
# D.


# 問題17: 次のPythonコードにおいて、ChildClassがParentClassから継承しているメソッドはどれですか？実行せずに答えてください。
class ParentClass:
    def method_a(self):
        print("Method A")

    def method_b(self):
        print("Method B")

class ChildClass(ParentClass):
    def method_b(self):
        print("Modified Method B")
# A. method_aのみ
# B. method_bのみ
# C. method_aとmethod_bの両方
# D. どちらのメソッドも継承していない

# <解答>
# C. method_aとmethod_bの両方


# 問題18: 以下のPythonクラス定義で、インスタンス化時に何も引数を渡さなかった場合、self.nameに設定される値は何ですか？実行せずに答えてください。
class Person:
    def __init__(self, name="John Doe"):
        self.name = name
# A. エラーが発生する
# B. None
# C. "John Doe"
# D. 空の文字列("")

# <解答>
# C. "John Doe"


# 問題19: Pythonでは、クラスに複数のコンストラクタメソッドを定義することができますか？実行せずに答えてください。
# A. 直接複数の`__init__`メソッドを定義できます。
# B. `@overload`デコレータを使用して複数の`__init__`メソッドを定義できます。
# C. 直接複数の`__init__`メソッドを定義することはできませんが、デフォルト引数や`*args`、`**kwargs`を使用して同様の振る舞いを実現できます。
# D. Pythonのクラスには唯一のコンストラクタしか存在しません。

# <解答>
# C. 直接複数の__init__メソッドを定義することはできませんが、デフォルト引数や*args、**kwargsを使用して同様の振る舞いを実現できます。


# 問題20: インスタンス、オブジェクト、クラスの違いを説明してください。自己理解できている説明出ない場合、クリアになりません。
# <解答>
# クラスとはオブジェクト指向プログラミングにおいて重要な概念。
# データとそのデータに関する操作をまとめたものである。
# クラスは属性とメソッドをもっており、前者はクラスに固有のデータを持たせ、
# 後者はそのデータを操作する関数である。
# オブジェクトとは、クラスから生成された具体的なデータの実体を指す。
# インスタンスは基本的にはオブジェクトと同義とされるが、クラスから生成された個々のオブジェクトをインスタンスと呼ぶこともある。
# インスタンスはオブジェクトに含まれると考えるとよい。