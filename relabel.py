# Tools for huamn listeners to manually identify sound types

import pyglet, scipy.io.wavfile, numpy, os

def relabel_by_timebin(wavfile,outfile,coding_start_time,coding_end_time,bin_size):
    
    # Label a child wav file in bins, asking whether or not each speaker type was present (including during overlap)
    
    sr, sounddata = scipy.io.wavfile.read(wavfile)
    
    # If the output file already exists,
    # use it to set coding_start_time to pick up where last left off,
    # and append to the output file rather than rewriting it.
    # If the output file does not already exist,
    # create it and the header line.
    if os.path.isfile(outfile):
        outf = open(outfile,'r')
        outfLines = outf.readlines()
        if len(outfLines)>1:
            lastOutfLine = outfLines[-1]
            coding_start_time = float(lastOutfLine.split(',')[0]) + bin_size 
        outf.close()
        outf = open(outfile,'a')
    else:
        outf = open(outfile,'w')
        outf.write('startSeconds,endSeconds,userInput,containsTargetChild,containsOtherChild,containsAdult\n')
        
    for playstart in numpy.arange(coding_start_time,coding_end_time,bin_size):
        if playstart+bin_size > coding_end_time:
            playend = coding_end_time
        else:
            playend = playstart+bin_size
        segsounddata = sounddata[playstart*sr:playend*sr]
        scipy.io.wavfile.write('temp.wav',sr,segsounddata)
        pygsound = pyglet.media.load('temp.wav',streaming=False)
        input('\n***Instructions***\n\nListen carefully because you will only '
              'get one opportunity to listen.\nBe on the lookout for any '
              'clearly audible vocalization that is primarily communicative '
              'or playful, such as speech, babble, cooing, crying, sighing,'
              'laughing, raspberries, clicks, etc. Please ignore vegetative '
              'sounds, such as heavy breathing, hiccups, sneezes, sniffles, '
              'and coughs, unless they appear to have been produced with a '
              'communicative or playful purpose). You will be asked to enter '
              'the codes (no spaces between) for the types of voices you '
              'heard in the segment that just played.\n\nCodes: t for child '
              'wearing the recorder, o for another child, a for adult.\n\nIf '
              'there are multiple voices present, enter the multiple codes '
              'without spaces in between. Order of the codes does not matter.'
              ' Leave the space blank if you did not hear any communicative '
              'or playful vocalizations.\n\nPress return to play the sound. '
              'Press control+c to quit the labeling session.')
        pygsound.play()
        userInput = input("\nType the codes for the voices you heard here, then press return: ")
        containsTargetChild = "t" in userInput
        containsOtherChild = "o" in userInput
        containsAdult = "a" in userInput
        outf.write(str(playstart) + ',' + str(playend) + ',' + userInput + ',' + str(containsTargetChild) + ',' + str(containsOtherChild) + ',' + str(containsAdult) + '\n')
        
    outf.close()
    
    return

def relabel_by_segment(wavfile,outfile,segmentsfile):
    
    # Using the output of segments.pl,
    # play all segments meeting certain criteria,
    # prompt the user to relabel who is speaking,
    # and save output to a CSV file.
    # Speaker types to be relabeled include:
    # C (child wearing the recorder), X (other child), and A (adult)
    
    return

