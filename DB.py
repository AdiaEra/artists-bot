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
                                    user_name VARCHAR(30) PRIMARY KEY,
                                    user_id BIGINT NOT NULL,
                                    chat_id BIGINT NOT NULL,
                                    nickname VARCHAR(30) NOT NULL,
                                    about VARCHAR(450) NOT NULL,
                                    style VARCHAR(30) NOT NULL,
                                    link_community TEXT NOT NULL,
                                    soc_data VARCHAR(30) NOT NULL,
                                    social_network VARCHAR(30),
                                    subscribers INTEGER NOT NULL,
                                    terms_partner TEXT,
                                    picture TEXT NOT NULL
                                );
                                CREATE TABLE IF NOT EXISTS user_liked(
                                    user_name VARCHAR(30) REFERENCES questionnaire(user_name)
                                    ON DELETE CASCADE,
                                    liked_user VARCHAR(40) NOT NULL,
                                    UNIQUE (user_name, liked_user)
                                );"""
            cur.execute(create_query)
            return 'Таблицы questionnaire and user_liked созданы'


    # print(create_db())
    conn.commit()


    def delete_db():
        """
        Функция, удаляющая таблицы базы данных
        :return: База данных удалена
        """
        with conn.cursor() as cur:
            delete_query = """DROP TABLE user_liked;                                      
                            DROP TABLE questionnaire
                            CASCADE;"""
            cur.execute(delete_query)
            return 'Таблица questionnaire удалена'


    # print(delete_db())
    conn.commit()


    def add_column():
        """
        Функция добавляет столбец subscription_days в таблицу questionnaire
        :return: Столбец subscription_days добавлен
        """
        with conn.cursor() as cur:
            cur.execute("""ALTER TABLE questionnaire ADD COLUMN subscription_days INTEGER""")
            return 'Столбец subscription_days добавлен'


    # print(add_column())
    conn.commit()
