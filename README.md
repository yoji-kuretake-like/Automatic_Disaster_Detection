# Automated disaster detection of satellite images
<p>This is my master project applying deep learning model to the satellite images.</p>
<p>The aim of this project is to detect the affected area by natural disasters by using the way of semantic segmentation and change detection method. The model of semantic segmentation in this project is the U-Net which has been widely used semantic segmentation network. The proposed approach achieved an overall accuracy 80% and an F1 score of 55%.</p>

# Table of content
1. Dataset
2. Preprocessing
3. Proposed Method
4. Build U-Net Model
5. Change Detection Method
6. Result

## 1. Dataset
<p>Training and Validation Data - ISPRS Potsdom dataset(Dataset consists of 36 images and each image size is 6000 × 6000) </p>
<p>Disaster Image Data - DigitalGlobe's Open data platform (The image is taken in Indonesia and the disaster types are Earthquake and Tsunami) </p>

## 2. Preprocessing
<p>Scaling the training images into the sizes of 6000 × 6000, 2560 × 2560, 1792 × 1792, 1024 × 1024</p>
<p>After the scale task, splitting the scaled images into the small patches size of 256 × 256 </p>

## 3. Proposed Method
<p>The overview of proposed method is as follows:</p>
<img width="1000" src="https://github.com/yoji-kuretake-like/Automatic_Disaster_Detection/blob/main/images/flow_of_method2.png">


