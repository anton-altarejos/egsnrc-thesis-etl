import pandas as pd
import os
from sph_extractor import type

cwd = os.getcwd()
Angle = cwd[-2:] # get the angle from the dir name
CellModel = cwd[-6:-3] # get the cell model from the dir name

def replace_line(filename, line_number, text):
  with open(filename) as file:
    lines = file.readlines()
  if (line_number <= len(lines)):
    lines[line_number - 1] = text + "\n"
    with open(filename, "w") as file:
      for line in lines:
        file.write(line)
  else:
    print("Line", line_number, "not in file.")
    print("File has", len(lines), "lines.")

filenames = ['sph_source_nucleus.csv','sph_source_cytoplasm.csv','sph_source_membrane.csv','sph_source_cell.csv']
source = ['N1','Cy1','M1', 'C1']
target = ['N1','Cy1','M1','C1','N2','Cy2','M2','C2']
#yields = pd.Series([5.06630,14.85480,15.05990,25.80400,38.00510])

for name in filenames:
    df = pd.read_csv(name)
    #print(df)
    df.columns = [source[filenames.index(name)]+'->'+target[3],'ERROR',source[filenames.index(name)]+'->'+target[0],'ERROR',source[filenames.index(name)]+'->'+target[1],'ERROR',source[filenames.index(name)]+'->'+target[2],'ERROR',source[filenames.index(name)]+'->'+target[4],'ERROR',source[filenames.index(name)]+'->'+target[5],'ERROR',source[filenames.index(name)]+'->'+target[6],'ERROR',source[filenames.index(name)]+'->'+target[7],'ERROR']
    #df[[source[filenames.index(name)]+'->'+target[3],source[filenames.index(name)]+'->'+target[0],source[filenames.index(name)]+'->'+target[1],source[filenames.index(name)]+'->'+target[2],source[filenames.index(name)]+'->'+target[4],source[filenames.index(name)]+'->'+target[5],source[filenames.index(name)]+'->'+target[6],source[filenames.index(name)]+'->'+target[7]]]=df[[source[filenames.index(name)]+'->'+target[3],source[filenames.index(name)]+'->'+target[0],source[filenames.index(name)]+'->'+target[1],source[filenames.index(name)]+'->'+target[2],source[filenames.index(name)]+'->'+target[4],source[filenames.index(name)]+'->'+target[5],source[filenames.index(name)]+'->'+target[6],source[filenames.index(name)]+'->'+target[7]]].mul(yields, axis = 0)
    df.insert(0, "Energy", ['001','003','005','006','007','008','009','010','012','014','016','018','020','022','024','026','028','030','035','40','45','050','055','060','065','070','100'])
    #df.rows = ['Tc-99m','In-111','I-123','I-125','Tl-201']
    #print(df)
    name.strip('.csv')
    name = name[3:-4]
    #df.to_csv('yield_'+name+'_'+CellModel+'_'+Angle+'.csv', sep=',')
    df.to_csv('yield_sph_'+type+name+'.csv', sep=',')
