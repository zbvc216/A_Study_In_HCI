import scipy.stats as stats


print '\nLook t-test ='
a = [7,5,6,6,4,5,4,7,6,6,3,3,6,6,6,5,6,3,5,6,2,6,8,4,7,5,1,7]
b = [9,7,9,9,8,8,9,9,8,9,8,8,8,8,7,8,10,8,8,8,8,8,9,8,9,8,7,7]
tStatistic, pValue = stats.ttest_rel(a,b)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nFeel t-test ='
a = [7,5,6,6,4,5,4,7,6,6,3,3,6,6,6,5,6,3,5,6,2,6,8,4,7,5,1,7]
b = [9,7,9,9,8,8,9,9,8,9,8,8,8,8,7,8,10,8,8,8,8,8,9,8,9,8,7,7]
tStatistic, pValue = stats.ttest_rel(a,b)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nNavigation t-test ='
a = [8,3,4,6,2,5,1,6,1,9,5,3,1,6,2,3,7,1,6,7,1,6,6,3,7,2,1,8]
b = [10,10,10,9,8,10,10,9,10,6,9,10,8,9,10,9,10,10,9,10,9,8,10,8,9,8,6,6]
tStatistic, pValue = stats.ttest_rel(a,b)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nProfessional chi squared ='
a = [0, 28]
b = [24, 4]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value 3 =', ("{0:.3f}".format(pValue))

print '\nClean chi squared ='
a = [3, 25]
b = [21, 7]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nMessy chi squared ='
a = [13, 15]
b = [0, 28]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value =', ("{0:.3f}".format(pValue))

print '\nPreferred chi squared ='
a = [1, 27]
b = [27, 1]
obs = [a, b]
chi2, pValue, dof, expected = stats.chi2_contingency(obs)
print 'p-value =', ("{0:.3f}".format(pValue))