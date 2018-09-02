import re

strs = "how much for the maple syrup? $20.99? That's. and's didn't - ricidulous!!!"
print(strs.strip())

nstr = re.sub(r'[?|$|.|!|-]',r'',strs)
print(nstr.replace("\'", ''))

nestr = re.sub(r'[^a-zA-Z0-9\' ]',r'',nstr)
print(nestr)
