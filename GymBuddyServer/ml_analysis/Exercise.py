import pandas as pd
from DBHandler import DBHandler
import numpy as np
from prepare_training_data import uniform_sampling




    

class Exercise:
    def __init__(self, data):
        if len(data) != 7:
            raise ValueError("Input tuple must have a length of 7.")

        self.id = data[0]
        self.type = data[1]
        self.csv_file_path = f"{data[4]}"
        self.quality = data[5]
        self.dataframe = self.read_csv()
        self.normalised_values = self.normalise()
        self.features = self.get_features()

    def read_csv(self):
        return pd.read_csv(self.csv_file_path)
    
    def normalise(self):
        normalized_rows = []
        
        for row in range(0, len(self.dataframe)):
            hips = [(self.dataframe._get_value(row, "keypoint 24 x") + self.dataframe._get_value(row, "keypoint 23 x")) / 2,
                            (self.dataframe._get_value(row, "keypoint 24 y") + self.dataframe._get_value(row, "keypoint 23 y")) / 2]
            shoulders = [(self.dataframe._get_value(row, "keypoint 12 x") + self.dataframe._get_value(row, "keypoint 11 x")) / 2,
                            (self.dataframe._get_value(row, "keypoint 12 y") + self.dataframe._get_value(row, "keypoint 11 y")) / 2]
            torso = np.sqrt((hips[0] - shoulders[0])**2 + (hips[1] - shoulders[1])**2)
            frame_Keypoints = self.dataframe.iloc[row]
            frame_Values = []
            
            for i in frame_Keypoints[1:-2]:
                frame_Values.append(i / torso)
            
            normalized_rows.append(frame_Values)
        
        normalized_df = pd.DataFrame(normalized_rows, columns=self.dataframe.columns[1:-2])
        normalized_csv_path = self.csv_file_path.replace(".csv", "_normalized.csv")
        normalized_df.to_csv(normalized_csv_path, index=False)
        array = normalized_df.to_numpy()
        # Reshape the array
        num_keypoints = 32
        reshaped_array = array.reshape(-1, num_keypoints, 2)
        return reshaped_array
    
    def get_features(self):
        return uniform_sampling(self.normalised_values, 5, self.type)

    

def main():
    db_handler = DBHandler("../db.sqlite3")
    unchecked_exercises = db_handler.get_unchecked_exercises()
    exercise = Exercise(unchecked_exercises[0])

    # print(exercise.dataframe) # Print the DataFrame

if __name__ == "__main__":
    main()