**This document provides instructions for listeners, such as research assistants, to set up and perform the listening task.**

For now I'm assuming you're using a Mac.

The first thing you should do is to install anaconda (https://www.anaconda.com/), so that you will have the necessary packages, such as scipy.

The task also requires pyglet to be installed. Here are some instructions that should work once you've installed anaconda: https://anaconda.org/conda-forge/pyglet

The task also assumes you are running Box Sync and that I've given you read and write permissions for our lab's HomeBankLabeling folder (https://ucla.app.box.com/folder/103573977921). Currently that folder is set to be readable by anyone, and anyone will be able to perform the task, but if you do not have write permissions, your data will not get synced and the data will not be usable by my lab.

To run the task, open up a Terminal window. Then run "cd Documents/Box\ Sync/HomeBankLabeling/homebank-child-voc-cleaning/"

Then type "python runRelabelCHN.py" (I need to change this to allow user input, so each user gets the right file and writes to the correct csv file).

After performing the task for awhile, the program may quit and say a bunch of technical stuff ending in "Error allocating buffer." Here is a screenshot:

<image src="https://github.com/AnneSWarlaumont/homeank-child-voc-cleaning/blob/master/screenshot-of-buffer-error.png" width="600">
  
If this happens to you, press the up arrow to copy the most recent command, then press return to restart.

The program will print a simple message when you are done listening through all the sounds in the file that were automatically identified by LENA as likely from the target child.
