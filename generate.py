from jinja2 import Environment, FileSystemLoader
from variables import *
from sponsors import sponsors
from speakers import speakers

# load templates folder to environment (security measure)
env = Environment(loader=FileSystemLoader('templates'))

# load the `index.jinja` template
index_template = env.get_template('index.jinja')
output_from_parsed_template = index_template.render(
  year=year,
  date=date,
  become_a_sponsor_url=become_a_sponsor_url,
  sponsors=sponsors,
  speakers=speakers,
  sponsor_blurb=sponsor_blurb,
 tickets_on_sale=tickets_on_sale,
 ticket_url=ticket_url,
 ticket_price=ticket_price,
  last_year_highlights=last_year_highlights
)

# write the parsed template
with open("site/index.html", "w") as chap_page:
  chap_page.write(output_from_parsed_template)
