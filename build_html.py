#!/usr/bin/env python3
"""Assemble landing page partials into index.html."""
from pathlib import Path

ROOT = Path(__file__).parent
PARTIALS = ROOT / "partials"

# Additional partials written by this script if missing
PARTIALS.mkdir(exist_ok=True)

def write(name: str, content: str) -> None:
    (PARTIALS / name).write_text(content.strip() + "\n", encoding="utf-8")

write("03-pillars.html", """
<section id="pillars">
  <div class="section-label reveal">The Four Pillars of Fluent</div>
  <h2 class="section-title reveal reveal-delay-1">One platform.<br>Four transformations.</h2>
  <p class="section-body reveal reveal-delay-2">Every stakeholder served. Every outcome measurable. Every interaction intelligent.</p>
  <div class="pillar-grid" style="margin-top:3.5rem">
    <div class="pillar-card p1 reveal">
      <div class="pillar-num">1</div>
      <div class="pillar-icon-wrap">🎯</div>
      <div class="pillar-tag">Pillar One</div>
      <div class="pillar-title">Teacher Excellence</div>
      <p class="pillar-desc">Teacher development is the highest-leverage investment a school can make. Fluent gives every teacher an AI assistant, a professional development pathway, and the tools to spend less time on administration and more time on what they do best — teaching.</p>
      <ul class="pillar-items">
        <li>CPD Programmes & Teaching Excellence Framework</li>
        <li>AI-generated lesson plans in under 60 seconds</li>
        <li>Automated marking with one-click teacher approval</li>
        <li>Teacher Growth Passport & wellbeing monitoring</li>
        <li>Workload management and burnout prevention</li>
      </ul>
      <div class="pillar-outcome">Outcome — Better teachers create better learning</div>
    </div>
    <div class="pillar-card p2 reveal reveal-delay-1">
      <div class="pillar-num">2</div>
      <div class="pillar-icon-wrap">✦</div>
      <div class="pillar-tag">Pillar Two</div>
      <div class="pillar-title">Student Academic Fluency</div>
      <p class="pillar-desc">Academic Fluency is the ability to understand, explain, discuss, question, and apply knowledge confidently. Fluent develops fluency across Science, Mathematics, and English — measuring Accuracy, Fluency, Understanding, and Confidence in every scholar.</p>
      <ul class="pillar-items">
        <li>Academic Fluency Score (AFS) — the single metric that matters</li>
        <li>Personalised learning paths — Support, Standard, Advanced</li>
        <li>AI study assistant available 24/7 — hints, never answers</li>
        <li>Mastery Ledger — a living map of what each scholar knows</li>
        <li>Digital portfolio growing from day one through graduation</li>
      </ul>
      <div class="pillar-outcome">Outcome — Students become scholars, not passive learners</div>
    </div>
    <div class="pillar-card p3 reveal">
      <div class="pillar-num">3</div>
      <div class="pillar-icon-wrap">🤝</div>
      <div class="pillar-tag">Pillar Three</div>
      <div class="pillar-title">Parent Partnership</div>
      <p class="pillar-desc">Parents do not receive reports. They receive intelligence. Ask our AI why your child is struggling in Science and get a specific, causal answer — not a grade table. Then get three things you can do at home tonight to help.</p>
      <ul class="pillar-items">
        <li>Weekly updates, monthly summaries, quarterly reviews</li>
        <li>Parent Intelligence Dashboard — real-time visibility</li>
        <li>AI Parent Assistant — conversational, causal, plain language</li>
        <li>Home Learning Guidance — specific, actionable, subject-relevant</li>
        <li>Direct messaging with British faculty and local teachers</li>
      </ul>
      <div class="pillar-outcome">Outcome — Parents gain visibility, confidence, and partnership</div>
    </div>
    <div class="pillar-card p4 reveal reveal-delay-1">
      <div class="pillar-num">4</div>
      <div class="pillar-icon-wrap">📊</div>
      <div class="pillar-tag">Pillar Four</div>
      <div class="pillar-title">School Intelligence</div>
      <p class="pillar-desc">School leaders move from reactive administrators to intelligence-led strategists. Real-time dashboards replace static reports. Predictive risk models replace gut instinct. Measurable improvement targets replace aspirational goals.</p>
      <ul class="pillar-items">
        <li>School Performance Dashboard with real-time intelligence</li>
        <li>Teacher development analytics and retention risk monitoring</li>
        <li>Student risk detection — 14+ days before crisis emerges</li>
        <li>Attendance intelligence and engagement trend analysis</li>
        <li>School improvement tracking with measurable outcomes</li>
      </ul>
      <div class="pillar-outcome">Outcome — Data-driven decisions that transform school performance</div>
    </div>
  </div>
</section>
""")

