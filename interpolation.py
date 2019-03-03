import ROOT
from ROOT import *

##################################

# Graph canvas for plotting
cGraph = ROOT.TCanvas() 


# X, Y positions of sources, plus correction factor (z)
x = [10, 20, 40,100, 200, 20, 180,80,50]
y = [100, 50, 10,20,40, 10,180,90,140]
z = [80, 20, 100,40,60, 15,100, 20,80]

# fill in the TGraph
graph =  TGraph2D()
i = 0
for i in range(0,len(x)):
    graph.SetPoint(i,x[i],y[i],z[i]);

# plot the surface graph (of colz graph)
# documentation in https://root.cern.ch/doc/master/classTGraph2D.html
cGraph.Draw()    
cGraph.cd()
graph.Draw("surf1");
cGraph.Update()
cGraph.Modified()

# I think you could get the interpolation easily from here: if you draw the 2D graph with "colz" option, it will be drawn like a
# 2D histogram making an interpolation of the points; there must be a way to extract it (like graph.GetHistogram() or something).
# Maybe it also works with "surf1" option. It is poorly interpolated though, and I don't know if there is a way to make a finer binning...
# Making a new histo is probably better

# get the 2D histogram with interpolated values (finer binning)

histo = ROOT.TH2D("histo","histo",200,0,200,200,0,200);
cHisto = ROOT.TCanvas("cHisto","2D interpolate example",0,0,600,600);
for i in range (1,200):
    for j in range(1,200):
        z_int = graph.Interpolate(i,j)
        histo.SetBinContent(i,j,z_int)
   
cHisto.Draw()   
histo.Draw("colz");
cHisto.Update()
cHisto.Modified()


raw_input()
