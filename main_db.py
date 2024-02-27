from pprint import pprint

import psycopg2.extras
from psycopg2.errors import UniqueViolation

from DB import conn


def add_artist(user_name: str, user_id: int, chat_id: int, nickname: str, about: str, style: str, link_community: str,
               soc_data: str, social_network: str, subscribers: int, terms_partner: str, picture: str):
    """
    Функция добавляет в таблицу анкет нового художника
    :param user_id: id художника
    :param chat_id: chat_id художника
    :param user_name: user_name художника
    :param nickname: имя или псевдоним художника
    :param about: информация художника о себе
    :param style: стиль, в котором работает художник
    :param link_community: ссылка на сообщество художника
    :param soc_data: как давно ведётся сообщество
    :param social_network: предпочтительная социальная сеть для продвижения
    :param subscribers: количество подписчиков
    :param terms_partner: условия партнёрства
    :param picture: ссылка на картину
    :return: 'Новый художник добавлен' или 'Художник с таким user_name уже есть в базе'
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_name FROM questionnaire WHERE user_name = %s""", (user_name,))
        cur.fetchone()
        if cur.fetchone() is None:
            try:
                cur.execute("""
                            INSERT INTO questionnaire (user_name, user_id, chat_id, nickname, about, style, link_community, 
                            soc_data, social_network, subscribers, terms_partner, picture)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                            (user_name, user_id, chat_id, nickname, about, style, link_community, soc_data,
                             social_network,
                             subscribers, terms_partner, picture))
            except UniqueViolation:
                return 'Художник с таким user_name уже есть в базе'
        return 'Новый художник добавлен'


us_id = 13333333333
user_chat_id = 4
us_name = 'Nina'
user_nick = 'Marcy'
user_about = 'крутой чел'
us_terms_partner = 'обмен опытом'
us_link = 'rfrve557858@##'
us_style = 'минимализм'
user_picture = 'rertr76878733dfg'
user_soc_network = 'instagramm'
user_subscribers = 1517
us_soc_data = 'больше 1 года'
# print(add_artist(us_name, us_id, user_chat_id, user_nick, user_about, us_style, us_link, us_soc_data, user_soc_network,
#                  user_subscribers, us_terms_partner, user_picture))
conn.commit()


def delete_artist(user_name: str):
    """
    Функция удаляет из таблицы акеты художника
    :param user_name: user_name художника
    :return: Художник удалён из базы данны
    """
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM questionnaire WHERE user_name = %s;""", (user_name,))
        return 'Художник удалён из базы данных'


us_name = 'Mina'
# print(delete_artist(us_name))
conn.commit()


def information_of_the_questionnaire(user_name: str):
    """
    Функция выводит список со словарём параматров: имя/псевдоним, стиль, картину, информацию о себе, социальную сеть, ссылку на сообщество,
    количество подписчиков, как давно ведётся сообщество, условия партнёрства
    :param user_name: user_name художника
    :return: список со словарём параметров: имя/псевдоним, стиль, картину, информацию о себе, социальную сеть, ссылку на сообщество,
    количество подписчиков, как давно ведётся сообщество, условия партнёрства
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""SELECT nickname, style, picture, about, style, link_community, social_network, subscribers, soc_data, terms_partner 
        FROM questionnaire WHERE user_name = %s""", (user_name,))
        res = cur.fetchall()
        res_list = [dict(row) for row in res]
        return res_list


us_name = 'Mina'


# print(information_of_the_questionnaire(us_name))


def update_nickname(nickname: str, user_name: str):
    """
    Функция обновления имени и фамилии или псевдонима художника
    :param nickname: имя и фамилия или псевдоним художника
    :param user_name: user_name художника
    :return: Nickname пользователя обновлён
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET nickname = %s WHERE user_name = %s""", (nickname, user_name))
        return 'Nickname пользователя обновлён'


us_name = 'Mina'
user_nick = 'Vova'
# print(update_nickname(user_nick, us_name))
conn.commit()


def update_about(about: str, user_name: str):
    """
    Функция обновления информации художника о себе
    :param about: информация художника о себе
    :param user_name: user_name художника
    :return: Информация пользователя о себе обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET about = %s WHERE user_name = %s""", (about, user_name))
        return 'Информация пользователя о себе обновлена'


us_name = 'Mina'
user_about = 'Какой есть'
# print(update_about(user_about, us_name))
conn.commit()


def update_style(style: str, user_name: str):
    """
    Функция обновления стиля художника
    :param style: стиль художника
    :param user_name: user_name художника
    :return: Стиль обновлён
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET style = %s WHERE user_name = %s""", (style, user_name))
        return 'Стиль обновлён'


us_name = 'Mina'
us_style = 'реализм'
# print(update_style(us_style, us_name))
conn.commit()


def update_link_community(link_community: str, user_name: str):
    """
    Функция обновления ссылки на сообщество художника
    :param link_community: ссылка на сообщество художника
    :param user_name: user_name художника
    :return: Ссылка на сообщество обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET link_community = %s WHERE user_name = %s""",
                    (link_community, user_name))
        return 'Ссылка на сообщество обновлена'


us_name = 'Mina'
us_link = '####tuynmiojo87865@@'
# print(update_link_community(us_link, us_name))
conn.commit()


def update_soc_da(soc_data: str, user_name: str):
    """
    Функция обновления времени ведения сообщества
    :param soc_data: как давно ведётся сообщество
    :param user_name: user_name художника
    :return: Информация о начале ведения сообщества обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET soc_data = %s WHERE user_name = %s""", (soc_data, user_name))
        return 'Информация о начале ведения сообщества обновлена'


