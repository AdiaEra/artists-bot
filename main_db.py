import psycopg2.extras
from psycopg2.errors import UniqueViolation

from DB import conn


def add_artist(user_id: int, chat_id: int, user_name: str, nickname: str, about: str, style: str, link_community: str,
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
    :return: 'Новый художник добавлен' или 'Художник с таким user_id уже есть в базе'
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_id FROM questionnaire WHERE user_id = %s""", (user_id,))
        cur.fetchone()
        if cur.fetchone() is None:
            try:
                cur.execute("""
                            INSERT INTO questionnaire (user_id, chat_id, user_name, nickname, about, style, link_community, 
                            soc_data, social_network, subscribers, terms_partner, picture)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                            (user_id, chat_id, user_name, nickname, about, style, link_community, soc_data,
                             social_network,
                             subscribers, terms_partner, picture))
            except UniqueViolation:
                return 'Художник с таким user_id или nickname уже есть в базе'
        return 'Новый художник добавлен'


us_id = 3333333333333
user_chat_id = 4
us_name = 'Marc'
user_nick = 'Marcy'
user_about = 'крутой чел'
us_terms_partner = 'обмен опытом'
us_link = 'rfrve557858@##'
us_style = 'минимализм'
user_picture = 'rertr76878733dfg'
user_soc_network = 'instagramm'
user_subscribers = 345
us_soc_data = 'больше 1 года'
# print(add_artist(us_id, user_chat_id, us_name, user_nick, user_about, us_style, us_link, us_soc_data, user_soc_network,
#                  user_subscribers, us_terms_partner, user_picture))
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
    :param user_id: id художника
    :return: список со словарём параметров: имя/псевдоним, стиль, информацию о себе, социальную сеть, ссылку на сообщество,
    количество подписчиков, условия партнёрства
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""SELECT nickname, style, about, about, style, link_community, social_network, subscribers, terms_partner 
        FROM questionnaire WHERE user_id = %s""", (user_id,))
        res = cur.fetchall()
        res_list = [dict(row) for row in res]
        return res_list


us_id = 22222222222222


# print(information_of_the_questionnaire(us_id))


def update_nickname(nickname: str, user_id: int):
    """
    Функция обновления имени и фамилии или псевдонима художника
    :param nickname: имя и фамилия или псевдоним художника
    :param user_id: id художника
    :return: Nickname пользователя обновлён
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET nickname = %s WHERE user_id = %s""", (nickname, user_id,))
        return 'Nickname пользователя обновлён'


us_id = 2222111133
user_nick = 'Vova'
# print(update_nickname(user_nick, us_id))
conn.commit()


def update_about(about: str, user_id: int):
    """
    Функция обновления информации художника о себе
    :param about: информация художника о себе
    :param user_id: id художника
    :return: Информация пользователя о себе обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET about = %s WHERE user_id = %s""", (about, user_id,))
        return 'Информация пользователя о себе обновлена'


us_id = 2222111133
user_about = 'Какой есть'
# print(update_about(user_about, us_id))
conn.commit()


def update_style(style: str, user_id: int):
    """
    Функция обновления стиля художника
    :param style: стиль художника
    :param user_id: id художника
    :return: Стиль обновлён
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET style = %s WHERE user_id = %s""", (style, user_id,))
        return 'Стиль обновлён'


us_id = 2222111133
us_style = 'реализм'
# print(update_style(us_style, us_id))
conn.commit()


def update_link_community(link_community: str, user_id: int):
    """
    Функция обновления ссылки на сообщество художника
    :param link_community: ссылка на сообщество художника
    :param user_id: id художника
    :return: Ссылка на сообщество обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET link_community = %s WHERE user_id = %s""", (link_community, user_id,))
        return 'Ссылка на сообщество обновлена'


us_id = 2222111133
us_link = '####tuynmiojo87865@@'
# print(update_link_community(us_link, us_id))
conn.commit()


def update_soc_da(soc_data: str, user_id: int):
    """
    Функция обновления времени ведения сообщества
    :param soc_data: как давно ведётся сообщество
    :param user_id: id художника
    :return: Информация о начале ведения сообщества обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET soc_data = %s WHERE user_id = %s""", (soc_data, user_id,))
        return 'Информация о начале ведения сообщества обновлена'


us_id = 2222111133
us_soc_data = 'менее 1 года'
# print(update_soc_da(us_soc_data, us_id))
conn.commit()


def update_social_network(social_network: str, user_id: int):
    """
    Функция обновления социальной сети для продвижения
    :param social_network: социальная сеть
    :param user_id: id художника
    :return: Социальная сеть обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET social_network = %s WHERE user_id = %s""", (social_network, user_id,))
        return 'Социальная сеть обновлена'


us_id = 2222111133
user_soc_network = 'ВКонтакте'
# print(update_social_network(user_soc_network, us_id))
conn.commit()


def update_subscribers(subscribers: int, user_id: int):
    """
    Функция обновления количества подписчиков
    :param subscribers: количество подписчиков
    :param user_id: id художника
    :return: Количество подписчиков обновлено
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET subscribers = %s WHERE user_id = %s""", (subscribers, user_id,))
        return 'Количество подписчиков обновлено'


us_id = 2222111133
user_subscribers = 315
# print(update_subscribers(user_subscribers, us_id))
conn.commit()


def update_terms_partner(terms_partner: str, user_id: int):
    """
    Функция обновления условий партнёрства
    :param terms_partner: условия партнёрства
    :param user_id: id художника
    :return: Условия партнёрства обновлены
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET terms_partner = %s WHERE user_id = %s""", (terms_partner, user_id,))
        return 'Условия партнёрства обновлены'


us_id = 2222111133
us_terms_partner = 'Гии'
# print(update_terms_partner(us_terms_partner, us_id))
conn.commit()


def update_picture(picture: str, user_id: int):
    """
    Функция обновления ссылки на другую картину художника
    :param picture: ссылка на другую картину
    :param user_id: id художника
    :return: Ссылка на картину обновлена
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE questionnaire SET picture = %s WHERE user_id = %s""", (picture, user_id,))
        return 'Ссылка на картину обновлена'


us_id = 2222111133
user_picture = 'ubuuy@@@##$$gfvgh hg'
# print(update_picture(user_picture, us_id))
conn.commit()
