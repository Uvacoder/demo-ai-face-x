# Face Detection using MTCNN

A number of deep learning methods have been developeed and demonstrated for face detection.

Perhaps one of the more popular approaches is called the _"Multi-Task Cascaded Convolutional Neural Network"_ **(MTCNN)** described by [Kaipeng Zhang](https://kpzhang93.github.io/) in the 2016 paper titled "[Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks](https://arxiv.org/abs/1604.02878)"

## Why MTCNN Popular?

- Because it achieved then state-of-the-art results on a range of benchmark datasets.
- Because it is capable of also recognizing other facial features such as eyes,nose and mouth,called landmark detection.

## Working of MTCNN

The network uses a cascade structure with three networks :

1. **Image Pyramid** - First the image is rescaled to a range of different sizes
2. **Proposal Network** - This first model proposes candidate facial regions.
3. **Refine Network** - This second model filters the bounding boxes.
4. **Output Network** - This third model proposes facial landmarks.

### Pictorial representation of above working

<img src="https://github.com/kuluruvineeth/Face-X/blob/issue887/Face-Detection/Face%20Detection%20using%20MTCNN/mtcnn.webp" height="700">

## How to setup MTCNN ?

- [mtcnn setup](https://pypi.org/project/mtcnn/)

## Photograps I used

<img src="https://github.com/kuluruvineeth/Face-X/blob/issue887/Face-Detection/Face%20Detection%20using%20MTCNN/test1.jpg" width="400" height="300">   <img src="https://github.com/kuluruvineeth/Face-X/blob/issue887/Face-Detection/Face%20Detection%20using%20MTCNN/test2.jpg" width="400" height="300">

## Resultant Photographs


<img src="https://github.com/kuluruvineeth/Face-X/blob/issue887/Face-Detection/Face%20Detection%20using%20MTCNN/res1.png" width="400" height="300"> <img src="https://github.com/kuluruvineeth/Face-X/blob/issue887/Face-Detection/Face%20Detection%20using%20MTCNN/res1.1.png" width="400" height="300"> <img src="https://github.com/kuluruvineeth/Face-X/blob/issue887/Face-Detection/Face%20Detection%20using%20MTCNN/res2.png">


## Conclusion

- Face detection is a computer vision problem for identifying and localizing faces in images
- State-of-the-art face detection can be achieved using a **Multi-task Cascade CNN** via the MTCNN library