us_name = 'Mina'
us_soc_data = 'менее 1 года'
# print(update_soc_da(us_soc_data, us_name))
conn.commit()


def update_social_network(social_network: str, user_name: str):
    """
    Функция обновления социальной сети для продвижения
    :param social_network: социальная сеть
    :param user_name: user_name художника
    :return: Социальная сеть обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET social_network = %s WHERE user_name = %s""",
                    (social_network, user_name))
        return 'Социальная сеть обновлена'


us_name = 'Colyan'
user_soc_network = 'VK+Inst+TG'
# print(update_social_network(user_soc_network, us_name))
conn.commit()


def update_subscribers(subscribers: int, user_name: str):
    """
    Функция обновления количества подписчиков
    :param subscribers: количество подписчиков
    :param user_name: user_name художника
    :return: Количество подписчиков обновлено
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET subscribers = %s WHERE user_name = %s""", (subscribers, user_name))
        return 'Количество подписчиков обновлено'


us_name = 'Mina'
user_subscribers = 1200
# print(update_subscribers(user_subscribers, us_name))
conn.commit()


def update_terms_partner(terms_partner: str, user_name: str):
    """
    Функция обновления условий партнёрства
    :param terms_partner: условия партнёрства
    :param user_name: user_name художника
    :return: Условия партнёрства обновлены
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET terms_partner = %s WHERE user_name = %s""", (terms_partner, user_name))
        return 'Условия партнёрства обновлены'


us_name = 'Mina'
us_terms_partner = 'Гии'
# print(update_terms_partner(us_terms_partner, us_name))
conn.commit()


def update_picture(picture: str, user_name: str):
    """
    Функция обновления ссылки на другую картину художника
    :param picture: ссылка на другую картину
    :param user_name: user_name художника
    :return: Ссылка на картину обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET picture = %s WHERE user_name = %s""", (picture, user_name))
        return 'Ссылка на картину обновлена'


us_name = 'Mina'
user_picture = 'ubuuy@@@##$$gfvgh hg'
# print(update_picture(user_picture, us_name))
conn.commit()


def serch(social_network: str, subscribers: int):
    """
    Функция поиска художников по параметрам социальной сети и количества подписчиков и вывода удовлетворяющих поиску кандидатов
    :param social_network: социальная сеть
    :param subscribers: количество подписчиков
    :return: список словарей с анкетами подходящих кандидатур
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            """SELECT user_name, nickname, style, picture, about, style, link_community, social_network, subscribers, soc_data, terms_partner FROM questionnaire WHERE social_network = %s AND subscribers BETWEEN (%s - 500) AND (%s + 500)""",
            (social_network, subscribers, subscribers))
        res = cur.fetchall()
        res_list = [dict(row) for row in res]
        return res_list


user_soc_network = 'VK'
user_subscribers = 1000


# print(serch(user_soc_network, user_subscribers))


def search_user(user_name: str):
    """
    Функция, которая проверяет по user_name есть ли такой пользователь в базе
    :param user_name: имя пользователя
    :return: имя пользователя либо None
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_name FROM questionnaire Where user_name = %s""", (user_name,))
        return cur.fetchone()


us_name = 'Mina'


# print(search_user(us_name))


def list_chat_id():
    """
    Функция выдаёт список chat_id пользователей
    :return: список chat_id пользователей
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT chat_id FROM questionnaire""")
        list_1 = [item for i in cur.fetchall() for item in i]
        return list_1


# print(list_chat_id())


def liked(user_name: str, liked_user: str):
    """
    Функция для записи пары (пользователь, выполняющий запрос-кандидат, который понравился) в таблицу user_liked
    :param user_name: пользователь, выполняющий запрос
    :param liked_user: кандидат, который понравился
    :return: Кандидат добавлен или Анкета этого кандидата уже просматривалась
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_name, liked_user FROM user_liked Where user_name = %s AND liked_user = %s""",
                    (user_name, liked_user))
        cur.fetchone()
        if cur.fetchone() is None:
            try:
                cur.execute("""
                       INSERT INTO user_liked(user_name, liked_user)
                       VALUES (%s, %s);""", (user_name, liked_user))
            except UniqueViolation:
                return 'Анкета этого кандидата уже просматривалась'
        return 'Кандидат добавлен'


us_name = 'Mina'
like_user = 'Sod'
# print(liked(us_name, like_user))
conn.commit()


def delete_user_liked(user_name):
    """
    Функция удаления по user_name художника и кандидатов, просмотренных им
    :param user_name: имя художника
    :return: Запись из табицы user_liked удалена
    """
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM user_liked WHERE user_name = %s;""", (user_name,))
        return 'Запись из табицы user_liked удалена'


us_name = 'Mina'
# print(delete_user_liked(us_name))
conn.commit()


def serch_by_soc_net():
    """
    Функция поиска художников по параметрам социальной сети и количества подписчиков и вывода удовлетворяющих поиску кандидатов
    :return: список словарей с анкетами подходящих кандидатур
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(f"""SELECT user_name, nickname, style, picture, about, style, link_community, social_network, subscribers, soc_data, terms_partner FROM questionnaire WHERE social_network ILIKE '%{data_order}%'""")
        res = cur.fetchall()
        res_list = [dict(row) for row in res]
        return res_list


data_order = 'Inst'

# pprint(serch_by_soc_net())
