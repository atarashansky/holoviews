"""
An example app demonstrating how to use the HoloViews API to generate
a bokeh app with complex interactivity. Uses a Selection1D stream
to compute the mean y-value of the current selection.

The app can be served using:

    bokeh serve --show selection_stream.py
"""

import numpy as np
import holoviews_samap as hv
from holoviews_samap.streams import Selection1D

renderer = hv.renderer('bokeh')
hv.opts("Points [tools=['box_select']]")

data = np.random.multivariate_normal((0, 0), [[1, 0.1], [0.1, 1]], (1000,))
points = hv.Points(data)
sel = Selection1D(source=points)
mean_sel = hv.DynamicMap(lambda index: hv.HLine(points.iloc[index]['y'].mean()
                                                if index else -10),
                         kdims=[], streams=[sel])

doc = renderer.server_doc(points * mean_sel)
doc.title = 'HoloViews Selection Stream'
