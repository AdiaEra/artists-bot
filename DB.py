import psycopg2


with psycopg2.connect(user="postgres",
                      password="",
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
                                chat_id BIGINT NOT NULL,
                                nickname VARCHAR(30) NOT NULL,
                                about VARCHAR(450) NOT NULL,
                                style VARCHAR(30) NOT NULL,
                                link_community TEXT NOT NULL,
                                terms_partner TEXT NOT NULL,
                                preferences TEXT NOT NULL
                                );
                                CREATE TABLE IF NOT EXISTS social_network(
                                user_id BIGINT REFERENCES questionnaire(user_id)
                                ON DELETE CASCADE,
                                social_network VARCHAR(20) NOT NULL,
                                subscribers VARCHAR(20) NOT NULL,
                                UNIQUE (user_id, social_network)
                                );
                                CREATE TABLE IF NOT EXISTS albums(
                                user_id BIGINT REFERENCES questionnaire(user_id)
                                ON DELETE CASCADE,
                                my_album TEXT NOT NULL,
                                UNIQUE (user_id, my_album)
                                )"""
            cur.execute(create_query)
            return 'База данных создана'


    # print(create_db())
    conn.commit()


    def delete_db():
        """
        Функция, удаляющая таблицы базы данных
        :return: База данных удалена
        """
        with conn.cursor() as cur:
            delete_query = """DROP TABLE albums;
                DROP TABLE social_network;
                DROP TABLE questionnaire
                CASCADE"""
            cur.execute(delete_query)
            return 'База данных удалена'


    # print(delete_db())
    conn.commit()
