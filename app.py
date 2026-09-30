from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

CAREERS = {
    'Software Developer': ['Python','C++','DSA','Git/GitHub','SQL','Problem Solving'],
    'Data Analyst': ['Python','SQL','Excel','Statistics','Power BI','Data Visualization'],
    'AI/ML Engineer': ['Python','Statistics','Machine Learning','SQL','NumPy','Pandas'],
    'Web Developer': ['HTML/CSS','JavaScript','React','Git/GitHub','APIs','Problem Solving']
}

COURSES = {
    'Python': 'Python Programming Fundamentals', 'C++': 'C++ & DSA Foundations', 'DSA': 'Data Structures & Algorithms Practice',
    'SQL': 'SQL & Database Essentials', 'Git/GitHub': 'Git & GitHub Essentials', 'Problem Solving': 'Problem Solving with Coding',
    'Excel': 'Advanced Excel for Analytics', 'Statistics': 'Statistics for Data Analysis', 'Power BI': 'Power BI Dashboard Project',
    'Data Visualization': 'Data Visualization Fundamentals', 'Machine Learning': 'Machine Learning Foundations',
    'NumPy': 'NumPy for Data Science', 'Pandas': 'Pandas Data Analysis', 'HTML/CSS': 'Modern HTML & CSS',
    'JavaScript': 'JavaScript Essentials', 'React': 'React Frontend Development', 'APIs': 'REST API Development'
}

OPPORTUNITIES = [
    {'title':'Software Developer Intern','type':'Internship','skills':['Python','DSA','Git/GitHub']},
    {'title':'Data Analyst Intern','type':'Internship','skills':['Python','SQL','Power BI']},
    {'title':'Junior Web Developer','type':'Job','skills':['HTML/CSS','JavaScript','React']},
    {'title':'AI/ML Trainee','type':'Job','skills':['Python','Machine Learning','Pandas']},
    {'title':'Government Technical Recruitment','type':'Government','skills':['C++','DSA','Problem Solving']}
]

def analyze(data):
    career = data.get('career','Software Developer')
    skills = [s.strip() for s in data.get('skills','').split(',') if s.strip()]
    projects = int(data.get('projects',0) or 0)
    certs = int(data.get('certs',0) or 0)
    interview = int(data.get('interview',50) or 50)
    communication = int(data.get('communication',60) or 60)
    required = CAREERS.get(career, CAREERS['Software Developer'])
    have = {s.lower() for s in skills}
    gaps = [s for s in required if s.lower() not in have]
    skill_score = round(((len(required)-len(gaps))/len(required))*100)
    project_score = min(projects*25,100)
    cert_score = min(certs*20,100)
    readiness = round(skill_score*.45 + project_score*.15 + cert_score*.10 + interview*.15 + communication*.15)
    return {'career':career,'required':required,'skills':skills,'gaps':gaps,'skill_score':skill_score,'project_score':project_score,'cert_score':cert_score,'interview':interview,'communication':communication,'readiness':readiness}

@app.route('/')
def home():
    return render_template('index.html', careers=list(CAREERS.keys()))

@app.post('/api/analyze')
def api_analyze():
    data = request.get_json(force=True)
    result = analyze(data)
    result['roadmap'] = [{'skill':g, 'course':COURSES.get(g, f'{g} Skill Module'), 'action':f'Learn {g}, build a mini-project, then take a skill test.'} for g in result['gaps']]
    matched=[]
    for o in OPPORTUNITIES:
        match = round(len(set(o['skills']) & set(result['skills'])) / len(o['skills']) * 100)
        matched.append({**o,'match':match})
    result['opportunities']=sorted(matched,key=lambda x:x['match'],reverse=True)
    result['generated_at']=datetime.utcnow().isoformat()+'Z'
    return jsonify(result)

@app.post('/api/resume')
def resume():
    d=request.get_json(force=True)
    name=d.get('name','Student'); career=d.get('career','Software Developer'); skills=d.get('skills','')
    return jsonify({'suggestions':[f'Add a targeted headline: Aspiring {career} | Student', 'Quantify project outcomes instead of only listing responsibilities.', f'Highlight evidence for these skills: {skills}.', 'Add GitHub/project links and measurable achievements.', 'Keep the resume to one page for entry-level applications.']})

@app.post('/api/interview')
def interview():
    career=request.get_json(force=True).get('career','Software Developer')
    questions={
      'Software Developer':['Explain how you would solve a duplicate-elements problem.','What is the difference between a stack and a queue?','Describe a project you built and one technical challenge you solved.'],
      'Data Analyst':['How would you handle missing values in a dataset?','Explain INNER JOIN vs LEFT JOIN.','Which chart would you use to compare categories and why?'],
      'AI/ML Engineer':['What is overfitting and how can you reduce it?','Explain train, validation and test data.','Describe a machine-learning project you have built.'],
      'Web Developer':['What is the DOM?','Explain the difference between REST and a frontend framework.','How would you improve a slow web page?']}
    return jsonify({'questions':questions.get(career,questions['Software Developer'])})

if __name__=='__main__':
    app.run(debug=True)
