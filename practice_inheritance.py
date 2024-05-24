# 問題 1: Pythonでの単純なクラスの継承を示す例を作成してください。Animalクラスを基底クラスとして、DogクラスがAnimalクラスを継承し、barkメソッドを持つようにしてください。
class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print('woof!')

class Dog(Animal):
    def run(self):
        print(f'{self.name}は走った')

# テスト
dog = Dog('pochi')
dog.bark()


# 問題 2: Pythonでのメソッドオーバーライディングを示す例を作成してください。Vehicleクラスを作成し、moveメソッドを持たせてください。次に、CarクラスがVehicleクラスを継承し、moveメソッドをオーバーライドして、Car movingと出力するようにしてください。
class Vehicle:
    def move(self):
        print(f'moving')

class Car(Vehicle):
    def move(self):
        print(f'car moving')

# テスト
car = Car()
car.move()


# 問題 3: 継承とsuper()関数の使用を示す例を作成してください。Personクラスを作成し、__init__メソッドでnameとageを初期化してください。EmployeeクラスがPersonクラスを継承し、__init__メソッドをオーバーライドして、salaryを追加で初期化し、super()関数を使用してPersonの__init__メソッドを呼び出す例を示してください。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

# テスト
employee1 = Employee('山田太郎', 25, 200000)
print('名前:', employee1.name)
print('年齢:', employee1.age)
print('給料:', employee1.salary)


# 問題 4: Pythonでの多重継承を示す例を作成してください。FatherクラスとMotherクラスを作成し、それぞれsurnameとlastname属性を持たせてください。次に、ChildクラスがFatherとMotherの両方を継承し、両親の属性を組み合わせたfullname属性を持つ例を示してください。
class Father:
    def __init__(self, surname):
        self.surname = surname

class Mother:
    def __init__(self, lastname):
        self.lastname = lastname

class Child(Father, Mother):
    def __init__(self, surname, lastname):
        Father.__init__(self, surname)
        Mother.__init__(self, lastname)
        self.fullname = f'{self.surname}{self.lastname}'
# テスト
child = Child('山田', '太郎')
print(child.fullname)


# 問題5: Pythonでクラスが別のクラスから継承する際の正しい構文はどれですか？実行せずに答えてください。
# A. class SubClass inherits BaseClass:
# B. class SubClass extends BaseClass:
# C. class SubClass(BaseClass):
# D. class SubClass: inherit BaseClass

# ＜解答＞
# C. class SubClass(BaseClass):


# 問題6:子クラスが親クラスのメソッドをオーバーライドするとは、どういう意味ですか？実行せずに答えてください。
# A. 子クラスが親クラスのメソッドを隠蔽する。
# B. 子クラスが親クラスのメソッドを削除する。
# C. 子クラスが親クラスのメソッドを新しい内容で再定義する。
# D. 子クラスと親クラスが同名のメソッドを共有する。

# ＜解答＞
# C. 子クラスが親クラスのメソッドを新しい内容で再定義する。


# 問題7: super()関数の使用目的は何ですか？実行せずに答えてください。
# A. 親クラスのメソッドを子クラスから直接呼び出す。
# B. 子クラスのメソッドを親クラスから呼び出す。
# C. 複数の親クラスから継承する。
# D. クラス階層内で最上位の親クラスを呼び出す。

# ＜解答＞
# A. 親クラスのメソッドを子クラスから直接呼び出す。


# 問題8: Pythonで多重継承を行う場合、どのようにクラスを定義しますか？実行せずに答えてください。
# A. class DerivedClass(Base1, Base2):
# B. class DerivedClass inherits Base1 and Base2:
# C. class DerivedClass: inherit Base1, Base2
# D. class DerivedClass(Base1 + Base2):

# ＜解答＞
# A. class DerivedClass(Base1, Base2):


# 問題9: 以下のPythonコードの説明として最も適切なものはどれですか？実行せずに答えてください。
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
# A. Animalクラスは具体的なメソッドmake_soundを持つ通常のクラスです。
# B. Animalクラスはインスタンス化できる抽象クラスです。
# C. Animalクラスは、make_soundメソッドを実装しなければならない子クラスのための抽象クラスです。
# D. Animalクラスは、make_soundメソッドをオーバーライドせずに使用できるインターフェースです。

# ＜解答＞
# C. Animalクラスは、make_soundメソッドを実装しなければならない子クラスのための抽象クラスです。


# 問題10: 以下のPythonコードにおいて、'Bird'クラスのインスタンスを作成した際に正しく実行されるコンストラクタはどれですか？実行せずに答えてください。
class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly
# A. Animalクラスのコンストラクタのみが実行されます。
# B. Birdクラスのコンストラクタのみが実行されます。
# C. 最初にBirdクラスのコンストラクタが実行され、次にAnimalクラスのコンストラクタが実行されます。
# D. 最初にAnimalクラスのコンストラクタが実行され、次にBirdクラスのコンストラクタが実行されます。

# ＜解答＞
# D. 最初にAnimalクラスのコンストラクタが実行され、次にBirdクラスのコンストラクタが実行されます。


# 問題11: Pythonにおけるクラスの継承の主なメリットは何ですか？実行せずに答えてください。
# A. プログラムの実行速度を向上させる
# B. コードの再利用を促進し、冗長性を減らす
# C. データを自動的に暗号化する
# D. すべてのクラスメソッドを静的（スタティック）メソッドに変換する

# ＜解答＞
# B. コードの再利用を促進し、冗長性を減らす