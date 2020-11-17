#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:58:51 2020

@author: slamani
"""

import glassdoor_scraper as gs
import pandas as pd

path= "/Users/slamani/Desktop/salary_pred/chromedriver"

df = gs.get_jobs('data-scientist', 910, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
