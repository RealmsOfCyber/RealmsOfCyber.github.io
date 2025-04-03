from jinja2 import Environment, FileSystemLoader
from variables import *

# load templates folder to environment (security measure)
env = Environment(loader=FileSystemLoader('templates'))

# load the `index.jinja` template
index_template = env.get_template('index.jinja')
output_from_parsed_template = index_template.render(
  year=year,
  become_a_sponsor_url=become_a_sponsor_url,
  sponsors=sponsors
)

# write the parsed template
with open("site/index.html", "w") as chap_page:
  chap_page.write(output_from_parsed_template)
