import numpy as np

def get_distance(kp1, kp2):
    return np.sqrt(((kp1[0] - kp2[0])**2) + ((kp1[1] - kp2[1])**2))

def get_angle(a, b, c):
    # Calculate vectors BA and BC
    ba = a - b
    bc = c - b

    # Calculate the dot product of BA and BC
    dot_product = np.dot(ba, bc)


    # Calculate the magnitudes of BA and BC
    ba_magnitude = np.linalg.norm(ba)
    bc_magnitude = np.linalg.norm(bc)


    # Calculate the cosine of angle ABC
    cosine_angle = dot_product / (ba_magnitude * bc_magnitude)

    # Make sure the cosine value is in the valid range
    cosine_angle = np.clip(cosine_angle, -1, 1)

    # Calculate the angle in radians
    angle_radians = np.arccos(cosine_angle)

    # Convert the angle to degrees
    angle_degrees = np.degrees(angle_radians)

    return angle_degrees


def get_features(frame, type):
    # squat values : What angles (knee bend, back straight, head up)
    # squat values : What distances  (distance between knees, feet)
    

    if type == "squat":
        # angles
        # knee bend
        knee_bend_1 = get_angle(frame[27], frame[25], frame[23])
        knee_bend_2 = get_angle(frame[28], frame[26], frame[24])
        # back straight
        back_straight_1 = get_angle(frame[25], frame[23], frame[11])
        back_straight_2 = get_angle(frame[26], frame[24], frame[12])
        # head up
        shoulder_mid_point = np.array([(frame[12][0] + frame[11][0]) / 2,
                        (frame[12][1] + frame[13][1]) / 2])
        head_up_1 = get_angle(frame[12], shoulder_mid_point, frame[0])
        head_up_2 = get_angle(frame[11], shoulder_mid_point, frame[0])
        
        # distances
        knees = get_distance(frame[26], frame[25])
        feet = get_distance(frame[28], frame[27])

        values = knee_bend_1, knee_bend_2, back_straight_1, back_straight_2, head_up_1, head_up_2, knees, feet
        features = np.array(values)
        return features
    
def main():
    pass

if __name__ == "__main__":
    main()
