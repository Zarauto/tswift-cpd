import os.path as o
import shutil

albuns = ['Taylor Swift', 'Fearless', 'Speak Now', 'Red', '1989', 'reputation', 'Lover', 'folklore', 'evermore', 'Midnights']
albuns_com_tv = [x + " (Taylor's Version)" for x in ['Fearless', 'Speak Now', 'Red']]

n = len(" (Taylor's Version)")

root = o.join('.','')
letras = o.join(root,'letras')
links = o.join(root,'urls')

for name in albuns:
    if not o.exists(o.join(letras,name+'.txt')):
        with open(o.join(letras,name+'.txt'), 'w') as file:
            continue
        
for name in albuns:
    if not o.exists(o.join(links,name+'.txt')):
        with open(o.join(links,name+'.txt'), 'w') as file:
            continue
        
"""for name in albuns_com_tv:
    src_name = name[:-n]
    src = o.join(letras,src_name+'.txt')
    tgt = o.join(letras,name+'.txt')
    shutil.copy(src,tgt)  """              
    
"""for name in albuns_com_tv:
    src_name = name[:-n]
    src = o.join(links,src_name+'.txt')
    tgt = o.join(links,name+'.txt')
    shutil.copy(src,tgt)            """