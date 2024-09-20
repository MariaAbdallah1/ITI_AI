import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance_image(image_path):
    image = cv2.imread(image_path)

    noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)

    alpha = 1.5  # Contrast (1~3)
    beta = 0    # Brightness (0~100)
    contrasted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    return image, noisy_image, contrasted_image

def augment_image(image):
    augmented_images = []
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    angle = 45
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    augmented_images.append(rotated_image)
    
    scale = 0.5
    scaled_image = cv2.resize(image, None, fx=scale, fy=scale)
    augmented_images.append(scaled_image)
    
    flipped_image = cv2.flip(image, 1)  # 1 means horizontal flip
    augmented_images.append(flipped_image)
    
    # Cropping
    start_x, start_y = 50, 50
    end_x, end_y = start_x + 200, start_y + 200
    cropped_image = image[start_y:end_y, start_x:end_x]
    augmented_images.append(cropped_image)
    
    return augmented_images

def display_images(images, titles):
    plt.figure(figsize=(12, 8))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')
    plt.show()

image_path = 'd:/Maria_iti/day 10/3.jpg'

image, noisy_image, contrasted_image = enhance_image(image_path)

image = cv2.imread(image_path)
augmented_images = augment_image(image)

display_images([image, noisy_image, contrasted_image], ["Original Image", "Noisy Image", "Contrasted Image"])

display_images(augmented_images, ["Rotated Image", "Scaled Image", "Flipped Image", "Cropped Image"])
