# The Qualitative HCI Landscape of UC Irvine Informatics — survey: who does qualitative, STS, and health information work

<div class="lang-switch" markdown>
🌐 Language / 语言：[中文](015-uci-informatics-qualitative.zh.md) · **English**
</div>

<div class='marg-meta'><span>📅 2026-09-05</span><span>🏷️ survey(department survey)</span><span>🐙 issue #39</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-015</td></tr><tr><td>title</td><td>The Qualitative HCI Landscape of UC Irvine Informatics — survey: who does qualitative, STS, and health information work</td></tr><tr><td>date</td><td>2026-09-05</td></tr><tr><td>published</td><td>2026-09-05</td></tr><tr><td>kind</td><td>survey(department survey)</td></tr><tr><td>issue</td><td>39</td></tr></table></details>

> A department survey. The question: within an informatics department, what scholarly communities make up the non-software-engineering half, and what are the **qualitative, STS, and anthropology-oriented** scholars actually doing? This note cross-validates four channels — a structured capture of the department's People page, the department's own yearly CHI/CSCW paper lists, per-author OpenAlex pulls (2022–2026), and self-descriptions from lab and personal sites. **Bottom line: the qualitative half of this department splits into three blocks plus one flank — critical/STS–anthropology; qualitative health + accessibility; games/learning/youth-culture — with a quantitative/implementation flank on the health side. Health information here is far more qualitative than the "systems plus user studies" stereotype suggests, and the biggest new cluster in 2025–26 is GenAI × disability/health.**

## 1. Motivation and method

Answering "who does qualitative work in department X" from memory or one-off searches fails fast: rosters change, names collide, emeriti mix with active faculty. Four channels, cross-checked:

1. **Roster table**: capture and structure the People page (rank, track, section) to separate core, affiliated, emeriti, and teaching-track faculty;
2. **Labs and students**: capture self-descriptions from lab/center sites (EVOKE, ARC, CREATE, CLL, PIE Lab, etc.) and infer student directions from paper author lists;
3. **Per-author OpenAlex pulls**: works 2022–2026 (watch name collisions — "Yunan Chen" resolves to a materials scientist and "Kai Zheng" to TCM literature unless you filter by name + institution);
4. **Venue sweep**: the department maintains its own yearly CHI/CSCW paper lists (more complete and faster than databases, including awards), plus institution-filtered journal queries for BD&S/STHV/ToCHI.

One practical note: UC Irvine's OpenAlex institution id is `I204250578`; combining `raw_author_name.search` with `institutions.id` avoids most homonym traps.

## 2. The landscape and recent changes

**Three blocks plus one flank** (excluding the SE side: van der Hoek, Malek, Ahmed, Garcia, Moshirpour, James A. Jones, Thomas Zimmermann, Daye Nam, etc.):

- **Critical / STS–anthropology**: Paul Dourish, Melissa Mazmanian, Roderic Crooks, Mimi Ito;
- **Qualitative health + accessibility**: Yunan Chen, Madhu Reddy, Daniel Epstein, Elena Agapie, Stacy Branham, Anne Marie Piper, Gillian Hayes;
- **Games / learning / youth culture** (under the Connected Learning Lab): Kurt Squire, Constance Steinkuehler, Katie Salen Tekinbas, Kylie Peppler, Aaron Trammell;
- **Quantitative/implementation flank** (the other face of health informatics): Kai Zheng, Sean Young; plus the sustainability outpost of Bill Tomlinson.

Recent structural changes (worth updating any mental model):

- **Emeriti**: Gloria Mark (attention), Bonnie Nardi (anthropology of technology), Geoffrey Bowker (STS), Gary & Judy Olson (CSCW founders), David Redmiles. Nardi still publishes (ToCHI 2023, *Post-growth Human–Computer Interaction*).
- **Departed**: Yubo Kou and Bryan Semaan no longer appear on the People page.
- **New arrivals**: Elena Agapie (ex-Microsoft Research), Anne Marie Piper, Madhu Reddy (ex-Penn State) — three strong qualitative HCI hires.
- **Administration and honors**: Yunan Chen is department chair; Dourish received the **2025 ACM SIGCHI Lifetime Achievement in Research Award** and directs the Steckler Center (CREATE); Hayes is now Vice Provost for Academic Personnel (still leading STAR); Mazmanian holds a joint appointment with the Merage School of Business; Piper chaired CHI 2026's Accessibility Subcommittee; Dourish-group PhD Eunkyung Jo won the CHI 2026 Outstanding Dissertation Award.

