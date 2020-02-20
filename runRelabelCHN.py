#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:19:16 2020
Updated on Thu Feb 20

@author: Anne S. Warlaumont
"""

import relabel

relabel.relabel_CHN('../0274_000221_scrubbed.wav',
                    '0274_000221_scrubbed_CHNrelabel_warlaumont.csv',
                    '0274_000221_segments.csv')
