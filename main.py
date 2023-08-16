from dotenv import load_dotenv
import smtplib
import os
load_dotenv()

text = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website% !
%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

> Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
> Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
> Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся > %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
text = text.replace("%friend_name%","Миша")
text = text.replace("%my_name%","Денис")
text = text.replace("%website%","http://polus101.ru/")
print(text)
x =os.getenv("LOGIN")

letter = f"""\
From: {x}
To: {x}
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";

{text}"""
password = os.getenv("PASSWORD")


letter = letter.encode("UTF-8")

print(letter)

server = smtplib.SMTP_SSL("smtp.yandex.ru:465")

server.login(x, password)
server.sendmail(x , x, letter )
server.quit()










