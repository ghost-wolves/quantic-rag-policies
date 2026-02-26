# Audit Report — 5 High-Risk Evaluation Items

This report is for manual verification of groundedness and citation accuracy.
It prints each question, the model answer, and the cited evidence chunks.
It also prints an overlap ratio as a *hint* (not a score).

## q08

**Question:**

> How do the documents define a cybersecurity incident (if defined)?

**Answer:**

```text
The provided excerpts do not contain a specific definition of a cybersecurity incident. They mention the importance of classifying what a security incident is and refer to guidelines from NIST, but do not provide a clear definition within the text. 

Citations: [C2], [C3], [C4]
```

**Answer↔Evidence keyword overlap ratio (hint):** `0.375`

**Top answer terms:** `do`(2), `definition`(2), `incident`(2), `provided`(1), `excerpts`(1), `contain`(1), `specific`(1), `cybersecurity`(1), `mention`(1), `importance`(1), `classifying`(1), `security`(1)

### Evidence chunks

#### C1: `mississippi-state-incident-response-plan__00039`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 25350-26150

```text
onent incident report or situational
awareness update
• Third-party reporting of network activity to known compromised
infrastructure, detection of malicious code, loss of services, etc.
• Analytics or hunt teams that identify potentially malicious or otherwise
unauthorized activity
Any of the previous events can initiate the incident response process (as described
previously) through the declaration of the incident, where “declaration” refers to the
identification of an incident and communications to ITS Security rather than formal
declaration of a major incident as defined in applicable law and policy.
A copy of the CIRP Response Checklist Template will be initiated to provide a timeline
and details of the steps taken of the response to the incident.
5.2.1.2 Determine Scope
A key compone
```

#### C2: `cybersecurity-incident-response-plans__00009`
- doc_id: `cybersecurity-incident-response-plans`
- title: Cybersecurity Incident
- span: 5850-6650

```text
ST

Cybersecurity Incident Response Plans
18
NIST Special Publication (SP) 800-61
• Computer Security Incident Handling Guide
 NIST SP 800-61 r2
• Seeks to give organizations practical guidelines
• Not regulatory documents
• Primary focus: Detecting, analyzing, prioritizing,
and handling incidents
19

What Is a Cybersecurity Incident
Response Plan?
20
Create an Incident Response Policy
• Initially creating an Incident Response Policy:
 Classify what a security incident is
 Who is responsible for responding to an event?
 Roles and responsibilities
 Documentation
 Reporting requirements
21
Prior to making an Incident Response Plan, it is recommended to create an incident response policy.
Source: pratum
Incident Response Plan Policy
• Provides a road map for a Statement of Management Co
```

#### C3: `cybersecurity-incident-response-plans__00010`
- doc_id: `cybersecurity-incident-response-plans`
- title: Cybersecurity Incident
- span: 6500-7300

```text
recommended to create an incident response policy.
Source: pratum
Incident Response Plan Policy
• Provides a road map for a Statement of Management Commitment, which outlines the
purpose and objectives of the policy incident response capabilities.
• Scope of the policy (to whom and what it applies, and under what circumstances)
• Definition of computer security incidents and related terms
• Organizational structure:
 Definitions of roles and responsibilities
 Levels of authority
• Prioritization or severity ratings of incidents
• Performance measures
• Reporting and contact forms
22
According to NIST: “Policy governing incident response is highly individualized to the organization. However,
most policies include the same key elements.”

What Is a Cybersecurity Incident Response Plan?
• A
```

#### C4: `cybersecurity-incident-response-plans__00011`
- doc_id: `cybersecurity-incident-response-plans`
- title: Cybersecurity Incident
- span: 7150-7950

```text
highly individualized to the organization. However,
most policies include the same key elements.”

What Is a Cybersecurity Incident Response Plan?
• A written and systematic approach that
establishes procedures and documentation.
• Incident Response Policy
• Can include items such as:
 Guidelines
 Roles and responsibilities
 Communication plans
 Standard protocols
• Incident Response Teams
• Tailored playbooks specific to the organization
23
Teams
Plans
Policy
Incident Response Plan Elements
• Measuring the capability and
effectiveness of incident response
• Planning for growth of incident
response capabilities
• How the program fits into the overall
organization
24
An Incident Response Plan is a written document that helps your organization before, during, and after a
security inciden
```

#### C5: `mississippi-state-incident-response-plan__00185`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 120250-121050

