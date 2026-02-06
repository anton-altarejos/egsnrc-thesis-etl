import pprint as pp
import pandas as pd

"""
This program will search a text file for a substring or sequence 
of characters and it will extract the row containing it.\n\n")

"""

energies=[1,3,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28,30,35,40,45,50,55,60,65,70,100]
types=['mdamb231','mdamb361','mdamb468']
type = types[2]
indices=[0,5,6,7,8] # locations of the data to be extracted; for later use

source_nucleus=[]
source_cytoplasm=[]
source_membrane=[]
source_cell=[]

#append the files names to lists for easy use
for i in energies:
   
    source_nucleus.append("sph_"+str(i).rjust(3, '0')+"_"+type+"_nucleus.egslog")
    source_cytoplasm.append("sph_"+str(i).rjust(3, '0')+"_"+type+"_cytoplasm.egslog")
    source_membrane.append("sph_"+str(i).rjust(3, '0')+"_"+type+"_membrane.egslog")
    source_cell.append("sph_"+str(i).rjust(3, '0')+"_"+type+"_cell.egslog")
"""
for i in energies:
    source_nucleus.append("sph_"+str(i).rjust(3, '0')+"_source_nucleus.egslog")
    source_cytoplasm.append("sph_"+str(i).rjust(3, '0')+"_source_cytoplasm.egslog")
    source_membrane.append("sph_"+str(i).rjust(3, '0')+"_source_membrane.egslog")
    source_cell.append("sph_"+str(i).rjust(3, '0')+"_source_cell.egslog")
"""
source_dict={ #filenames; dict key is outout file name
    "sph_source_nucleus":source_nucleus,
    "sph_source_cytoplasm":source_cytoplasm,
    "sph_source_membrane":source_membrane,
    "sph_source_cell":source_cell
}

#the keywords or labels for the data to be extracted 
#keywords = ['Isotropic source ','target_nucleus ','target_cytoplasm ','target_membrane ','total ']
key = 'main     '

# function for extracting data from a text file (.egslog in this case)
def extract(filenames): # filenames is a dict key
    data=[]#initialize list containing data
    for i in source_dict[filenames]:
        #print(i)
        file = open(i, 'r')
        filecontent = file.readlines()
        entries = [] # initiaize the list of the lines of text containing the keywords
        entries_cleaned = [] # initialize the list containing relevant data from entries

        for line in filecontent: #extract relevant entries
            #for item in range(1):
            if key in line:
                #print(line)
                line=line.replace('\n',' ').replace('\t',' ')
                entries.append(line)
        #print("entries")
        pp.pprint(entries)
        print(len(entries))
        
        
        
        
        for i in entries:
            entries_split = i.split()
            print(entries_split)
            entries_cleaned.append(float(entries_split[1]))
            if ('%' in entries_split[3]):
                entries_cleaned.append(100.0)
            else:
                entries_cleaned.append(float(entries_split[3]))
            #entries_cleaned.append(float(entries_split[3]))
            print(entries_cleaned)

        """
        for i in indices: #split the items in entries into indiv words and take only the values
            print(i)
            if i == 0:
                entries_split = entries[0].split()
                print(entries_split)
                #entries_cleaned.append(float(entries_split[10]))
            elif i in [5,6,7,8]:
                entries_split = entries[i].split()
                entries_cleaned.append(float(entries_split[1]))
                entries_cleaned.append(entries_split[3])
            #print(entries_cleaned)
            
            if len(entries_cleaned) == 9:
                print(f"Energy: {entries_cleaned[0]}",
                      f"\n Nucleus: {entries_cleaned[1]}\t{entries_cleaned[2]}",
                      f"\n Cytoplasm: {entries_cleaned[3]}\t{entries_cleaned[4]}",
                      f"\n Membrane: {entries_cleaned[5]}\t{entries_cleaned[6]}",
                      f"\n Total: {entries_cleaned[7]}\t{entries_cleaned[8]}\n")
        """
        
        data.append(entries_cleaned)
        
    #print(data)
    df = pd.DataFrame(data)
    df.to_csv(filenames+'.csv', index=False)
    print(f"\nCSV filename\t{filenames}.csv")
    

extract('sph_source_nucleus')
extract('sph_source_cytoplasm')
extract('sph_source_membrane')
extract('sph_source_cell')
#print(source_dict['source_nucleus'])

"""
#energies=[1,3]

names_energies=[]
filenames=[]
indices=[0,1,2,3,4] 
for i in energies:
    names_energies.append(str(i).rjust(3, '0'))

for i in names_energies:
    filenames.append(i+'_cytoplasm.egslog')


keywords = ['Isotropic source ','target_nucleus ','target_cytoplasm ','target_membrane ','total ']


compileddata = []

for i in filenames:
    print(i)
    file = open(i, 'r')
    filecontent = file.readlines()
    entries = [] # initiaize the list of the lines of text containing the keywords
    data = [] # initialize the list containing relevant data from entries
    


    for line in filecontent: #extract relevant entries
        for item in keywords:
            if item in line:
                #print(line)
                line=line.replace('\n',' ').replace('\t',' ')
                entries.append(line)

    for i in indices:
        if i == 0:
            entries_split = entries[0].split()
            data.append(entries_split[10])
        elif i in indices[1:5]:
            entries_split = entries[i].split()
            #print(extract_split)
            data.append(entries_split[1])
            data.append(entries_split[3])
    compileddata.append(data)
    #print(data)


pp.pprint(compileddata)
df = pd.DataFrame(compileddata)
df.to_csv('compiledvacuum.csv', index=False)
#pprint.pprint(rawdata[1][2][3])
"""


"""

#print(names_energies)
print(entries)



"""
"""
file = open('out.txt','r')
text = file.readlines()
list = ['Isotropic source ','target_nucleus ','target_cytoplasm ','target_membrane ','total ']
extract = [] #the lines containing the entries from list
data = [] #relevant data extracted from extract
"""
"""
for line in text:
    for item in list:
        if item in line:
            line=line.replace('\n',' ').replace('\t',' ')
            extract.append(line)
"""
#indices = [0,1,2,3,4]


"""
for i in indices:
    if i == 0:
        extract_split = extract[0].split()
        data.append(extract_split[10])
    elif i in indices[1:5]:
        extract_split = extract[i].split()
        #print(extract_split)
        data.append(extract_split[1])
        data.append(extract_split[3])
"""

#print(data)
"""
information inside data
electron energy, nuc_dose, nuc_dose error, cyt_dose, cyt_dose error, mem_dose, mem_dose error, total cell dose, total cell dose error
"""
