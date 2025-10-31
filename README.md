DiscX - Django Mini Project
A real-time study room application built with Django where users can create rooms, join discussions, and collaborate on various topics.
🚀 Features
* User Authentication - Register, login, and user profiles
* Study Rooms - Create and join topic-based discussion rooms
* Real-time Messaging - Multi-line message support with proper formatting
* Topic Management - Categorize rooms by topics (Python, Django, etc.)
* User Profiles - Customizable user profiles with avatars
* Search Functionality - Search rooms by topics, names, or descriptions
* Responsive Design - Works on desktop and mobile devices
🛠️ Tech Stack
* Backend: Django, Python
* Frontend: HTML, CSS, JavaScript
* Database: SQLite (default)
* Authentication: Django AllAuth
* Styling: Custom CSS with CSS Variables
📋 Prerequisites
* Python 3.8+
* Django 4.0+
* Pillow (for image handling)
🚀 Installation
1. Clone the repository
git clone [https://github.com/rajchaudhary-95/djangominiproject.git](https://github.com/rajchaudhary-95/djangominiproject.git)
cd djangominiproject

2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (optional)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver

7. Access the application
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

📁 Project Structure
djangominiproject/
├── base/                # Main Django app
│   ├── templates/base/    # HTML templates
│   ├── static/            # CSS, JS, images
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   └── urls.py            # App URL routes
├── static/                # Static files
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
└── manage.py              # Django management script

🎯 Key Features Implementation
User Authentication
   * Custom user model with email authentication
   * User registration and profile management
   * Secure password handling
Study Rooms
   * Create, read, update, delete rooms
   * Topic-based room categorization
   * Room hosting and participant management
Messaging System
   * Multi-line message support
   * Real-time message display
   * Message formatting preservation
   * Message deletion (user-specific)
Search & Filtering
   * Search rooms by topic, name, or description
   * Topic-based filtering
   * Recent activities feed
🎨 UI/UX Features
   * Dark theme with blue accent colors
   * Responsive design for all devices
   * Interactive message threads
   * User avatar support
   * Clean and modern interface
🔧 Customization
Adding New Topics
Topics are automatically created when users create rooms with new topic names.
Styling
The application uses CSS custom properties for easy theming:
:root {
 --color-main: #71c6dd;
 --color-dark: #3f4156;
 --color-bg: #2d2d39;
 /* ... more variables */
}

👥 User Roles
   * Guest Users: Browse rooms and view messages
   * Registered Users: Create rooms, send messages, manage profiles
   * Room Hosts: Edit or delete their rooms
   * Message Authors: Delete their own messages
📱 Usage
   1. Register/Login - Create an account or login
   2. Browse Rooms - View existing study rooms
   3. Create Room - Start a new discussion room
   4. Join Discussion - Participate in room conversations
   5. Manage Profile - Update your avatar and information
🐛 Troubleshooting
Common Issues
   1. Static files not loading
   * Run python manage.py collectstatic
   2. Database errors
   * Delete db.sqlite3 and run migrations again
   3. Image upload issues
   * Ensure Pillow is installed: pip install Pillow
🤝 Contributing
   1. Fork the repository
   2. Create a feature branch: git checkout -b feature/amazing-feature
   3. Commit changes: git commit -m 'Add amazing feature'
   4. Push to branch: git push origin feature/amazing-feature
   5. Open a Pull Request
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Developers
   * Raj Chaudhary 
   * Kapish Pathrikar 
🙏 Acknowledgments
   * Django documentation and community
   * Inspiration from various study platform designs
   * Contributors and testers
Note: This is a mini project for educational purposes. For production use, consider implementing additional security features and using a production-ready database.
