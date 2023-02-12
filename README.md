# Likelion10-Django

:star: 멋쟁이 사자처럼 10기 백엔드 <br>
Django 추가 공부

<hr>

해당 파일을 다운로드 받은 후에, 가상환경 생성 뒤,
myproject > manage.py 에서 우클릭하여 터미널을 켭니다.
```
pip install django
```
django를 설치하고,
```
python manage.py runserver
```
를 통해 서버를 실행시키면 됩니다.

<hr>

## no such table 에러 해결 방법 2가지<br>

- 1번

```
python manage.py makemigrations
```

```
python manage.py migrate
```

- 2번
```
python manage.py migrate --run-syncdb
```



