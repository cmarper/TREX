import ROOT

# 3 identical scintillators 
dimX = 20
dimY = 50

# Z position of the scintillators
Z1 = 0 
Z2 = -30
Z3 = -60

FirstHit = 10000 # number of iterations
SecondHit = 0	
ThirdHit = 0

# a muon is generated choosing a random point on the first scintillator and random direction
for i in range(FirstHit):
	# hit on first detector
	hitX1 = ROOT.gRandom.Uniform(0,dimX)
	hitY1 = ROOT.gRandom.Uniform(0,dimY)
	costheta = ROOT.gRandom.Uniform(-1/2,1/2)
	phi = ROOT.gRandom.Uniform(0,ROOT.TMath.Pi()*2)   
	theta = ROOT.TMath.ACos(costheta)
	R = Z2/costheta

	#hit on second detector
	X2 = R*ROOT.TMath.Sin(theta)*ROOT.TMath.Cos(phi)
	Y2 = R*ROOT.TMath.Sin(theta)*ROOT.TMath.Sin(phi)
	hitX2 = hitX1 + X2
	hitY2 = hitY1 + Y2
	
	if((hitX2>0) and (hitX2<dimX) and (hitY2>0) and (hitY2<dimY)):
		SecondHit +=1		
		#hit on third detector
		R = Z3/costheta
		X3 = R*ROOT.TMath.Sin(theta)*ROOT.TMath.Cos(phi)
		Y3 = R*ROOT.TMath.Sin(theta)*ROOT.TMath.Sin(phi)
		hitX3 = hitX1 + X3
		hitY3 = hitY1 + Y3
		
		if((hitX3>0) and (hitX3<dimX) and (hitY3>0) and (hitY3<dimY)):
			ThirdHit +=1

Fraction2 = SecondHit/float(FirstHit)
Fraction3 = ThirdHit/float(FirstHit)

print 'Fraction of muons hitting 2 scintillators = {0:.2f}'.format(Fraction2)
print 'Fraction of muons hitting 3 scintillators = {0:.2f}'.format(Fraction3)