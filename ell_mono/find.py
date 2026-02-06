"""
    Find the name of the working directory which contains the cell model and angle.
    Replace the relevant values in the scripts
    
"""

import os

cwd = os.getcwd()
Angle = cwd[-2:] # get the angle from the dir name
CellModel = cwd[-6:-3] # get the cell model from the dir name

# function for replacing a line of text given a file name and line number
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

def getval(filename, line_number):
  with open(filename) as file:
    lines = file.readlines()
  if (line_number <= len(lines)):
    return lines[line_number-1]
  else:
    print("Line", line_number, "not in file.")
    print("File has", len(lines), "lines.")



# rename the template input file accordingly
try:
    os.rename('ell_mdamb231.egsinp','ell_mdamb'+CellModel+'.egsinp')
except:
    pass
try:
    os.rename('ell_mdamb361.egsinp','ell_mdamb'+CellModel+'.egsinp')
except:
    pass
try:
    os.rename('ell_mdamb468.egsinp','ell_mdamb'+CellModel+'.egsinp')
except:
    pass

# Apply changes/updates to the ellipsoid builder python file and base input file

builder = "build_ellipsoids.py"
baseinput = 'ell_mdamb'+CellModel+'.egsinp'

if (CellModel == '468'):
    replace_line(builder, 37, "NucleusMajorAxis = 1.0600000000E-03")
    replace_line(builder, 38, "NucleusMinorAxis = 3.7476659403E-04")
    replace_line(builder, 40, "CytoplasmMajorAxis = 1.5000000000E-03")
    replace_line(builder, 41, "CytoplasmMinorAxis = 5.3033008589E-04")
    replace_line(builder, 43, "MembraneMajorAxis = 1.5010000000E-03")
    replace_line(builder, 44, "MembraneMinorAxis = 5.3133008589E-04")
    
    replace_line(baseinput, 172, "\t\tcavity mass = 1.7749990196E-09")
    replace_line(baseinput, 180, "\t\tcavity mass = 6.2361451932E-10")
    replace_line(baseinput, 188, "\t\tcavity mass = 1.1435313483E-09")
    replace_line(baseinput, 196, "\t\tcavity mass = 7.8531519094E-12")
    replace_line(baseinput, 205, "\t\tcavity mass = 6.2361451932E-10")
    replace_line(baseinput, 213, "\t\tcavity mass = 1.1435313483E-09")
    replace_line(baseinput, 221, "\t\tcavity mass = 7.8531519094E-12")
    replace_line(baseinput, 229, "\t\tcavity mass = 1.7749990196E-09")
    
elif (CellModel == '361'):
    replace_line(builder, 37, "NucleusMajorAxis = 1.1600000000E-03")
    replace_line(builder, 38, "NucleusMinorAxis = 4.1012193309E-04")
    replace_line(builder, 40, "CytoplasmMajorAxis = 1.7600000000E-03")
    replace_line(builder, 41, "CytoplasmMinorAxis = 6.2225396744E-04")
    replace_line(builder, 43, "MembraneMajorAxis = 1.7610000000E-03")
    replace_line(builder, 44, "MembraneMinorAxis = 6.2325396744E-04")
    
    replace_line(baseinput, 172, "\t\tcavity mass = 2.8653525769E-09")
    replace_line(baseinput, 180, "\t\tcavity mass = 8.1728323444E-10")
    replace_line(baseinput, 188, "\t\tcavity mass = 2.0372600040E-09")
    replace_line(baseinput, 196, "\t\tcavity mass = 1.0809338469E-11")
    replace_line(baseinput, 205, "\t\tcavity mass = 8.1728323444E-10")
    replace_line(baseinput, 213, "\t\tcavity mass = 2.0372600040E-09")
    replace_line(baseinput, 221, "\t\tcavity mass = 1.0809338469E-11")
    replace_line(baseinput, 229, "\t\tcavity mass = 2.8653525769E-09")
    