```text
t. In NIST Computer
Security Resource Center Glossary of Key Information Security Terms.
https://csrc.nist.gov/glossary/term/cybersecurity_incident#:~:text=Definitions%3A,NIST
%20Cybersecurity%20Framework%20Version%201.1
National Institute of Standards and Technology. (n.d.) Threat Actor. In NIST Computer
Security Resource Center Glossary of Key Information Security Terms.
https://csrc.nist.gov/glossary/term/threat_actor
National Institute of Standards and Technology. (n.d.) Vulnerability. In NIST Computer
Security Resource Center Glossary of Key Information Security Terms.
https://csrc.nist.gov/glossary/term/vulnerability
Payment Card Industry Security Standards Council. (2022). Cardholder. In Payment
Card Industry Data Security Standard: Requirements and Testing Procedures.
https://docs-
```

### Manual scoring checklist
- Groundedness (1/0): Are *all key claims* in the answer supported by the evidence above?
- Citation accuracy (1/0): Do the cited chunks contain the specific supporting statements?

---

## q10

**Question:**

> Who should be notified first when a cybersecurity incident is detected (if specified)?

**Answer:**

```text
The first person to be notified when a cybersecurity incident is detected is the Chief Information Security Officer (CISO). The CISO then notifies and activates the Cybersecurity Incident Response Team (CIRT) and declares the incident, after which an Incident Manager is assigned [C1].

Citations: [C1]
```

**Answer↔Evidence keyword overlap ratio (hint):** `0.682`

**Top answer terms:** `incident`(4), `cybersecurity`(2), `ciso`(2), `c1`(2), `first`(1), `person`(1), `notified`(1), `detected`(1), `chief`(1), `information`(1), `security`(1), `officer`(1)

### Evidence chunks

#### C1: `mississippi-state-incident-response-plan__00115`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 74750-75550

```text
ion within
TeamDynamics. Incident response can end after documentation.
• High/Emergency: notify CISO, CISO notifies/activates CIRT, declares
incident, Incident Manager assigned.
• Activate communication channels needed for the appropriate CIRT members
needed for the incident and others that must be notified, including:
• If health information, see Appendix C for further details.
• MDITS
- By the end of the next business day following discovery of
incident if there is any impact to the University (including Low
severity incidents).
• Local/federal law enforcement.
• Federal agency/agencies (such as CISA or DoD).
• Determine initial investigation scope.
• Internal
- How many endpoints were affected?
- How many servers were affected?
- Were backups affected?
- Was Shared folder location affe
```

#### C2: `mississippi-state-incident-response-plan__00061`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 39650-40450

```text
ee Appendix G for further details.
• MDITS
Page 16

- By the end of the next business day following discovery of
incident if there is any impact to the University (including Low
severity incidents).
• Local/federal law enforcement
• Federal agency/agencies (such as CISA or Department of Defense (DoD))
• Determine initial investigation scope.
• Perform technical analysis (step is complete when incident has been verified,
scope determined, method(s) of persistent access to the network has/have been
identified, impact has been assessed, hypothesis for the narrative of exploitation
has been created (TTPs and IOCs), and all stakeholders are proceeding with a
common operating picture)
• Collect logs related to the event. These include, but are not limited to:
- Network devices
- Centralized logg
```

#### C3: `mississippi-state-incident-response-plan__00033`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 21450-22250

```text
e appropriate
individuals/teams shall be notified as soon as possible.
To use the Escalation Path table, the individual/team will notify the individual/team
directly to the right of themselves for that level of severity tier as the incident progresses
and the severity tier potentially increases. For example, an “Emergency” severity incident
will first be handled by the Service Desk, then be in communication with the Incident
Manager (once one is assigned by the CISO). The Incident Manager will then inform the
CISO of the escalation, then the CISO will notify the CIO, and then the CIO will notify
Legal of the escalation. The Incident Manager will then notify the CTTO of the
escalation of the incident and the CTTO will notify the Office of Strategic
Communications if they deem it necessary.
```

#### C4: `mississippi-state-incident-response-plan__00080`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 52000-52800

