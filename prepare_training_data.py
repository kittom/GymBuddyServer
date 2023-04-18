from FeatureLoader import get_features
import numpy as np

def uniform_sampling(frames, num_samples, type):
    sampled_frames = []
    total_frames = len(frames)
    step = total_frames // num_samples

    for i in range(0, total_frames, step):
        sampled_frames.append(get_features(frames[i], type))

    sampled_array = np.array(sampled_frames[:num_samples])
    return sampled_array.flatten()

if __name__ == "__main__":
    # exercise = training_data[2][0]
    # values = np.array(uniform_sampling(exercise.normalised_values, 5, exercise.type))
    # print(values)
    pass