write("04-how-ai.html", """
<section id="how">
  <div class="section-label reveal">End-to-End Workflow</div>
  <h2 class="section-title reveal reveal-delay-1">From onboarding to graduation.<br>Every step intelligent.</h2>
  <p class="section-body reveal reveal-delay-2">Fifteen steps. One continuous learning loop. Zero manual administration left on the table.</p>
  <div class="flow-steps" style="margin-top:3rem">
    <div class="flow-step reveal"><div class="step-num">01</div><div><div class="step-title">School Onboarding</div><p class="step-desc">Upload your school structure, curriculum, timetable, and student list. AI automatically creates all profiles, dashboards, and subject structures. Ready on day one.</p><div class="step-tags"><span class="step-tag tag-t">Admin</span><span class="step-tag tag-g">Automation</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">02</div><div><div class="step-title">AI Lesson Planning</div><p class="step-desc">Teacher enters topic and objective. AI generates a full lesson plan, resources, and three differentiated versions — Support, Standard, Advanced — in under 60 seconds.</p><div class="step-tags"><span class="step-tag tag-t">Teacher Tools</span><span class="step-tag tag-g">Differentiation</span><span class="step-tag tag-p">60 Seconds</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">03</div><div><div class="step-title">Live Lesson & Real-Time Engagement</div><p class="step-desc">Students join live. AI monitors participation, response patterns, and confusion signals. Teacher sees engaged / confused / inactive split in real time — and knows exactly who needs support.</p><div class="step-tags"><span class="step-tag tag-t">Real-Time</span><span class="step-tag tag-r">Engagement</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">04</div><div><div class="step-title">End-of-Lesson Reflection</div><p class="step-desc">Students complete "5 Things I Learned". AI evaluates understanding scores, detects misconceptions, and identifies knowledge gaps per student — updating the knowledge graph immediately.</p><div class="step-tags"><span class="step-tag tag-t">Metacognition</span><span class="step-tag tag-p">Knowledge Graph</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">05</div><div><div class="step-title">Personalised Homework Generation</div><p class="step-desc">AI creates individualised homework for every student immediately after class. The AI tutor provides hints, examples, and guided questions — never direct answers. Independent thinking protected.</p><div class="step-tags"><span class="step-tag tag-g">Personalisation</span><span class="step-tag tag-m">AI Tutor</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">07</div><div><div class="step-title">AI Grading & Assessment</div><p class="step-desc">Objective questions marked automatically at 100% accuracy. Subjective work evaluated on logic, structure, and understanding. Teacher reviews and approves — 30 seconds instead of 4 hours.</p><div class="step-tags"><span class="step-tag tag-t">Auto-Marking</span><span class="step-tag tag-g">60–80% Time Saved</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">09</div><div><div class="step-title">Digital Portfolio — Lifelong Record</div><p class="step-desc">Every activity, grade, reflection, skill, and achievement automatically added to the student's living digital portfolio. By Year 11 or 13, a complete evidence-based growth record from day one.</p><div class="step-tags"><span class="step-tag tag-p">Portfolio</span><span class="step-tag tag-m">Skills Tracking</span><span class="step-tag tag-g">Lifelong</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">11</div><div><div class="step-title">Early Intervention System</div><p class="step-desc">AI identifies at-risk students before problems become crises. Declining grades + falling homework + attendance drop triggers a structured intervention plan — pre-populated, ready to act on.</p><div class="step-tags"><span class="step-tag tag-r">Risk Detection</span><span class="step-tag tag-t">Proactive</span><span class="step-tag tag-g">14+ Days Early</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">12</div><div><div class="step-title">Mental Health & Wellbeing Intelligence</div><p class="step-desc">Wellbeing check-ins plus passive signal collection — writing tone, submission timing, reflection depth — detect what students won't say. Safeguarding alerts delivered before escalation.</p><div class="step-tags"><span class="step-tag tag-r">Wellbeing</span><span class="step-tag tag-p">Safeguarding</span><span class="step-tag tag-t">Passive Signals</span></div></div></div>
    <div class="flow-step reveal"><div class="step-num">15</div><div><div class="step-title">School Leadership Dashboard</div><p class="step-desc">Headteachers see everything in real time — teacher workload and retention risk, student cohort wellbeing, performance trends, risk forecasting. Intelligence, not reports.</p><div class="step-tags"><span class="step-tag tag-p">Leadership</span><span class="step-tag tag-t">Real-Time</span><span class="step-tag tag-g">Strategic</span></div></div></div>
  </div>
</section>
<section id="ai-section">
  <div class="section-label reveal">The Role of AI</div>
  <h2 class="section-title reveal reveal-delay-1">Assist. Augment. Accelerate.</h2>
  <p class="section-body reveal reveal-delay-2">AI exists to support people — not replace them. Every AI capability in Fluent has one purpose: to give humans more time, better information, and earlier opportunity to act.</p>
  <div class="ai-grid reveal reveal-delay-3">
    <div class="ai-card"><div class="ai-who" style="color:var(--teal2)">🎯  For Teachers</div><div class="ai-card-title">AI Teaching Assistant</div><ul class="ai-items"><li>Lesson plan generation in 60 seconds</li><li>Automated marking & bulk approval</li><li>Progress analysis per student</li><li>Parent report drafting</li><li>Intervention recommendations</li><li>Workload monitoring & alerts</li></ul></div>
    <div class="ai-card"><div class="ai-who" style="color:var(--gold2)">✦  For Students</div><div class="ai-card-title">AI Study Assistant</div><ul class="ai-items"><li>Personalised revision pathways</li><li>Concept scaffolding — hints, not answers</li><li>Academic fluency practice</li><li>Knowledge gap detection</li><li>Curriculum-grounded answers</li><li>24/7 availability, zero judgement</li></ul></div>
    <div class="ai-card"><div class="ai-who" style="color:#E88080">🤝  For Parents</div><div class="ai-card-title">AI Parent Intelligence</div><ul class="ai-items"><li>Plain language progress explanations</li><li>Causal insight — why, not just what</li><li>Home learning guidance tonight</li><li>Wellbeing trend visibility</li><li>Communication support</li><li>Conversational — ask any question</li></ul></div>
    <div class="ai-card"><div class="ai-who" style="color:#9B8FD8">🏛️  For School Leaders</div><div class="ai-card-title">AI School Intelligence</div><ul class="ai-items"><li>Real-time trend analysis</li><li>Predictive performance insights</li><li>Teacher retention risk monitoring</li><li>Student cohort risk forecasting</li><li>Strategic planning intelligence</li><li>School improvement tracking</li></ul></div>
  </div>
  <p class="ai-tagline reveal">"AI is not the product. <strong>Teachers are not replaced.</strong> Technology does not lead learning."</p>
</section>
""")