def relabel_CHN(wavfile,outfile,segmentsfile,instructionsv):
    
    # Using the output of segments.pl,
    # play all the CHN segments,
    # ask the user if the sound contained the target child and nothing else,
    # and save output to a CSV file.
    
    # read in the sound file
    sr, sounddata = scipy.io.wavfile.read(wavfile)
    
    # Parse the wav filename to find out the age of the child
    ageYYMMDD = wavfile.split('_')[1][0:6]
    print(ageYYMMDD[0:2])
    
    # Set the name of the file that will hold the currently playing wav file
    # We want this to be unique to the listener, in case multiple listeners
    # are working at the same time.
    tempwav = 'temp_' + outfile + '.wav'
    
    # If the output file already exists,
    # use it to set coding_start_time to pick up where last left off,
    # and append to the output file rather than rewriting it.
    # If the output file does not already exist,
    # create it and the header line.
    if os.path.isfile(outfile):
        outf = open(outfile,'r')
        outfLines = outf.readlines()
        if len(outfLines)>1:
            lastOutfLine = outfLines[-1]
            coding_start_time = float(lastOutfLine.split(',')[1])
        else:
            coding_start_time = 0
        outf.close()
    else:
        outf = open(outfile,'w')
        if instructionsv == '2':
            outf.write('startSeconds,endSeconds,includesTargetChild\n')
        elif instructionsv == '3':
            outf.write('startSeconds,endSeconds,targetChildProminence\n')
        outf.close()
        coding_start_time = 0
        
    segf = open(segmentsfile,'r')
    segfLines = segf.readlines()
    for segfLine in segfLines[1:]:
        segdata = segfLine.split(',')
        segtype = segdata[0]
        segstart = float(segdata[1])
        segend = float(segdata[2])
        if segstart >= coding_start_time and segtype[0:3]=='CHN':
            # play the segment and request user input
            segsounddata = sounddata[int(segstart*sr):int(segend*sr)]
            scipy.io.wavfile.write(tempwav,sr,segsounddata)
            pygsound = pyglet.media.load(tempwav,streaming=False)
            if instructionsv == '2':
                input('\n***'
                      '\n\n***Instructions***'
                      '\n\nListen carefully because you will only get one opportunity to listen.'
                      '\n\nYou will be asked whether the clip contains a vocalization'
                      '\nproduced by the child wearing the recorder (i.e. the target child).'
                      '\n\nA target child vocalization may include speech, singing, babble, crying,'
                      '\ntrilling the lips, coughing, grunting, or any other sound produced'
                      '\nusing the throat, lips, and/or tongue.'
                      '\n\nIf there are other sounds present, such as other people or animals,'
                      '\nbackground noise, rustling, music, etc. that is fine. You need only pay'
                      '\nattention to whether there is some sound produced by the target child\'s'
                      '\nvocal tract.'
                      '\n\nNote that the target child in this case is '+ageYYMMDD[0:2]+' year(s), '+ageYYMMDD[2:4]+' month(s), '
                      '\nand '+ageYYMMDD[4:6]+' day(s) old.'
                      '\n\nPress return to play the sound. To quit, press control+c.')
            elif instructionsv == '3':
                input('\n***'
                      '\n\n***Instructions***'
                      '\n\nListen carefully because you will only get one opportunity to listen.'
                      '\n\nYou will be asked about the prominence within the clip of the voice '
                      '\nof the child wearing the recorder (i.e. the target child) compared to '
                      '\nall other sounds, such as other voices, background noise, rustling, etc.'
                      '\n\nA target child vocalization may include speech, singing, babble, crying,'
                      '\ntrilling the lips, coughing, grunting, or any other sound produced'
                      '\nusing the throat, lips, and/or tongue.'
                      '\n\nNote that the target child in this case is '+ageYYMMDD[0:2]+' year(s), '+ageYYMMDD[2:4]+' month(s), '
                      '\nand '+ageYYMMDD[4:6]+' day(s) old.'
                      '\n\nPress return to play the sound. To quit, press control+c.')
            pygsound.play()
            os.remove(tempwav)
            
            if instructionsv == '2':
                userInput = input('\n***'
                                  '\n\n(At this time, you may quit without saving a judgment by pressing'
                                  '\ncontrol+c. If you quit then next time you start the program it will'
                                  '\nreply the sound. So this may be a good option if you need to play'
                                  '\nthe sound again before making your judgment.)'
                                  '\nType y if the clip included a target child vocalization.'
                                  '\nIf there was no vocalization by the target child, please enter n.'
                                  '\nThen press return:\n')
                while ((userInput != 'y') & (userInput != 'n')):
                    userInput = input('\nPlease enter y or n.\n')
                isTargetChild = "y" in userInput
                outf = open(outfile,'a')
                outf.write(str(segstart) + ',' + str(segend) + ',' + str(isTargetChild) + '\n')
                outf.close()
            elif instructionsv == '3':
                userInput = input('\n***'
                                  '\n\n(At this time, you may quit without saving a judgment by pressing'
                                  '\ncontrol+c. If you quit then next time you start the program it will'
                                  '\nreply the sound. So this may be a good option if you need to play'
                                  '\nthe sound again before making your judgment.)'
                                  '\n\nType 1 if you heard only the target child\'s voice.'
                                  '\n\nType 2 if you heard some background noise or other sound(s) but '
                                  '\nthe infant vocalization is clearly the dominant sound in the clip.'
                                  '\n\nType 3 if you heard some background noise or other sound(s) and '
                                  '\nthe target child vocalization and the other sound(s) are similar in'
                                  '\n how dominant they are within the clip.'
                                  '\n\nType 4 if you heard a target chid vocalization but it was definitely '
                                  '\nnot the dominant sound in the clip.'
                                  '\n\nType 5 if there did not appear to be a target child vocalization'
                                  '\n within the clip.'
                                  '\n\nThen press return:\n')
                while ((userInput != '1') & (userInput != '2') & (userInput != '3') & (userInput != '4') & (userInput != '5')):
                    userInput = input('\nPlease enter a number between 1 and 5.\n')
                outf = open(outfile,'a')
                outf.write(str(segstart) + ',' + str(segend) + ',' + userInput + '\n')
                outf.close()
            
    print('\nYou have finished labeling the file. Congratulations & thank you!')
    
    return
        
        