class User:
    """
    A class representing a system user.

    Attributes:
        id (int): Unique user identifier.
        nick (str): User's nickname/login.
        first (str): User's first name.
        last (str): User's last name.
        middle (str): User's middle name.
        gender (str): User's gender.
        name (str): Full name (last, first, middle joined).
    """

    def __init__(self, id, nick_name, first_name, last_name='', middle_name='', gender=''):
        """
        Initialize a User object.

        Args:
            id (int): Unique user identifier.
            nick_name (str): User's nickname/login.
            first_name (str): User's first name.
            last_name (str, optional): User's last name. Defaults to ''.
            middle_name (str, optional): User's middle name. Defaults to ''.
            gender (str, optional): User's gender. Defaults to ''.
        """
        self.id = id
        self.nick = nick_name
        self.first = first_name
        self.last = last_name
        self.middle = middle_name
        self.gender = gender
        name = [self.last, self.first, self.middle]
        self.name = ' '.join(part for part in name if part)

    def __str__(self):
        """
        Return a formatted string representation of the user.

        Returns:
            str: Formatted string with ID, login, name, and gender.
        """
        info_dict = {self.id: 'ID',
                     self.nick: 'LOGIN',
                     self.name: 'NAME',
                     self.gender: 'GENDER'
                     }
        return ' '.join(f'{value}: {key}'
                        for key, value in info_dict.items() if key)

    def __repr__(self):
        """
        Return an unambiguous string representation of the user.

        Returns:
            str: The user's nickname.
        """
        return self.nick

    def update(self, id1=0, nick1='', first1='', last1='', middle1='', gender1=''):
        """
        Update user attributes with non-empty values.

        Args:
            id1 (int, optional): New user ID. Defaults to 0.
            nick1 (str, optional): New nickname. Defaults to ''.
            first1 (str, optional): New first name. Defaults to ''.
            last1 (str, optional): New last name. Defaults to ''.
            middle1 (str, optional): New middle name. Defaults to ''.
            gender1 (str, optional): New gender. Defaults to ''.
        """
        if id1:
            self.id = id1
        if nick1:
            self.nick = nick1
        if first1:
            self.first = first1
        if last1:
            self.last = last1
        if middle1:
            self.middle = middle1
        if gender1:
            self.gender = gender1


user_1 = User(12, 'alex', 'Алексей')
print(user_1)
user_2 = User(44, 'andru', 'Андрей', 'Петров')
print(user_2)
user_3 = User(25, 'nik', 'Николай', 'Иванов', 'Федорович')
print(user_3)
user_4 = User(61, 'ivan', 'Денис', 'Сидоров', 'Алексеевич', 'M')
print(user_4)
user_5 = User(47, 'ann', 'Анна', gender='F')
print(user_5)
user_4.update(0, '', 'Ваня')
print(user_4)
user_3.update(15, '', 'Никита', '', 'Петрович')
print(user_3)
users = [user_2, user_4, user_5, user_1, user_3]
print(users)


