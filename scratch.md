# NOTES


call_sheet_template.txt
budget_breakdown.txt
shot_list_template.txt
client_brief_template.txt
project_proposal_template.txt
crew_contact_list.txt
release_form_template.txt


touch /app/static/files/call_sheet_template.txt /app/static/files/budget_breakdown.txt /app/static/files/shot_list_template.txt /app/static/files/client_brief_template.txt /app/static/files/project_proposal_template.txt /app/static/files/crew_contact_list.txt /app/static/files/release_form_template.txt


touch app/static/files/budget_breakdown.txt app/static/files/shot_list_template.txt app/static/files/client_brief_template.txt app/static/files/project_proposal_template.txt app/static/files/crew_contact_list.txt app/static/files/release_form_template.txt



### copy paste


```html
<ul class="list-group" style="outline: red solid 1px;">
      
      <li class="list-group-item py-2 d-flex justify-content-between align-items-center min-height-auto card-body" style="outline: red solid 1px;">
        <!-- Left Content -->
        <div style="outline: red solid 1px;" class="d-flex flex-column min-height-auto">
          <h5 class="mb-1">Call Sheet Template</h5>
          <p class="mb-2">Standard call sheet template</p>
          <small class="text-muted d-block mb-2">
            none
            
          </small>
          <!-- Download Link -->
<a href="/app/static/files/call_sheet_template.txt" download="" class="align-bottom text-primary mb-0">cs_job.txt</a>

        </div>

        <!-- Right-Side Content -->
        <div style="outline: red solid 1px;" class="d-flex align-items-center bd-highlight p-5">
          <!-- Popover Button for Additional Info -->
          
          <button data-bs-content="Hard borders. Easy to modify. Sized for page print." data-bs-placement="left" data-bs-toggle="popover" class="btn btn-outline-secondary me-5 bd-highlight px-3 py-0 flex-shrink-0	" type="button">
            Notes
          </button>
          


        </div>
    <div class="gap-5"></div>
      </li>


```



###copy paste backup of templates.html


```html
<!-- allign left -->
<div class="container my-5">
  <div class="text-center mb-4">
    <h1 class="mb-3"><small>📂</small>Templates</h2>
      <p class="lead">Selection of commonly used and custom templates for film production</p>
  </div>

  {% for section in templates %}
  <div class="mb-5 pb-3 border-bottom">
    <h4 class="mb-3">{{ section.section }}</h4>
    <ul class="list-group">
      {% for template in section.templates %}
      <li class="list-group-item card-body py-2 d-flex justify-content-between align-items-center min-height-auto">
        <!-- Left Content -->
        <div class="d-flex flex-column min-height-auto">
          <h5 class="mb-1">{{ template.title }}</h5>
          <p class="mb-2">{{ template.description }}</p>
          <small class="text-muted d-block mb-2">
            {{ template.author if template.author else "Unknown" }}
            {% if template.date %} | {{ template.date }} {% endif %}
          </small>
          <!-- Download Link -->
          <a href="{{ template.file_path }}" download class="text-primary align-bottom mb-0">{{ template.file_name
            }}</a>
        </div>

        <!-- Right-Side Content -->
        <div class="d-flex align-items-center ms-auto px-5 py-1">
          <!-- Popover Button for Additional Info -->
          {% if template.additional %}
          <button type="button" class="btn btn-outline-secondary me-5 px-3 py-0 flex-shrink-0" data-bs-toggle="popover"
            data-bs-placement="left" data-bs-content="{{ template.additional }}">
            Notes
          </button>
          {% endif %}
          <div class="gap-5"></div>
          <div class="gap-5"></div>


        </div>
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}
</div>

```


### resources.html backup

{% extends 'base.html' %}

{% block title %}
Resources | FilmShit
{% endblock %}

{% block content %}


<div class="text-center mb-4">
  <h1 class="mb-3">Resources</h1>
  <p class="lead">Reference material & tools</p>
</div>



<h2 class="text-center">Listing</h2>
<div class="directory-grid">
  {% for section in resources %}
  <div class="directory-section mb-5 pb-3 border-bottom">
    <h4 class="mb-3">📁 {{ section.section }}</h4>
    <ul class="list-group">
      {% for item in section.items %}
      <li class="list-group-item card-body py-2 d-flex justify-content-between align-items-center min-height-auto">
        <div class="d-flex flex-column min-height-auto">
          <h5 class="mb-1">{{ item.title }}</h5>
          <p class="mb-1">{{ item.description }}</p>
          <small class="text-muted d-block mb-2">{{ item.author }} | {{ item.date }}</small>
          {{ item.author }} | {{ item.date }}</small>
        </div>
        <div class="d-flex align-items-center ms-auto px-5 py-1">
          <a href="{{ item.url }}" class="btn btn-sm btn-outline-info" target="_blank" rel="noopener noreferrer">🌐 {{
            item.url }}</a>
        </div>
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}
</div>