elif (CellModel == '231'):
    replace_line(builder, 37, "NucleusMajorAxis = 1.0600000000E-03")
    replace_line(builder, 38, "NucleusMinorAxis = 3.7476659403E-04")
    replace_line(builder, 40, "CytoplasmMajorAxis = 1.9200000000E-03")
    replace_line(builder, 41, "CytoplasmMinorAxis = 6.7882250994E-04")
    replace_line(builder, 43, "MembraneMajorAxis = 1.9210000000E-03")
    replace_line(builder, 44, "MembraneMinorAxis = 6.7982250994E-04")
    
    replace_line(baseinput, 172, "\t\tcavity mass = 3.7188362478E-09")
    replace_line(baseinput, 180, "\t\tcavity mass = 6.2361451932E-10")
    replace_line(baseinput, 188, "\t\tcavity mass = 3.0823589713E-09")
    replace_line(baseinput, 196, "\t\tcavity mass = 1.2862757191E-11")
    replace_line(baseinput, 205, "\t\tcavity mass = 6.2361451932E-10")
    replace_line(baseinput, 213, "\t\tcavity mass = 3.0823589713E-09")
    replace_line(baseinput, 221, "\t\tcavity mass = 1.2862757191E-11")
    replace_line(baseinput, 229, "\t\tcavity mass = 3.7188362478E-09")
else:
   print("ERROR: CELL MODEL NOT RECOGNIZED")
    
if (Angle == '90'):
    replace_line(builder, 54, 'Angle = pi/2')
elif (Angle == '45'):
    replace_line(builder, 54, 'Angle = pi/4')
elif (Angle == '00'):
    replace_line(builder, 54, 'Angle = 0')
else:
   print("ERROR: ANGLE NOT RECOGNIZED")



# Regions for 100 segments

#membrane1 = " 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 "
#cytoplasm1 = " 101 201 301 401 501 601 701 801 901 1001 1101 1201 1301 1401 1501 1601 1701 1801 1901 2001 2101 2201 2301 2401 2501 2601 2701 2801 2901 3001 3101 3201 3301 3401 3501 3601 3701 3801 3901 4001 4101 4201 4301 4401 4501 4601 4701 4801 4901 5001 5101 5201 5301 5401 5501 5601 5701 5801 5901 6001 6101 6201 6301 6401 6501 6601 6701 6801 6901 7001 7101 7201 7301 7401 7501 7601 7701 7801 7901 8001 8101 8201 8301 8401 8501 8601 8701 8801 8901 9001 9101 9201 9301 9401 9501 9601 9701 9801 9901 10001 "
#nucleus1 = " 10101 20101 30101 40101 50101 60101 70101 80101 90101 100101 110101 120101 130101 140101 150101 160101 170101 180101 190101 200101 210101 220101 230101 240101 250101 260101 270101 280101 290101 300101 310101 320101 330101 340101 350101 360101 370101 380101 390101 400101 410101 420101 430101 440101 450101 460101 470101 480101 490101 500101 510101 520101 530101 540101 550101 560101 570101 580101 590101 600101 610101 620101 630101 640101 650101 660101 670101 680101 690101 700101 710101 720101 730101 740101 750101 760101 770101 780101 790101 800101 810101 820101 830101 840101 850101 860101 870101 880101 890101 900101 910101 920101 930101 940101 950101 960101 970101 980101 990101 1000101 "

