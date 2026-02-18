📦 Claribox
The MUST Student Voice Project

Claribox is a secure, anonymous student suggestion platform built for Mbarara University of Science and Technology (MUST).

It provides students with a verified and protected channel to submit feedback, grievances, and institutional suggestions — without fear of exposure.

🌟 The Core Philosophy — “The Identity Shredder”

Most platforms claim anonymity.

They don’t actually mean it.

They store your account.
They keep your login trail.
They preserve linkage.

Claribox takes a stricter, zero-compromise approach.

🔐 Step 1 — Verification

Students authenticate using their official:

@std.must.ac.ug Google account.

This ensures that only legitimate MUST students can access the system.

📝 Step 2 — Submission

The student submits their feedback through the platform interface.

🧨 Step 3 — The Shredder

Immediately after submission:

The suggestion is securely saved.

The authenticated session is destroyed.

The temporary user account is permanently deleted.

✅ Final Result

The feedback remains.
The identity trail does not.

No email.
No account.
No recovery.
No linkage.

🚀 Key Features
🔒 Domain-Locked SSO

Only std.must.ac.ug accounts are allowed access.

🕵️ True Anonymity

Automatic account and session destruction upon submission.

📊 Administrative Dashboard

A custom-built dashboard for authorized staff to:

Monitor trends

Track top categories

Identify recurring institutional issues

⏲️ Auto-Session Cleanup

5-minute inactivity timeout to prevent misuse on shared campus computers.

🤖 AI-Ready Architecture

Built-in structural hooks for:

Sentiment analysis

Automated categorization

Pattern detection

🛠️ Tech Stack
Layer	Technology
Framework	Django 6.0
Authentication	Django-Allauth + Google OAuth2
Frontend	HTML5 / CSS3
Database (Development)	SQLite
Database (Production)	PostgreSQL
Security	CSRF Protection, HTTP-only cookies, Domain-restricted login

Built with a traditional, battle-tested Django architecture.
No gimmicks. Clean engineering.

⚙️ Local Setup
1️⃣ Clone the Repository
git clone https://github.com/kamukamaosbertl/ClariBox.git
cd ClariBox

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install django django-allauth

4️⃣ Configure Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret


(Obtain credentials from Google Cloud Console.)

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Create Superuser
python manage.py createsuperuser

7️⃣ Run Development Server
python manage.py runserver


Visit:

http://127.0.0.1:8000/

🔐 Security Design Principles

No persistent student identity storage

Minimal data retention

Server-side domain validation

Restricted admin-only analytics

Session destruction after submission

Claribox operates on one principle:

If identity exists, it can leak.
So eliminate it.

👨‍💻 Author

Kamukama
Software Engineer
Building tools that empower the MUST community.