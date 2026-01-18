import os
import yaml
from jinja2 import Environment, FileSystemLoader
import markdown
import pdfkit
from docx import Document

# ===================== PATHS =====================

DATA_FILE = "data/cv_data.yaml"
TEMPLATE_DIR = "templates"
MD_TEMPLATE = "cv_template.md"
CSS_TEMPLATE = "style_template.css"

OUTPUT_DIR = "output"
MD_OUTPUT = os.path.join(OUTPUT_DIR, "cv.md")
HTML_OUTPUT = os.path.join(OUTPUT_DIR, "cv.html")
PDF_OUTPUT = os.path.join(OUTPUT_DIR, "cv.pdf")
DOCX_OUTPUT = os.path.join(OUTPUT_DIR, "cv.docx")
CSS_OUTPUT = os.path.join(OUTPUT_DIR, "generated_style.css")

WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===================== STYLE =====================

style = {
    "font_size": 10.8,
    "line_height": 1.30,
    "margin": 0.70,
    "header_padding": 12,
    "section_spacing": 6,
    "title_size": 22,
    "subtitle_size": 10.5,
    "section_title_size": 14,
    "item_title_size": 11.5,
}

# ===================== LOAD DATA =====================

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
md_template = env.get_template(MD_TEMPLATE)
css_template = env.get_template(CSS_TEMPLATE)

# ===================== GENERATE MD =====================

rendered_md = md_template.render(**data)

with open(MD_OUTPUT, "w", encoding="utf-8") as f:
    f.write(rendered_md)

# ===================== MD → HTML =====================

html_body = markdown.markdown(rendered_md)
html = f"""
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
{html_body}
</body>
</html>
"""

with open(HTML_OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

# ===================== GENERATE PDF =====================

css = css_template.render(**style)

with open(CSS_OUTPUT, "w", encoding="utf-8") as f:
    f.write(css)

pdfkit.from_file(
    HTML_OUTPUT,
    PDF_OUTPUT,
    css=CSS_OUTPUT,
    configuration=config
)

# ===================== GENERATE DOCX =====================

doc = Document()
for line in rendered_md.split("\n"):
    doc.add_paragraph(line)
doc.save(DOCX_OUTPUT)

# ===================== DONE =====================

print("✅ CV généré avec succès :")
print("- output/cv.md")
print("- output/cv.pdf")
print("- output/cv.docx")
