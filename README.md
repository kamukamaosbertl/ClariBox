📦 Claribox
The MUST Student Voice Project

Claribox is a secure, anonymous student suggestion platform built for Mbarara University of Science and Technology (MUST).

It gives students a safe, verified channel to submit feedback, grievances, and suggestions directly to administration — without fear of exposure.

🌟 The Core Philosophy — “The Identity Shredder”

Most platforms claim anonymity.

They lie.

They still store your account. They still keep the trail.

Claribox takes a radically stricter approach.

🔐 Step 1 — Verification

Students authenticate using their official:

@std.must.ac.ug


Google account.
This guarantees that only real MUST students can access the platform.

📝 Step 2 — Submission

The student submits their feedback.

🧨 Step 3 — The Shredder

Immediately after submission:

The suggestion is saved.

The authenticated user session is destroyed.

The temporary user account is deleted.

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

Custom-built dashboard for authorized staff to:

Monitor trends

Track top categories

Identify recurring institutional issues

⏲️ Auto-Session Cleanup

5-minute inactivity timeout to prevent misuse on shared campus computers.

🤖 AI-Ready Architecture

Hooks built in for future:

Sentiment analysis

Categorization

Pattern detection

🛠️ Tech Stack
Layer	Technology
Framework	Django 6.0
Authentication	Django-Allauth + Google OAuth2
Frontend	HTML5 / CSS3
Database (Dev)	SQLite
Database (Production)	PostgreSQL
Security	CSRF Protection, HTTP-only cookies, domain-restricted login

Built with a traditional, battle-tested Django architecture. No gimmicks. Just clean engineering.

⚙️ Local Setup
1️⃣ Clone the Repository
git clone https://github.com/kamukamaosbertl/ClariBox.git
cd claribox

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

Create a .env file and add:

SECRET_KEY=your_secret_key
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret


(You’ll obtain Google credentials from Google Cloud Console.)

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Create Superuser
python manage.py createsuperuser

7️⃣ Run the Development Server
python manage.py runserver


Visit:

http://127.0.0.1:8000/

🔐 Security Design Principles

No persistent student identity storage

Minimal data retention

Server-side validation of email domain

Restricted admin-only analytics

Session destruction after submission

Claribox assumes:

If identity exists, it can leak.
So we eliminate it.

👨‍💻 Author

Kamukama
Software Engineer
Building tools that empower the MUST community.