<div class="header-banner">
    <h1>{{ personal.first_name }} {{ personal.last_name }}</h1>
    <p>{{ personal.title }}</p>
</div>

<div class="contact-info">
    {{ personal.location }} · ✉️ {{ personal.email }} · 📞 {{ personal.phone }} · 
    <a href="{{ personal.linkedin }}">LinkedIn</a> · 
    <a href="{{ personal.github }}">GitHub</a>
</div>


<!-- <div class="contact-info">
    {{ personal.location }} · ✉️ {{ personal.email }} · 📞 {{ personal.phone }}
    <br>
    🔗 <a href="{{ personal.linkedin }}">LinkedIn</a> · <a href="{{ personal.github }}">GitHub</a>
</div> -->

---

## PROFIL

{{ profile }}

---

## COMPÉTENCES TECHNIQUES

**Langages :** {{ skills.languages }}  
**ML & NLP :** {{ skills.ml }}  
**Bases de données :** {{ skills.database }}  
**Visu :** {{ skills.visualization }}  
**Outils :** {{ skills.tools }}

---

## EXPÉRIENCES

{% for job in work_experience %}
### {{ job.title }} — {{ job.period }}
**{{ job.company }}**

{{ job.description }}

{% endfor %}

---

## FORMATION

{% for edu in education %}
**{{ edu.school }}** — {{ edu.degree }} ({{ edu.period }})
{% endfor %}

---

## CERTIFICATIONS

{% for cert in certifications %}
- {{ cert }}
{% endfor %}

---

## LANGUES

{% for l in languages %}
- {{ l }}
{% endfor %}

---

## CENTRES D’INTÉRÊT

{% for i in interests %}
- {{ i }}
{% endfor %}
