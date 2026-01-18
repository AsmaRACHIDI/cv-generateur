<div class="header-banner">
<h1>{{ personal.first_name }} {{ personal.last_name }}</h1>
<p>{{ personal.title }}</p>
</div>

<div class="contact-info">
{{ personal.location }} · {{ personal.email }} · {{ personal.phone }}<br>
LinkedIn : {{ personal.linkedin }} · GitHub : {{ personal.github }}
</div>

## PROFIL
{{ profile }}

## COMPÉTENCES TECHNIQUES

<div class="skills-row">

<div class="skill-col">
<strong>Langages</strong>
<ul>{% for i in skills.languages %}<li>{{ i }}</li>{% endfor %}</ul>
</div>

<div class="skill-col">
<strong>Machine Learning & NLP</strong>
<ul>{% for i in skills.ml %}<li>{{ i }}</li>{% endfor %}</ul>
</div>

<div class="skill-col">
<strong>Deep Learning</strong>
<ul>{% for i in skills.deep_learning %}<li>{{ i }}</li>{% endfor %}</ul>
</div>

</div>

<div class="skills-row">

<div class="skill-col">
<strong>Bases de données</strong>
<ul>{% for i in skills.databases %}<li>{{ i }}</li>{% endfor %}</ul>
</div>

<div class="skill-col">
<strong>Visualisation</strong>
<ul>{% for i in skills.visualization %}<li>{{ i }}</li>{% endfor %}</ul>
</div>

<div class="skill-col">
<strong>Outils & Méthodes</strong>
<ul>{% for i in skills.tools %}<li>{{ i }}</li>{% endfor %}</ul>
</div>

</div>

## EXPÉRIENCES PROFESSIONNELLES
{% for job in work_experience %}
### {{ job.title }}
**{{ job.company }}** — {{ job.period }}
{% for b in job.bullets %}- {{ b }}
{% endfor %}
{% endfor %}

## PROJETS
{% for p in projects %}
**{{ p.name }}** — {{ p.stack }}  
{{ p.description }}  
{{ p.link }}
{% endfor %}

## FORMATION
{% for e in education %}
**{{ e.school }}** — {{ e.degree }} ({{ e.period }})
{% endfor %}

## CERTIFICATIONS
{{ certifications | join(" · ") }}

## LANGUES
{{ languages | join(" · ") }}

## CENTRES D’INTÉRÊT
{{ interests | join(" · ") }}
