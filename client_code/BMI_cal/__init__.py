from ._anvil_designer import BMI_calTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class BMI_cal(BMI_calTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    height = float(self.text_height.text)
    weight = float(self.text_weight.text)
    BMI = weight/(height**2)
    self.label_answer.text = f'your BMI is: {BMI}
