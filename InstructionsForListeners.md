**This document provides instructions for listeners, such as research assistants, to set up and perform the child vocalization cleaning task.**

For now I'm assuming you're using a Mac.

The first thing you should do is to install anaconda (https://www.anaconda.com/products/individual), so that you will have the necessary packages, such as scipy. (Select the Python 3 version, Mac OS, Graphical Installer.)

The task also requires pyglet to be installed. After successfully installing anaconda, you will need to open up the Terminal app, type or copy in this line:
"conda install -c conda-forge pyglet", press enter, and then make sure there are no errors. If asked to proceed with updates, enter "y". (Reference: https://anaconda.org/conda-forge/pyglet.)

These instructions assume you are running Box Drive and that I've given you edit permissions for our lab's HomeBankLabeling/homebank-child-voc-cleaning folder (https://ucla.app.box.com/folder/103573977921), which includes a subfolder containing a clone of this GitHub repository. *(If you are not a member of our lab and are interested in trying out the task, you are free to download and try things out on your own system, though you will need to make some minor edits to a few files and you'll also need to supply your own audio--some publicly available at homebank.talkbank.org. Or you can email me if you're interested in contributing as a volunteer to our labeling effort!)*

To run the task, open up the Terminal application. Then run "cd Box/HomeBankLabeling/homebank-child-voc-cleaning/" (you may need to change this line if your Box Drive folder is located in a different directory).

Then type "python runRelabelCHN.py"

The program will prompt you for your UCLA Logon ID. This allows it to run your particular listening assignments, which it finds in relabelCHN_assignments_<yourID>.txt.

After performing the task for awhile, the program may quit and say a bunch of technical stuff ending in "Error allocating buffer." Here is a screenshot:

<image src="https://github.com/AnneSWarlaumont/homeank-child-voc-cleaning/blob/master/screenshot-of-buffer-error.png" width="600">
  
If this happens to you, press the up arrow to copy the most recent command, then press return to restart.

The program will print a simple message when you are done listening through all the automatically(LENA)-tagged target child sounds for a given daylong audio recording and then will move on immediately to your next assignment until you've finished everything that has been assigned to you.
