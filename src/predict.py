import pickle
import numpy as np
from skimage.io import imread
from skimage.transform import resize

model = pickle.load(open("model.p", "rb"))
categories = ['tree_a', 'tree_b', 'tree_c', 'tree_d']

def preprocess_image(image_path):
    img = imread(image_path)
    img = resize(img, (15, 15)) 
    img = img.flatten()          
    return img

def main():
    image_path = input("Enter the path to the image you want to classify: ")

    try:
        img = preprocess_image(image_path)
        img = np.array(img).reshape(1, -1)

        prediction = model.predict(img)[0]
        print(f"\nPredicted class: {categories[prediction]}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
