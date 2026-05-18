# MySite

Небольшой учебный проект на Django.

В проекте есть главная страница, страница "О нас", приложение со статьями и простая система регистрации/входа.

## Что есть в проекте

- `mysite` - основной проект Django.
- `articles` - приложение со статьями.
- `accounts` - приложение для регистрации, входа и выхода пользователя.
- `static/css/style.css` - общий файл стилей.
- `media/images/` - загруженные картинки для статей.

## Страницы сайта

- `/` - главная страница.
- `/about/` - страница о сайте.
- `/articles/` - список статей.
- `/articles/<slug>` - отдельная статья.
- `/accounts/signup/` - регистрация.
- `/accounts/login/` - вход.
- `/accounts/logout/` - выход.
- `/admin/` - админ-панель Django.

## Модель Article

В приложении `articles` есть модель статьи:

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True)
```

У статьи есть заголовок, slug для ссылки, текст, дата создания и необязательная картинка.

## Как запустить проект

Перейти в папку проекта:

```bash
cd /Users/ivan/Desktop/web_firstLab/mysite
```

Активировать виртуальное окружение:

```bash
source /Users/ivan/Desktop/web_firstLab/.venv/bin/activate
```

Проверить проект:

```bash
python manage.py check
```

Применить миграции, если нужно:

```bash
python manage.py migrate
```

Запустить сервер:

```bash
python manage.py runserver
```

После запуска сайт будет доступен по адресу:

```text
http://127.0.0.1:8000/
```

## Static и Media

Static-файлы используются для CSS:

```text
static/css/style.css
```

Media-файлы используются для загруженных изображений статей:

```text
media/images/
```

В `settings.py` для этого настроены:

```python
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## Авторизация

В приложении `accounts` используются стандартные формы Django:

- `UserCreationForm` для регистрации;
- `AuthenticationForm` для входа;
- `logout` для выхода.

После регистрации или входа пользователь перенаправляется на страницу со статьями.
