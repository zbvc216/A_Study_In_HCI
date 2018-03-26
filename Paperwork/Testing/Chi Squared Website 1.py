import scipy.stats as stats


print '\nLook t-test ='
a = [8,10,9,8,8,7,9,8,8,9,9,8,8,5,9,8,7,10,8,8,9,10,10,7,8,9,9,8]
b = [8,6,8,7,7,8,8,7,5,9,9,7,9,8,8,9,6,10,8,5,8,8,10,9,7,9,4,10]
tStatistic, pValue = stats.ttest_rel(a,b)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nFeel t-test ='
a = [7,10,10,7,7,7,8,8,8,9,9,9,9,10,10,10,10,10,8,9,10,10,10,7,8,9,9,10]
b = [7,10,10,7,6,7,7,8,7,9,9,9,8,10,9,9,10,10,8,8,10,10,10,7,8,9,9,10]
tStatistic, pValue = stats.ttest_rel(a,b)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nFormal chi squared ='
a = [21, 7]
b = [2, 26]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value 3 =', ("{0:.3f}".format(pValue))

print '\nInformal chi squared ='
a = [2, 26]
b = [18, 10]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nRelaxing chi squared ='
a = [4, 24]
b = [18, 10]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nPreferred chi squared ='
a = [16, 12]
b = [12, 16]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value =', ("{0:.3f}".format(pValue))