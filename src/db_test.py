import sqlite3


def test_sqlite3_connection():
    with sqlite3.connect('uncommitted/warehouse.db') as con:
        cursor = con.cursor()

        cursor.execute('''
        DROP TABLE IF EXISTS staging_posts
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS staging_posts (
            Id text,
            PostTypeId text,
            AcceptedAnswerId text,
            CreationDate text,
            Score text,
            ViewCount text,
            Body text,
            AnswerCount text,
            CommentCount text,
            FavouriteCount text,
            ContentLicence text
        )
        ''')

        cursor.execute(
            "INSERT INTO staging_posts VALUES ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')")

        con.commit()

        assert list(cursor.execute('SELECT * FROM staging_posts')
                    ) == [('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')]