## 3. The core table

Method/theory attributions are my reading of self-descriptions plus publication patterns; quoted keywords are verbatim where possible.

| Scholar | Position | Self-description (keywords) | Method/theory | Recent topics |
|---|---|---|---|---|
| **Paul Dourish** | Chancellor's Professor; CREATE director | Applies anthropology, STS, cultural studies to digital practice; **data imaginaries**; pragmatism, symbolic interactionism, practice theory, British cultural studies, feminist epistemology, decolonial critique, ethnomethodology | Ethnography; critical theory | Data relations in local governance (CSCW'24, *Reconfiguring Data Relations*); aesthetics of programming (STHV'24, with Mazmanian) |
| **Melissa Mazmanian** | Professor; joint with Merage School | "Trained as a sociologist of work"; technologies as used-in-practice (creative work, predictive systems, quantification, busy professionals' everyday lives) | Organizational ethnography; meso-organization theory | Data integrity as ecosystem (MISQ'25, *The Myth of Good Data*); government data storytelling (BD&S'25); the crisis of care; data work of direct service providers (CHI'26) |
| **Roderic Crooks** | Associate Professor; EVOKE Lab PI | Continues **social informatics**: "racial, cultural, ethical, and political dimensions of computing"; draws on HCI, STS, media studies, **Black studies** | Social informatics; data justice; qualitative and design | Community organizers' data practices; the carceral state; surveillance and race (Surveillance & Society); governments as design contexts |
| **Mimi Ito** | Professor in Residence; CLL director | Cultural anthropologist of digital youth culture + learning scientist; connected learning | Cultural anthropology; participatory/design research | Ed. *Youth Well-Being by Design* (MIT Press 2026); Youth Connections for Wellbeing; neurodiversity × AI; algorithmic rights for children |
| **Stacy Branham** | Associate Professor; ARC | Accessible computing; "informed by **disability studies, critical theory, participatory design, action research**" | Qualitative; co-design; autoethnography | BLV users and GenAI; adult braille learners; career mobility of BLV software professionals; technology adoption at life transitions (TACCESS'26) |
| **Anne Marie Piper** | Associate Professor; CREATE associate director | Accessibility, aging, caregiving, human–AI interaction | Qualitative/mixed; participatory design | *The Accessibility Paradox* of BLV employees (CSCW'25 Best Paper); GenAI for information access; conversational AI for aging (review); Chinese Deaf creators' translation work (CHI'26 HM) |
| **Yunan Chen** | Professor & **department chair** | HCI × CSCW × health informatics; "how health information is generated, managed, shared, and utilized" | Strongly qualitative CSCW; sociotechnical information practices | Nannies' risk work (CSCW'25 HM + CHI'26); car dwellers (CHI'26); ChatGPT in mental health conversations (CSCW'25 Best Paper); adolescents and health AI via design fiction |
| **Madhu Reddy** | Professor; Grad Programs Associate Dean | CSCW × mental health / health IT; patient safety | Qualitative + co-design | Depression self-management kits; co-designing digital mental health with Asian Americans (CHI'25); Taiwanese emerging adults; tools for Black adults; Reddit support-seeking (CSCW'25) |
| **Daniel Epstein** | Associate Professor; PIE Lab | Personal informatics; HCI × health | Qualitative+mixed; deployment + interviews | Temporality of baby tracking; family health-tracking ecologies; women's health and genetics; abandonment; public agencies' AI health chatbots |
| **Elena Agapie** | Assistant Professor (ex-MSR) | **Goals** and behavior change in HCI × health; engagement in digital mental health | Qualitative+mixed; clinical collaboration | Therapist–client goal collaboration (CSCW'24); goals-for-behavior-change meta-analysis (CHI'25); everyday disruptions to goals (CHI'26) |
| **Gillian Hayes** | Chancellor's Professor; Vice Provost | "Design, develop, deploy, and evaluate technologies…in sensitive and ethically responsible ways"; assistive + educational tech + health informatics | Mixed methods; participatory design | Autism × LLM bias (CHI'25); wearables for noise sensitivity (CHI'26); collaborative practices of ADHD students; co-design in low-income South African settings |
| **Kurt Squire / Constance Steinkuehler / Katie Salen / Kylie Peppler** | CLL cluster | Games × learning; toxicity/extremism (discourse analysis); play theory; learning sciences/making | Design research; mixed; discourse analysis | Community-based GenAI design with reentry youth; game toxicity; museums and curiosity (CHI'25 HM); craft × computational thinking; child–AI co-creation |
| **Aaron Trammell** | Professor | Game studies, subculture, race/whiteness in game culture; Analog Game Studies editor | Critical media studies; cultural studies | D&D, rules, race and desire; geeks and whiteness; postfeminist control (GLaDOS chapter) |
| **Kai Zheng / Sean Young** | Professors | Health IT, ambient AI; social media × public health behavior | Quantitative/implementation science, with qualitative strands | Clinician edits to ambient AI documentation (JAMIA'26 series); implementing digital mental health; social-media HIV testing interventions |

Affiliated faculty often counted in this circle: Bonnie Ruberg (now Film & Media Studies; **queer game studies**; qualitative + critical media theory), June Ahn (School of Education, Informatics by courtesy; participatory design/RPP), Stephen Schueller and Candice Odgers (Psychological Science; digital mental health / adolescent wellbeing), Mark Warschauer (Education).

## 4. The two faces of health informatics

Health informatics here is **double-layered**, and it is the easiest part of the department to misread:

- **The qualitative CSCW wing**: Chen's information-practices tradition (in-situ studies of caregivers' and patients' work), Reddy's mental-health co-design, Epstein's personal informatics, Agapie's goals-and-clinics line. Their output lives mostly in PACMHCI and leans on interviews, fieldwork, and co-design;
- **The quantitative/implementation wing**: Zheng's clinical NLP and ambient-AI documentation research (a JAMIA output machine), Young's social-media behavioral interventions (public-health trials), and the Future Health Institute's wearables and agentic AI (engineering-led, directed by Ramesh Jain / Amir Rahmani).

The two wings share institutes but have nearly incompatible academic tastes. Prospective students who want qualitative health research should read the door signs carefully.

## 5. Venue sweep

The department maintains its own yearly lists (fresher than any database, including awards and committee roles):

- **CSCW 2025: 14 papers.** Two Best Papers (Piper's accessibility paradox; Chen group's ChatGPT mental-health conversations) plus an Honorable Mention (the Chen group's nannies' risk work). Clusters: mental health × LLM/platforms, accessibility, care and gig work, government data and public records, infrastructural work around housing insecurity.
- **CHI 2025: 28 papers** (incl. LBW/SIG/Workshop). Digital mental health × minoritized groups, BLV × GenAI, personal informatics, aging × conversational AI, clinically useful AI in a global frame, games and learning.
- **CHI 2026: 23 full papers.** The largest new cluster is **GenAI × disability/health** (autism LLM bias, blind users' GenAI, co-designing stuttered-speech annotation, AI-for-accessibility rhetoric vs responsibility, adolescents' views of health AI).
- **Journals (OpenAlex 2023–26):** PACMHCI 36; Big Data & Society 1 (Mazmanian group, government data storytelling); STHV 1 (Dourish/Mazmanian, aesthetics of programming); ToCHI 5. The 4S conference is not well indexed by OpenAlex and can only be tracked via homepages.

## 6. Method notes and limitations

- **Homonym disambiguation is the biggest trap** in per-author pulls: without name+institution filtering, a professor's recent output can appear to teleport into an unrelated field; always spot-check titles;
- **The department's own yearly paper lists are an underrated data source**: fresher than OpenAlex (2026 items already live), awards and committee roles included, already filtered to departmental affiliation;
- Snapshot validity: roster data as of 2026-09-05; whether emeriti still advise and whether labs are recruiting should be checked against their own pages (EVOKE, for one, states it accepts students only via the Graduate Division with relevant experience);
- This note maps public information; it is not an admissions or application judgment.

---

*Read this note in [中文](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/015-uci-informatics-qualitative/note.zh.md).*


---

> 🌐 [阅读中文版](015-uci-informatics-qualitative.zh.md)

