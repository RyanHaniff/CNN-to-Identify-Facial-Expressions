# COMP_473_Project Guide to Run

#### Download the CK+ Dataset here: https://www.kaggle.com/datasets/shareef0612/ckdataset
     Locate the download and reaplce any comments that say "YOUR DIRECTORY PATH HERE" with the location of the CK+ dataset
     
     
### 1. Preprocessing the dataset to be augemented (rotated, cropping, intensity normalization) go to DataPreparation.ipyn
     - Each augemented dataset should have three shuffled datasets: Dataset1, Dataset2 and Dataset3
     - Within each Dataset it will contain train and val directories
     - The testing dataset will be standalone directories to run for cross-validation: Text1, Test2, Test3
     The output will look something like this when using split-folders library:
     output/
    train/
        happy/
            img1.jpg
            ...
        sad/
            imga.jpg
            ...
    val/
        happy/
            img2.jpg
            ...
        sad/
            imgb.jpg
            ...
    Test/
        happy/
            img2.jpg
            ...
        sad/
            imgb.jpg
            ...
        
 <ol>
    <li>You have to run each facial expression directory individually to rotate all the images inside between -10.5 degrees and 10.5 degrees</li>
  <li>To make sure the training set doesnt contain any subject from the testing set run the create_dataset_without_duplicate_subject() function</li>
  <li>Now we can make the data set with face cropping. Run the face_preprocessing() function to crop the images accordingly</li>
  <li>Finally, we need to make the data set for intensity normalization to increase the contrast of the image</li>
</ol>

### 2. Now we use our augemented datasets to run 
