import ROOT
from ROOT import gStyle

histo = ROOT.TH1F("histo","Histogram Title",20,-10,-10)

canvas = ROOT.TCanvas()
for x in range(0,1000):
	histo.Fill(ROOT.gRandom.Gaus(0,2))

myFunc = ROOT.TF1("Function Name","[0]*exp(-0.5*((x-[1])/[2])^2)",-10,10)

myFunc.SetParameters(1.0, 1.0, 1.0)
gStyle.SetOptFit(1111)
histo.Fit(myFunc)

canvas.SaveAs("fit.png")