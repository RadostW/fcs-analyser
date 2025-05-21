import os

import scipy.integrate
# Patch the missing `simps` alias for pycorfit
scipy.integrate.simps = scipy.integrate.simpson

import pycorrfit as pcf
from pycorrfit.correlation import Correlation
from pycorrfit.fit import Fit

import matplotlib.pyplot as plt

data_path = "sample_data/simple_sample.fcs"
data = pcf.readfiles.open_any(data_path)

corr = pcf.Correlation(
    correlation=data["Correlation"][0],
    traces=data["Trace"][0],
    corr_type=data["Type"][0],
    filename=os.path.basename(data_path),
    title="test correlation",
    fit_model=6012,
)

fitted = pcf.Fit(corr,global_fit=True)

# Plot individual traces
#

# for trace in data['Trace']:
#     plt.plot(trace[:,0],trace[:,1])
# plt.show()

fit_dict = {str(n):float(v) for n,v in zip(fitted.fit_parm_names, fitted.fit_parm)}
print(fit_dict)

for cor in data['Correlation']:
    plt.plot(cor[:,0],cor[:,1],'.',c='gray')
plt.xscale('log')  # Set x-axis to logarithmic scale

fitted_x = fitted.x
fitted_y = fitted.func(fitted.fit_parm, fitted.x)

plt.plot(fitted_x,fitted_y,'r-')
plt.show()
