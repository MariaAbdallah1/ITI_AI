DotProduct
import numpy as np
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("The dot product of v1 and v2 is: ",  np.dot(v1, v2))

def cosine_angle(v1, v2):
    dot_product = np.dot(v1, v2)
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)
    cosine_angle = dot_product / (magnitude_v1 * magnitude_v2)
    return cosine_angle

cosine_value = cosine_angle(v1, v2)
angle_in_degrees = np.arccos(cosine_value) * (180 / np.pi)

print(f"Cosine angle between the vectors: {cosine_value}")
print(f"Angle in degrees: {angle_in_degrees}")