# Program just to see what colors are in the plotly colorscales.
# This program is VERY short (just 4 lines! excluding comments/whitespace)
from plotly import colors

print(colors.PLOTLY_SCALES)
print("\n")

for key in colors.PLOTLY_SCALES.keys():
    print(key)