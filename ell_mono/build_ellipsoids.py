import math
from decimal import Decimal

#Approximate an ellipsoid as conestacks

"""
Ellipsoid Equation

x2/NucleusMajorAxis + y2/NucleusMinorAxis + z2/c2 = 1
x2/NucleusMajorAxis + y2/NucleusMinorAxis = 1

"""

#Cell Model Spherical Dimensions; EVERYTHING IS IN CENTIMETERS w/o ScalingFactor!!!

ScalingFactor = 10**(-4)# 1 for testing; 10e^-4 for actual, to micrometers
Round=10 #only applies to results of calculations; input should be manually rounded
Squeeze = math.sqrt(1/2) #how much the minor axes shorten
pi = math.pi # convenient value of pi

CytoplasmRadius = ScalingFactor*9.6
NucleusRadius = ScalingFactor*5.3
MembraneRadius = ScalingFactor*(9.6) + ScalingFactor*10**(-2)

#Convert spherical cell model into an ellipsoid; major axis is doubled and the minor is multiplied by sqrt(1/2)
"""
CytoplasmMajorAxis=CytoplasmRadius * 2 #major axis length
CytoplasmMinorAxis=CytoplasmRadius * Squeeze #minor axis length

NucleusMajorAxis = NucleusRadius*2#nucleus models axes
NucleusMinorAxis = NucleusRadius * Squeeze

MembraneMajorAxis=MembraneRadius*2
MembraneMinorAxis=MembraneRadius * Squeeze
"""

NucleusMajorAxis = 1.0600000000E-03
NucleusMinorAxis = 3.7476659403E-04

CytoplasmMajorAxis = 1.9200000000E-03
CytoplasmMinorAxis = 6.7882250994E-04

MembraneMajorAxis = 1.9210000000E-03
MembraneMinorAxis = 6.7982250994E-04

#Geometry 'resolution' parameter; total number of segment would be twice this number
SegmentNumber = 50 #minimum 1 for one half of the ellipsoid

TotalVolume = 0

Material = 'estar_unit_density_water'

#Center of 2nd cell model
Angle = pi/4
#cartesian coordinates of the center of 2nd cell
X2 = 2*MembraneMajorAxis*math.cos(Angle) 
Y2 = 2*MembraneMinorAxis*math.sin(Angle) 

#function for finding the radius of a circle consisting a cross section of the ellipse along the minor axis
def CrossSectionRadius(Major, Minor, Xvalue): 
    Yvalue = Minor*math.sqrt(abs((Xvalue**(2))/(Major**(2))-1))
    return Yvalue