```text
ident.
• Cyber Security
- Check with REN- ISAC.
- Check with Cloud Hosting Service Providers.
- If DNS related, contact Cisco (Umbrella) or DNS
service provider.
• Office of Strategic Communications Team
Page 22

- Check with Cloud Service Provider hosting their
materials.
- Check social media (Facebook, Instagram, X, etc.).
• Check global reports of similar incidents to help determine scope.
- Are there reports of global issues where the institution would be
collateral damage?
• Check internet health and traffic reports to rule out global
issues.
• Check Content Delivery Network (CDN).
- Validate organization communication.
• Email
• VOIP infrastructure
• Identify root cause and enabling conditions.
- Attempt to identify root cause of the incident and collect threat
information for furthe
```

#### C5: `mississippi-state-incident-response-plan__00159`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 103350-104150

```text
information about the
possible breach so he or she can conduct an appropriate risk
assessment. The information should describe the nature of the
PHI that was disclosed, how well people were identified on it,
where it was exposed, who might have seen it, and whether or
not it was delivered.
• MDITS
- By the end of the next business day following discovery of
incident if there is any impact to the University (including Low
severity incidents).
Page 49

• Local/federal law enforcement
• Affected Individuals: Covered entities are required to notify affected
individuals whose PHI/ePHI has been compromised as a result of the
breach. Notifications should be provided in writing and include specific
information about the breach, steps individuals can take to protect
themselves, and resources for a
```

### Manual scoring checklist
- Groundedness (1/0): Are *all key claims* in the answer supported by the evidence above?
- Citation accuracy (1/0): Do the cited chunks contain the specific supporting statements?

---

## q13

**Question:**

> Do the documents mention preserving evidence or logs during an incident? Summarize.

**Answer:**

```text
Yes, the documents mention preserving evidence and logs during an incident. Specifically, they outline the importance of collecting and preserving data for incident verification, categorization, prioritization, mitigation, and reporting. This includes gathering logs from various affected devices such as perimeter, internal network, endpoint, audit logs, connection logs, system performance logs, and user activity logs. Additionally, it emphasizes the need to maintain a detailed log for all evidence collected, in compliance with applicable policies and standards, including the NIST Computer Security Incident Handling Guide. Incident documentation should also be kept for at least three years unless otherwise required by law enforcement or federal agency policy.

Citations: [C1], [C3], [C4]
```

**Answer↔Evidence keyword overlap ratio (hint):** `0.690`

**Top answer terms:** `logs`(6), `incident`(4), `preserving`(2), `evidence`(2), `yes`(1), `documents`(1), `mention`(1), `during`(1), `specifically`(1), `outline`(1), `importance`(1), `collecting`(1)

### Evidence chunks

#### C1: `mississippi-state-incident-response-plan__00042`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 27300-28100

```text
incident through its classification.
5.2.1.3 Collect and Preserve Data
Collect and preserve (including for potential law enforcement investigation) data for
incident verification, categorization, prioritization, mitigation, reporting, and ascribing.
Data and logs should be collected from as many of the affected devices as possible,
including, but not limited to, data from the perimeter, internal network, endpoint (server
and host), audit logs, connection logs, system performance logs, and user activity logs.
Collection of evidence, including forensic data, happens during this component of the
incident response with meeting all applicable polices and standards that include a detailed
log that is kept for all evidence (refer to NIST Computer Security Incident Handling
Guide, SP 800-61 r2).
```

#### C2: `mississippi-state-incident-response-plan__00109`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 70850-71650

```text
lerts, and Log Collection
• Add enterprise-wide detections to mitigate against adversary TTPs that
were executed to cause the incident.
• Identify and mitigate operational “blind spots” to complete coverage
moving forward.
Page 31

• Continue to monitor the University environment for evidence of persistent
presence.
6.3.3.2 Finalize Reports
• Provide post-incident updates as required by law and policy.
• Publish post-incident report. Provide a step-by-step review of the entire
incident and answer the “Who”, “What”, “Where”, “Why”, and “How”
questions. Provide a completed version of the CIRP Response Checklist
Template and the Incident Response Report in Appendix E.
• Work with MDITS and any other agencies and law enforcement to
provide any additional information/evidence/actions required.
```

#### C3: `mississippi-state-incident-response-plan__00053`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 34450-35250

```text
iety of incidents and can be used with tailoring to
specific incidents.
• Reconnecting rebuilt/new systems to networks.
• Tightening perimeter security (e.g., firewall rulesets, boundary router access
control lists) and zero trust access rules.
• Testing systems (including security controls) thoroughly.
• Monitoring operations for additional abnormal behaviors.
5.3 Post-incident
The goal of this phase is to document the incident, inform leadership, harden the
environment to prevent similar incidents, and develop then apply lessons learned to
Page 14

improve incident handling in the future. Unless otherwise required by law enforcement or
federal agency policy, incident documentation should be kept for at least three years
(NIST SP 800-61r2).
5.3.1 Adjust sensors, alerts, and log collection
```

