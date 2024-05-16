import easyocr
import os
import cv2

folder_path = "./ic_images"

for images in os.listdir(folder_path):
    image_path = os.path.join(folder_path, images)

    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

# # print(result)
    image = cv2.imread(image_path)

    for (bbox, text, prob) in result:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = (int(top_left[0]), int(top_left[1]))
        top_right = (int(top_right[0]), int(top_right[1]))
        print(f'Text: {text}, Probability: {prob}, bbox: {bbox}')

        cv2.rectangle(image, (int(top_left[0]), int(top_left[1])), (int(bottom_right[0]), int(bottom_right[1])), (0, 0, 255), 3)

    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.imshow("frame", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
