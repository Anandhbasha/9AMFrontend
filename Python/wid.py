# %%
import ipywidgets as wid
from IPython.display import display
slider = wid.FloatSlider(min=0,max=10,value=20)
display(slider)

text = wid.Text(value="", placeholder = "Please enter your name", description = "Name")

display(text)
textarea = wid.Text(value="", placeholder = "Please enter your comments", description = "Comments")
display(textarea)
# %%