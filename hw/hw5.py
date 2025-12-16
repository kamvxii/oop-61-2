class User:
    class User:
        def __init__(self, username: str, role: str):
            self.username = username
            self.role = role

        def __str__(self):
            return f'{self.username} ({self.role})'

permissions = {
    "admin": ["start", "ban", "stop"],
    "user": ["start", "message"]}

def check_permissions(command):
    def decorator(func):
        def wrapper(self, user):
            if command in permissions[user.role]:
                print(f' {user.username} ({user.role}) выполняет {command}')
                func(self, user)
            else:
                print(f' {user.username} не может выполнять команду "{command}"')
        return wrapper
    return decorator
class CommandHandler:
    @staticmethod
    def get_commands():
        return {'start', 'ban', 'stop', 'message'}

    @classmethod
    def show_roles(cls):
        print('Доступные роли и команды:')
        for role, commands in permissions.items():
            print(f' - {role}: {commands}')
        print()

    @classmethod
    def start(self, user):
        print(' Система запущена')

    @staticmethod
    def ban(self, user):
        print(' Пользователь заблокирован')

    @staticmethod
    def stop(self, user):
        print('Система остановлена')

    @staticmethod
    def message(self, user):
        print(f'Пользователь {user.username} отправил сообщение')

admin = User('Alice', 'admin')

user = User('Bob',  'user')




#task2
class Student:
    count=0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count+=1
        Student.total_gpa+=gpa
    def get_info(self):
        return f'{self.name} {self.gpa}'
    @classmethod
    def get_count(cls):
        return f'{cls.count} Общее gpa'
    @classmethod
    def average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return Student.total_gpa/cls.count
student = Student('kamila',4.0)
student2 = Student('Iskender',2.0)
print(Student.get_count())
print(Student.get_average_gpa())



