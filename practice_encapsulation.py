# 問題1: 以下のCircleクラスに対して、radius属性をプライベートに変更し、その値を設定・取得するためのメソッドを追加してください。class Circle:
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, value):
        self.__radius = value

# テスト
circle1 = Circle(4)

print(circle1.get_radius())
circle1.set_radius(5)
print(circle1.get_radius())


# 問題2: Personクラスにage属性をプライベートとして追加し、年齢を1歳増やすメソッドbirthday()を実装してください。
class Person:
    def __init__(self, name, age):
        self.name = name
        # ageをプライベート属性として追加
        self.__age = age

    def birthday(self):
        self.__age += 1

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('ageは正数で指定してください。')
        self.__age = value

# テスト
person1 = Person('山田太郎', 20)
print(person1.age)
person1.birthday()
print(person1.age)


# 問題3: Bookクラスにタイトルと著者をプライベート属性として追加し、これらの属性に対するゲッターメソッドを実装してください。
class Book:
    def __init__(self, title, author):
        # タイトルと著者をプライベート属性として設定
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author

# テスト
book1 = Book('リゼロ', '長月達平')
# print(book1.title) →　エラー
print(book1.get_title())
print(book1.get_author())


# 問題4:Studentクラスにプライベート属性__grades（リスト）を追加し、成績を追加するメソッドと、平均成績を取得するメソッドを実装してください。
class Student:
    def __init__(self, name, grades):
        self.name = name
        # __grades属性とメソッドを追加
        self.__grades = grades
    
    def add_grades(self, value):
        self.__grades.append(value)

    def get_avg_grade(self):
        return (sum(self.__grades) / len(self.__grades))

# テスト
student1 = Student('山田太郎',[70, 69, 90])
student1.add_grades(80)
# print(student1.__grades)　→　エラー
print(student1.get_avg_grade())


# 問題5: Rectangleクラスに幅と高さをプライベート属性として設定し、面積を計算するメソッドを実装してください。また、幅と高さの値を変更するためのセッターメソッドも追加してください。
class Rectangle:
    def __init__(self, width, height):
        # 幅と高さをプライベート属性として設定
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError('ageは正数で指定してください。')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('ageは正数で指定してください。')
        self.__height = value

# テスト
rectangle1 = Rectangle(4, 5)
print(rectangle1.calculate_area())
rectangle1.width = 6
rectangle1.height = 7
print(rectangle1.calculate_area())


# 問題6: Accountクラスにプライベート属性__balance（残高）と__passwordを追加し、残高を確認するためのメソッドget_balance(password)を実装してください。正しいパスワードが提供された場合のみ残高を返し、そうでない場合はエラーメッセージを表示してください。
class Account:
    def __init__(self, password, balance):
        # __balanceと__passwordをプライベート属性として設定
        self.__password = password
        self.__balance = balance
    
    def get_balance(self, passsword):
        if passsword == self.__password:
            return self.__balance
        else:
            return 'ログインに失敗しました。パスワードが間違っています。'

# テスト
account1 = Account(123456, 200000)
print(account1.get_balance(123456))
print(account1.get_balance(193857))


# 問題7: カプセル化にはいくつかのメリットがありますが、その中で最も重要なものはどれでしょうか？実行せずに答えてください。
# A. コードの実行速度を向上させることができる
# B. コードの可読性を下げることにより、セキュリティを強化できる
# C. オブジェクトの内部状態を隠蔽し、外部から直接アクセスを制限することで、データの不正な変更を防ぐことができる
# D. クラスのインスタンス化を自動化することができる

# ＜解答＞
# C. オブジェクトの内部状態を隠蔽し、外部から直接アクセスを制限することで、データの不正な変更を防ぐことができる


# 問題8: Pythonにおいて、カプセル化を実現するためにクラス内の属性をどのように宣言すべきですか？実行せずに答えてください。
# A. 公開属性として宣言し、外部から直接アクセスさせる
# B. 属性名を大文字で始めることでプライベートとする
# C. 先頭に二重アンダースコア ('__') を付けてプライベート属性とする
# D. 先頭に単一のアンダースコア ('_') を付けてプライベート属性とする

# ＜解答＞
# C. 先頭に二重アンダースコア ('__') を付けてプライベート属性とする


# 問題9: カプセル化の目的は何ですか？実行せずに答えてください。
# A. クラスのメソッドを隠し、外部からのアクセスを完全に禁止すること
# B. クラスの実装詳細を隠蔽し、外部からの直接アクセスを制限すること
# C. クラスのコードを短縮し、読みやすくすること
# D. クラスの属性とメソッドを公開し、外部から自由にアクセスできるようにすること

# ＜解答＞
# B. クラスの実装詳細を隠蔽し、外部からの直接アクセスを制限すること


# 問題10: プロパティデコレータ ('@property') の使用目的は何ですか？実行せずに答えてください。
# A. クラスのメソッドを静的（スタティック）メソッドに変換するため
# B. クラスのメソッドをクラスメソッドに変換するため
# C. クラスの属性へのアクセスを制御し、ゲッターとセッターメソッドを定義するため
# D. クラスのすべての属性をプライベートにするため

# ＜解答＞
# C. クラスの属性へのアクセスを制御し、ゲッターとセッターメソッドを定義するため