#### C4: `mississippi-state-incident-response-plan__00054`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 35100-35900

```text
ral agency policy, incident documentation should be kept for at least three years
(NIST SP 800-61r2).
5.3.1 Adjust sensors, alerts, and log collection
Add/modify/update enterprise-wide detections to mitigate against adversary TTPs that
were successfully used during the incident. Identify and address gaps in security and
notifications (“blind spots”) to ensure adequate coverage in the future. Monitor the
environment for evidence of adversarial persistence.
5.3.2 Finalize reports
Provide post-incident updates as required by law and policy. This activity includes
working with the appropriate law enforcement or agency to provide required artifacts
and/or take additional response actions.
Provide a completed version of the CIRP Response Checklist Template and the Incident
Response Report in App
```

#### C5: `mississippi-state-incident-response-plan__00044`
- doc_id: `mississippi-state-incident-response-plan`
- title: Mississippi State University Cybersecurity Incident Response Plan (CIRP)
- span: 28600-29400

```text
Correlate events and document timeline: acquire, store, and analyze logs
to correlate adversarial activity. Documentation and timeline of relevant
findings are established.
• Identify anomalous activity: assess and profile affected systems and
networks for subtle activity that could be adversary behavior. This process
allows for the finding of deviations from established baseline activity that
could be adversarial behavior.
• Identify root cause and enabling conditions: attempt to identify the root
cause of the incident and collect corresponding threat information that can
be used in further searches and to inform subsequent response efforts.
Identifying the conditions that enabled the adversary to carry out the
incident within the environment, along with assessing networks and
systems for
```

### Manual scoring checklist
- Groundedness (1/0): Are *all key claims* in the answer supported by the evidence above?
- Citation accuracy (1/0): Do the cited chunks contain the specific supporting statements?

---

## q17

**Question:**

> Do the policies mention monitoring of IT resources or user activity? Summarize.

**Answer:**

```text
Yes, the policies mention monitoring of IT resources and user activity. Specifically, Trinity University reserves the right to monitor the network and computers attached to it, and has the authority to examine files and account information to protect the security of its information, network, computing resources, and users [C5]. Additionally, users at Radford University are responsible for all activity that occurs in or through their accounts, indicating a level of accountability and monitoring of user actions [C4].

Citations: [C4], [C5]
```

**Answer↔Evidence keyword overlap ratio (hint):** `0.667`

**Top answer terms:** `monitoring`(2), `resources`(2), `user`(2), `activity`(2), `university`(2), `network`(2), `information`(2), `users`(2), `c5`(2), `c4`(2), `yes`(1), `policies`(1)

### Evidence chunks

#### C1: `trinity-uni-use-policy__00010`
- doc_id: `trinity-uni-use-policy`
- title: Page 1 of 15 Document Name: Acceptable Use Policy
- span: 6500-7300

```text
oped and implemented comprehensive Usage policies for critical
people-facing technologies, which encompass the following categories and supporting activities.
These policy directives and supporting procedures will be fully enforced by Trinity University for
ensuring the usage policies for critical employee-facing technologies are executed in a formal
manner and on a consistent basis for all system components and all other IT resources deemed
critical by Trinity University.
Data, software, network capacity, and computer systems have value and must be treated
accordingly. Use of IT systems that are shared by many users imposes certain additional
obligations. Each member of the University community is personally responsible for their use of
these information and technology resources.
Acceptab
```

#### C2: `colorado-state-uni-use-policy__00001`
- doc_id: `colorado-state-uni-use-policy`
- title: POLICIES	OF	THE	COLORADO	STATE	UNIVERSITY	SYSTEM
- span: 650-1450

```text
ation	systems,	as	well	as	violations	of	other	laws	and	policies	(such	as
those	concerning	conflicts	of	interest,	privacy,	etc.).	The	purpose	of	this	policy	is	to	establish
what	constitutes	acceptable	use	of	these	resources	in	order	to	assure	that	they	are	available
to	everyone	as	needed	for	an	Institution’s	business	needs.
APPLICATION	OF	THIS	POLICY
This policy applies to all students, faculty and staff, affiliates, and all other persons and
organizational	units	having	access	to	technology	and	information	systems	deployed,	offered
by	and/or	contracted	by	an	Institution	(“Users”).
DEFINITIONS	USED	IN	THIS	POLICY
"Resources" include, but are not limited to, Institutional technology devices, servers,
networks,	storage	devices	and	systems	(including	cloud	storage),	data,	applications,	installe
```

