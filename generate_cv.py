import yaml
from jinja2 import Environment, FileSystemLoader
import markdown
import pdfkit

# Fichiers
DATA_FILE = "data/cv_data.yaml"
TEMPLATE_DIR = "templates"
TEMPLATE_MD = "cv_template.md"
OUTPUT_MD = "output/cv.md"
OUTPUT_PDF = "output/cv.pdf"
CSS_FILE = "templates/style_with_banner.css"

# Charge YAML
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Template
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_MD)
rendered_md = template.render(**data)

# Sauvegarde Markdown
with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write(rendered_md)

# Markdown → HTML
html = markdown.markdown(rendered_md)

# HTML → PDF
pdfkit.from_string(html, OUTPUT_PDF, css=CSS_FILE)

print("CV généré dans output/cv.pdf")
# Génère un CV en PDF à partir de données YAML et d'un template Markdown