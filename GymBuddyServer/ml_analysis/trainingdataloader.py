from Exercise import Exercise
# from FeatureLoader import get_features
# from Normalizer import normaliseValues


training_data = [
    [Exercise((1,
              "squat",
              None,
              None,
              "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_1.csv",
               "bad",
               None,
               )), 0],

    [Exercise((2,
              "squat",
              None,
              None,
              "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_2.csv",
               "bad",
               None,
               )), 0],

    [Exercise((3,
              "squat",
              None,
              None,
              "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_1.csv",
               "good",
               None,
               )), 1],

    [Exercise((4,
              "squat",
              None,
              None,
              "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_2.csv",
               "good",
               None,
               )), 1],
    [Exercise((5,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_3.csv",
            "good",
            None,
            )), 1],
    [Exercise((6,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_4.csv",
            "good",
            None,
            )), 1],
    [Exercise((7,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_3.csv",
            "bad",
            None,
            )), 0],
    [Exercise((8,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_4.csv",
            "bad",
            None,
            )), 0],
    [Exercise((9,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_5.csv",
            "bad",
            None,
            )), 0],
    [Exercise((10,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_6.csv",
            "bad",
            None,
            )), 0],
    [Exercise((11,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_7.csv",
            "bad",
            None,
            )), 0],
    [Exercise((12,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_8.csv",
            "bad",
            None,
            )), 0],
    [Exercise((13,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_9.csv",
            "bad",
            None,
            )), 0],
    [Exercise((14,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_10.csv",
            "bad",
            None,
            )), 0],
    [Exercise((15,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/bad_squat_11.csv",
            "bad",
            None,
            )), 0],
    [Exercise((16,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_5.csv",
            "good",
            None,
            )), 1],
    [Exercise((17,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_6.csv",
            "good",
            None,
            )), 1],
    [Exercise((18,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_7.csv",
            "good",
            None,
            )), 1],
    [Exercise((19,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_8.csv",
            "good",
            None,
            )), 1],
    [Exercise((20,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_9.csv",
            "good",
            None,
            )), 1],
            # Removed due to incomplete data
    [Exercise((21,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_10.csv",
            "good",
            None,
            )), 1],
    [Exercise((22,
            "squat",
            None,
            None,
            "/Users/morgankitto/Desktop/GymBuddyBackup/GymBuddyServer/GymBuddyServer/ml_analysis/training_data/csvs/good_squat_11.csv",
            "good",
            None,
            )), 1],
 
]

def main():
    # print(f"id : {exercise.id}")
    # normaliseValues(exercise)
    # norm_path = i[0].normalised_values
    # feature_values = get_features()
    # features = training_data[2][0]
    # val = training_data[2][0]
    # get_features(training_data[2][0].normalised_values[7], training_data[2][0].type)
    # print(norm_path)
    pass

if __name__ == "__main__":
    main()


