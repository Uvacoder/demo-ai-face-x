from PIL import Image
import cv2
import numpy as np
import torch
import torch.nn as nn
from torchvision import transforms
from glob import glob
import os
from models import *

# change device to GPU if available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Loading the cascades
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# number of unique faces + 1
classes = list(
    map(
        lambda x: x.split("\\")[-1],
        glob(os.path.join(os.getcwd(), "Datasets", "train", "*")),
    )
)


def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns None
    faces = face_classifier.detectMultiScale(img, 1.3, 5)
    if faces is ():
        return None
    # Crop all faces found
    cropped_face = 0
    for (x, y, w, h) in faces:
        x = x - 10
        y = y - 10
        cropped_face = img[y : y + h + 50, x : x + w + 50]
    cv2.rectangle(img, (x, y), (x + w + 30, y + h + 40), (0, 255, 255), 2)
    return cropped_face


# preprocess frame
preprocess = transforms.Compose(
    [
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]
)



# Initialize webcam
video_capture = cv2.VideoCapture(0)

# load model
model = NASNetAMobile(2).to(device)
model.load_state_dict(torch.load("saved_model.pt"))
model.eval()

# Recognize faces
while True:
    _, frame = video_capture.read()
    face = face_extractor(frame)
    if face is not None:
        face = cv2.resize(face, (224, 224))
        im = Image.fromarray(face, "RGB")
        img = preprocess(im)
        img = torch.unsqueeze(img, 0)
        preds = model(img)

        name = "None matching"

        _, pred = preds.max(dim=1)
        if pred != 0:
            name = "Face found:{}".format(classes[pred])
        cv2.putText(frame, name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(
            frame,
            "No face found",
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2,
        )
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
