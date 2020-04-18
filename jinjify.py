import os
from jinja2 import FileSystemLoader, Template, Environment

def main(folder='templates'):

    floader = FileSystemLoader(folder)
    env = Environment(loader=floader)
    for template in env.list_templates(extensions=['html']):
        
        rendered = env.get_template(template).render()
        equ = template == "index.html"
        with open(f"html/{template}" if template != "index.html" else "./index.html", 'w') as f:

            f.write(rendered)



if __name__ == "__main__":
    
    main()