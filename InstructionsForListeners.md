**This document provides instructions for listeners, such as research assistants, to set up and perform the child vocalization cleaning task.**

For now I'm assuming you're using a Mac.

The first thing you should do is to install anaconda (https://www.anaconda.com/products/individual), so that you will have the necessary packages, such as scipy. (Select the Python 3 version, Mac OS, Graphical Installer.)

The task also requires pyglet to be installed. After successfully installing anaconda, you will need to open up the Terminal app, type or copy in this line:
"conda install -c conda-forge pyglet", press enter, and then make sure there are no errors. If asked to proceed with updates, enter "y". (Reference: https://anaconda.org/conda-forge/pyglet.)

The task also assumes you are running Box Drive and that I've given you read and write permissions for our lab's HomeBankLabeling folder (https://ucla.app.box.com/folder/103573977921). Currently that folder is set to be readable by anyone, and anyone will be able to perform the task, but if you do not have write permissions, your data will not get synced and the data will not be usable by my lab.

To run the task, open up a Terminal window. Then run "cd Box/HomeBankLabeling/homebank-child-voc-cleaning/" (you may need to change this line if your Box Drive folder is located in a different directory).

Then type "python runRelabelCHN.py"

The program will prompt you for your UCLA Logon ID. This allows it to run your particular listening assignments, which it finds in relabelCHN_assignments_<yourID>.txt.

After performing the task for awhile, the program may quit and say a bunch of technical stuff ending in "Error allocating buffer." Here is a screenshot:

<image src="https://github.com/AnneSWarlaumont/homeank-child-voc-cleaning/blob/master/screenshot-of-buffer-error.png" width="600">
  
If this happens to you, press the up arrow to copy the most recent command, then press return to restart.

The program will print a simple message when you are done listening through all the automatically(LENA)-tagged target child sounds for a given daylong audio recording and then will move on immediately to your next assignment until you've finished everything that has been assigned to you.
