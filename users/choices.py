
class UserRole:
    ADMIN = 'admin'
    DEVELOPER = 'developer'

    ITEMS = [
        ADMIN,
        DEVELOPER,
    ]

    CHOICES = (
        (ADMIN, 'Администратор портала'),
        (DEVELOPER, 'Разработчик'),
    )