PLATFORM_URL = "https://fluent-woad.vercel.app"

write("05-platform.html", f"""
<section id="platform">
  <div class="section-label reveal">The Platform</div>
  <h2 class="section-title reveal reveal-delay-1">Four dashboards.<br>One intelligent platform.</h2>
  <p class="section-body reveal reveal-delay-2">Every stakeholder has their own dedicated interface — built specifically for how they think, what they need, and the decisions they make every day.</p>
  <div class="dashboard-grid">
    <a href="{PLATFORM_URL}/student" class="dash-card dash-teal reveal" target="_blank" rel="noopener">
      <div class="dash-icon">🎓</div>
      <div class="dash-label">For Scholars</div>
      <div class="dash-title">Scholar Studio</div>
      <p class="dash-desc">The scholar's complete learning environment — from AI-powered revision to the Mastery Ledger, Confidence Studio, and the living digital portfolio that grows from day one.</p>
      <ul class="dash-features">
        <li>Home Dashboard with Academic Fluency Score (AFS)</li>
        <li>AI Tutor — RAG-grounded, curriculum-accurate, Socratic</li>
        <li>Mastery Ledger — visual knowledge map per subject</li>
        <li>Confidence Studio — speaking practice and fluency tracking</li>
        <li>Digital Portfolio — automatic, lifelong, skills-mapped</li>
        <li>Global Forum — peer learning and faculty moderation</li>
      </ul>
      <div class="dash-btn">Enter Scholar Studio <span class="dash-arrow">→</span></div>
    </a>
    <a href="{PLATFORM_URL}/parent" class="dash-card dash-gold reveal reveal-delay-1" target="_blank" rel="noopener">
      <div class="dash-icon">👨‍👩‍👧</div>
      <div class="dash-label">For Guardians</div>
      <div class="dash-title">Guardian Portal</div>
      <p class="dash-desc">Continuous, real-time visibility into your child's learning journey. Ask the AI any question about their progress and receive a specific, causal, actionable answer in plain language.</p>
      <ul class="dash-features">
        <li>Real-time AFS and wellbeing dashboard</li>
        <li>AI Parent Assistant — ask anything, get real answers</li>
        <li>Urgency-tiered alert system — academic, wellbeing, attendance</li>
        <li>Weekly, monthly, and quarterly structured reports</li>
        <li>Direct faculty messaging and 1:1 session booking</li>
        <li>Home learning guidance — specific and actionable</li>
      </ul>
      <div class="dash-btn">Enter Guardian Portal <span class="dash-arrow">→</span></div>
    </a>
    <a href="{PLATFORM_URL}/teacher" class="dash-card dash-rose reveal" target="_blank" rel="noopener">
      <div class="dash-icon">📚</div>
      <div class="dash-label">For Teachers</div>
      <div class="dash-title">Teacher Dashboard & CPD Hub</div>
      <p class="dash-desc">Your AI teaching assistant, CPD growth tracker, and class intelligence system — all in one place. Spend your time teaching, not administering.</p>
      <ul class="dash-features">
        <li>AI Lesson Planner — full plan in 60 seconds</li>
        <li>Real-time class engagement monitoring</li>
        <li>Bulk marking approval — 30 minutes, not 4 hours</li>
        <li>Student concern briefs — who needs support today</li>
        <li>Teacher Growth Passport and CPD tracker</li>
        <li>Wellbeing check-in and workload visibility</li>
      </ul>
      <div class="dash-btn">Enter Teacher Dashboard <span class="dash-arrow">→</span></div>
    </a>
    <a href="{PLATFORM_URL}/school" class="dash-card dash-purple reveal reveal-delay-1" target="_blank" rel="noopener">
      <div class="dash-icon">🏛️</div>
      <div class="dash-label">For School Leaders</div>
      <div class="dash-title">School Intelligence Dashboard</div>
      <p class="dash-desc">Replace lagging reports with real-time institutional intelligence. Know what is happening across your school — teachers, students, parents — before it becomes a problem.</p>
      <ul class="dash-features">
        <li>School performance trends and subject analysis</li>
        <li>Teacher wellbeing, workload, and retention risk</li>
        <li>Student cohort risk monitoring — 14+ days early</li>
        <li>Attendance intelligence and punctuality patterns</li>
        <li>Parent engagement metrics and communication quality</li>
        <li>School improvement tracking with measurable targets</li>
      </ul>
      <div class="dash-btn">Enter Leadership Dashboard <span class="dash-arrow">→</span></div>
    </a>
  </div>
</section>
""")

