import gspread
import sys
script, name = sys.argv

#Each individual's google worksheet is stored under a worksheet under their name
# Install gspread and get API access via google drive and google sheets

sa = gspread.service_account()
sh = sa.open("microbiome_modifier")

wks = sh.worksheet(name)
all = wks.get_all_records()
new = {} #Dictionary to store all the modifiers with a non-zero gain value

for item in all:
    if item['Gain']:
        new.update({item['Microbiome Modifier']:item['Gain']})

new_sorted = sorted(new.items(), key=lambda x:x[1])
sortdict = dict(new_sorted)

l = len(sortdict)
num = int(input("\n How many modifiers do you want to read?> "))
print("\033[31m The top 10 modfiers to AVOID with NetGain score are: \n",list(sortdict.items())[0: num])
print("\n\n \033[32m The top 10 modfiers to INCREASE with NetGain score are: \n",list(sortdict.items())[l-num: l])
