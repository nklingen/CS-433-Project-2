# Road segmentation project

Team:   
- Natasha Ørregaard Klingenbrunn
- Clara Bonnet
- Daniel-Florin Dosaru

How to train the neural network:   
  `cd scripts`   
  (place the images into training and test_set_images folders)    
  `python3 run.py --train`     train and predict  

Change the value of MODEL_PATH variable in `constants.py`:      
`MODEL_PATH  = '../best_model.weights' `     
`python3 run.py --predict`   predict test images      

See results by running in the same folder (`scripts`):    
`python3 overlayPredictions.py`

Install:    
For Ubuntu 18.04 LTS run:     
`sudo apt-get update`      
`sudo apt install python3-pip`
than ,    

Install all the necessary dependencies:
```bash
pip3 install -r requirements.txt
sudo apt-get install python3-tk
sudo pip3 install scikit-image
```

Requirements:
* Python 3.6.9  
* torch 1.3.1
* torchvision 0.4.2
* sklearn 0.22
* matplotlib 2.1.0  
* scikit-image

Optional   
* torchsummary  (used to print neural network details)
* psutil (used to print memory usage)
