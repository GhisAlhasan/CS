


import nsfg
import thinkplot
import thinkstats2


pres = nsfg.ReadFemResp()

preshist = thinkstats2.Hist(pres)

age = thinkstats2.Hist(pres.fmar1age)

print (sorted(age.Values()))
thinkplot.Hist(age)
thinkplot.Show(xlabel='age', ylabel='frequency')

marriagenum=thinkstats2.Hist(pres.fmarno)

print (sorted(marriagenum.Values()))
thinkplot.Hist(marriagenum)
thinkplot.Show(xlabel='mariages #', ylabel='frequency')

income=thinkstats2.Hist(pres.totincr)
print (sorted(income.Values()))
thinkplot.Hist(income)
thinkplot.Show(xlabel='income', ylabel='frequency')

width = 0.30
neverMarried = pres[pres.fmarno == 0]
Married = pres[pres.fmarno != 0]
never = thinkstats2.Hist(neverMarried.totincr, label = "Never Married")
married = thinkstats2.Hist(Married.totincr, label = "Married")

thinkplot.Hist(never, align= "left", width = width)
thinkplot.Hist(married, width = width)
thinkplot.Show(xlabel='income', ylabel='frequency')


NeverMarriedMean = neverMarried.totincr.mean()
NeverMarriedMin = neverMarried.totincr.min()
NeverMarriedMax = neverMarried.totincr.max()
NeverMarriedVar = neverMarried.totincr.var()
NeverMarriedSTD = neverMarried.totincr.std()

MarriedMean = Married.totincr.mean()
MarriedMin = Married.totincr.min()
MarriedMax = Married.totincr.max()
MarriedVar = Married.totincr.var()
MarriedSTD = Married.totincr.std()

for i in ["Never Married Mean: "+str(NeverMarriedMean), "Married Mean: "+str(MarriedMean), "Never Married Minimum: " + str(NeverMarriedMin), "Married Minimum: "+str(MarriedMin), "Never Married Max: " + str(NeverMarriedMax),"Married Max: " + str(MarriedMax), "Never Married Variance: " + str(NeverMarriedVar), "Married Variance: " + str(MarriedVar), "NeverMarried Standard Deviation: " + str(NeverMarriedSTD), "Married Standard Deviation: " + str(MarriedSTD)]:
    print i

