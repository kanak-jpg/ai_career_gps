# CareerGPS — AI-Powered Career Readiness & Employability Platform

CareerGPS is a hackathon MVP for a student-focused **AI Career GPS**. It turns career planning into a continuous loop:

**Assess → Identify Gaps → Learn → Build → Prove → Reassess → Apply**

## MVP features
- Student career profile
- Career-path skill maps
- Skill-gap analysis
- Dynamic Job Readiness Score
- Learn → Build → Prove roadmap
- AI-style resume improvement suggestions
- Adaptive mock-interview question generation
- Internship/job/government opportunity matching
- Responsive dashboard UI

## Tech stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python + Flask
- Data layer: in-memory prototype data (ready for PostgreSQL)
- AI layer: recommendation/NLP integration point (LLM or ML API can be connected)
- Deployment: Render/Railway/AWS/Azure/GCP

## Run locally
```bash
python -m venv venv
# Windows: venv\\Scripts\\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## Suggested production architecture
React/Next.js → FastAPI → PostgreSQL + Object Storage → ML/NLP/LLM services → Opportunity APIs.
Use OAuth/JWT, encryption, role-based access, consent, audit logs and data minimization for student privacy.

## GitHub upload
Create a new GitHub repository named `ai-career-gps`, then run:
```bash
git init
git add .
git commit -m "Initial CareerGPS hackathon MVP"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-career-gps.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. Do not put API keys or student personal data in the repository.
