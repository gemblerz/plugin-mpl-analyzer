import sys
from matplotlib import pyplot as plt

import act

try:
    import pyart

    PYART_AVAILABLE = True
except ImportError:
    PYART_AVAILABLE = False

input_file = sys.argv[1]
# Read in sample mini-MPL data
# files = act.tests.sample_files.EXAMPLE_SIGMA_MPLV5
obj = act.io.mpl.read_sigma_mplv5(
    filename=input_file,
    afterpulse="MMPL5037_Afterpulse_202008131600.bin",
    dead_time="MMPL5037_SPCM30891_Deadtime10.bin",
    overlap="MMPL5037_Overlap_201902140400.bin"
)

display = act.plotting.TimeSeriesDisplay(obj)
# display.time_height_scatter("channel_2")
display.plot("channel_2")
plt.show()

# # Create a PyART Radar Object
# radar = act.utils.create_pyart_obj(
#     obj, azimuth='azimuth_angle', elevation='elevation_angle', range_var='range'
# )
# # Creat Plot Display
# if PYART_AVAILABLE:
#     display = pyart.graph.RadarDisplay(radar)
#     display.plot('nrb_copol', sweep=0, title_flag=False, vmin=0, vmax=1.0, cmap='jet')
#     plt.show()