#function for building the ellipsoid models
def BuildEllipsoid(inp_SegmentNumber, MajorAxis, MinorAxis, FileName, Designation,Material, X, Y):
    TotalVolume = 0
    inp_SegmentThickness = MajorAxis/inp_SegmentNumber
    df = open(FileName, 'w')
    """
    df.write('\n:start media defintion:')
    df.write('\n\t ae=0.512')
    df.write('\n\t:start estar_unit_density_water:')
    df.write('\n\t\tdensity correction file = ')
    df.write(Material)
    df.write('\n\t:stop estar_unit_density_water:')
    df.write('\n:stop media definition:')
    """
    df.write('\n:start geometry definition: \n:start geometry:')
    df.write('\nlibrary = egs_cones \n type = EGS_ConeStack \nname = ')
    df.write(Designation)
    df.write('\naxis = ')
    df.write(str(X-MajorAxis))
    df.write(' ')
    df.write(str(Y))
    df.write(' 0 1 0 0')
    j=0

    for i in range(int(inp_SegmentNumber),0,-1):
        lower_radius = round(CrossSectionRadius(MajorAxis, MinorAxis, (i-1)*(inp_SegmentThickness)),Round)
        upper_radius = round(CrossSectionRadius(MajorAxis, MinorAxis, (i)*(inp_SegmentThickness)),Round)
        segment_thickness = inp_SegmentThickness
        layer = str(j)

        #print("Segment",j,"\t\t Lower Radius:",lower_radius,"\t\t Upper Radius:",upper_radius)

        df.write("\n:start layer: #")
        df.write(layer)
        df.write('\n')
        df.write("\t")
        df.write("thickness = ")
        df.write(str(segment_thickness))
        df.write('\n')
        df.write("\t")
        df.write("top radii = ")
        df.write(str(upper_radius))
        df.write('\n')
        df.write("\t")
        df.write("bottom radii = ")
        df.write(str(lower_radius))
        
        df.write("\n\tmedia = ")
        df.write(Material)
        
        df.write("\n:stop layer:")
        df.write('\n')
        j=j+1
        SegmentVolume = (pi*segment_thickness/3)*((lower_radius**2)+lower_radius*upper_radius+upper_radius**2)
        TotalVolume = TotalVolume + SegmentVolume
    #print(Designation,'first half done!')
    
    for i in range(0,int(inp_SegmentNumber)):
        lower_radius = round(CrossSectionRadius(MajorAxis, MinorAxis, (i+1)*inp_SegmentThickness),Round)
        upper_radius = round(CrossSectionRadius(MajorAxis, MinorAxis, (i)*inp_SegmentThickness),Round)
        segment_thickness = inp_SegmentThickness
        layer = str(j)

        #print("Segment",j,"\t\t Lower Radius:",lower_radius,"\t\t Upper Radius:",upper_radius   )

        df.write("\n:start layer: #")
        df.write(layer)
        df.write('\n')
        df.write("\t")
        df.write("thickness = ")
        df.write(str(segment_thickness))
        df.write('\n')
        df.write("\t")
        df.write("top radii = ")
        df.write(str(upper_radius))
        df.write('\n')
        df.write("\t")
        df.write("bottom radii = ")
        df.write(str(lower_radius))
        
        df.write("\n\tmedia = ")
        df.write(Material)
        
        df.write('\n')
        df.write(":stop layer:")
        df.write('\n')
        
        """
        :start media definition:

    ae  = 0.512 
    #ap  = lowest  energy for photon production   (kinetic)
    #ue  = maximum energy for electrons (kinetic+0.511)
    #up  = maximum energy for photons   (kinetic)

    :start estar_unit_density_water:
        density correction file    = estar_liquid_water
    :stop estar_unit_density_water:

:stop media definition:
        """
        j=j+1
        SegmentVolume = (pi*segment_thickness/3)*(lower_radius**2+lower_radius*upper_radius+upper_radius**2)
        TotalVolume = TotalVolume + SegmentVolume
    #print(Designation,'second half done!')
    
    df.write(':stop geometry: \nsimulation geometry = ')
    df.write(Designation)
    df.write('\n:stop geometry definition:')
    
    #print('Volume of one cell',TotalVolume)
    return TotalVolume


 


NucleusVolume = BuildEllipsoid(SegmentNumber,NucleusMajorAxis,NucleusMinorAxis,'ell_nucleus.geom','nucleus','estar_unit_density_water',0,0)

CytoplasmVolume = BuildEllipsoid(SegmentNumber,CytoplasmMajorAxis,CytoplasmMinorAxis,'ell_cytoplasm.geom','cytoplasm','estar_unit_density_water',0,0)

EllVolume = BuildEllipsoid(SegmentNumber,MembraneMajorAxis,MembraneMinorAxis,'ell_membrane.geom','membrane','estar_unit_density_water',0,0)

BuildEllipsoid(SegmentNumber,NucleusMajorAxis,NucleusMinorAxis,'ell_nucleus2.geom','nucleus','estar_unit_density_water',X2,Y2)

BuildEllipsoid(SegmentNumber,CytoplasmMajorAxis,CytoplasmMinorAxis,'ell_cytoplasm2.geom','cytoplasm','estar_unit_density_water',X2,Y2)

BuildEllipsoid(SegmentNumber,MembraneMajorAxis,MembraneMinorAxis,'ell_membrane2.geom','membrane','estar_unit_density_water',X2,Y2)


#print('\n')
#print('Major Axis Length\n\t',MembraneMajorAxis,'\nMinor Axis Length\n\t',MembraneMinorAxis)
#print(EllVolume)
CalculatedVolume = (4*pi/3)*(MembraneMajorAxis*MembraneMinorAxis*MembraneMinorAxis)
VolDiff = abs((EllVolume - CalculatedVolume)/CalculatedVolume)*100
print('Difference between calculated and actual volume\n\t',VolDiff)
#print(''VolDiff<0.01)
#print('Cell 2 origin point\n\t at (',X2,',', Y2,')')
#print('source cylinder size \n\th',2*MembraneMajorAxis,'r',MembraneMinorAxis)
#print('space size along x-axis:\n\t',6*MembraneMajorAxis)
#print('space size along y-axis:\n\t',6*MembraneMinorAxis)
#print('space size along z-axis:\n\t',2*MembraneMinorAxis)

"""
    Volume of each region
"""

print(f"Nuclear Volume : {NucleusVolume}")
print(f"Cytoplasmic Volume : {CytoplasmVolume-NucleusVolume}")
print(f"Membrane Volume : {EllVolume - CytoplasmVolume}")
print(f"Total Volume : {EllVolume}")


"""
    Script to generate the labels
"""
"""
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
"""