{% endblock %}


### COPY PASTE AGAIN


<h2 class="text-center">Listing</h2>
<div class="directory-grid">
  {% for category in resources %}
  <div class="directory-section mb-5 pb-3 border-bottom">
    <h3 class="mb-3">📁 {{ category.category }}</h3>
    <ul class="list-group">
      {% for entry in category.entries %}
      <li class="list-group-item card-body py-2 d-flex justify-content-between align-items-center min-height-auto">
        <div class="d-flex flex-column">
          <div class="d-flex flex-row align-items-center">
            <div> <small class="text-muted d-block ms-3">{{ entry.item_source_author}}:</small></div>
            <div class="ms-3">{{ entry.item_name }} </div>
            <div class="ms-3"> <a href="{{ entry.item_link }}" class="btn btn-sm btn-outline-info" target="_blank"
                rel="noopener noreferrer">
                {{ entry.item_link }}
              </a></div>


      </li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}
</div>

{% endblock %}


####


<h2 class="text-center">Listing</h2>
<div class="directory-grid">
  {% for category in resources %}
  <div class="directory-section mb-5 pb-3 border-bottom">
    <h3 class="mb-3">📁 {{ category.category }}</h3>
    <ul class="list-group">
      {% for entry in category.entries %}
      <div class="bs-component">
        <div class="card border-light py-3">
          <li class="list-group-item card-body d-flex justify-content-between align-items-center">

            <div class="d-flex flex-column">
              <div class="d-flex flex-row align-items-center ">
                <div class="ms-3"> <small class="text-muted d-block ">{{ entry.item_source_author}}:</small></div>
                <div class="ms-3">{{ entry.item_name }} </div>
                <div class="ms-3"> <a href="{{ entry.item_link }}" class="btn btn-sm btn-outline-info" target="_blank"
                    rel="noopener noreferrer">
                    {{ entry.item_link }}
                  </a></div>

              </div>

          </li>
        </div>
        {% endfor %}
    </ul>
  </div>
  {% endfor %}
</div>

{% endblock %}


### resources.yaml backup

```yaml
- category: Software Tools
  entries:
    - item_source_author: "Hot Bricks"
      item_name: "Hot Budget"
      item_link: "https://hotbudget.com/download/"

    - item_source_author: "Hot Bricks"
      item_name: "Hot Budget Manual"
      item_link: "https://downloads.hotbudget.com/HotBudget_v3.0_UserGuide.pdf"

    - item_source_author: "Revolution Payroll"
      item_name: "True Budget"
      item_link: "https://truebudget.io/"

    - item_source_author: "Revolution Payroll"
      item_name: "True Budget Manual"
      item_link: "https://www.truebudget.io/assets/website/document/TrueBudget_UserGuide-v1.4.pdf"

    - item_source_author: "Media Services"
      item_name: "Showbiz Budgeting"
      item_link: "https://www.mediaservices.com/showbiz-software/upgrade-showbiz-budgeting/"

    - item_source_author: "Media Services"
      item_name: "Showbiz Budgeting Tutorials"
      item_link: "https://www.mediaservices.com/showbiz-software/upgrade-showbiz-budgeting/"

    - item_source_author: "Actual"
      item_name: "GetActual.io"
      item_link: "https://getactual.io"

    - item_source_author: "Saturation"
      item_name: "Saturation.io"
      item_link: "https://saturation.io/"
      
    - item_source_author: "RogueWave"
      item_name: "Rogue Budget (beta)"
      item_link: "https://roguewave.tv/roguebudget/"


- category: Bidding Guidelines
  entries:
    - item_source_author: "AICP"
      item_name: "National Bidding Guidelines"
      item_link: "https://aicp.com/assets/editor/AICP_National_Live_Action_Guidelines_April2020_FINAL.pdf"

    - item_source_author: "AICP"
      item_name: "Best Practices when Bidding (memo)"
      item_link: "https://aicp.com/assets/editor/AICP_BiddingGuidelines_BestPractices_June2017.pdf"


- category: Actualization Guidelines
  entries:
    - item_source_author: "Media Services"
      item_name: "Labor Guide (web)"
      item_link: "https://laborguide.mediaservices.com/labor-guide/show-all/"

    - item_source_author: "Media Services"
      item_name: "2025 Labor Guidelines (pdf)"
      item_link: "https://4517874.fs1.hubspotusercontent-na1.net/hubfs/4517874/Labor%20Guide/CommercialGuide_011025.pdf?hsCtaAttrib=164499129412"


- category: Digital Payroll Services
  entries:
    - item_source_author: "Wrapbook"
      item_name: "Wrapbook"
      item_link: "https://wrapbook.com"

    - item_source_author: "Greenslate"
      item_name: "Greenslate"
      item_link: "https://greenslate.com/"


- category: Antiquated Payroll Services
  entries:
    - item_source_author: "TEAM Companies"
      item_name: "CAPS, Media Services Payroll"
      item_link: "https://www.capspayroll.com/contact/"

    - item_source_author: "Entertainment Partners"
      item_name: "EP Payroll"
      item_link: "https://www.ep.com/"

    - item_source_author: "Revolution Entertainment Services"
      item_name: "Revolution Payroll "
      item_link: "https://revolutiones.com/"

    - item_source_author: "Extreme Reach Payroll"
      item_name: "Extreme Reach Payroll"
      item_link: "https://www.xr.global/solutions/production-studios"



- category: Digital Communities
  entries:
    - item_source_author: "Variable"
      item_name: "Variable: a filmmaker wellness community"
      item_link: "https://wearevariable.com/"

    - item_source_author: "Reddit"
      item_name: "r/FilmTvBudgeting"
      item_link: "https://www.reddit.com/r/FilmTVBudgeting/"

    - item_source_author: "Fishbowl"
      item_name: "bowl/Production"
      item_link: "https://www.fishbowlapp.com/bowl/production"

    - item_source_author: "CoPros"
      item_name: "Line Producer, Production Manager network (invite only)"
      item_link: null

- category: Content
- category: Podcast
  entries:
    - item_source_author: "Jordan Brady"
      item_name: "Respect The Process"
      item_link: "https://jordanbrady.com/respect-the-process/"

- category: Blog
  entries:
    - item_source_author: "Josh Parkhill"
      item_name: "Frame By Brand"
      item_link: "https://framebybrand.substack.com/"

```

