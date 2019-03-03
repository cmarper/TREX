import ROOT
import random

canvas = ROOT.TCanvas("canvas","canvas",600,600)
hPoisson = ROOT.TH1F("histo","Poisson Distribution",50,0,50)

l = 10

for i in range(0,10000):
    
    U = random.random()
    n = 0
    
    q = ROOT.TMath.Exp(-l)
    p = q
    F = q
    

    while (U > F):
            n+=1
            p*=l/float(n)
            F+=p

    X = n
    hPoisson.Fill(X)

#normalize to 1
norm = hPoisson.Integral()
hPoisson.Scale(1/float(norm))

hPoissonROOT = ROOT.TH1F("histoROOT","Poisson Distribution",50,0,50)
for i in range(0,10000):
    N = ROOT.gRandom.Poisson(10)
    hPoissonROOT.Fill(N)
    
#normalize to 1
norm = hPoissonROOT.Integral()
hPoissonROOT.Scale(1/float(norm))


hPoisson.SetLineColor(4)
hPoisson.SetFillColor(4)
hPoisson.GetXaxis().SetTitle("X")
hPoisson.Draw('hist')

hPoissonROOT.Draw('same hist')
hPoissonROOT.SetLineColor(2)
hPoissonROOT.SetLineWidth(2)


ROOT.gStyle.SetOptStat(0)

leg = ROOT.TLegend(0.55,0.78,0.89,0.89)
leg.AddEntry(hPoisson,"Inversion method","f")
leg.AddEntry(hPoissonROOT,"TRandom","l")
leg.Draw('same')

canvas.Update()
canvas.Modify()
canvas.Draw()
raw_input()