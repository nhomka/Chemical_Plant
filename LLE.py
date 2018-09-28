import FluidStream as FS
import FermentationMassBalance as FMB
import TieLines as TL
import matplotlib.lines as lines
import matplotlib.pyplot as plt
from sympy import *
init_printing(use_unicode=True)

# Liquid Liquid Extraction Process
STAGE_COUNT = 8

# Raffinate Stream - fermentation output
mixer_mass = 280000
mixer_output_stream = FS.FluidStream(.005*mixer_mass, .00056*mixer_mass, 0, 0, 0, 0, 0, .9943*mixer_mass, 80)
raffinate_feed = mixer_output_stream
raffinate_feed_la_conc = raffinate_feed.LacticAcid / raffinate_feed.TotalMass

raffinate_out_mass = 296000
raffinate_output = FS.FluidStream(.04*raffinate_out_mass, .02*raffinate_out_mass, 0, 0, 0, 0, 0, .94*raffinate_out_mass, 80)
raffinate_output_la_conc = raffinate_output.LacticAcid / raffinate_output.TotalMass

# Extract Stream - Nearly pure octanol
extract_feed = FMB.output_stream
extract_feed_la_conc = extract_feed.LacticAcid / extract_feed.TotalMass

extract_output_water = raffinate_feed.Water + extract_feed.Water - raffinate_output.Water
extract_output_la = raffinate_feed.LacticAcid + extract_feed.LacticAcid - raffinate_output.LacticAcid
extract_output = FS.FluidStream(extract_output_water, extract_output_la, 0, 0, 0, 0, 0, 0, 80)
extract_output_la_conc = extract_output.LacticAcid / extract_output.TotalMass


# Mixed Stream
mixture_mass = raffinate_feed.TotalMass + extract_feed.TotalMass
mixture_la_conc = (extract_feed.LacticAcid + raffinate_feed.LacticAcid) / mixture_mass
yM = ((raffinate_feed.TotalMass*raffinate_feed_la_conc) + (extract_feed.TotalMass*extract_feed_la_conc)) / mixture_mass
print "yM Calc:", yM, extract_feed.TotalMass, extract_feed_la_conc

# Matrix math
v_n1_x = 1
dx = 0
iter_counter = 0
while abs(v_n1_x - dx) > .0001 and iter_counter < 50:
    v_n1_x = dx
    iter_counter += 1
    print iter_counter, "iter_counter"
    if v_n1_x == 0:
        matrix_11 = 1/((extract_feed_la_conc - raffinate_feed_la_conc)/(0 - .5))
    else:
        matrix_11 = 1/((extract_feed_la_conc - raffinate_feed_la_conc)/(0 - v_n1_x))
    matrix_34 = (.96 - extract_feed_la_conc)
    LLE_Matrix = Matrix([[matrix_11, 0, -1], [0, -1, -1], [1, -1, 0]])
    result_Matrix = Matrix([0, 0, matrix_34])
    print LLE_Matrix
    print result_Matrix

    inverse_Matrix = LLE_Matrix.inv()
    print inverse_Matrix

    multiply_matrices = inverse_Matrix * result_Matrix
    print multiply_matrices
    dy1 = multiply_matrices[0]
    dy2 = multiply_matrices[1]
    dx = multiply_matrices[2]

print dy1, dy2, dx

# Define Stream Lines
# Line (1) L(0) -- V(N+1)
L0_VN1_slope = (raffinate_feed_la_conc - extract_feed_la_conc) / (dx - 0)
L0_VN1_x_int = dx + ((0 - raffinate_feed_la_conc) / L0_VN1_slope)
L0_VN1_y_int = extract_feed_la_conc + (L0_VN1_slope * (0 - 0))
L0_VN1_x_data = [0, L0_VN1_x_int]
L0_VN1_y_data = [L0_VN1_y_int, 0]
line_L0_VN1 = lines.Line2D(L0_VN1_x_data, L0_VN1_y_data, linewidth=1, color="red")

# Line (2) L(0) -- V(1)
L0_V1_x_int_x = TL.x_tie_line_values[TL.find_nearest(TL.x_tie_line_values, raffinate_output_la_conc)]
print "find nearest:", L0_V1_x_int_x, raffinate_output_la_conc, TL.x_tie_line_values
L0_V1_x_int_y = raffinate_output_la_conc
L0_V1_y_int_x = 0
L0_V1_y_int_y = L0_VN1_y_int
L0_V1_x_data = [L0_V1_x_int_x, L0_V1_y_int_x]
L0_V1_y_data = [L0_V1_x_int_y, L0_V1_y_int_y]
L0_V1_slope = (L0_V1_x_int_y - L0_V1_y_int_y) / (L0_V1_x_int_x - L0_V1_y_int_y)
line_L0_V1 = lines.Line2D(L0_V1_x_data, L0_V1_y_data, linewidth=1, color="orange")
print L0_V1_x_int_x, L0_V1_x_int_y, L0_V1_y_int_x, L0_V1_y_int_y

# Mixture xM
xM = dx + ((yM - raffinate_feed_la_conc) / L0_VN1_slope)
print dx, yM, raffinate_feed_la_conc, L0_VN1_slope
V1x = L0_V1_x_int_x

# Line (3) L(N) -- V(1)
LN_V1_slope = (yM - raffinate_output_la_conc) / (xM - V1x)
LN_V1_x_int_x = xM - ((yM - 0) / LN_V1_slope)
print xM, yM, LN_V1_slope
LN_V1_x_int_y = 0
LN_V1_y_int_x = 0
LN_V1_y_int_y = extract_output_la_conc + (LN_V1_slope * (0 - 0))
print LN_V1_slope, LN_V1_x_int_x, LN_V1_y_int_y
LN_V1_x_data = [LN_V1_x_int_x, LN_V1_y_int_x]
LN_V1_y_data = [LN_V1_x_int_y, LN_V1_y_int_y]
line_LN_V1 = lines.Line2D(LN_V1_x_data, LN_V1_y_data, linewidth=1, color="blue")

# Line (4) L(N) -- V(N+1)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
eq_curve_x = [.96, .9541, .9482, .9423, .9364, .9305, .9246]
eq_curve_y = [0, .0059, .0118, .0177, .0236, .0295, .0354]
tie_line_y = [0, .02, .04, .06, .08, .10, .12]
ax.plot(eq_curve_x, eq_curve_y, '-o')
ax.add_line(line_L0_VN1)
ax.add_line(line_L0_V1)
ax.add_line(line_LN_V1)
for i in range(0, len(eq_curve_x), 1):
    ax.plot([0, eq_curve_x[i]], [tie_line_y[i], eq_curve_y[i]], '-o', color="black", linewidth=1, linestyle="dashed", markersize=3)
plt.show()


