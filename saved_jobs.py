from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    jobs = anvil.server.call('get_saved_jobs')
    self.repeating_panel_1.items = jobs
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')