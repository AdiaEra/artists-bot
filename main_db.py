import psycopg2.extras
from psycopg2.errors import UniqueViolation

from DB import conn


def add_artist(user_id: int, chat_id: int, nickname: str, about: str, style: str, link_community: str,
               terms_partner: str, preferences: str):
    """
    Функция добавляет в таблицу анкет нового художника
    :param user_id: id художника
    :param chat_id: chat_id художника
    :param nickname: имя или псевдоним художника
    :param about: о себе
    :param style: стиль
    :param link_community: ссылка на сообщество
    :param terms_partner: условия партнёрства
    :param preferences: предпочтительная социальная сеть и количество подписчиков
    :return: 'Новый художник добавлен' или 'Художник с таким user_id уже есть в базе'
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_id FROM questionnaire WHERE user_id = %s""", (user_id,))
        cur.fetchone()
        if cur.fetchone() is None:
            try:
                cur.execute("""
                            INSERT INTO questionnaire (user_id, chat_id, nickname, about, style, link_community, terms_partner, preferences)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
                            (user_id, chat_id, nickname, about, style, link_community, terms_partner, preferences))
            except UniqueViolation:
                return 'Художник с таким user_id уже есть в базе'
        return 'Новый художник добавлен'


us_id = 22222222222222
user_chat_id = 1
user_nick = 'Army'
user_about = 'крутой чел'
us_terms_partner = 'обмен опытом'
us_preferences = 'VK, 500'
us_link = 'rfrve557858@##'
us_style = 'минимализм'
# print(add_artist(us_id, user_chat_id, user_nick, user_about, us_style, us_link, us_terms_partner, us_preferences))
conn.commit()


def add_picture(user_id: int, my_album: str):
    """
    Функция добавления ссылки на картину по id художника
    :param user_id: id художника
    :param my_album: ссылка на картину
    :return: 'Ссылка на картину данного художника добавлена' или 'Така работа у данного художника уже существует в базе'
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_id, my_album FROM albums WHERE user_id = %s AND my_album = %s""",
                    (user_id, my_album))
        cur.fetchone()
        if cur.fetchone() is None:
            try:
                cur.execute("""INSERT INTO albums(user_id, my_album)
                               VALUES (%s, %s);""", (user_id, my_album))
            except UniqueViolation:
                return 'Такая работа у данного художника уже существует в базе'
        return 'Ссылка на картину данного художника добавлена'


us_id = 111111111111
user_picture = 'dvd@@niubku7t'
# user_picture = 'rertr76878733dfg'
print(add_picture(us_id, user_picture))
conn.commit()


def list_pictures(user_id: int):
    """
    Функция выводит список картин конкретного художника
    :param user_id: id художника
    :return: список картин
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT my_album FROM albums WHERE user_id = %s""", (user_id,))
        list_1 = [item for i in cur.fetchall() for item in i]
        return list_1


us_id = 111111111111


# print(list_pictures(us_id))


def add_social_network(user_id: int, social_network: str, subscribers: str):
    """
    Функция добавляет социальную сеть и количество подписчиков
    :param user_id: id художника
    :param social_network: социальная сеть
    :param subscribers: количество подписчиков
    :return:
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_id, social_network FROM social_network WHERE user_id = %s AND social_network = %s""",
                    (user_id, social_network))
        cur.fetchone()
        if cur.fetchone() is None:
            try:
                cur.execute("""INSERT INTO social_network(user_id, social_network, subscribers)
                               VALUES (%s, %s, %s);""", (user_id, social_network, subscribers))

            except UniqueViolation:
                return 'Такая соц сеть у данного художника уже существует в базе'
        return 'Социальная сеть и количество подписчиков добавлены'


us_id = 111111111111
user_soc_network = 'instagramm'  # Импрессионизм
user_subscribers = '1000 - 1500'
# print(add_social_network(us_id, user_soc_network, user_subscribers))
conn.commit()


def delete_artist(user_id: int):
    """
    Функция удаления художника из базы данных
    :param user_id: id художника
    :return: 'Художник удалён из базы данных'
    """
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM questionnaire WHERE user_id = %s;""", (user_id,))
        return 'Художник удалён из базы данных'


us_id = 3534543
# print(delete_artist(us_id))
conn.commit()


def information_of_the_questionnaire(user_id: int):
    """
    Функция выводит список со словарём параматров: имя/псевдоним, стиль, информацию о себе, социальную сеть, ссылку на сообщество,
    количество подписчиков, условия партнёрства
    :param user_id:id художника
    :return: список со словарём параметров: имя/псевдоним, стиль, информацию о себе, социальную сеть, ссылку на сообщество,
    количество подписчиков, условия партнёрства
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""SELECT nickname, style, about, about, style, link_community, social_network, subscribers, terms_partner 
        FROM questionnaire AS q
        JOIN albums AS a ON q.user_id = a.user_id
        JOIN social_network AS sn ON a.user_id = sn.user_id 
        WHERE q.user_id = %s""", (user_id,))
        res = cur.fetchall()
        res_list = [dict(row) for row in res]
        return res_list


us_id = 111111111111
# print(information_of_the_questionnaire(us_id))




# def add_style(user_id: int, style: str):
#     """
#     Функция добавления определённого стиля по id художника
#     :param user_id: id художника
#     :param style: стиль
#     :return: 'Стиль добавлен' или 'Такой стиль у данного художника уже существует в базе'
#     """
#     with conn.cursor() as cur:
#         cur.execute("""SELECT user_id, style FROM styles WHERE user_id = %s AND style = %s""",
#                     (user_id, style))
#         cur.fetchone()
#         if cur.fetchone() is None:
#             try:
#                 cur.execute("""INSERT INTO styles(user_id, style)
#                                VALUES (%s, %s);""", (user_id, style))
#
#             except UniqueViolation:
#                 return 'Такой стиль у данного художника уже существует в базе'
#         return 'Стиль добавлен'
#
#
# us_id = 111111111111
# user_style = 'Ммнимализм'  # Импрессионизм
# # print(add_style(us_id, user_style))
# conn.commit()
