import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.Connection(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute('Insert INTO `users` (`user_id`) VALUES (?)', (user_id,))

    def set_count(self, count):
        with self.connection:
            return self.cursor.execute('Insert INTO `all_datas` (`count`) VALUES (?)', (count,))

    def set_snils(self, count, snils):
        with self.connection:
            return self.cursor.execute('UPDATE `all_datas` SET `snils` = ? WHERE count = ?', (snils, count,))

    def set_balls(self, count, balls):
        with self.connection:
            return self.cursor.execute('UPDATE `all_datas` SET `balls` = ? WHERE count = ?', (balls, count,))

    def get_last_count(self):
        with self.connection:
            result = self.cursor.execute('SELECT `count` FROM all_datas').fetchall()
            return result[-1][-1]

    def get_snils(self, count):
        with self.connection:
            result = self.cursor.execute('SELECT `snils` FROM all_datas WHERE count = ?', (count,)).fetchone()
            return result[0]

    def get_balls(self, snils):
        with self.connection:
            result = self.cursor.execute('SELECT `balls` FROM all_datas WHERE snils = ?', (snils,)).fetchone()
            return result[0]

    def check_number(self, count):
        result = self.cursor.execute('SELECT `count` FROM all_datas WHERE count = ?', (count,)).fetchall()
        return bool(len(result))

    def most_main_check(self):
        with self.connection:
            result = self.cursor.execute("SELECT `balls` FROM all_datas WHERE snils = '173-327-323 57'").fetchone()
            if result is None:
                return False

            else:
                return True

    def get_data_with_snils(self, snils):
        with self.connection:
            result = self.cursor.execute('SELECT `count`, `balls` FROM all_datas WHERE snils = ?', (snils,)).fetchall()
            return result[0]

    def set_current_len(self, current_len):
        with self.connection:
            return self.cursor.execute('Insert INTO `users` (`current_len`) VALUES (?)', (current_len,))

    def get_current_len(self):
        with self.connection:
            result = self.cursor.execute('SELECT `current_len` FROM `users`').fetchone()
            return result[0]

    def delete_current_len(self, current_len):
        with self.connection:
            return self.cursor.execute('DELETE FROM `users` WHERE current_len = ?', (current_len,))


db = Database(db_file='data.db')