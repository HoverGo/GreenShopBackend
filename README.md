# Создание и запуск виртуального окружение
Виртуальное окружение будет содержать такую же версию python, которым оно было создано.

Linux:

```shell
python3 -m venv venv
source  venv/bin/activate
```

Windows:

```shell
python -m venv venv
venv\Scripts\activate
```

Выйти из виртуального окружения можно командой (Linux и Windows):

```shell
deactivate
```

Установка зависимостей:

```shell
pip install -r requirements.txt 
```
