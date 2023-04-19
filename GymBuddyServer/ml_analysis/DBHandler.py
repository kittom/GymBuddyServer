import sqlite3


class DBHandler:
    def __init__(self, db_file):
        self.db_file = db_file

    def get_connection(self):
        return sqlite3.connect(self.db_file)

    def get_unchecked_exercises(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM Exercises WHERE quality = 'unchecked'"
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def get_specific_exercise(self, account_id, exercise_type, timestamp):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM Exercises WHERE account_id = ? AND exercise_type = ? AND datetime = ? AND quality = 'unchecked'"
            cursor.execute(query, (account_id, exercise_type, timestamp))
            result = cursor.fetchone()
        return result

class CSVHandler:
    def __init__(self, csv_file):
        self.csv_file = csv_file


def main():

    db_handler = DBHandler("db.sqlite3")
    unchecked_exercises = db_handler.get_unchecked_exercises()
    for exercise in unchecked_exercises:
        print(exercise)
        
if __name__ == "__main__":
    main()
