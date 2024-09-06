# GANZurvey

The purpose of this program is to offer a very simple online survey to compare GAN/genAI-generated images with one another.

![Survey page](/static/screenshots/screenshot1.png)
*Survey page*

## Features
* randomize images in columns 1 and 2 by model, so users can't just click column 1 or column 2 images
* user can select the most realistic image by clicking on the image
* uses sessions to keep track of which image was selected by each user
* easy setup


## Original requirements
* Tested with Python 3.8
* images with identical names in subdirectories of the same folder
* images with identical name are compared to each other
* there's a little text + image introduction to explain the program to the participants at the beginning of the page

## How it works
### Setup
* create a virtual environment with python3.8 and pip installed. `python3.8 -m venv .venv && source .venv/bin/activate`
* install the requirements with pip: `pip3 install -r requirements.txt`
* Put the images from your model into the A image subfolder, the ones of your comparison in the B subfolder. The names of the images  must be identical, e.g. for each PNG file in the A subfolder there must be a corresponding file in the B subfolder (see `static/images/real` folder structure for an example).
* adjust the config.json `IMG_PATH` to point to your image (root) folder
* adjust the `NUM_QUESTIONS` to the number of questions you want to ask in the survey. The default is 20.
* execute the `generate-image-dict.py` script to generate the image dictionary from the images in your image folder. This is necessary for the program to work properly.

### Run the server
* You can now run the server and send the survey link to your participants.
* `python3 app.py`

### Evaluating the results
* The results are stored under the `results` folder.
* See how many times the images in subfolder A have been preferred over the images of subfolder B by running `python3 evaluate-result.py`.

## Sceenshots

![Thanks page after finishing survey](/static/screenshots/screenshot2.png)
*Confirmation and thank you page after finishing survey*

## Story of the app

This app can be used to generate **Human perceptual test** for genAI techniques and has been used in the perecptual test for the paper [MirrorGAN: Learning Text-to-image Generation by Redescription
](https://ar5iv.labs.arxiv.org/html/1903.05854).
