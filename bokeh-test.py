from bandit import Bandit
from bokeh import io
from bokeh.plotting import figure, output_file, show

bandit = Bandit()
io.output_file(bandit.output_dir + "my-cool-plot-for-alex.html")

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
# output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)
