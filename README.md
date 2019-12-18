# Road segmentation project

Team:   
- Natasha Ørregaard Klingenbrunn
- Clara Bonnet
- Daniel-Florin Dosaru

Install all the necessary dependencies:
```bash
pip3 install -r requirements.txt
```

On Google cloud  (choose image Ubuntu 18.04 LTS) and you also need to run  :     
`sudo apt-get update`      
`sudo apt install python3-pip`   
than install the dependencies    


How to train the neural network:   
  `cd scripts`   
  `python3 run.py --train`     train and predict     
  `python3 run.py --predict`   predict  test images    

Requirements:

* Python 3.6.9  
* torch 1.3.1
