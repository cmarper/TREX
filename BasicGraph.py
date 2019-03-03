
import root 

graph = ROOT.TGraph()

n = 10
for i in range(n):
		x = i
		y = x*x
		graph.SetPoint(i,x,y)

canvas = ROOT.TCanvas()
graph.Draw()
canvas.SaveAs("graph.png")