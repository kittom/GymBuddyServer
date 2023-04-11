import pandas as pd
from DBHandler import DBHandler

class Exercise:
    def __init__(self, data):
        if len(data) != 7:
            raise ValueError("Input tuple must have a length of 7.")

        self.id = data[0]
        self.exercise_type = data[1]
        self.csv_file_path = f"{data[4]}"
        self.dataframe = self.read_csv()

    def read_csv(self):
        return pd.read_csv(self.csv_file_path)

def main():
    db_handler = DBHandler("db.sqlite3")
    unchecked_exercises = db_handler.get_unchecked_exercises()
    exercise = Exercise(unchecked_exercises[0])
    print(exercise.id)
    print(exercise.dataframe)  # Print the DataFrame

if __name__ == "__main__":
    main()