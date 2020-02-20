#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:19:16 2020

@author: Anne S. Warlaumont
"""

import relabel

relabel.relabel_CHN('0833_010606.wav',
                    '0833_010606_CHNrelabel_warlaumont.csv',
                    '0833_010606_segments.csv')
