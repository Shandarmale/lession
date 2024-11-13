class User:
    def __init__(self, nickname, hashpass, age):
        self.nickname = nickname
        self.hashpass = hashpass
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.video = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashpass = hash(password)
        for user in self.users:
            if (user.nickname == nickname) and (user.password == hashpass):
                self.current_user = user
            return True
        return False

    def register(self, nickname, password, age):
        hashpass = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        new_user = User(nickname, hashpass, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегестрирован")
        return

    def log_out(self):
        self.current_user = None
        print("Выход выполнен")

    def add(self, *args):
        for video in args:
            for v in self.video:
                if v.title == video.title:
                    print('Видео с таким же названием существует')
                    break
            else:
                self.video.append(video)
                print(f'Видео {video.title} добавлено')

    def get_videos(self, search_word):
        result = []
        for video in self.video:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        for video in self.video:
            if video.title == title:
                if video.adult_mode and (self.current_user is None or self.current_user.age < 18):
                    print("Ограничение по возрасту")
                    return
                for time_pos in range(video.duration):
                    video.time_now += 1
                    print(video.time_now, end='')
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')