### resources.html for loop backup

```html
<div class="text-center mb-4">
  <h1 class="mb-3">Resources</h1>
  <p class="lead">Reference material & tools</p>
</div>



<h2 class="text-center">Listing</h2>
<div class="directory-grid">
  {% for category in resources %}
  <div class="directory-section mb-5 pb-3 border-bottom">
    <h3 class="mb-3">📁 {{ category.category }}</h3>
    <ul class="list-group">
      {% for entry in category.entries %}
      <li class="list-group-item card border-light py-2">
        <!-- <div class="card border-light py-3"> -->
        <div class="card-body d-flex justify-content-between align-items-center">

          <div class="d-flex flex-column">
            <div class="d-flex flex-row align-items-center">
              <div class="ms-3">
                <small class="text-muted d-block">{{ entry.item_source_author }}:</small>
              </div>
              <div class="ms-3">{{ entry.item_name }}</div>
              <div class="ms-3">
                <a href="{{ entry.item_link }}" class="btn btn-sm btn-outline-info" target="_blank"
                  rel="noopener noreferrer">
                  {{ entry.item_link }}
                </a>
              </div>
            </div>
          </div>

        </div>
        <!-- </div> -->
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}
</div>

{% endblock %}
```


### resources.html seperated by group name

```html
{% extends 'base.html' %}

{% block title %}
Resources | FilmShit
{% endblock %}

{% block content %}


<div class="text-center mb-4">
  <h1 class="mb-3">Resources</h1>
  <p class="lead">Reference material & tools</p>
</div>

<div class="directory-grid">
  {% for category in resources %}
  <div class="directory-section mb-5 pb-3 border-bottom">
    <h3 class="mb-3">📁 {{ category.category }}</h3>

    {% for group in category.groups %}
    <div class="group-section mb-4">
      <h5 class="mb-2">{{ group.group_name }}</h5>
      <ul class="list-group">
        {% for entry in group.entries %}
        <li class="list-group-item card border-light py-2">
          <div class="card-body d-flex justify-content-between align-items-center">
            <div class="d-flex flex-column">
              <div class="d-flex flex-row align-items-center">
                <div class="ms-3">{{ entry.item_name }}</div>
                <div class="ms-3">
                  <a href="{{ entry.item_link }}" class="btn btn-sm btn-outline-info" target="_blank"
                    rel="noopener noreferrer">
                    {{ entry.item_link }}
                  </a>
                </div>
              </div>
            </div>
          </div>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endfor %}

  </div>
  {% endfor %}
</div>

{% endblock %}
```
