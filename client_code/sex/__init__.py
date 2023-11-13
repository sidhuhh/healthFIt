from ._anvil_designer import sexTemplate
from anvil import *

class sex(sexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('weight')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('weight')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('weight')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('weight')

