from ._anvil_designer import weightTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class weight(weightTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    weight = self.text_box_1.text
    anvil.server.call('next', weight=weight)
    open_form('height')
