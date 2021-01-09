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
<p>The flow of proposed method is as follows:</p>
<img width="900" src="https://github.com/yoji-kuretake-like/Automatic_Disaster_Detection/blob/main/images/flow_of_method2.png">
<p> After the preprocessing task was carried out, the segmentation model was trained using the preprocessed images. Then, the trained model was applied to the pre and post disaster images in order to classify all pixels into 6 classes(Impervious road, Buildings, Low vegetation, Trees, cars, Clutter). Finally, the segmented output images from the trained model were assesed with the change detection method to create the final output.</p>

<p>The detail of way to train the model is as follows:</p>
<img width="700" src="https://github.com/yoji-kuretake-like/Automatic_Disaster_Detection/blob/main/images/method.png">
<p>In this project, four types of methods were used for training models, then comparing each model performance of disaster ditection task and choosing the best model.</p>

## 4. Build U-Net Model
<p>Model architecture used in this project is as follows:</p>
<img width="900" src="https://github.com/yoji-kuretake-like/Automatic_Disaster_Detection/blob/main/images/model_archi.png">

## 5. Change Detection Method
<p>After the predicted segmentation masks of pre and post disaster images were created by the trained semantic segmentation model, the impacted regions are extracted to compare these two images by using the pixel-based change detection method with a sliding window. The areas that satisfy below equation can be considered as the damaged area by disasters.</p>
<img width="750" src="https://github.com/yoji-kuretake-like/Automatic_Disaster_Detection/blob/main/images/equation.png">
<p>In this project, the threshold and window size are set as 0.7 and 64×64 pixels respectively for the models to avoid recognizing the few changes that occurred due to the time series as the impacted area. The window is slid over the segmentation masks both of pre and post disaster images, and if the area within the window satisfies the above formula, it is labelled as the damaged zone by disasters.</p>

