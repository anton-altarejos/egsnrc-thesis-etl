"""

create the egsinp for radionuclides


"""

# Replace a line in a file
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
"""
tc99m_energies = "\t\t\tenergies = 0.0153 0.0178 0.0000429 0.00205 0.00232 0.00266 0.000116 0.000226 0.0000334 0.00182 0.119 0.137 0.14 0.122 0.14"
tc99m_yield = "\t\t\tprobabilities = 0.0126 0.0047 0.0193 0.0868 0.0137 0.0012 0.747 1.1 1.98 0.991 0.0843 0.0136 0.0037 0.0059 0.0025"

in111_energies="\t\t\tenergies = 0.0191 0.0223 0.0255 0.000183 0.00259 0.00306 0.00353 0.000125 0.00035 0.0000388 0.00000847 0.145 0.167 0.171 0.219 0.241 0.245"
in111_yield="\t\t\tprobabilities = 0.103 0.0394 0.0036 0.151 0.835 0.19 0.0109 0.915 2.09 2.54 7.82 0.0824 0.01 0.0014 0.0521 0.0091 0.0019"

i123_energies="\t\t\tenergies = 0.0224 0.0263 0.0302 0.000213 0.00304 0.00366 0.00428 0.000127 0.000461 0.0000298 0.0000325 0.000006 0.127 0.154 0.158"
i123_yield="\t\t\tprobabilities = 0.0838 0.0384 0.0035 0.156 0.751 0.202 0.013 0.869 1.97 2.1 6.54 2.18 0.13 0.0179 0.0053"

i125_energies="\t\t\tenergies = 0.0224 0.0264 0.0302 0.000219 0.00305 0.00367 0.00434 0.000127 0.000461 0.0000299 0.0000324 0.000006 0.00365 0.0306 0.0347"
i125_yield="\t\t\tprobabilities = 0.138 0.059 0.0065 0.264 1.25 0.34 0.0211 1.44 3.28 3.51 10.9 3.66 0.797 0.11 0.0284"

tl201_energies="\t\t\tenergies = 0.055 0.0663 0.0775 0.000773 0.00758 0.00985 0.012 0.000406 0.00183 0.000172 0.0000644 0.0000453 0.0000161 0.000895 0.0122 0.0159 0.0277 0.0174 0.0294 0.0522 0.121 0.133 0.0828 0.0843 0.153 0.165"
tl201_yield="\t\t\tprobabilities = 0.0268 0.0153 0.0015 0.322 0.541 0.235 0.0191 0.923 2.03 4.41 7.93 2.84 17.6 0.608 0.0022 0.0861 0.0236 0.0724 0.0237 0.0797 0.0152 0.0027 0.0025 0.159 0.0269 0.0094"
"""
#energies = [['tc99m',tc99m_energies,tc99m_yield],['in111',in111_energies,in111_yield],['i123',i123_energies,i123_yield],['i125',i125_energies,i125_yield],['tl201',tl201_energies,tl201_yield]]
regions = [["nucleus","\t\tselected regions = 1"],["cytoplasm","\t\tselected regions = 2"],["membrane","\t\tselected regions = 3"],["cell","\t\tselected regions = 1 2 3"]]
#yields = [tc99m_yield, in111_yield, i123_energies, i125_yield, tl201_yield]
energies=[1,3,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28,30,35,40,45,50,55,60,65,70,100]

filecounter = 0
for i in energies: #radionuclide spectra
  for j in regions: #source region
    filename = "sph_"+str(i).rjust(3, '0')+"_mdamb468_"+j[0]+".egsinp"
    replace_line(filename, 92, "\t\t\tenergy = "+str(0.001*i))
    #replace_line(filename, 93, i[2])
    replace_line(filename, 81, j[1])

    filename = "sph_"+str(i).rjust(3, '0')+"_mdamb361_"+j[0]+".egsinp"
    replace_line(filename, 92, "\t\t\tenergy = "+str(0.001*i))
    #replace_line(filename, 93, i[2])
    replace_line(filename, 81, j[1])

    filename = "sph_"+str(i).rjust(3, '0')+"_mdamb231_"+j[0]+".egsinp"
    replace_line(filename, 92, "\t\t\tenergy = "+str(0.001*i))
    #replace_line(filename, 93, i[2])
    replace_line(filename, 81, j[1])

    












    



