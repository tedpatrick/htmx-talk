# Modern Web Applications with HTMX

This repository contains the slides and code for the talk "Modern Web Applications with HTMX"

HTMX is a 14KB JavaScript library providing a lightweight, declarative hypertext for web application development. HTMX enhances HTML elements with attributes for calling services, swapping elements, triggering events, and tapping into server-side rendering to generate even more hypertext.
This presentation delves into the fundamentals of using HTMX, explores common usage patterns, and gives insights into where using HTMX makes sense.

Author: Ted Patrick (ted@acumity.com)

Run the server

## Using Pip

```bash
pip3 install -r requirements.txt
python manage.py runserver
```

## Using Conda

```bash
conda env create
conda activate htmx
python manage.py runserver
```

## Run Tailwind Compiler - Will update CSS as you change any file within the `server/apps/theme/templates/` directory

```bash
cd server/apps/theme/static_src
npm install
npm run dev
```

Open the browser to http://localhost:8000/

Django Admin at http://localhost:8000/admin/
--> Username: admin, Password: admin
