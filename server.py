import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def save_job(item):
  app_tables.jobs.add_row(title=item['title'], company_name=item['company_name'], url=item['url'])
  
@anvil.server.callable
def get_saved_jobs():
  return app_tables.jobs.search()

@anvil.server.callable
def delete_job(item):
  rows = app_tables.jobs.search(title=item['title'], company_name=item['company_name'], url=item['url'])
  for r in rows:
    r.delete()