#### C3: `ISM-0-Metropolitan-Government-Information-Security-Management-Policy__00020`
- doc_id: `ISM-0-Metropolitan-Government-Information-Security-Management-Policy`
- title: Metropolitan Government of Nashville & Davidson County Page 1 of 8
- span: 13000-13800

```text
ith these
Policies;
• Managing (i.e., documents, tracks, and reports) the security state of department
information systems and the environments in which those systems operate;
• Monitoring compliance of third-party personnel (contractors, vendors, etc.) with applicable
security requirements;
• Ensuring compliance with information security requirements;
• Establishing access requirements;
• Addressing operational interests of department’s end users;
• Auditing on a periodic basis, their department for compliance to all policies, procedures,
standards, etc. and
• Approving new information technology for implementation and use, ensuring those
technologies operate within the appropriately defined security standards.

5.3 Metropolitan Government's Director of Information Technology Services
Met
```

#### C4: `radford-uni-use-policy__00002`
- doc_id: `radford-uni-use-policy`
- title: Policy Title:  Acceptable Use Policy for University
- span: 1300-2100

```text
tions of this policy may be subject
to disciplinary action. Violators may also be subject to prosecution under various relevant
federal, state, or local laws.
B. Specific requirements and responsibilities of users for access to University information
systems are as follows:
1. Users are responsible for all activity that occurs in or through their accounts and/or their
computers or network enabled devices, whether personally or University owned.
2. Users must not share credentials to their individually assigned accounts.
3. If an account has been compromised, users must follow the instructions provided by the
University’s Information Security Office or Technology Assistance Center (TAC). Accounts
may be disabled until the issue is resolved.

Acceptable Use Policy for University Computers an
```

#### C5: `trinity-uni-use-policy__00038`
- doc_id: `trinity-uni-use-policy`
- title: Page 1 of 15 Document Name: Acceptable Use Policy
- span: 24700-25500

```text
s of Policy Violation:
Enforcement
To ensure adherence to the Information and Technology Responsible Use Policy and to protect
the integrity of University resources, Trinity University reserves the right to monitor the network
and computers attached to it. In addition, Trinity University shall have the authority to examine
files and account information, and to test passwords, to protect the security of the University’s
information, network, computing resources and its users.
Any behavior in violation of this policy is cause for disciplinary action. Violations will be
adjudicated, as appropriate, by the CIO, the Office of the Dean of Students, the Office of Housing
and Residential Life, and/or the Office of Human Resources. Sanctions as a result of violations of
this policy may result in, b
```

### Manual scoring checklist
- Groundedness (1/0): Are *all key claims* in the answer supported by the evidence above?
- Citation accuracy (1/0): Do the cited chunks contain the specific supporting statements?

---

## q15

**Question:**

> Are users allowed to install software on institution-owned devices (if addressed)?

**Answer:**

```text
Users are not allowed to install software on institution-owned devices unless it is explicitly for academic instruction or needed to complete assigned job responsibilities. This is stated in the Acceptable Use Policy for the University, which specifies that software not used for these purposes must not be installed by users on University-owned equipment or systems [C1].

Citations: [C1]
```

**Answer↔Evidence keyword overlap ratio (hint):** `0.833`

**Top answer terms:** `users`(2), `software`(2), `owned`(2), `university`(2), `c1`(2), `allowed`(1), `install`(1), `institution`(1), `devices`(1), `unless`(1), `explicitly`(1), `academic`(1)

### Evidence chunks

#### C1: `radford-uni-use-policy__00004`
- doc_id: `radford-uni-use-policy`
- title: Policy Title:  Acceptable Use Policy for University
- span: 2600-3400

```text
ectronic Communications and Social Media.
7. Software not used explicitly for academic instruction, or otherwise needed to complete
assigned job responsibilities, must not be installed by users on University‐owned
equipment or systems.
8. Users must not remove or alter software or hardware on University‐owned equipment or
systems that adversely affects the security, integrity, and/or performance of the
University systems and data.
9. Users must not attempt to interfere with the normal operation, integrity, validity, or the
security of any University information system.
10. Users must not attempt to gain access to other user accounts or passwords through any
means.
11. Users must not use other computers or programs to decode passwords, access restricted
system control information, or monito
```

