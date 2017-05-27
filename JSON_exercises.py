

import pandas as pd
import json
from pandas.io.json import json_normalize

#1 find the 10 countries with most projects
bproj= pd.read_json('data/world_bank_projects.json')
print(bproj.head())

print(bproj.countryname.value_counts().head(10))

#2 top ten major project themes
bproj= json.load((open('data/world_bank_projects.json')))
btheme=json_normalize(bproj, 'mjtheme_namecode', ['id'])
print(btheme)
print(btheme.code.value_counts().head(10))


#3 creation of dataframe with missing major theme names filled in
btheme.loc[btheme.code=="1", "name"]="Economic management"
btheme.loc[btheme.code=="2", "name"]="Public sector governance"
btheme.loc[btheme.code=="3", "name"]="Rule of law"
btheme.loc[btheme.code=="4", "name"]="Financial and private sector development"
btheme.loc[btheme.code=="5", "name"]="Trade and integration"
btheme.loc[btheme.code=="6", "name"]="Social protection and risk management"
btheme.loc[btheme.code=="7", "name"]="Social dev/gender/inclusion"
btheme.loc[btheme.code=="8", "name"]="Human development"
btheme.loc[btheme.code=="9", "name"]="Urban development"
btheme.loc[btheme.code=="10", "name"]="Rural development"
btheme.loc[btheme.code=="11", "name"]="Environment and natural resources management"
print(btheme)