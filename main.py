import json
from dotenv import load_dotenv
import smtplib
import os



load_dotenv()



with open('mails.json', 'r', encoding="CP1251") as my_file:
  file_contents = my_file.read()
mail_file_contents = json.loads(file_contents)


if __name__ == "__main__":
  password = os.getenv("PASSWORD")  
  friend_name="Миша"
  my_name="Денис"
  website_in_mail="http://polus101.ru/"

  text_in_mail = f"""Привет, {friend_name}! {my_name} приглашает тебя на сайт {website_in_mail} !
  {website_in_mail} — это новая версия онлайн-курса по программированию. 
  Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

  Как будет проходить ваше обучение на {website_in_mail}? 

  > Попрактикуешься на реальных кейсах. 
  Задачи от тимлидов со стажем от 10 лет в программировании.
  > Будешь учиться без стресса и бессонных ночей. 
  Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
  > Подготовишь крепкое резюме.
  Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

  Регистрируйся > {website_in_mail}
  На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

 
  mail_from=os.getenv("LOGIN")
 
  
  server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
  server.login(mail_from, password)
 
  for mail in mail_file_contents:
    mail_to= mail

    letter = f"""\
From: {mail_from}
To: {mail_to}
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";

{text_in_mail}"""
    letter = letter.encode("UTF-8")
    server.sendmail( mail_from, mail_to, letter )
server.quit()  