#### C2: `colorado-state-uni-use-policy__00007`
- doc_id: `colorado-state-uni-use-policy`
- title: POLICIES	OF	THE	COLORADO	STATE	UNIVERSITY	SYSTEM
- span: 4550-5350

```text
ned to me,	including	implementing	such	measures	as	outlined	within	my	Institution’s	IT	Security	Policy	and any related procedures and guidelines, as well as in federal and state	regulations	that	may	apply	(such	as	FERPA	and	HIPAA).	This	also	includes	applying,	in a timely manner, operating system and software patches, and implementing	malware	scanning	that	protects	my	computing	devices	from	unauthorized	access.	f. I	will	only	use	the	Resources	for	their	intended	purposes.	I	will	only	access	Resources	that	have	been	authorized	for	my	use,	or	which	are	publicly	available.	g. I	understand	that	the	Institution	retains	ownership	rights	to	all	its	collective	data.	I	acknowledge	that,	unless	specifically	authorized	by	an	Institutional	official,	copying	Institutional	data	to	a	personal	device,	sto
```

#### C3: `trinity-uni-use-policy__00017`
- doc_id: `trinity-uni-use-policy`
- title: Page 1 of 15 Document Name: Acceptable Use Policy
- span: 11050-11850

```text
wed onto the network.
•All users (system administrative
users) must be responsible for
the proper use of these devices.
•All network system
administrative rights and
subsequent activities are subject
to audit and review as needed.
Technologies Management Approval
Process Usage Policy
Operating
Systems
All system administrative users
and end-users of operating
systems (Windows, UNIX,
LINUX) and other related
operating systems must gain
ITS management approval to
use these systems devices.
•Operating systems may not be
added, removed, or modified
unless explicit consent is given
by appropriate personnel.
•Any operating system obtained
without proof of purchase and
licensing rights will not be
allowed onto the network.
•All users (system administrative
users) must be responsible for
the prope
```

#### C4: `colorado-state-uni-use-policy__00002`
- doc_id: `colorado-state-uni-use-policy`
- title: POLICIES	OF	THE	COLORADO	STATE	UNIVERSITY	SYSTEM
- span: 1300-2100

```text
t limited to, Institutional technology devices, servers,
networks,	storage	devices	and	systems	(including	cloud	storage),	data,	applications,	installed
software,	and	system	credentials.
POLICY	STATEMENT
All	Users	have	the	res ponsibility	to	make	use	of	the	Resources	in	an	efficient,	ethical,	and
legal	manner.	The	Resources	are	to	be	used	in	a	manner	consistent	with	the	instructional,
research,	and	administrative	objectives	of	the Institution	in	general,	and	for	the	purposes
such Resources were provided. Access to the Resources is a privilege and imposes upon
Users	certain	responsibilities	and	obligations,	as	further	described	in	this	policy.
POLICY	PROVISIONS
Access	to	the	Resources	is	granted	subject	to	CSU	System	and	Institutional	policies	and	local,
state,	and	federal	laws.	Acceptable	u
```

#### C5: `NimbusHarbor_IT_Corporation_Security_Policy_Handbook__00004`
- doc_id: `NimbusHarbor_IT_Corporation_Security_Policy_Handbook`
- title: Nimbus Harbor Technologies, Inc.
- span: 2600-3400

```text
ated to all users within 10 business days.
3. Acceptable Use
Allowed use

Company systems may be used for business purposes and limited incidental personal use that does
not interfere with work, violate law, or increase risk.
Prohibited activities (must not)

Disabling or bypassing endpoint security controls (EDR/AV, disk encryption, firewall).

Installing unapproved software that requires administrative privileges.

Using peer-to-peer file sharing or unauthorized remote access tools.

Accessing, storing, or transmitting illegal content or material that violates harassment/discrimination
policies.
Testable controls

Endpoints must run the standard security agent and report healthy status daily.

Admin privilege must be restricted to approved roles and tracked in an access system.

N
```

### Manual scoring checklist
- Groundedness (1/0): Are *all key claims* in the answer supported by the evidence above?
- Citation accuracy (1/0): Do the cited chunks contain the specific supporting statements?

---
