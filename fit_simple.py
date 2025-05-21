import pycorrfit
import matplotlib.pyplot as plt

data_path = "sample_data/sample.fcs"
data = pycorrfit.readfiles.open_any(data_path)

for trace in data['Trace']:
    plt.plot(trace[:,0],trace[:,1])

plt.show()

for trace in data['Correlation']:
    plt.plot(trace[:,0],trace[:,1])
plt.xscale('log')  # Set x-axis to logarithmic scale

plt.show()