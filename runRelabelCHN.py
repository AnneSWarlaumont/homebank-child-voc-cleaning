#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:19:16 2020
Updated on Thu Feb 20

@author: Anne S. Warlaumont
"""

import relabel, csv, fileinput

# Get the user to enter their ID
# so we can look up what they should be listening to
# and where their judgments should be written
userID = input('\nWhat is your UCLA Logon ID? ')

# Read in the user's assignments txt file
userAssignmentsFile = open('relabelCHN_assignments_'+userID+'.txt','r')
userAssignmentsLines = userAssignmentsFile.readlines()
userAssignmentsFile.close()


# Find the first line that doesn't end in "finished" and call
# relabel.relabel_CHN on each unfinished line.
for assignment in userAssignmentsLines[1:]:
    assignmentElements = assignment.rstrip('\n').split(',')
    status = assignmentElements[3]
    instructionsv = assignmnetElements[4]
    if status != 'finished':
        
        if status == 'unstarted':
            # edit the userAssignmentsFile line to make status "inprogress"
            updatedLine = assignment.replace("unstarted","inprogress")
            for line in fileinput.input('relabelCHN_assignments_'+userID+'.txt', inplace=True):
                print(line.replace(assignment,updatedLine), end="")
        
        relabel.relabel_CHN('../'+assignmentElements[0],
                            assignmentElements[2],
                            assignmentElements[1],
                            instructionsv)
        
        # edit the userAssignmentsFile line to make status "finished"
        updatedLine = assignment.replace("inprogress","finished")
        for line in fileinput.input('relabelCHN_assignments_'+userID+'.txt', inplace=True):
            print(line.replace(assignment,updatedLine), end="")
