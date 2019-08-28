#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""   
Please extract different data variations from the text file date.txt
Please use Regular Expression to complete this assignment

"""

# Importing necessary modules
import pandas as pd

# Loading the dates.txt 
doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)

# =============================================================================
# ## (1) 04/20/2009; 04/20/09; 4/20/09; 4/3/09 (20 points)
# 
# # The first part is to extract the dates with the above patterns
# # The code is already given
# =============================================================================

a1_1 = df.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2})\b')
a1_2 = df.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b')
a1 = pd.concat([a1_1,a1_2])
print(a1)

# =============================================================================
# ## (2)Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009; (20 points)
# 
# # Please extract the dates with the above patterns
# # Please finish your code here
# =============================================================================

a2 = df.str.extractall(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-.]* )(\d{1,2}[ ,-]*)(\d{4})\b')
print(a2)

# =============================================================================
# ## (3) 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009 (20 points)
# 
# # Please extract the dates with the above patterns
# # Please finish your code here
# =============================================================================

a3 = df.str.extractall(r'((?:\d{1,2} ))?((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[?: ,-]*)(\d{4})\b')
print(a3)

# =============================================================================
# ## (4) Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009 (20 points)
# 
# # Please extract the dates with the above patterns
# # Please finish your code here
# =============================================================================

a4 = df.str.extractall(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z])((?:\d{1,2}(?:st|nd|rd|th)[,])\d{4})\b')
print(a4)
 
# =============================================================================
# ## (5) 6/2008; 12/2009 (20 points)
# 
# # Please extract the dates with the above patterns
# # Please finish your code here
# =============================================================================

a5 = df.str.extractall(r'(\d{1,2})[/](\d{4})\b')
print(a5)

# =============================================================================
# #Please concat all 5 parts together
# =============================================================================

final = pd.concat([a1,a2,a3,a4,a5])
print(final)

# =============================================================================