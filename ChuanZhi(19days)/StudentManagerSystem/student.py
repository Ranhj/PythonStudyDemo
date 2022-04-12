class Student(object):
    def __init__(self, name, gender, tel):
        # 姓名、性别、手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'

# aa = Student('a', 'nan', 111)
# print(aa)