#membrane2 = " 1010101 1010102 1010103 1010104 1010105 1010106 1010107 1010108 1010109 1010110 1010111 1010112 1010113 1010114 1010115 1010116 1010117 1010118 1010119 1010120 1010121 1010122 1010123 1010124 1010125 1010126 1010127 1010128 1010129 1010130 1010131 1010132 1010133 1010134 1010135 1010136 1010137 1010138 1010139 1010140 1010141 1010142 1010143 1010144 1010145 1010146 1010147 1010148 1010149 1010150 1010151 1010152 1010153 1010154 1010155 1010156 1010157 1010158 1010159 1010160 1010161 1010162 1010163 1010164 1010165 1010166 1010167 1010168 1010169 1010170 1010171 1010172 1010173 1010174 1010175 1010176 1010177 1010178 1010179 1010180 1010181 1010182 1010183 1010184 1010185 1010186 1010187 1010188 1010189 1010190 1010191 1010192 1010193 1010194 1010195 1010196 1010197 1010198 1010199 1010200 "
#cytoplasm2 = " 1010201 1010301 1010401 1010501 1010601 1010701 1010801 1010901 1011001 1011101 1011201 1011301 1011401 1011501 1011601 1011701 1011801 1011901 1012001 1012101 1012201 1012301 1012401 1012501 1012601 1012701 1012801 1012901 1013001 1013101 1013201 1013301 1013401 1013501 1013601 1013701 1013801 1013901 1014001 1014101 1014201 1014301 1014401 1014501 1014601 1014701 1014801 1014901 1015001 1015101 1015201 1015301 1015401 1015501 1015601 1015701 1015801 1015901 1016001 1016101 1016201 1016301 1016401 1016501 1016601 1016701 1016801 1016901 1017001 1017101 1017201 1017301 1017401 1017501 1017601 1017701 1017801 1017901 1018001 1018101 1018201 1018301 1018401 1018501 1018601 1018701 1018801 1018901 1019001 1019101 1019201 1019301 1019401 1019501 1019601 1019701 1019801 1019901 1020001 1020101 "
#nucleus2 = " 1020201 1030201 1040201 1050201 1060201 1070201 1080201 1090201 1100201 1110201 1120201 1130201 1140201 1150201 1160201 1170201 1180201 1190201 1200201 1210201 1220201 1230201 1240201 1250201 1260201 1270201 1280201 1290201 1300201 1310201 1320201 1330201 1340201 1350201 1360201 1370201 1380201 1390201 1400201 1410201 1420201 1430201 1440201 1450201 1460201 1470201 1480201 1490201 1500201 1510201 1520201 1530201 1540201 1550201 1560201 1570201 1580201 1590201 1600201 1610201 1620201 1630201 1640201 1650201 1660201 1670201 1680201 1690201 1700201 1710201 1720201 1730201 1740201 1750201 1760201 1770201 1780201 1790201 1800201 1810201 1820201 1830201 1840201 1850201 1860201 1870201 1880201 1890201 1900201 1910201 1920201 1930201 1940201 1950201 1960201 1970201 1980201 1990201 2000201 2010201 "

# lines of code for listing the region labels and writing them into the input file
SegmentNumber=50
Segments = SegmentNumber*2 # SegmentNumber * 2
Label = 1

with open('labels.txt', 'w') as f:
    f.write("Cell 1 Membrane \n")
    for i in range (0,Segments):
        #print(Label)
        f.write(f"{Label} ")
        Label = Label + 1

    f.write("\n\nCell 1 Cytoplasm \n")
    for i in range (0,Segments):
        #print(Label)
        f.write(f"{Label} ")
        Label = Label + Segments

    f.write("\n\nCell 1 Nucleus \n")
    for i in range (0,Segments):
        #print(Label)
        f.write(f"{Label} ")
        Label = Label + Segments**2

    f.write("\n\nCell 2 Membrane \n")
    for i in range (0,Segments):
        #print(Label)
        f.write(f"{Label} ")
        Label = Label + 1

    f.write("\n\nCell 2 Cytoplasm \n")
    for i in range (0,Segments):
        #print(Label)
        f.write(f"{Label} ")
        Label = Label + Segments

    f.write("\n\nCell 2 Nucleus \n")
    for i in range (0,Segments):
        #print(Label)
        f.write(f"{Label} ")
        Label = Label + Segments**2


membrane1 = getval("labels.txt",2).strip("\n")
cytoplasm1 = getval("labels.txt",5).strip("\n")
nucleus1 = getval("labels.txt",8).strip("\n")

membrane2 = getval("labels.txt",11).strip("\n")
cytoplasm2 = getval("labels.txt",14).strip("\n")
nucleus2 = getval("labels.txt",17).strip("\n")

filename="ell_mdamb"+CellModel+".egsinp"

replace_line(filename, 128, "\t\tset label = membrane1 "+membrane1)
replace_line(filename, 129, "\t\tset label = cytoplasm1 "+cytoplasm1)
replace_line(filename, 130, "\t\tset label = nucleus1 "+nucleus1)

replace_line(filename, 132, "\t\tset label = membrane2 "+membrane2)
replace_line(filename, 133, "\t\tset label = cytoplasm2 "+cytoplasm2)
replace_line(filename, 134, "\t\tset label = nucleus2 "+nucleus2)





