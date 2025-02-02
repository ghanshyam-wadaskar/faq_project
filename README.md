
FAQ API - Django REST Framework
A RESTful API for managing FAQs with multi-language support, Redis caching, and WYSIWYG editor integration.

��� Features
✅ Create, Read, Update, and Delete (CRUD) FAQs
✅ Multi-language support (?lang=hi, ?lang=bn, etc.)
✅ RichText WYSIWYG editor for FAQ answers
✅ Caching with Redis for optimized performance
✅ Dockerized setup for easy deployment

��� Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/faq_project.git
cd faq_project
2️⃣ Create & Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate      # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Setup the Database
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5️⃣ Run Redis (If not using Docker)
Make sure Redis is installed and running:

bash
Copy
Edit
redis-server
6️⃣ Start the Development Server
bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/

��� Running with Docker
1️⃣ Build and Start the Containers
bash
Copy
Edit
docker-compose up --build
This will run:

Django App on http://127.0.0.1:8000/
Redis on 127.0.0.1:6379
To stop the containers:

bash
Copy
Edit
docker-compose down
��� API Endpoints
1️⃣ List FAQs (GET)
http
Copy
Edit
GET /api/faqs/
Example Response:

json
Copy
Edit
[
    {
        "id": 1,
        "question": "What is this API?",
        "answer": "<p>This is an FAQ API.</p>",
        "translated_question": "यह एक प्रश्नोत्तर एपीआई है।"
    }
]
2️⃣ Create FAQ (POST)
h
Copy
Edit
POST /api/faqs/
Request Body:

json
Copy
Edit
{
    "question": "What is Django?",
    "answer": "Django is a Python web framework."
}
3️⃣ Retrieve Single FAQ (GET)
http
Copy
Edit
GET /api/faqs/1/
4️⃣ Update FAQ (PUT)
http
Copy
Edit
PUT /api/faqs/1/
5️⃣ Delete FAQ (DELETE)
h
Copy
Edit
DELETE /api/faqs/1/
���‍��� Contribution Guidelines
Want to contribute? Follow these steps:

1️⃣ Fork the repository
2️⃣ Create a new branch: git checkout -b feature-new
3️⃣ Make your changes and commit: git commit -m "feat: Add new feature"
4️⃣ Push changes: git push origin feature-new
5️⃣ Submit a Pull Request
