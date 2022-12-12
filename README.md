# COMP_473_Project Guide to Run

#### Download the CK+ Dataset here: https://www.kaggle.com/datasets/shareef0612/ckdataset
     Locate the download and reaplce any comments that say "YOUR DIRECTORY PATH HERE" with the location of the CK+ dataset
     
     
### 1. Preprocessing the dataset to be augemented (rotated, cropping, intensity normalization) go to DataPreparation.ipyn notebook
     - Each augemented dataset should have three shuffled datasets: Dataset1, Dataset2 and Dataset3
     - Within each Dataset it will contain train and val directories
     - The testing dataset will be standalone directories to run for cross-validation: Text1, Test2, Test3
     The output will look something like this when using split-folders library:
     Project Directory/
          Dataset1/
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
           Dataset2/
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
         Test1/
             happy/
                 img2.jpg
                 ...
             sad/
                 imgb.jpg
                 ...
         Test2/
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

### 2. Now we use our augemented datasets to run the tensorflow models. Go to the Experiments_And_Restults.ipynb notebook
<ul>
  <li>This notebook is automated to run from the start once you have all the file paths located for each pre-processing method directory </li>
  <li>Once all the filepaths are entered, run the first code block to import any missing libraries</li>
  <li>Three models per pre-processing method will be saved as .h5 for future testing. The testing of each model with its respective test directory will also be done on its own. </li>
</ul>
