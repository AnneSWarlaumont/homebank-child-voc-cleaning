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

Some additional known issues and FAQ:

Q: "I was going through the audio file as usual and was rating each audio clip when suddenly all of the audio clips were completely silent. At first, I thought the audio files were simply silent so I repeatedly input "5", but then I grew suspicious that there might be a technical difficulty considering the amount of times it was silent."

A: The silence is probably a period of time that was scrubbed following the vetting process, to silence private material. I need to put more about this in the instructions, or make the program automatically skip over those sections, but in the meantime, just keep entering "5" and eventually the sound should resume.

Q: "In a certain recording, there tends to be lots of rusting or maybe the TV on very very softly in the background. In those instances, where the background noise is barely audible I have still been labeling the segment as a “2” (some background noise but it is clear the dominant sound is he child vocalization). I was wondering though, is this correct? Or should I be labeling is as a “1” when the background noise is this minimal? I had interpreted a “1” to be solely the child’s voice and no background noise (so no rustling or anything at all) I just wanted to check in before I continue on."

A: "The way you interpreted it is exactly what I intended."

Q: "I have noticed that for some sound clips, there are instances where the initial sound of the clip is background noise followed by a brief (yet audible) vocalization of the child. Thus far, I have been judging these instances as a 4 given the child's vocalization is not the primary sound, lengthwise, of the clip. I just wanted to confirm if this form of judgment is appropriate, or if we are judging the clips solely based on the volume of the child's vocalization relative to all other background noise?"

A: "I have been taking both duration and loudness into account in determining relative prominence. It sounds like what you are doing would make sense, at least in a lot of cases! (If the child vocalization is much louder than the other sound, even if it is shorter, then I might give it a 3 or a 2.)"



