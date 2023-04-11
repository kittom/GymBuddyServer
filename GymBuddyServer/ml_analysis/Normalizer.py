import numpy as np
from Exercise import Exercise
from DBHandler import DBHandler


db_handler = DBHandler("db.sqlite3")
unchecked_exercises = db_handler.get_unchecked_exercises()
exercise = Exercise(unchecked_exercises[0])

# DO NOT TOUCH
#############################################################

# calculate Euclidian distances rel torso = 1
# get keypoints for hips
# get keypoints for shoulders
# find the halfway points for both
# calculate euclidean distance

# 
for row in range(0, len(exercise.dataframe)):
    hips = [(exercise.dataframe._get_value(row, "keypoint 24 x") + exercise.dataframe._get_value(row, "keypoint 23 x")) / 2,
                    (exercise.dataframe._get_value(row, "keypoint 24 y") + exercise.dataframe._get_value(row, "keypoint 23 y")) / 2]
    shoulders = [(exercise.dataframe._get_value(row, "keypoint 12 x") + exercise.dataframe._get_value(row, "keypoint 11 x")) / 2,
                    (exercise.dataframe._get_value(row, "keypoint 12 y") + exercise.dataframe._get_value(row, "keypoint 11 y")) / 2]
    torso = np.sqrt((hips[0] - shoulders[0])**2 + (hips[1] - shoulders[1])**2)
    print(f"{row} : {torso}")

# Still need to be done: 
# _____________________
#  - divide all keypoint values in csv by euclidean distance
#  - write to new csv in same filepath.
#  - turn everything into an object

def main():
    pass

if __name__ == "__main__":
    main()