from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    jobs = http.request('https://remotive.io/api/remote-jobs?limit=100', json = True)['jobs']
    self.repeating_panel_1.items = jobs

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')