write("06-pricing.html", """
<section id="pricing">
  <div class="section-label reveal">Pricing</div>
  <h2 class="section-title reveal reveal-delay-1">Institutional partnerships.<br>Family subscriptions.</h2>
  <p class="section-body reveal reveal-delay-2">Fluent operates a dual revenue model — designed to serve both schools and families simultaneously, at every investment level.</p>
  <p class="pricing-note reveal">All prices in Indian Rupees. B2B pricing in ₹/student/month (annual contract). B2C pricing per scholar/month.</p>
  <div class="pricing-tabs reveal">
    <button class="pricing-tab active" onclick="switchTab('b2b', this)">School Partnerships (B2B)</button>
    <button class="pricing-tab" onclick="switchTab('b2c', this)">Family Programmes (B2C)</button>
  </div>
  <div id="b2b-panel" class="pricing-panel b2b-panel active">
    <div class="price-card">
      <div class="price-name">Pilot Programme</div>
      <div class="price-amount">₹415 <span>/student/month</span></div>
      <div class="price-period">8-week pilot · 50% of annual rate · Converts on outcomes</div>
      <p class="price-desc">Prove the model. One cohort, 8 weeks, full platform access. If AFS does not improve by 15+ points, no obligation to continue.</p>
      <ul class="price-features"><li>Full platform access for pilot cohort</li><li>British faculty sessions (2x/week)</li><li>Teacher CPD workshop</li><li>AFS outcomes report at close</li><li>Guardian Portal for pilot families</li></ul>
      <a href="#contact" class="btn-outline">Apply for Pilot</a>
    </div>
    <div class="price-card featured">
      <div class="price-badge">Most Popular</div>
      <div class="price-name">School Partnership</div>
      <div class="price-amount">₹830 <span>/student/month</span></div>
      <div class="price-period">Annual contract · Minimum 100 students · ₹9.96 lakh/year</div>
      <p class="price-desc">The full Fluent Institute school transformation programme — every pillar, every feature, every intelligence layer, for your entire institution.</p>
      <ul class="price-features"><li>Full platform — Scholar Studio, Guardian Portal, Dashboards</li><li>British faculty sessions embedded in timetable</li><li>Complete Teacher CPD programme</li><li>School Intelligence Dashboard</li><li>AI lesson planning, marking, reporting</li><li>Parent engagement platform with AI assistant</li><li>Dedicated school success manager</li></ul>
      <a href="#contact" class="btn-gold">Book a School Demo</a>
    </div>
  </div>
  <div id="b2c-panel" class="pricing-panel b2c-panel">
    <div class="price-card">
      <div class="price-name">Guardian Protocol</div>
      <div class="price-amount">₹8,500 <span>/month</span></div>
      <div class="price-period">AI-supported independent learning</div>
      <p class="price-desc">Full AI scaffolding, curriculum vault, and parent dashboard. For families wanting intelligent independent revision support.</p>
      <ul class="price-features"><li>Scholar Studio full access</li><li>AI Tutor — RAG curriculum-grounded</li><li>Guardian Portal and weekly updates</li><li>Mastery Ledger and AFS tracking</li><li>Home learning guidance</li></ul>
      <a href="#contact" class="btn-outline">Get Started</a>
    </div>
    <div class="price-card featured">
      <div class="price-badge">Flagship</div>
      <div class="price-name">Mastery Cohort</div>
      <div class="price-amount">₹14,500 <span>/month</span></div>
      <div class="price-period">Live British faculty · Cohorts capped at 20 scholars</div>
      <p class="price-desc">Direct instruction from British faculty, AI grounding, Synthesis Labs, and full parent partnership. The complete Fluent scholar experience.</p>
      <ul class="price-features"><li>Everything in Guardian Protocol</li><li>Live British faculty sessions (2x/week)</li><li>Synthesis Labs — applied learning workshops</li><li>Monthly Guardian progress report</li><li>Small cohort (max 20 scholars)</li><li>Priority faculty messaging</li></ul>
      <a href="#contact" class="btn-gold">Enrol Your Scholar</a>
    </div>
    <div class="price-card">
      <div class="price-name">Synthesis Elite</div>
      <div class="price-amount">₹30,000 <span>/month</span></div>
      <div class="price-period">Premium personalised · University & exam focused</div>
      <p class="price-desc">Highly personalised for scholars targeting Oxbridge, IIT, NEET, or international university admissions. A dedicated academic coach.</p>
      <ul class="price-features"><li>Everything in Mastery Cohort</li><li>1:1 sessions with British faculty</li><li>Personal academic coach</li><li>Custom learning pathway</li><li>University application support</li><li>Quarterly strategy sessions</li></ul>
      <a href="#contact" class="btn-outline">Apply for Elite</a>
    </div>
  </div>
</section>
""")

