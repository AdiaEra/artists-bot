import psycopg2

with psycopg2.connect(user="postgres",
                      password="Hun$917&305TpS",
                      port="5432",
                      database="artists_db") as conn:
    def create_db():
        """
        Функция, создающая структуру БД (таблицы)
        :return: База данных создана
        """
        with conn.cursor() as cur:
            create_query = """ CREATE TABLE IF NOT EXISTS questionnaire(
                                user_id BIGINT PRIMARY KEY,
                                chat_id INTEGER NOT NULL,
                                user_name VARCHAR(30),
                                nickname VARCHAR(30) NOT NULL,
                                about VARCHAR(450) NOT NULL,
                                style VARCHAR(30) NOT NULL,
                                link_community TEXT NOT NULL,
                                soc_data VARCHAR(30) NOT NULL,
                                social_network VARCHAR(30),
                                subscribers INTEGER NOT NULL,
                                terms_partner TEXT,
                                picture TEXT NOT NULL
                                );"""
            cur.execute(create_query)
            return 'Таблица questionnaire создана'


    # print(create_db())
    conn.commit()


    def delete_db():
        """
        Функция, удаляющая таблицы базы данных
        :return: База данных удалена
        """
        with conn.cursor() as cur:
            delete_query = """DROP TABLE questionnaire"""
            cur.execute(delete_query)
            return 'Таблица questionnaire удалена'


    # print(delete_db())
    conn.commit()