write("07-rest.html", """
<section id="roadmap">
  <div class="section-label reveal">Product Roadmap</div>
  <h2 class="section-title reveal reveal-delay-1">Built in phases.<br>Each one proven before the next begins.</h2>
  <div class="roadmap-timeline">
    <div class="roadmap-phase rp1 reveal">
      <div class="rp-phase">Phase 1 — Now to Q4 2026</div>
      <div class="rp-period">Academic Fluency Platform</div>
      <div class="rp-title">The Foundation</div>
      <ul class="rp-items"><li>Scholar Studio — 9 interfaces live</li><li>Guardian Portal — 10 sections live</li><li>AI RAG tutor (Gemini, CBSE/ICSE)</li><li>Lesson plan generator</li><li>Auto-marking engine</li><li>Academic Fluency Score (AFS)</li><li>First school pilot — Bengaluru</li><li>Outcomes data generation</li></ul>
      <div class="rp-milestone">Target: First school contract Q3 2026</div>
    </div>
    <div class="roadmap-phase rp2 reveal reveal-delay-1">
      <div class="rp-phase">Phase 2 — Q1 to Q2 2027</div>
      <div class="rp-period">School Transformation Platform</div>
      <div class="rp-title">The Intelligence</div>
      <ul class="rp-items"><li>Student knowledge graph (Neo4j)</li><li>Triangulated signal engine</li><li>Passive behavioural signal collection</li><li>Agentic intervention loop (LangGraph)</li><li>Parent conversational AI</li><li>Teacher wellbeing module</li><li>5 school contracts</li><li>Seed round — £500K–£1M</li></ul>
      <div class="rp-milestone">Target: 500+ scholars, 5 schools Q2 2027</div>
    </div>
    <div class="roadmap-phase rp3 reveal reveal-delay-2">
      <div class="rp-phase">Phase 3 — Q3 2027 to Q4 2028</div>
      <div class="rp-period">Learning Intelligence Ecosystem</div>
      <div class="rp-title">The Digital Twin</div>
      <ul class="rp-items"><li>Full AI Education Brain</li><li>W3C Verifiable Credential layer</li><li>Portable student credential wallet</li><li>All CBSE/ICSE subjects covered</li><li>EU pilot institution (UK/Germany)</li><li>25+ school contracts</li><li>5,000+ scholars on platform</li><li>Series A initiated</li></ul>
      <div class="rp-milestone">Target: The Digital Twin of Human Learning</div>
    </div>
  </div>
</section>
<section id="investor">
  <div class="section-label reveal">For Investors</div>
  <h2 class="section-title reveal reveal-delay-1">A category of one.<br>Seed round open.</h2>
  <div class="investor-grid">
    <div class="investor-metrics reveal">
      <div class="inv-metric"><div class="inv-num">$103<span>B</span></div><div class="inv-label">India K-12 Private Market (2025)</div></div>
      <div class="inv-metric"><div class="inv-num">$276<span>B</span></div><div class="inv-label">Projected 2034 at 13% CAGR</div></div>
      <div class="inv-metric"><div class="inv-num">400<span>K</span></div><div class="inv-label">Affordable Private Schools in India</div></div>
      <div class="inv-metric"><div class="inv-num">₹4.5<span>cr</span></div><div class="inv-label">Projected Phase 2 Annual ARR</div></div>
      <div class="inv-metric"><div class="inv-num">70<span>%</span></div><div class="inv-label">Gross Margin at Phase 2 Scale</div></div>
      <div class="inv-metric"><div class="inv-num">20<span>:1</span></div><div class="inv-label">B2B LTV:CAC Ratio</div></div>
    </div>
    <div class="investor-text reveal reveal-delay-1">
      <div class="inv-block"><div class="inv-block-title">The Category Opportunity</div><div class="inv-block-body">No platform occupies the intersection of live British faculty + subject academic fluency + school-integrated AI intelligence. Fluent is a category of one — not competing with LEAD, Extramarks, or PlanetSpark, but solving a problem they are structurally unable to solve.</div></div>
      <div class="inv-block"><div class="inv-block-title">The Structural Moat</div><div class="inv-block-body">Every day the platform runs, the student knowledge graph deepens. After 18 months of student data, the graph becomes impossible to replicate overnight. First-mover advantage compounds. Network effects protect. Credential portability creates lifetime retention.</div></div>
      <div class="inv-block"><div class="inv-block-title">The Founding Team</div><div class="inv-block-body">Dr. Gnaneshwer Jadav (CEO) — PhD Immunology, South East London, product leader. Akhil (CTO) — full-stack engineering. William Hardman — practising UK teacher, CPD design. The British-Indian dual context is Fluent's unfair advantage.</div></div>
      <div class="inv-block"><div class="inv-block-title">The Ask</div><div class="inv-block-body">Seed round: £500K–£1M. Use of funds: 2 additional engineers, 1 school sales executive, regulatory compliance, and 6-month runway to 5 school contracts and £35–40 lakh MRR. Series A targeted Q4 2028 with 25+ schools and 5,000+ scholars.</div></div>
    </div>
  </div>
  <div class="investor-cta reveal">
    <div class="section-label" style="justify-content:center;display:flex">Interested in Fluent?</div>
    <p>We are building the most intelligent school transformation platform in the world — starting in India, expanding to Europe. If you are an investor aligned with education, AI, or emerging market growth, we would welcome a conversation.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
      <a href="mailto:info@fluent.academy" class="btn-primary">Request Investor Deck</a>
      <a href="mailto:info@fluent.academy" class="btn-outline">Schedule a Call</a>
    </div>
  </div>
</section>
<section id="belief">
  <div class="section-label" style="display:block;text-align:center;margin-bottom:.8rem">Our Belief</div>
  <p class="belief-quote">Education should not merely produce students who can <strong>pass examinations</strong>. It should produce individuals who can think critically, communicate clearly, solve problems confidently, and contribute meaningfully to society.</p>
  <div class="belief-tagline">That is why Fluent exists.</div>
  <p class="belief-sub">We do not teach subjects. We architect scholars.</p>
</section>
<section id="contact">
  <div class="section-label reveal">Get in Touch</div>
  <h2 class="section-title reveal reveal-delay-1" style="max-width:20ch">Book a demo.<br>Transform your school.</h2>
  <p class="section-body reveal reveal-delay-2" style="margin-bottom:3rem">Whether you are a school principal, an aspirational parent, a prospective teacher, or an investor — we would love to speak with you.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;max-width:800px" class="reveal">
    <a href="mailto:info@fluent.academy?subject=School Demo Request" class="btn-primary" style="text-align:center;padding:1.1rem 2rem">Book a School Demo →</a>
    <a href="mailto:info@fluent.academy?subject=Family Enrolment" class="btn-gold" style="text-align:center;padding:1.1rem 2rem">Enrol Your Scholar →</a>
  </div>
  <div style="height:4rem"></div>
  <div class="contact-divider"></div>
  <div class="contact-grid">
    <div class="contact-brand">
      <a href="#hero" class="nav-logo">Fl<span>u</span>ent</a>
      <p class="contact-desc">School Transformation & Learning Intelligence Platform. Building better teachers, developing confident scholars, and creating smarter schools — from London to Bengaluru.</p>
    </div>
    <div class="contact-links">
      <h4>Platform</h4>
      <ul>
        <li><a href="#platform">Scholar Studio</a></li>
        <li><a href="#platform">Guardian Portal</a></li>
        <li><a href="#platform">Teacher Dashboard</a></li>
        <li><a href="#platform">School Intelligence</a></li>
        <li><a href="#pricing">Pricing</a></li>
      </ul>
    </div>
    <div class="contact-links">
      <h4>Contact</h4>
      <div class="contact-info">
        <div class="contact-info-item"><span class="contact-info-icon">✉</span>info@fluent.academy</div>
        <div class="contact-info-item"><span class="contact-info-icon">📱</span>+44 7553 886303 (WhatsApp)</div>
        <div class="contact-info-item"><span class="contact-info-icon">🌐</span>fluent.institute</div>
        <div class="contact-info-item"><span class="contact-info-icon">📍</span>London, United Kingdom</div>
        <div class="contact-info-item"><span class="contact-info-icon">📍</span>Bengaluru, India</div>
      </div>
    </div>
  </div>
  <div class="contact-divider"></div>
  <div class="contact-bottom">
    <div class="contact-copy">© 2026 Fluent Institute. All rights reserved. · <a href="#">Privacy Policy</a> · <a href="#">Terms</a></div>
    <div class="contact-bottom-right">We do not teach subjects. We architect scholars.</div>
  </div>
</section>
""")

ORDER = [
    "01.html",
    "02.html",
    "03-pillars.html",
    "04-how-ai.html",
    "05-platform.html",
    "06-pricing.html",
    "07-rest.html",
]

body_parts = []
for fname in ORDER:
    path = PARTIALS / fname
    if path.exists():
        body_parts.append(path.read_text(encoding="utf-8").strip())

body = "\n\n".join(body_parts)

index = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fluent Institute — School Transformation & Learning Intelligence Platform</title>
<meta name="description" content="Fluent Institute transforms schools through teacher excellence, student academic fluency, parent partnership, and AI-powered school intelligence.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&family=Outfit:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{body}
<script src="main.js"></script>
</body>
</html>
"""

(ROOT / "index.html").write_text(index, encoding="utf-8")
print(f"Assembled index.html ({len(index)} bytes)")
