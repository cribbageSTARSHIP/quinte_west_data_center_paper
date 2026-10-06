# Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates ears
**arXiv ID:** 2502.00565v1
**Source File:** arxiv_acoustics_2502.00565v1.pdf

## Page 1

Do neonates hear what we measure? Assessing neonatal ward
soundscapes at the neonates’ ears
Bhan Lama,∗, Ph.D., Peijin Esther Monica Fanb, RN, Yih Yann Tayb, RN, Woei Bing Poonc,
MRCPCH, FAMS, Zhen-Ting Onga, Kenneth Ooia, Ph.D., Woon-Seng Gana, Ph.D. and Shin
Yuh Angb,∗, MBA, RN
aSchool of Electrical and Electronic Engineering, Nanyang Technological University, 50 Nanyang Ave, 639798, Singapore
bNursing Division, Singapore General Hospital, Outram Rd, 169608, Singapore
cDepartment of Neonatal and Developmental Medicine, Singapore General Hospital, Outram Rd, 169608, Singapore
A R T I C L E I N F O
Keywords:
neonatal intensive care
indoor noise
hospital soundscape
binaural
hospital acoustics
building acoustics
A B S T R A C T
Acoustic guidelines for neonatal intensive care units (NICUs) aim to protect vulnerable neonates from
noise-induced physiological harm. However, the lack of recognised international standards for mea-
suring neonatal soundscapes has led to inconsistencies in instrumentation and microphone placement
in existing literature, raising concerns about the relevance and effectiveness of these guidelines. This
study addresses these gaps through long-term acoustic measurements in an operational NICU and
a high-dependency ward. We investigate the influence of microphone positioning, bed placement,
and ward layout on the assessment of NICU soundscapes. Beyond traditional A-weighted decibel
metrics, this study evaluates C-weighted metrics for low-frequency noise, the occurrence of tonal
sounds (e.g., alarms), and transient loud events known to disrupt neonates’ sleep. Using linear mixed-
effects models with aligned ranks transformation ANOVA (LME-ART-ANOVA), our results reveal
significant differences in measured noise levels based on microphone placement, highlighting the
importance of capturing sound as perceived directly at the neonate’s ears. Additionally, bed position
and ward layout significantly impact noise exposure, with a NICU bed position consistently exhibiting
the highest sound levels across all (psycho)acoustic metrics. These findings support the adoption of
binaural measurements along with the integration of additional (psycho)acoustic metrics, such as
tonality and transient event occurrence rates, to reliably characterise the neonatal auditory experience.
1. Introduction
1.1. Background and Motivation
The development of the auditory system begins very
early in gestation. By 26 weeks of gestation, the human fetus
begins to react to auditory stimuli. The auditory system then
continues to develop to be fine-tuned to specific frequen-
cies, to process acoustic stimuli into electric signals sent
to the brainstem, to discern different speech phonemes and
to facilitate learning and memory formation [1]. Following
birth, neonates become increasingly attuned to their acous-
tic surroundings. They can distinguish auditory cues from
background noise and differentiate human speech from non-
biological sounds as early as 28 weeks [2].
While sensory input due to the acoustic environment
has an impact on the structure and function of the neural
systems throughout life, its influence is most pronounced
during infancy [3]. Hence, the auditory environment of a
developing infant is extremely important to its development.
In the uterus, the fetus receives auditory input via bone
conduction and is surrounded by fluid and maternal tis-
sues which attenuates high frequency sounds more so than
low frequency sounds [4]. Preterm exit from the optimal
environment of the womb means that preterm infants are
∗Corresponding authors
blam002@e.ntu.edu.sg (B. Lam); ang.shin.yuh@singhealth.com.sg
(S.Y. Ang)
ORCID(s): 0000-0001-5193-6560 (B. Lam); 0000-0002-6325-154X
(P.E.M. Fan); 0000-0002-1249-4760 (Z.-T. Ong); 0000-0001-5629-6275 (K.
Ooi); 0000-0002-7143-1823 (W.-S. Gan); 0000-0001-9614-7012 (S.Y. Ang)
exposed to hearing via air conduction, as well as sounds
of higher frequencies and higher volumes (especially in the
Neonatal Intensive Care Unit (NICU)). Prolonged exposure
to high-frequency noise, especially in NICUs, can disrupt
physiological and developmental processes. Studies have
shown that such noise may lead to alterations in blood pres-
sure, respiratory rates, and sleep cycles, all of which could
be detrimental to neural growth and auditory development
[4, 5, 6, 7].
In the NICU, loud transient sounds can induce immedi-
ate physiological responses, including elevated heart rates,
altered respiratory patterns, and disrupted sleep cycles [8,
9, 10]. These sudden noises are likely to trigger startle
reflexes and stress-mediated defensive response, which may
interfere with homeostatic regulation and delay neurological
development [9, 11].
The absence of in utero maternal sounds increases the
risk of long-term speech and language deficits in preterm
neonates [1, 12]. Evidence suggests that interventions in-
volving the introduction of spoken or recorded maternal
sounds, can mitigate these effects, promoting improved au-
ditory and visual orientation as well as enhanced cognitive
and language outcomes later in life [13]. Consequently, opti-
mizing the NICU soundscape by minimizing non-biological
noise is essential, as it may enhance the efficacy of maternal
voice interventions [2, 6]. However, a recent systematic
review found that no NICU meets the American Academy
of Pediatrics guidelines of 45 dB(A), indicating a need for
Lam et al.: Preprint submitted to Elsevier
Page 1 of 16
arXiv:2502.00565v1  [eess.AS]  1 Feb 2025

---

## Page 2

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
improved NICU designs to support auditory and develop-
mental health [14].
1.2. Acoustic design guidelines and regulations in
NICUs
In the context of neonatal ward soundscapes, it is cru-
cial to adhere to established and updated guidelines and
regulations to ensure an optimal acoustic environment to
protect the well-being of vulnerable neonates. Among the
various guidelines available, the World Health Organisa-
tion (WHO) followed by American Academy of Pediatrics
(AAP) guidelines are frequently referenced in the literature
[15]. The WHO recommends stringent acoustic standards for
hospital wards, including an A-weighted equivalent sound
pressure level (SPL) indoors of 𝐿AF,24 h ≤30 dB(A) and an
instantaneous maximum SPL level of 𝐿AFmax ≤40 dB(A)
[16], where the subscript {⋅}F refers to the ‘fast’ time re-
sponse (125 ms) according to IEC 61672-1 [17]. Similarly,
the AAP Guidelines suggests maintaining sound pressure
levels (SPL) below a day-night averaged SPL (10 dB(A)
penalty to nighttime levels) of 𝐿dn ≤45 dB(A) [18], based
on the U.S. Environmental Protection Agency guidelines for
hospitals [19].
While acknowledging the widespread referencing of the
WHO (1999) and AAP (1997) guidelines in the literature, it
is important to recognise the possibility that these guidelines
may now be outdated. Consequently, in response to the need
for more intuitive and realistic standards, the Consensus
Committee (CC) on Recommended Design Standards for
Advanced Neonatal Care has consistently revised the “Rec-
ommended Standards for Newborn ICU Design”. The most
recent update, the 10th edition in 2023 [20], reflects these
changes aimed at enhancing the standard’s practicality and
alignment with current research and practices in neonatal
care.
According to the CC, the recommended one-hour SPLs
are 𝐿AS50,1 h ≤50 dB(A) and 𝐿AS10,1 h ≤65 dB(A), as mea-
sured three feet from an infant bed or other relevant listening
position. Here, subscript {⋅}S refers to the ‘slow’ (1 s) time
response, while {⋅}50 and {⋅}10 represent the percentage
exceedance levels as described in ISO 1966-1 [21]. Notably,
the 9th edition update replaced the equivalent SPL guidelines
of 𝐿AS,1 h ≤45 dB(A) to the 50 % exceedance levels of
𝐿AS50,1 h ≤50 dB(A); increased the 𝐿AS10,1 h from 50 dB(A)
to 65 dB(A); and removed the maximum SPL requirement
of 𝐿ASmax ≤65 dB(A). Various portions of the CC NICU
design standards have been adopted in American Institute
of Architects/Facilities Guidelines Institute Guidelines [22],
AAP/American College of Obstetricians and Gynecologists’
(ACOG) Guidelines for Perinatal Care [23], and forms the
basis for noise emission limits in infant incubators in IEC
60601-2-19 [24].
In Singapore, there are no specific guidelines or reg-
ulations governing the acoustic environment in NICUs or
buildings in general. However, under the Environmental
Protection and Management Act of 1999, two statutory reg-
ulations control noise levels emitted from construction sites
and factory premises, with specific limits for noise sensitive
buildings such as hospitals. For construction noise [25], the
maximum permissible levels for hospitals as measured 1 m
from the facade, are as follows: (1) 𝐿AF,12 h ≤60 dB(A)
between 7am to 7pm, (2) 𝐿AF,12 h ≤50 dB(A) between 7pm
to 7am, (3) 𝐿AF,5 min ≤75 dB(A) between 7am to 7pm, and
(4) 𝐿AF,5 min ≤55 dB(A) between 7pm to 7am. Regarding
factory premises, the maximum permissible levels measured
on the boundary facing the hospital are: (1) 𝐿AF,12 h ≤
65 dB(A) between 7 am and 7 pm, (2) 𝐿AF,3 h ≤55 dB(A)
between 7 pm and 11 pm, and (3) 𝐿AF,9 h ≤50 dB(A)
between 11 pm and 7 am [26].
Another point of reference for NICU acoustic design
requirements in Singapore can be found in the BCA Green
Mark 2021 (GM: 2021) green building certification for
healthcare facilities. The acoustic requirements in GM:2021
are derived from guidelines provided by the United Kingdom
(UK) [27] and a joint standard established by Australia and
New Zealand (ANZ) [28]. The Healthcare Technical Mem-
orandum (HTM 08-01) from the UK, sets limits for external
sound sources within multi-bed wards, with recommended
levels of 𝐿AF,1 h ≤40 dB(A) during the day and 𝐿AF,1 h ≤
35 dB(A) at night (11pm to 7am), as well as 𝐿AFmax ≤
45 dB(A). Noise rating (NR) limits were also specified for
mechanical and electrical services within the ward (i.e.
NR ≤30). In contrast to the broader guidelines applicable to
hospital wards in general, the ANZ standard (AS/NZS 2107)
provides specific interior noise limits tailored for NICUs
and pediatric ICUs (PICU). These standards define acoustic
targets such as 𝐿ASmax ≤50 dB(A) for external transient
noise, as well as interior ambient noise levels of 𝐿AS,1 h ≤
45 dB(A) and 𝐿AS10,1 h ≤50 dB(A) for NICU/PICU wards.
The recommended acoustic limits and guidelines discussed
are summarised in Table 1.
Despite notable advancements in noise control technol-
ogy, a growing body of literature highlights the increas-
ing noise levels within hospitals [15, 31, 32, 33]. Within
neonatal intensive care units (NICUs), the role of acoustics
becomes even more critical as it directly impacts the survival
rates and recovery process of vulnerable neonates. Previous
measurements of A-weighted equivalent sound pressure lev-
els (SPL) near the ears of infants in open-box incubators
have revealed values ranging from 54.7 to 60.44 dB(A),
surpassing the recommended guidelines outlined in Table 1.
Furthermore, neonates are frequently exposed to loud
transient sounds, reaching levels between 62–90.6 dB(A), as
indicated by variations in the 𝐿Amax indicators presented in
Table 2. These transient noises can be attributed to various
sources, including medical-staff activities, medical devices,
or alarm peaks [34]. Such high sound levels pose poten-
tial risks to the delicate hearing system of neonates, with
𝐿Amax levels reaching up to 94.8 dB(A) inside incubators
[35], potentially resulting in permanent cochlear damage
[36] or temporary hearing threshold shifts [37]. Moreover,
sudden sounds can trigger startle responses in neonates,
interrupting their rest and recovery [38]. It is worth noting
that the 𝐿AS10,1 h measurements reported by Krueger et al.
Lam et al.: Preprint submitted to Elsevier
Page 2 of 16

---

## Page 3

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
Table 1
Acoustic standards and guidelines for Neonatal Intensive Care
Units (NICU) / Pediatric Intensive Care Units (PICU)
Source1
NICU/
PICU
Ambient Sound
Level
External Sound
Intrusion
WHO
[16]
No
𝐿AF,24 h ≤30 dB(A)
𝐿AFmax ≤40 dB(A)
-
AAP
[18]
Yes
𝐿dn ≤45 dB(A)
-
CC (8th
ed) [29]
Yes
𝐿AS,1 h ≤45 dB(A)
𝐿AS10,1 h ≤50 dB(A)
𝐿ASmax ≤65 dB(A)
-
CC
(9
&
10th
ed)
[30, 20]
Yes
𝐿AS50,1 h ≤50 dB(A)
𝐿AS10,1 h ≤65 dB(A)
-
HTM
08-01
[27]
No
NR ≤30
𝐿AF,1 h ≤40 dB(A)
(7am to 11pm)
𝐿AF,1 h ≤35 dB(A)
(11pm to 7am)
𝐿AFmax ≤45 dB(A)
AS/NZS
2107
[28]
Yes
𝐿AS,1 h ≤45 dB(A)
𝐿AS10,1 h ≤50 dB(A)
𝐿ASmax ≤50 dB(A)
IEC
60601-
2-19
[24]
Yes
𝐿ASmax ≤60 dB(A)
(ambient sound
inside incubator)
𝐿ASmax ≤80 dB(A)
(alarm sounding
inside incubator)
-
1 World Health Organisation (WHO), American Academy of Pediatrics (AAP),
Consensus Committee (CC) on recommended design standards for advanced
neonatal care, HTM (Health Technical Memoranda), Australian/New Zealand
Standard (AS/NZS), International Electrotechnical Commission (IEC)
fall well within the NICU design guidelines of the 9th edition
(𝐿AS10,1 h ≤65 dB(A)) ranging from 59.26–60.6 dB(A).
1.3. NICU soundscape assessment
Unlike established standards for acoustic characterisa-
tion of performance spaces [45] and open-plan offices [46],
as well as airborne [47], impact [48] and facade sound
insulation [49], there is currently a lack of internationally
recognised standards for acoustic measurements in health-
care institutions. This absence of established measurement
guidelines, including accuracy and placement of acoustic
measurement equipment, adds to the ambiguity surrounding
sound level guidelines specific to NICUs [11].
In the literature, NICU sound levels are commonly mea-
sured in the centre of the room [40, 4, 35], which may not
accurately represent the sound levels experienced at the ears
of the neonates, as the sound sources are typically situated
near their head-area [50]. To estimate the sound levels
experienced by neonates more effectively while minimising
disruption to clinical operations, some studies have placed
sound level meters (SLMs) [39, 41, 42], noise dosimeters
[35, 44], or microphones [43, 34, 51] near the neonates’
head area at varying distances. However, due to the dynamic
nature of the critical care environment, the sound field sur-
rounding the measurement instruments may inadvertently
be influenced by reflective surfaces and proximity to noise
sources, such as respirators and CPAP machines. Conse-
quently, the most accurate measurement of neonates’ noise
exposure can be obtained by measuring sound levels very
close to the opening of their ears or within the ear canal itself
on actual patients [36] or on neonate simulators [34, 51].
Regarding measurement accuracy, traceable calibration
to international standards ensures repeatability and relia-
bility of acoustic measurements. This involves adhering to
standards such as IEC 61672-1 classification for SLMs and
noise dosimeters [17], as well as the IEC 61094-1 and
IEC 61094-4 standards for laboratory and working standard
measurement microphones, respectively [52, 53]. Achieving
similar accuracy with SLMs and dosimeters in the measure-
ment of SPLs in a random-incidence field requires the use
of measurement microphone diaphragms that are as small as
possible (≤13 mm) or up to 26 mm with random-incidence
correction [45].
1.4. Research questions
To address the gaps in determining sensible acous-
tic guidelines for NICUs, we investigated the microphone
placements through a long-term measurement campaign
in an operational neonatal unit. Specifically, the following
research questions were addressed:
RQ1 Do different microphone positions influence the mea-
surement of noise levels in neonatal critical care envi-
ronments?
RQ2 What role do bed position and ward layout play in
shaping neonatal noise exposure in critical care units?
RQ3 How suitable are additional (psycho)acoustic met-
rics for assessing the complex sound environment in
neonatal critical care?
2. Method
2.1. Site characteristics and administration
Singapore General Hospital serves as the largest tertiary
hospital in Singapore and houses the Department of Neona-
tal and Development Medicine, offering a comprehensive
spectrum of services for newborns, ranging from standard to
intensive care. Within this department, there is a dedicated
newborn nursery, a neonatal high dependency (HD) unit, and
a neonatal intensive care unit (NICU).
This study specifically focused on the neonatal HD and
NICU units. The HD unit comprises two rooms housing a
total of 18 cots, where neonates classified as level 2 under the
Provincial Council for Maternal and Child Health Standard-
ized Levels of Care infant acuity levels receive specialized
care. Simultaneously, the NICU encompasses 10 incubators
or warmers, tending to neonates categorized as level 3.
The units were equipped with a comprehensive array of
medical resources, including a central monitoring station,
refrigerators (1 for medication and another 2 for breast milk
(fresh and frozen)), computers on wheels, ventilators, warm-
ers, infusion pumps, oxygen-air proportioners, phototherapy
Lam et al.: Preprint submitted to Elsevier
Page 3 of 16

---

## Page 4

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
Table 2
A summary of acoustic measurement studies in neonatal intensive care units (NICU) with reported acoustic indicators and
measurement equipment standards.
Source
Indicator
Value
[dB(A)]
Measurement
Period
Measurement Equipment
Placement
Measurement
Equipment
Krueger
et al. 2007
𝐿AS,1 h
60.44
Before: 8 h/day
for 9 days
Behind bed spaces 2–3 feet above
countertop
SLM (Class 1)
𝐿AS10,1 h
59.26
𝐿ASmax,1 h
78.39
𝐿AS,1 h
56.4
After: 8 h/day
for 2 days
𝐿AS10,1 h
60.6
𝐿ASmax,1 h
90.6
Darcy et al.
2008
𝐿AS,1 s
53.9–60.6
5/h in 2 h
Center of bay
SLM (Class 2)
Lahav 2015
𝐿A,24 h
60.05
5 days
Center of bay
SLM (Class 1)
𝐿A,24 h
58.67
Romeu et al.
2016
𝐿A,1 s
53.4–62.5
56 h
Inside incubator (roof)
SLM (Class 1)
𝐿A,1 s
60.4–65.5
56 h
Outside incubator
Shoemark
et al. 2016
𝐿AS
58
720/h in 24 h
Near head-end of bed
SLM (Class 1)
𝐿ASmax
62
𝐿ASmin
55
Park et al.
2017
𝐿A,10 min
56.7
24 h
Inside incubator
IEC 61094-4 WS2P
𝐿A,10 min
57.1
24 h
Outside incubator
Parra et al.
2017
𝐿A
59.5
3600/h in 24 h
Center of bay
Dosimeter (Class 2)
𝐿A10
61.8
𝐿Amax
85.2
𝐿A
65.8
3600/h in 24 h
Inside incubator, 30 cm from the ears
𝐿A10
68.1
𝐿Amax
94.8
Smith et al.
2018
𝐿AF,1 s
58.1
60/h in 4 h
Open-pod; between two Isolette
Dosimeter (Class 2)
𝐿AF,1 s
54.7
60/h in 4 h
Private room; near ears
This study
𝐿AS,1h
56.09 (3.48)
981 h
Binaural microphone affixed to ears
on neonate doll in a open bassinet
(HD-A)
IEC 61094-4 WS2F
𝐿AS10,1h
58.98 (3.87)
𝐿AS50,1h
51.59 (3.36)
𝐿ASmax,1h
73.76 (4.20)
𝐿AS,1h
59.38 (1.90)
392 h
Binaural microphone affixed to ears
on neonate doll in a open-type
incubator (NICU-A)
𝐿AS10,1h
61.40 (2.70)
𝐿AS50,1h
57.63 (1.38)
𝐿ASmax,1h
73.4 (4.12)
𝐿AS,1h
58.29 (1.81)
98 h
Binaural microphone affixed to ears
on neonate doll in a open-type
incubator (NICU-B)
𝐿AS10,1h
59.89 (2.27)
𝐿AS50,1h
56.80 (1.15)
𝐿ASmax,1h
71.47 (4.81)
lights, ultrasound machine, EEG, cooling machines, and
nitric oxide delivery systems. These resources collectively
facilitate extensive care services for both term and preterm
newborns, with each NICU bed equipped with a bedside
monitoring device.
To prioritize patient care, the least utilized bedspaces
were chosen as measurement locations. In both the NICU
and HD wards, a primary bedspace was designated for
measurements and labeled with the suffix “A,” as depicted
in Figure 1. Secondary bedspaces were labeled sequentially,
e.g., NICU-B. Potential noise sources, such as wash basins,
telephones, nurse stations, storage cabinets, and pneumatic
tubes, were identified and marked in Figure 1. Due to the
critical condition of NICU patients, medical equipment
sounds—such as ventilators and alarms—were more preva-
lent in the NICU compared to the HD wards. It is important
to note that measurements captured only noises external to
the bedspace, i.e. no medical device sounds were simulated.
Maintaining a nurse-to-patient ratio of 1:1.5 for NICU
neonates and 1:4 for HD neonates, the unit sustains a robust
staffing structure with 10 nurses during day and evening
shifts and 7 nurses during the night shift. Additionally, the
space accommodates various healthcare professionals not
Lam et al.: Preprint submitted to Elsevier
Page 4 of 16

---

## Page 5

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
Bed
Cabinet
Storage
NICU
Nurses Station
Reception
Area
NICU
Scale
0 m
1 m
2 m
3 m
4 m
5 m
HD
CORRIDOR
Bed
Bed
Bed
Bed
Bed
Bed
Bed
Bed
Bed
SoundSign
NICU-A
NICU-B
Bed
Bed
Bed
Bed
Bed
Bed
Bed
Bed
Bed
Bed
Bed
HD
Nurses
Station
Pneumatic
Tube
Bed
Bed
Bed
Bed
HD-A
Figure 1: Floor plan depicting the layout of the neonatal intensive care unit (NICU) and high dependency (HD) ward. Measurement
positions within the NICU are highlighted in violet, while the measurement point in the HD ward is marked in green. In both the
NICU and HD wards, a SoundSign device was strategically positioned high on the wall.
Table 3
Bed movement schedule during the measurement period
Ward
Date
Time
Location
Remarks
NICU
2022-03-03
15:15
NICU-A
Designated bedspace
NICU
2022-03-17
11:20
NICU-B
NICU-A →NICU-B
NICU
2022-03-21
12:45
NICU-A
NICU-B →NICU-A
HD
2022-03-03
15:15
HD-A
Designated bedspace
HD
2022-04-03
09:00
HD-B
HD-A →HD-B
HD
2022-04-03
10:00
HD-A
HD-B →HD-A
exclusively stationed in the unit but utilizing the facility to
assess and administer treatments to the infants.
The average patient occupancy rate for both the NICU
and HD wards was approximately 60 %. Notably, there were
no restrictions imposed on the visitation schedule, even
during the COVID-19 pandemic. However, it is important to
highlight that only the parents of the patients were permitted
to visit the wards. Additionally, the feeding regimen fol-
lowed a schedule with intervals of three hours, each session
lasting approximately one hour.
In a previous effort to reduce operational noise in the
NICU, two SPL-activated warning signs named “Sound-
Sign” (Cirrus Research plc, North Yorkshire, UK) was in-
stalled at high visibility areas on the wall in the NICU and
HD wards, as shown in Figure 1. The SoundSign would light
up continously for 30 s upon triggering at 𝐿AS= 65 dB(A),
which corresponds to the 𝐿ASmax limit in the previous edi-
tions of the Recommended Design Standards for Advanced
Neonatal Care. Currently, there is no implementation of
scheduled daily "Quiet Time" or structured programs to
reduce environmental noise in the NICU or HD wards.
2.2. Acoustic measurement: equipment and
procedure
Measurements were carried out over a period of 20
consecutive days in March 2022, using a single incubator
within the NICU ward. Similarly, within the HD ward,
measurements were conducted using a single basinet for 41
consecutive days between March and April 2022.
To simulate how sound is perceived at the ears of
neonates without capturing self-noise, calibrated binaural
microphones (TYPE 4101-B, Hottinger Brüel & Kjær A/S,
Virum, Denmark) were affixed on the ears of two neonate
dolls with surgical tape. One doll was placed in an open-
box incubator (CosyCotTM, Fisher & Paykel Healthcare
Limited, Auckland, New Zealand), and the other was placed
in a bassinet (Huntleigh Healthcare Limited, Wales, United
Kingdom), as shown in Figure 2(a) and (c). The left and right
microphone channels of the binaural microphone would be
referenced as 𝑚L and 𝑚R, respectively. Both the incubator
and bassinet were open-type configurations, representative
of those commonly used in the NICU and HD wards under
investigation.
In addition, both the incubator and bassinet were fit-
ted with a IEC 61672-1 Class 1 compliant sound pres-
sure acquisition system: IEC 61094-4 WS2F microphone
(146AE, GRAS Sound & Vibration A/S, Holte, Denmark)
connected to a data acquisition system (SQoBold, HEAD
acoustics GmbH, Herzogenrath, Germany). To capture the
sound levels around the incubator, two 146AE microphones
were attached to the incubator, one secured to the IV pole
1.6 m from the ground (𝑚out) and the other 30 cm from the
incubator bed, above the raised walls (𝑚in). Due to resource
constraints, only one 146AE microphone was secured to the
bassinet behind the head area 1.6 m from the ground (𝑚out).
Before and after the measurements, each acoustic mea-
surement device was examined to be within ±0.1 dB of
94 dB and 114 dB at both 1 kHz and 250 Hz using a cali-
brator (42AG, GRAS Sound & Vibration A/S, Holte, Den-
mark).
2.3. (Psycho)acoustic metrics
To evaluate the influence of microphone and bed po-
sitions on the acoustics, slow time weighted, A- and C-
weighted sound pressure metrics along with their sum-
mary statistics were computed. Equivalent sound pressure
levels (𝐿AS,1 h, 𝐿CS,1 h), along with summary statistics of
maximum levels (𝐿ASmax,1 h, 𝐿CSmax,1 h), 10 % exceedance
levels (𝐿AS10,1 h, 𝐿CS10,1 h), and 50 % exceedance levels
Lam et al.: Preprint submitted to Elsevier
Page 5 of 16

---

## Page 6

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
(a)
1.6 m
0.3 m
mL
mR
min
mout
(b)
(c)
1.6 m
mL
mR
mout
(d)
Figure 2: (a) Photo and (b) diagram of the in-situ measure-
ment setup of the incubator in the NICU, and (c) a photo and
(d) diagram of bassinet setup in the high-dependency ward.
(𝐿AS50,1 h, 𝐿CS50,1 h) were the primary focus. The inclu-
sion of C-weighted metrics examines the presence of low-
frequency noise, which could be heard by neonates as
low as 250 Hz [54]. The summary statistics, allows for a
nuanced understanding of temporal variations influenced
by specific microphone positions during the measurement
period. Subscript reference to the 1-h averaging is henceforth
dropped for brevity.
The occurrence rate, OR(N) [55, 56], which describes the
percentage of time a threshold level N was exceeded, was
adopted to evaluate the possibility that the neonate would
be awakened by loud sounds. A conservative threshold of
5 dB(A) signal-to-noise ratio (SNR) above the background
noise (SNR < 5) was employed to mitigate the chance of
awakening to less than 30 % [57]. The ORℎ
SNR(5) was com-
puted for each one hour period in a day, ℎ∈{0, 1, ⋯, 23},
where the SNR was determined as [44]
SNR = Lℎ
ASmax,1min −Lℎ
AS50.
(1)
Hence, ORℎ
SNR(5) = 75 indicates that the SNR exceeded
5 dB(A) at least once in 45 out of 60 one minute intervals
in the ℎ-th hour.
Designed to quantify tonal and modulated sounds, the
tonality metric, 𝑇, based on Sottek’s hearing model as de-
scribed in the ECMA-418-2 [58], could indicate the promi-
nence of alarm sounds and potentially speech. Therefore, the
prominence of tonal sounds were determined by the occur-
rence rate where the tonality 𝑇exceeded 0.4 tuHMS [58],
within one minute periods of the ℎ-th hour, i.e. ORℎ
𝑇(0.4).
2.4. Data analysis
The acoustic and psychoacoustic indices were com-
puted with a commercial software package (ArtemiS SUITE,
HEAD acoustics GmbH, Herzogenrath, Germany). Decibel-
based metrics and their associated statistics were computed
in accordance with ISO 1996-1 guidelines [21]. Tonality
was assessed using the hearing-model variant specified in
ECMA-418-2 Ecma International [58].
Due to non-normal residual distributions as indicated
by the Anderson-Darling test, differences in each decibel
metric across all microphones were evaluated separately
for each location using a linear mixed-effects aligned ranks
transformation ANOVA (LME-ART-ANOVA). Microphone
type (𝑚HD
out , 𝑚HD
L , 𝑚HD
R , 𝑚NICU
in
, 𝑚NICU
out
, 𝑚NICU
L
, 𝑚NICU
R
) was
treated as a fixed effect, while the 1-h time intervals served
as a random intercept. Similarly, within- and between-ward
differences for each A- and C-weighted metric were analyzed
with LME-ART-ANOVA, with bed position as the fixed ef-
fect and both the 1-h time intervals and binaural microphone
positions as random effects. Differences in occurrence rates
for SNR and tonality exceedances were also assessed using
LME-ART-ANOVA, with bed position as the fixed effect
and the 1-h time intervals as a random effect.
All data analyses were conducted with the R program-
ming language (R version 4.4.1) [59] on a 64-bit ARM en-
vironment. The analyses were performed with these specific
R packages: KS test and BH correction, with stats (Version
4.4.1, R Core Team [59]), LME-ART-ANOVA with ARTool
(Version 0.11.1, Kay et al. [60]), partial omega squared effect
size with effectsize (Version 0.8.3, Ben-Shachar et al. [61]),
and acoustic data analyses with timetk (Version 2.9.0, Dan-
cho and Vaughan [62]) and seewave (Version 2.2.3, Sueur
et al. [63]).
3. Acoustic variation between microphone
positions
This section analyses the influence of microphone po-
sitions on the assessment of noise exposure in neonatal
critical care, directly addressing the first research question
(RQ1). A detailed examination of disparities in A- and
C-weighted decibel metrics was conducted, following the
prescribed standards in Table 1. The computations, em-
ploying slow time-weighting and aggregation over 1-hour
intervals, spanned a continuous monitoring period of 329.5
hours, ranging from 03/03/2022 at 17:00:00 to 17/03/2023
at 10:30:00 concurrently at both NICU-A and HD-A. Cru-
cially, this time frame remained free from disruptions related
to bed changes or data collection.
Lam et al.: Preprint submitted to Elsevier
Page 6 of 16

---

## Page 7

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
Table 4
Mean and standard deviation of the differences in 1-h slow time-weighted metrics at the HD-A and NICU-A bed positions measured
from 03/03/2022 17:00:00 to 17/03/2022 10:30:00. Difference pairs with significant ART contrasts are indicated in bold.
HD-A
NICU-A
𝑚L −𝑚
𝑚L −𝑚R
𝑚R −𝑚
𝑚in −𝑚out
𝑚L −𝑚in
𝑚L −𝑚out
𝑚L −𝑚R
𝑚R −𝑚in
𝑚R −𝑚out
𝐿AS10
-1.62 (0.97)
-0.17 (0.50)
-1.45 (0.87)
-0.47 (0.46)
2.90 (0.56)
2.44 (0.54)
-0.00 (0.65)
2.91 (0.46)
2.44 (0.61)
𝐿AS50
-1.24 (0.71)
-0.20 (0.24)
-1.04 (0.66)
-0.36 (0.42)
3.29 (0.58)
2.93 (0.57)
0.11 (0.70)
3.17 (0.43)
2.82 (0.56)
𝐿AS
-1.34 (1.18)
-0.07 (0.82)
-1.27 (0.79)
-0.38 (0.40)
3.02 (0.54)
2.64 (0.50)
0.04 (0.55)
2.98 (0.38)
2.60 (0.51)
𝐿ASmax
-1.27 (2.77)
0.04 (2.13)
-1.31 (1.83)
-0.59 (1.20)
3.04 (1.62)
2.44 (1.61)
0.54 (1.47)
2.50 (1.39)
1.90 (1.62)
𝐿CS10
-0.52 (0.44)
-0.92 (0.16)
0.40 (0.54)
-0.33 (0.11)
1.28 (0.35)
0.95 (0.38)
0.41 (0.24)
0.87 (0.46)
0.54 (0.50)
𝐿CS50
-0.16 (0.16)
-1.08 (0.06)
0.92 (0.19)
-0.36 (0.06)
0.94 (0.13)
0.57 (0.14)
0.54 (0.15)
0.40 (0.17)
0.04 (0.19)
𝐿CS
-0.29 (0.64)
-0.96 (0.55)
0.67 (0.36)
-0.35 (0.07)
1.09 (0.19)
0.73 (0.20)
0.48 (0.16)
0.60 (0.25)
0.25 (0.27)
𝐿CSmax
-1.16 (2.94)
-0.28 (1.76)
-0.88 (1.93)
-0.39 (0.79)
2.19 (0.84)
1.81 (0.98)
0.31 (0.71)
1.88 (0.87)
1.50 (1.14)
Differences were evaluated for each metric with the
microphone positions as the repeated measures factor in
the LME-ART-ANOVA and subsequent post-hoc contrast
tests, as summarised in Table A.1 and Table A.2 for HD
and NICU wards, respectively. The differences in metrics
between microphone positions were further examined by
computing the mean differences by
𝜇𝑘,𝑥−𝑦
𝑧
= 1
𝑁
𝑁
∑
𝑛=1
(𝐿𝑧,𝑚𝑘𝑥(𝑛) −𝐿𝑧,𝑚𝑘𝑦(𝑛)),
(2)
where 𝐿𝑧,𝑚𝑘𝑥(𝑛) and 𝐿𝑧,𝑚𝑘𝑦(𝑛) refer to the decibel level indices
at microphone 𝑚𝑘
𝑥and 𝑚𝑘
𝑦, respectively, at the 𝑛th 1-h period.
Here, 𝐿𝑧∈{𝐿AS, 𝐿CS, 𝐿ASmax, 𝐿CSmax, 𝐿AS10, 𝐿CS10, 𝐿AS50,
𝐿CS50}, {𝑥, 𝑦} ∈{L, R, out, in} for 𝑘= NICU, {𝑥, 𝑦} ∈
{L, R, out} for 𝑘= HD, and 𝑁is the total number of 1-h
periods. For reference, 𝜇HD,L−out
AS50
refers to the mean of the
differences in 𝐿AS50 between the left binaural microphone
𝑚HD
L
and the standard microphone 𝑚HD
out in the HD ward.
3.1. HD ward
For measurements at HD-A, LME-ART-ANOVA also
revealed significant differences across all A-weighted deci-
bel metrics at 0.01 % significance level. Except between 𝑚L
and 𝑚R in 𝐿AS and 𝐿ASmax, significant differences were
found between all microphone pairs in the post-hoc contrast
tests.
A reverse trend was observed in HD-A, where the
measurement microphones were louder than the binaural
microphones across all A-weighted metrics between all
but one binaural-measurement microphone pair. Except
between 𝑚R and 𝑚out (𝜇
Δ𝑚R,out
𝐿AS10
=
1.45 dB(A)), mean
differences across all A-weighted metrics in the rest of the
binaural-measurement microphone pairs ranged from −1.62
to −1.04 dB(A), as shown in Table 4. Hence, on average, the
sound level that was exceeded 10 % of the time was louder at
the right ear than the measurement microphone 1.6 m from
the ground above the bassinet in HD-A.
For each C-weighted decibel metric, main effects reached
significance with LME-ART-ANOVA at a 0.01 % signifi-
cance level, indicating a large effect size. Post-hoc contrast
tests further demonstrated significant differences across all
microphone pairs for each C-weighted metric at HD-A, also
at a 0.01 % significance level.
Mean differences between 𝑚L and 𝑚R in C-weighted
metrics were significant but small: 𝜇
Δ𝑚L,R
𝐿CS
= −0.96, 𝜇
Δ𝑚L,R
𝐿CSmax =
−0.29, 𝜇
Δ𝑚L,R
𝐿CS10
= −0.92, and 𝜇
Δ𝑚L,R
𝐿CS50
= −1.08 dB(C).
Additionally, the variability in mean differences between the
binaural microphones and 𝑚out was more pronounced, rang-
ing from 𝜇Δ𝐿CSmax,1 h ∈[1.91, 6.41] dB(C) and 𝜇Δ𝐿CS10,1 h ∈
[0.56, 1.56] dB(C), while remaining comparable in 𝜇Δ𝐿CS,1 h ∈
[0.46, 0.71] dB(C) and 𝜇Δ𝐿CS50,1 h ∈[0.92, 1.09] dB(C).
Between binaural channels, low-frequency sounds were
slightly louder at the right ear (𝑚L) across all C-weight met-
rics: 𝜇
Δ𝑚L,R
𝐿CS
= −0.96, 𝜇
Δ𝑚L,R
𝐿CSmax = −0.29, 𝜇
Δ𝑚L,R
𝐿CS10 = −0.92,
and 𝜇
Δ𝑚L,R
𝐿CS50 = −1.08 dB(C). As compared to the standard
measurement microphone, C-weighted metrics were slightly
higher than the left but slightly lower than the right binaural
channel, with the exception of the mean difference in 𝐿CSmax
levels between 𝑚R and 𝑚out: 𝜇
Δ𝑚R,out
𝐿CSmax = −0.88 dB(C).
3.2. NICU ward
The non-parametric LME-ART-ANOVA revealed sig-
nificant differences across 𝐿AS, 𝐿ASmax, 𝐿AS10 and 𝐿AS50
at 0.01 % significance level. Subsequent pairwise post-hoc
ART contrast tests indicated significant differences among
all microphone pairs, except between the left and right
binaural channels (𝑚L and 𝑚R) in 𝐿AS and 𝐿AS10 at NICU-
A.
Overall, sound levels were higher at the binaural micro-
phones than the standard measurement microphones, indi-
cated by mean differences across all A-weighted metrics.
Mean differences in 𝐿AS among all binaural-standard micro-
phone pairs ranged between 𝜇
Δ𝑚R,out
𝐿AS
= 2.60 and 𝜇
Δ𝑚L,in
𝐿AS
=
3.02 dB(A). For maximum levels, mean difference varied
from 𝜇
Δ𝑚R,out
𝐿ASmax = 1.90 to 𝜇
Δ𝑚L,in
𝐿ASmax = 3.04 dB(A). Likewise,
mean differences in the 10 % and 50 % exceedance levels fell
within the range of 𝜇
Δ𝑚L,out
𝐿AS10
= 2.44 to 𝜇
Δ𝑚R,in
𝐿AS10 = 2.91 dB(A),
and 𝜇
Δ𝑚R,out
𝐿AS50
= 2.82 to 𝜇
Δ𝑚L,in
𝐿AS50 = 3.29 dB(A), respectively.
Sound levels recorded at the standard measurement mi-
crophone outside the incubator (𝑚out) were generally sig-
nificantly louder than the standard microphone inside the
incubator (𝑚in) across all A-weighted metrics, indicating
elevated external sound sources. However, mean differences
Lam et al.: Preprint submitted to Elsevier
Page 7 of 16

---

## Page 8

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
across all A-weighted metrics were notably smaller than
those between binaural and measurement microphones. For
instance, mean differences ranged between 𝜇
Δ𝑚in,out
𝐿AS50
= −0.36
and 𝜇
Δ𝑚in,out
𝐿ASmax = −0.60 dB(A).
Although the 1-h aggregated sound levels of higher
frequencies (A-weighted) were similar across both ears
(𝜇
Δ𝑚L,R
𝐿AS
= 0.039), temporal variation between 𝑚L and 𝑚R is
evident in the significant differences 50 % exceedance levels
𝜇
Δ𝑚L,R
𝐿AS50 = 0.11 dB(A). The significant differences between
𝑚L and 𝑚R in the loudest events (𝜇
Δ𝑚L,R
𝐿ASmax = 0.54) contrasted
with the lack of difference in loud events that occurred for
about 10 % of the time (𝜇
Δ𝑚L,R
𝐿AS10 = −0.00), which indicate the
infrequent transient nature of the loud sounds.
Statistically significant differences emerged across all C-
weighted decibel metrics through LME-ART-ANOVA at a
significance level of 0.01 %, with a large effect size. Sub-
sequent post-hoc contrast tests revealed significant differ-
ences among all microphone pairs for all C-weighted decibel
metrics at the 0.01 % significance level, with exceptions
for comparisons between 𝑚L and 𝑚R, and between 𝑚out
and 𝑚R, both occurring at 𝐿CS50. In these two instances at
𝐿CS50, differences were identified at a significance level of
1 % between 𝑚L and 𝑚R, while no significant differences
manifested between 𝑚out and 𝑚R.
Significant differences between 𝑚L and 𝑚R across all C-
weighted metrics indicate that left ear experienced slightly
higher low-frequency sounds on average at NICU-A: 𝜇
Δ𝑚L,R
𝐿CS
=
0.48, 𝜇
Δ𝑚L,R
𝐿CS10 = 0.41, 𝜇
Δ𝑚L,R
𝐿CS50 = 0.54, and 𝜇
Δ𝑚L,R
𝐿CSmax = 0.31
dB(C). Similarly, low-frequency sound levels were slightly
louder outside (𝑚out) than near to (𝑚in) the infant tray on
average: 𝜇
Δ𝑚in,out
𝐿CS
= −0.35 , 𝜇
Δ𝑚in,out
𝐿CSmax = −0.39, 𝜇
Δ𝑚in,out
𝐿CS10
=
−0.36, and 𝜇
Δ𝑚in,out
𝐿CS50
= −0.33 dB(C).
Differences between the binaural microphones and the
standard measurement microphones for low-frequency sounds
were most pronounced for the loudest sounds, while differ-
ences were small for the rest of the C-weighted metrics.
Mean difference in 𝐿Cmax levels of binaural-standard mi-
crophone pairs ranged from 𝜇
Δ𝑚R,out
𝐿CSmax = 1.50 to 𝜇
Δ𝑚L,in
𝐿CSmax =
2.19 dB(C), whereas other C-weighted metrics ranged from
𝜇
Δ𝑚R,out
𝐿CS
= 0.25 to 𝜇
Δ𝑚L,in
𝐿CS10 = 1.28 dB(C). Peculiarly, sound
levels that were exceeded 50 % of the time were similar
between the right ear and the standard microphone 1.6 m
above the ground: 𝜇
Δ𝑚R,out
𝐿CS50
= 0.04 dB(C).
4. Acoustic variation within-between wards
Building on the findings from Section 3, acoustic dif-
ferences between and within wards were further analysed
using only the binaural channels. The analysis focused on
three bed positions: HD-A, NICU-A, and NICU-B, omitting
HD-B due to the limited duration of data collection, as noted
in Table 3. For each A- and C-weighted metric, LME-ART-
ANOVA was performed with bed position as a fixed effect,
and microphones and time as random effects. Post-hoc con-
trast tests were conducted for results with significance at the
1 % level.
4.1. A- and C-weighted metrics
The LME-ART-ANOVA revealed statistically signifi-
cant differences between bed positions for all A- and C-
weighted metrics at the 1 % significance level. Large effect
sizes were consistently observed across most metrics, except
for 𝐿ASmax and 𝐿CSmax, which exhibited small and medium
effect sizes, respectively, as summarised in Table A.3. In the
post-hoc contrast tests for A-weighted metrics, significant
differences were found across all bed position pairs with
large effect sizes, except for HD-A vs. NICU-B in 𝐿AS10
and HD-A vs. NICU-A in 𝐿ASmax. Similarly, post-hoc tests
for C-weighted metrics indicated significant differences with
large effect sizes for all bed position pairs, except for HD-A
vs. NICU-B in both 𝐿CS and 𝐿CS50.
In general, NICU-A exhibited significantly higher A- and
C-weighted metrics compared to both HD-A and NICU-B,
as shown in Figure 3, Between HD-A and NICU-B, 𝐿AS,
𝐿AS50, and 𝐿CS50 levels were higher at NICU-B, while
𝐿ASmax, 𝐿CS10, and 𝐿CSmax were higher at HD-A.
4.2. Acoustic guidelines
Measurements of 𝐿AS10 and 𝐿AS50 across HD-A, NICU-
A, and NICU-B were evaluated primarily using the 9th and
10th editions of the CC NICU design recommendations, as
outlined in Table 1. For comparison, additional assessments
were conducted based on 𝐿AS and 𝐿ASmax using the 8th
edition guidelines.
At HD-A, compliance with the 𝐿AS10 guideline was
achieved for up to 97 % of the 𝑁= 981 1-hour measurement
periods, while the 𝐿AS50 limits were up to 40 % compliant,
as shown in Table 5. Compliance rates for 𝐿AS10 and 𝐿AS50
varied depending on the microphone type, with binaural
measurements showing up to 8 % higher compliance for
𝐿AS10 and up to 9 % higher compliance for 𝐿AS50.
At NICU-A, compliance with the 𝐿AS10 guideline was
achieved for up to 99 % of the 𝑁= 492 1-hour measurement
periods, while the 𝐿AS50 limits were consistently exceeded.
Notably, microphone type influenced compliance, with bin-
aural measurements resulting in up to 8 % lower compliance
for 𝐿AS10.
At NICU-B, a similar trend to NICU-A was observed re-
garding adherence to 𝐿AS10 and 𝐿AS50 guidelines across the
𝑁= 98 1-hour measurement periods, although compliance
rates remained consistent across different microphone types.
The 𝐿ASmax and 𝐿AS guidelines from the 8th edition
were exceeded almost consistently at across HD-A, NICU-A
and NICU-B, suggesting the presence of very loud events
near neonates (𝐿ASmax ≥65 dB(A)), though these events
were infrequent, occurring less than 10 % of the time.
While 𝐿AS exceedance patterns were consistent with
previous studies irrespective of microphone placement [14],
Lam et al.: Preprint submitted to Elsevier
Page 8 of 16

---

## Page 9

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
LAS
LAS10
LAS50
LASmax
0
6
12
18
24 0
6
12
18
24 0
6
12
18
24 0
6
12
18
24
50
60
70
dB(A)
LCS
LCS10
LCS50
LCSmax
0
6
12
18
24 0
6
12
18
24 0
6
12
18
24 0
6
12
18
24
70
75
80
Hour
dB(C)
Location
HD−A
NICU−A
NICU−B
Figure 3: A- and C-weighted decibel metrics averaged by hour of the day across the entire measurement duration at NICU-A,
NICU-B and HD-A measurement points.
𝐿AS levels recorded near neonates’ ears in this study aligned
closely with those reported in similar NICU environments
[39, 44]. However, 𝐿AS levels measured within enclosed
incubators in prior studies were generally up to 6 dB(A)
higher [41, 35], as summarized in Table 2.
Compared to [39, 35], 𝐿ASmax levels in this study were
up to 23 dB(A) lower, while 𝐿AS10 levels were compara-
ble. The discrepancy in 𝐿ASmax levels may reasonably be
attributed to the absence of bedside medical devices during
our measurements, though the specific cause cannot be
definitively determined.
4.3. Occurrence rates
Significant differences in the frequency of loud events
(ORℎ
SNR(5)) were found across HD-A, NICU-A, and NICU-
B. Post-hoc contrasts revealed that loud events occurred
significantly more frequently at HD-A than at both NICU-
A and NICU-B, as depicted in Figure 4. Although slightly
higher at NICU-A than NICU-B, the difference in ORℎ
SNR(5)
was still statistically significant.
The hourly variation in loud event occurrences remained
relatively stable throughout the measurement period, as indi-
cated by the standard error in Figure 4. At HD-A, the average
occurrence remained consistent throughout the day, whereas
at NICU-A and NICU-B, loud events were more frequent
between 7 a.m. and 9 p.m.
Lam et al.: Preprint submitted to Elsevier
Page 9 of 16

---

## Page 10

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
Table 5
Summary of mean A-weighted metrics and percentage of time where the metrics were within CC guidelines over 𝑁= 981,
𝑁= 392, and 𝑁= 98 1-h periods at HD-A, NICU-A and NICU-B bed positions, respectively.
HD-A
NICU-A
NICU-B
𝑚out
1
𝑚L
1
𝑚R
1
𝑚in
2
𝑚out
2
𝑚L
2
𝑚R
2
𝑚in
3
𝑚out
3
𝑚L
3
𝑚R
3
𝐿AS
57.18
(3.64)
56.05
(3.87)
56.09
(3.48)
56.45
(1.93)
56.78
(2.09)
59.33
(1.90)
59.38
(1.90)
55.05
(1.88)
55.87
(1.78)
57.47
(2.01)
58.29
(1.81)
𝐿AS10
60.25
(4.09)
58.74
(3.85)
58.98
(3.87)
58.54
(2.73)
58.96
(2.86)
61.33
(2.65)
61.40
(2.70)
56.73
(2.54)
57.55
(2.33)
59.15
(2.74)
59.89
(2.27)
𝐿AS50
52.48
(3.71)
51.35
(3.30)
51.59
(3.36)
54.53
(1.43)
54.79
(1.55)
57.61
(1.43)
57.63
(1.38)
53.47
(1.10)
54.60
(1.27)
55.97
(1.44)
56.80
(1.15)
𝐿ASmax
74.85
(4.14)
73.97
(5.28)
73.76
(4.20)
70.96
(4.00)
71.55
(3.99)
73.94
(4.21)
73.40
(4.12)
68.44
(4.85)
68.78
(4.92)
70.71
(5.05)
71.47
(4.81)
𝐿AS10 ≤65 dB(A) (CC 9th/10th ed)
Yes
877
(89%)
953
(97%)
942
(96%)
387
(99%)
386
(98%)
360
(92%)
353
(90%)
98
(100%)
98
(100%)
97 (99%)
97 (99%)
No
104
(11%)
28
(2.9%)
39
(4.0%)
5 (1.3%)
6 (1.5%)
32
(8.2%)
39
(9.9%)
0 (0%)
0 (0%)
1 (1.0%)
1 (1.0%)
𝐿AS50 ≤50 dB(A) (CC 9th/10th ed)
Yes
309
(31%)
389
(40%)
368
(38%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
No
672
(69%)
592
(60%)
613
(62%)
392
(100%)
392
(100%)
392
(100%)
392
(100%)
98
(100%)
98
(100%)
98
(100%)
98
(100%)
𝐿ASmax ≤65 dB(A) (CC 8th ed)
Yes
8 (0.8%)
21
(2.1%)
19
(1.9%)
24
(6.1%)
14
(3.6%)
6 (1.5%)
4 (1.0%)
24 (24%)
22 (22%)
12 (12%)
10 (10%)
No
973
(99%)
960
(98%)
962
(98%)
368
(94%)
378
(96%)
386
(98%)
388
(99%)
74 (76%)
76 (78%)
86 (88%)
88 (90%)
𝐿AS ≤45 dB(A) (CC 8th ed)
Yes
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
0 (0%)
No
981
(100%)
981
(100%)
981
(100%)
392
(100%)
392
(100%)
392
(100%)
392
(100%)
98
(100%)
98
(100%)
98
(100%)
98
(100%)
1 𝑁= 981; 2 𝑁= 392; 3 𝑁= 98; Mean (SD); n (%)
Significant differences were also noted in the occur-
rence of tonal events (ORℎ
T(0.4)) across HD-A, NICU-A, and
NICU-B. Post-hoc tests showed that the ORℎ
T(0.4) values
for NICU-A and NICU-B were statistically similar, but both
were significantly higher than those for HD-A.
At NICU-A and NICU-B, tonal or modulated signals
were present almost continuously (𝑇> 0.4), while at HD-A,
such signals occurred consistently only between 7 a.m. and
9 p.m.
5. Results and Discussion
The following discussion seeks to research questions
established in Section 1.4 in the context of providing in-
sight into the implications for clinical practice and NICU
design guidelines. Section 5.1 examines how microphone
positions influences the measurement of noise levels (RQ1).
Section 5.2 explores the influence of bed positions and ward
layout on neonatal auditory perception of the environment
(RQ2). Section 5.3 reviews the suitability of non-traditional
(psycho)acoustic parameters in assess the neonatal critical
care acoustic environment. Finally, limitations and future
work are presented in Section 5.4
5.1. Do different microphone positions influence
the measurement of noise levels in neonatal
critical care environments?
The results indicate that microphone positioning signifi-
cantly impacts the assessment of noise exposure in neona-
tal critical care environments. In NICU-A, overall sound
levels were consistently higher at the binaural microphones
compared to the standard microphones, whereas in HD-A,
the opposite trend was observed, with standard microphones
capturing higher sound levels than the binaural ones. This
contrast suggests that the spatial location of microphones
relative to the neonate’s ears plays a crucial role in accurately
capturing their auditory experience, especially in reverber-
ant environments and dynamic noise sources.
When comparing the left and right binaural micro-
phones, A-weighted metrics — which capture higher fre-
quency sounds — were generally similar between both ears
in both NICU-A and HD-A. However, a notable difference
emerged during the loudest events (𝐿ASmax) in NICU-A,
where the higher frequency sounds were more pronounced
in one ear, indicating potential directional sound sources,
such as cardiac alarms. On the other hand, C-weighted
metrics, which focus on lower frequency sounds, showed
consistent disparities between the left and right binaural
microphones. These differences were more pronounced
in HD-A than in NICU-A, suggesting that low-frequency
sounds are perceived differently across both ears and are
more variable in open ward environments like HD-A.
Lam et al.: Preprint submitted to Elsevier
Page 10 of 16

---

## Page 11

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
T
L AS
0
6
12
18
24
0
6
12
18
24
0
25
50
75
100
0
25
50
75
100
Hour
% of time over threshold
sub_location
HD−A
NICU−A
NICU−B
Figure 4: Occurrence rate of ORℎ
SNR(5) and ORℎ
𝑇(0.4) averaged
over the same daily 1-h period throughout the entire measure-
ment campaign. A-weighted decibel metrics and tonality met-
rics averaged by hour of the day across the entire measurement
duration at NICU-A, NICU-B and HD-A measurement points.
The distinctions observed in C-weighted metrics can
be attributed to the significant mean differences in low-
frequency sound levels, as highlighted in Table 4. This
finding highlights the importance of placing microphones at
or near ear level within open incubators, particularly in the
NICU, to accurately capture fluctuations in low-frequency
sounds over time. Given that neonates can discriminate
sounds as low as 250 Hz, monitoring C-weighted metrics
is crucial for a comprehensive assessment of their auditory
environment.
The influence of microphone positions is further ev-
ident in the varying compliance rates in the CC guide-
lines. In NICU-A and NICU-B, lower compliance was noted
with binaural microphones, whereas in HD-A, the standard
microphones showed reduced compliance. These findings
highlight the need for future guidelines to adopt standard-
ized protocols and equipment that more accurately reflect
the soundscape experienced by neonates. For instance, ISO
12913-2 [64] mandates the use of artificial head and torso
simulators (HATS) with traceable calibration for soundscape
assessments. However, since HATS that replicate neona-
tal hearing mechanisms are not yet available, standardized
neonatal mannequins equipped with calibrated binaural mi-
crophones, as employed in this study, could provide a suit-
able alternative.
Additionally, it is crucial to acknowledge that the obser-
vations in this study pertain only to external noise sources,
as self-noise, such as sounds from medical equipment, care-
giving activities, or crying infants, was not captured. Here,
“crying infants” refers specifically to the sounds that would
have been recorded if the microphones were affixed to actual
infants rather than neonatal dolls. This distinction ensures
that the findings focus on environmental noise external to
the measurement setup.
5.2. What role do bed position and ward layout
play in shaping neonatal noise exposure in
critical care units?
Measurements revealed that bed position and ward lay-
out considerably influence neonatal noise exposure. The
differences between NICU-A, NICU-B, and HD-A bed po-
sitions were statistically significant across both A- and C-
weighted metrics, with large effect sizes in most cases.
NICU-A consistently had the highest noise levels across
metrics, likely due to its proximity and frequency of noise
sources such as cardiac monitor alarms and personnel ac-
tivities of the reception area in the vicinity. This suggests
that NICU design and bed placement can play a significant
role in either mitigating or exacerbating noise exposure for
neonates.
In contrast, NICU-B exhibited lower noise levels than
NICU-A across most metrics but was still louder than HD-
A in specific instances, such as for 𝐿AS, 𝐿AS50, and 𝐿CS50.
The relative quietness in HD-A may be attributed to its
spatial configuration, which is more isolated from noise
sources, or differences in staff activity levels, or reduced re-
verberance. These findings emphasise the need for strategic
bed placement and ward design to minimise harmful noise
exposure, considering both the location of noise sources and
the acoustic properties of the ward environment.
5.3. How suitable are additional (psycho)acoustic
metrics for assessing the complex sound
environment in neonatal critical care?
While traditional A-weighted metrics remain useful, the
results suggest that incorporating additional (psycho)acoustic
metrics such as tonality and signal-to-noise ratio can offer a
more comprehensive evaluation of the sound environment
in neonatal critical care. The differences observed in the
frequency of loud events and tonal occurrences across bed
positions and wards highlights the variability in how noise
manifests, both temporally and spectrally.
For instance, the NICU wards exhibited continuous tonal
signals (𝑇> 0.4), which were more frequent than in the
HD ward. Such signals, though not necessarily loud, could
contribute to sensory overload for neonates and affect their
development if persistent [65]. Loud event occurrence rates
were higher at HD-A than at both NICU-A and NICU-B,
suggesting that while average sound levels may be lower,
transient loud noises are more frequent, potentially disrupt-
ing sleep and physiological outcomes [57].
These findings indicate that integrating (psycho)acoustic
metrics with standard decibel-based measurements could
lead to a more nuanced understanding of the neonatal sound-
scapes. This is particularly relevant when designing in-
terventions or making decisions on NICU layouts, as it
aligns more closely with the perceptual impact of noise on
neonates, potentially leading to better health outcomes.
Lam et al.: Preprint submitted to Elsevier
Page 11 of 16

---

## Page 12

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
5.4. Limitations and future work
This study provides valuable insights into noise assess-
ment in neonatal critical care units (NICUs), yet several
limitations warrant consideration. Although binaural micro-
phones offer a closer approximation of what neonates might
experience, they do not fully replicate the unique auditory
anatomy of neonates. The absence of standardised HATS
designed specifically for neonates limits the generalisabil-
ity and replicability of these findings, given that existing
HATS are calibrated for adult sound perception. Developing
neonatal-specific HATS or alternative simulation models
could bridge this gap in future research.
Second, owing to operational constrains, the study only
assessed soundscapes in three bed positions across two dif-
ferent wards, which may not fully capture the variability in
noise exposure across diverse neonatal intensive care unit
(NICU) layouts and configurations. Expanding this research
to encompass varied ward layouts and larger number of
measurement points is needed to enhance generalizability of
these findings and would provide a broader understanding
of how ward design, equipment placement, and caregiving
activities influence noise exposure.
Lastly, while this study incorporated (psycho)acoustic
metrics such as tonality and transient event occurrences, it
is important to note that the thresholds used were primarily
derived from adult hearing models (e.g., 𝑇> 0.4 from [58])
or limited empirical evidence (e.g., SNR > 5 dB(A) for
possible waking events in [57]). Future research should focus
on establishing neonatal-specific thresholds and models for
(psycho)acoustic metrics, taking into account their unique
auditory profiles and developmental stages.
6. Conclusion and recommendations
Despite the existence of specific acoustic guidelines for
neonatal intensive care units (NICU), no internationally
recognised standards for acoustic measurements in health-
care settings currently exist. This has inadvertently resulted
in notable disparities in how NICU soundscapes are assessed
across the literature, particularly in terms of instrument type
and placement, resulting in reduced reliability and com-
parability of the results. Through a detailed measurement
campaign in an operational NICU and high dependency
(HD) ward, this work investigated the impact of microphone
type and placement, bed positioning, and ward layout on the
assessment of neonatal soundscapes. To investigate the po-
tential limitations of ubiquitous A-weighted decibel metrics,
neonatal soundscapes were further assessed with other (psy-
cho)acoustic parameters such as C-weighted sound pressure
level, tonality and signal-to-noise ratio.
Assessment of microphone positions across all (psy-
cho)acoustic parameters within each ward revealed signif-
icant differences between standard measurement and bin-
aural microphones, which were affixed to the ears of a
neonate doll. With differences also occurring for loud events
(𝐿ASmax) and low-frequency sounds (C-weighted metrics)
between binaural channels, it further indicates that binaural
microphone placements would provide a more representa-
tive aural experience for neonates. Furthermore, significant
differences between bed positions in NICU and across wards
lend further support to binaural monitoring (with artificial
simulators) for more holistic assessment in dynamic neona-
tal critical care environments. Notably, the need for addi-
tional (psycho)acoustic metric assessment is evidenced in
the high occurrence rates for loud events occurring 5 dB(A)
above the background noise levels and prominent tonal
events that were not captured by A-weighted decibel metrics.
Evidence gathered in this study point towards a pressing
need for further investigation and development of stan-
dardized international acoustic measurement protocols and
instruments that accurately capture the aural experience of
vulnerable neonates This includes employing binaural mea-
surements with standardized neonate dolls and incorporating
additional metrics, such as C-weighted levels and tonality.
These enhancements offer actionable insights for tailoring
acoustic treatments and care protocols, aiming to minimize
loud events, reduce low-frequency noise propagation, and
improve the accessibility and audibility of maternal voice,
which is essential for neonatal development..
Implementation of the proposed measurement tech-
niques and guidelines would require close collaboration
between engineers and clinicians during initial design and
construct of the NICU environment, in order to optimize po-
sitioning of cots and equipment, balancing between acoustic
quality, infection prevention measures and work efficiency.
Collaboration between medical device companies, hospital
engineers and clinicians is also crucial in designing future
devices or modules suitable for the NICU patient population.
In addition is a need for management commitment to
invest in monitoring equipment and regular conduct of such
exercises to allow for continuous improvement in a timely
manner.
Data Availability
The data that support the findings of this study are openly
available in NTU research data repository DR-NTU (Data)
at https://doi.org/10.21979/N9/8GHNGX, and replication
code used in this study is available on GitHub at the follow-
ing repository: https://doi.org/10.5281/zenodo.14643228.
Declaration of competing interest
The authors declare that they have no known competing
financial interests or personal relationships that could have
appeared to influence the work reported in this paper.
Acknowledgments
This work was made possible through a research collab-
oration agreement between Nanyang Technological Univer-
sity and Singapore General Hospital.
Lam et al.: Preprint submitted to Elsevier
Page 12 of 16

---

## Page 13

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
CRediT authorship contribution statement
Bhan Lam: Conceptualization, Methodology, Software,
Validation, Formal analysis, Investigation, Project admin-
istration, Data Curation, Writing - Original Draft, Writ-
ing - Review & Editing, Visualization, Supervision. Pei-
jin Esther Monica Fan: Conceptualization, Methodology,
Resources, Writing - Review & Editing, Project adminis-
tration. Yih Yann Tay: Conceptualization, Investigation,
Resources, Writing - Review & Editing, Project adminis-
tration. Woei Bing Poon: Conceptualization, Investigation,
Resources, Writing - Review & Editing, Project administra-
tion. Zhen-Ting Ong: Resources, Investigation, Data Cu-
ration, Project administration. Kenneth Ooi: Formal anal-
ysis, Resources, Writing - Review & Editing. Woon-Seng
Gan: Resources, Writing - Review & Editing, Supervision,
Supervision. Shin Yuh Ang: Conceptualization, Resources,
Investigation, Writing - Review & Editing, Supervision.
References
[1] E. McMahon, P. Wintermark, A. Lahav, Auditory brain development
in premature infants: the importance of early experience, Annals of
the New York Academy of Sciences 1252 (2012) 17–24. Publisher:
Blackwell Publishing Inc.
[2] P. Kuhn, A. Dufour, C. Zores, The Auditory Sensitivity of Preterm
Infants Toward Their Atypical Auditory Environment in the NICU
and Their Attraction to Human Voices, in: Early Vocal Contact and
Preterm Infant Brain Development, Springer, Cham, 2017, pp. 113–
130. URL: https://link-springer-com.remotexs.ntu.edu.sg/chapter/10.
1007/978-3-319-65077-7_7. doi:10.1007/978-3-319-65077-7_7.
[3] J. C. Dahmen, A. J. King, Learning to hear: plasticity of auditory
cortical processing, Current Opinion in Neurobiology 17 (2007) 456–
464.
[4] A. Lahav,
Questionable sound exposure outside of the womb:
frequency analysis of environmental noise in the neonatal intensive
care unit, Acta Paediatrica 104 (2015) e14–e19. Publisher: Blackwell
Publishing Ltd.
[5] A. Lahav, E. Skoe, An acoustic gap between the NICU and womb: a
potential risk for compromised neuroplasticity of the auditory system
in preterm infants, Frontiers in Neuroscience 8 (2014). Publisher:
Frontiers.
[6] D. E. El-Metwally, A. E. Medina,
The potential effects of NICU
environment and multisensory stimulation in prematurity, Pediatric
Research 88 (2020) 161–162. Publisher: Nature Publishing Group.
[7] C. Retsa, H. Turpin, E. Geiser, F. Ansermet, C. Müller-Nix, M. M.
Murray, Longstanding Auditory Sensory and Semantic Differences
in Preterm Born Children, Brain Topography 37 (2024) 536–551.
[8] E. M. Wachman, A. Lahav, The effects of noise on preterm infants
in the NICU, Archives of Disease in Childhood - Fetal and Neonatal
Edition 96 (2011) F305–F309.
[9] P. Kuhn, C. Zores, T. Pebayle, A. Hoeft, C. Langlet, B. Escande,
D. Astruc, A. Dufour, Infants born very preterm react to variations of
the acoustic environment in their incubator from a minimum signal-
to-noise ratio threshold of 5 to 10 dBA, Pediatric Research 71 (2012)
386–392. Number: 1 Publisher: Nature Publishing Group.
[10] A. Shimizu, H. Matsuo, Sound Environments Surrounding Preterm
Infants Within an Occupied Closed Incubator, Journal of Pediatric
Nursing 31 (2016) e149–e154.
[11] M. K. Philbin,
The Sound Environments and Auditory Percep-
tions of the Fetus and Preterm Newborn, in: M. Filippa, P. Kuhn,
B. Westrup (Eds.), Early Vocal Contact and Preterm Infant Brain
Development: Bridging the Gaps Between Research and Practice,
Springer International Publishing, Cham, 2017, pp. 91–111. doi:10.
1007/978-3-319-65077-7.
[12] A. R. Webb, H. T. Heller, C. B. Benson, A. Lahav,
Mother’s
voice and heartbeat sounds elicit auditory plasticity in the hu-
man brain before full gestation,
Proceedings of the Na-
tional Academy of Sciences 112 (2015) 3152–3157. _eprint:
https://www.pnas.org/doi/pdf/10.1073/pnas.1414924112.
[13] K. Philpott-Robinson, S. J. Lane, L. Korostenski, A. E. Lane, The
impact of the Neonatal Intensive Care Unit on sensory and develop-
mental outcomes in infants born preterm: A scoping review, British
Journal of Occupational Therapy 80 (2017) 459–469. Publisher:
SAGE Publications Ltd STM.
[14] L. Andy, H. Fan, S. Valerie, W. Jing,
Systematic review
of environmental noise in neonatal intensive care units,
Acta
Paediatrica 114 (2025) 35–50. _eprint: https://onlinelibrary-wiley-
com.remotexs.ntu.edu.sg/doi/pdf/10.1111/apa.17445.
[15] E. de Lima Andrade, D. C. da Cunha e Silva, E. A. de Lima, R. A.
de Oliveira, P. H. T. Zannin, A. C. G. Martins, Environmental noise in
hospitals: a systematic review, Environmental Science and Pollution
Research 28 (2021) 19629–19642. Publisher: Springer Science and
Business Media Deutschland GmbH.
[16] B. Berglund, T. Lindvall, D. H. Schwela, World Health Organization.
Occupational and Environmental Health Team, Guidelines for Com-
munity Noise, World Health Organization, London, UK, 1999. URL:
https://apps.who.int/iris/handle/10665/66217, issue: April.
[17] International Electrotechnical Commission, IEC 61672-1: Electroa-
coustics — Sound level meters - Part 1: Specifications, 2013.
[18] Committee on Environmental Health, Noise: A Hazard for the Fetus
and Newborn,
Pediatrics 100 (1997) 724–727. ISBN: 1098-4275
(Electronic).
[19] The U.S. Environmental Protection Agency Office of Noise Abate-
ment and Control, Information on levels of environmental noise
requisite to protect public health and welfare with an adequate margin
of safety, Technical Report, U.S. Government Printing Office Wash-
ington, Washington, D.C., USA, 1974.
[20] L. Altimier, S. A. Barton, J. Bender, J. Browne, D. Harris, C. B.
Jaeger, B. H. Johnson, C. Kenner, K. J. S. Kolberg, A. Loder, G. L.
Martin, S. Mohammed, T. Oelrich, L. Wilson Orr, M. K. Philbin,
M. McCuskey Shepley, J. Shultz, J. A. Smith, T. S. Thompson, R. D.
White, Recommended standards for newborn ICU design, Journal of
Perinatology 43 (2023) 2–16.
[21] International Organization for Standardization, ISO 1996-1 Acoustics
— Description, measurement and assessment of environmental noise
— Part 1: Basic quantities and assessment procedures, International
Organization for Standardization, Geneva, Switzerland, 2016.
[22] Facilities Guidelines Institute, FGI Guidelines for Design and Con-
struction of Hospitals, Dallas, TX, 2022.
[23] AAP Comm. on Fetus and Newborn, ACOG Comm. on Obstetric
Practice, Guidelines for Perinatal Care, American Academy of Pedi-
atrics, 2017. URL: https://publications.aap.org/aapbooks/book/522/
Guidelines-for-Perinatal-Care. doi:10.1542/9781610020886.
[24] International Electrotechnical Commission, IEC 60601-2-19: Medi-
cal electrical equipment — Part 2-19: Particular requirements for the
basic safety and essential performance of infant incubators, Interna-
tional Electrotechnical Commission, Brussels, Belgium, 2020.
[25] Environmental Protection and Management (Control of Noise At
Construction Sites) Regulations, Cap 94A, Rg 2, Rev Eds 77,
2008. URL: https://sso.agc.gov.sg/SL/EPMA1999-RG2?DocDate=
20110825&WholeDoc=1, publisher: Singapore Attorney-General’s
Chambers Place: Singapore.
[26] Environmental Protection and Management (Boundary Noise Limits
for Factory Premises) Regulations, Cap 94A, Rg 1, Rev Ed s 77,
2008. URL: https://sso.agc.gov.sg/SL/EPMA1999-RG1, publisher:
Singapore Attorney-General’s Chambers Place: Singapore.
[27] Department of Health, Health Technical Memorandum 08-01: Acous-
tics, Office of Public Sector Information, Surrey, UK, 2013.
[28] Standards Australia/Standards New Zealand, AS/NZS 2107: Acous-
tics — Recommended design sound levels and reverberation times
for building interiors, Standards Australia/Standards New Zealand,
Sydney, Australia/Wellington, New Zealand, 2016.
Lam et al.: Preprint submitted to Elsevier
Page 13 of 16

---

## Page 14

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
[29] R. D. White, J. A. Smith, M. M. Shepley, Recommended standards
for newborn ICU design, eighth edition, Journal of Perinatology 33
(2013) S2–S16. Publisher: Nature Publishing Group.
[30] R. D. White, Recommended standards for newborn ICU design, 9th
edition, Journal of Perinatology 40 (2020) 2–4. Publisher: Springer
Nature ISBN: 8282138002.
[31] I. Busch-Vishniac, Hospital Soundscapes: Characterization, Impacts,
and Interventions, Acoustics Today 15 (2019) 11.
[32] I. Busch-Vishniac, E. Ryherd, Hospital Soundscapes, in: B. Schulte-
Fortkamp, A. Fiebig, J. Sisneros, A. Popper, R. Fay (Eds.), Sound-
scapes: Humans and Their Acoustic Environment. Springer Hand-
book of Auditory Research, Springer, Cham, 2023, pp. 277–311.
doi:10.1007/978-3-031-22779-0_10.
[33] B. Lam, E. M. P. Fan, K. Ooi, Z.-T. Ong, J. Y. Hong, W.-S. Gan,
S. Y. Ang,
Assessing the perceived indoor acoustic environment
quality across building occupants in a tertiary-care public hospital in
Singapore, Building and Environment 222 (2022) 109403.
[34] M. Bertsch, C. Reuter, I. Czedik-Eysenberg, A. Berger, M. Olischar,
L. Bartha-Doering, V. Giordano,
The “Sound of Silence” in a
Neonatal Intensive Care Unit—Listening to Speech and Music Inside
an Incubator, Frontiers in Psychology 11 (2020) 1–13.
[35] J. Parra, A. de Suremain, F. Berne Audeoud, A. Ego, T. Debillon,
Sound levels in a neonatal intensive care unit significantly exceeded
recommendations, especially inside incubators, Acta Paediatrica 106
(2017) 1909–1914. Publisher: Blackwell Publishing Ltd.
[36] S. S. Surenthiran, Noise levels within the ear and post-nasal space in
neonates in intensive care, Archives of Disease in Childhood - Fetal
and Neonatal Edition 88 (2003) 315F–318.
[37] G. McCullagh, D. Watson, The noise exposure of infants in incuba-
tors, Journal of Sound and Vibration 67 (1979) 231–244.
[38] M. K. Philbin, A. Robertson, J. W. Hall, Recommended Permissible
Noise Criteria for Occupied, Newly Constructed or Renovated Hos-
pital Nurseries, Journal of Perinatology 19 (1999) 559–563.
[39] C. Krueger, S. Schue, L. Parker,
Neonatal Intensive Care Unit
Sound Levels Before and After Structural Reconstruction, MCN: The
American Journal of Maternal/Child Nursing 32 (2007) 358–362.
[40] A. E. Darcy, L. E. Hancock, E. J. Ware, A Descriptive Study of Noise
in the Neonatal Intensive Care Unit Ambient Levels and Perceptions
of Contributing Factors, Advances in Neonatal Care 8 (2008) 165–
175.
[41] J. Romeu, L. Cotrina, J. Perapoch, M. Linés, Assessment of environ-
mental noise and its effect on neonates in a Neonatal Intensive Care
Unit, Applied Acoustics 111 (2016) 161–169. Publisher: Elsevier Ltd.
[42] H. Shoemark, E. Harcourt, S. J. Arnup, R. W. Hunt, Characterising
the ambient sound environment for infants in intensive care wards,
Journal of Paediatrics and Child Health 52 (2016) 436–440.
[43] M. Park, R. Vermeulen, S. Laroche, . M. Gillies,
A preliminary
analysis of the sources of noise in an open-plan neonatal intensive care
unit, in: INTER-NOISE and NOISE-CON Congress and Conference
Proceedings, Institute of Noise Control Engineering, Hong Kong
SAR, China, 2017, pp. 4617–4624.
[44] S. W. Smith, A. J. Ortmann, W. W. Clark,
Noise in the neonatal
intensive care unit: A new approach to examining acoustic events,
Noise and Health 20 (2018) 121–130. Publisher: Wolters Kluwer
Medknow Publications.
[45] International Organization for Standardization, ISO 3382-1:2009
Acoustics — Measurement of room acoustic parameters — Part 1:
Performance spaces, International Organization for Standardization,
2009.
[46] International Organization for Standardization, ISO 3382-3: Acous-
tics — Measurement of room acoustic parameters — Part 3: Open
plan offices, International Organization for Standardization, Geneva,
Switzerland, 2022.
[47] International Organization for Standardization, ISO 16283-1:2017
Acoustics — Field measurement of sound insulation in buildings and
of building elements — Part 1: Airborne sound insulation, Interna-
tional Organization for Standardization, 2017.
[48] International Organization for Standardization, ISO 16283-2: Acous-
tics — Field measurement of sound insulation in buildings and of
building elements — Part 2: Impact sound insulation, International
Organization for Standardization, Geneva, Switzerland, 2020.
[49] International Organization for Standardization, ISO/TS 12913-3:2019
- Acoustics — Soundscape - Part 3: Data analysis, International
Organization for Standardization, Geneva, Switzerland, 2019.
[50] J. L. Darbyshire, M. Müller-Trapet, J. Cheer, F. M. Fazi, J. D. Young,
M. Müller-Trapet, J. Cheer, F. M. Fazi, J. D. Young, Mapping sources
of noise in an intensive care unit, Anaesthesia 74 (2019) 1018–1025.
Publisher: John Wiley & Sons, Ltd.
[51] C. Reuter, L. Bartha-Doering, I. Czedik-Eysenberg, M. Maeder, M. A.
Bertsch, K. Bibl, P. Deindl, A. Berger, V. Giordano,
Living in a
box: Understanding acoustic parameters in the NICU environment,
Frontiers in Pediatrics 11 (2023) 1–10.
[52] International Electrotechnical Commission, IEC 61904-1: Electroa-
coustics — Measurement Microphones — Part 1: Specifications
for Laboratory Standard Microphones, International Electrotechnical
Commission, Brussels, Belgium, 2001.
[53] International Electrotechnical Commission, IEC 61094-4:1996 Mea-
surement microphones — Part 4: Specifications for working standard
microphones, 1996.
[54] N. Novitski, M. Huotilainen, M. Tervaniemi, R. Näätänen, V. Fell-
man,
Neonatal frequency discrimination in 250–4000-Hz range:
Electrophysiological evidence, Clinical Neurophysiology 118 (2007)
412–419.
[55] J. M. Bliefnick, E. E. Ryherd, R. Jackson,
Evaluating hospital
soundscapes to improve patient experience,
The Journal of the
Acoustical Society of America 145 (2019) 1117–1128. Publisher:
Acoustical Society of America.
[56] E. E. Ryherd, K. P. Waye, L. Ljungkvist, Characterizing noise and
perceived work environment in a neurological intensive care unit, The
Journal of the Acoustical Society of America 123 (2008) 747–756.
[57] P. Kuhn, C. Zores, T. Pebayle, A. Hoeft, C. Langlet, B. Escande,
D. Astruc, A. Dufour, Evaluating Further the Auditory Sensitivity
of Infants Born Very Preterm : Physiological, Cerebral and Behav-
ioral Responses to Environmental Sounds in Incubators, Pediatric
Research 70 (2011) 182–182. Publisher: Nature Publishing Group.
[58] Ecma International, ECMA 418-2 — Psychoacoustic metrics for ITT
equipment — Part 2 (models based on human perception), ECMA,
Geneva, Switzerland, 2020.
[59] R Core Team, R: A Language and Environment for Statistical Com-
puting, 2023. URL: https://www.r-project.org/, place: Vienna, Aus-
tria.
[60] M. Kay, L. A. Elkin, J. J. Higgins, J. O. Wobbrock, {ARTool}:
Aligned Rank Transform for Nonparametric Factorial ANOVAs,
2021. URL: https://github.com/mjskay/ARTool. doi:10.5281/zenodo.
594511.
[61] M. Ben-Shachar, D. Lüdecke, D. Makowski, effectsize: Estimation
of Effect Size Indices and Standardized Parameters, Journal of Open
Source Software 5 (2020) 2815.
[62] M. Dancho, D. Vaughan, timetk: A Tool Kit for Working with Time
Series, 2023. URL: https://CRAN.R-project.org/package=timetk.
[63] J. Sueur, T. Aubin, C. Simonis,
Seewave, a Free Modular
Tool
for
Sound
Analysis
and
Synthesis,
Bioacoustics
18
(2008)
213–226.
Publisher:
Taylor
&
Francis
_eprint:
https://doi.org/10.1080/09524622.2008.9753600.
[64] International Organization for Standardization, ISO/TS 12913-2:2018
Acoustics — Soundscape — Part 2: Data collection and reporting re-
quirements, International Organization for Standardization, Geneva,
Switzerland, Switzerland, 2018.
[65] F. Lejeune, J. Parra, F. Berne-Audéoud, L. Marcus, K. Barisnikov,
E. Gentaz, T. Debillon,
Sound Interferes with the Early Tactile
Manual Abilities of Preterm Infants,
Scientific Reports 6 (2016)
23329. Publisher: Nature Publishing Group.
Lam et al.: Preprint submitted to Elsevier
Page 14 of 16

---

## Page 15

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
Appendix A. Statistical test results
Table A.1: Summary of LME-ART-ANOVA and posthoc contrast tests with microphone type as the fixed effect, and 1-h time
periods as the random effect for each acoustic metric at the HD ward.
Metric
Term
Test1
𝑝-value2
𝜔2
P
3
𝐿AS
microphone
LME-ART-ANOVA
****0.0000
(L)0.57
𝑚HD
out – 𝑚HD
L
ART Contrasts
****0.0000
𝑚HD
out – 𝑚HD
R
ART Contrasts
****0.0000
𝑚HD
L – 𝑚HD
R
ART Contrasts
0.1147
𝐿ASmax
microphone
LME-ART-ANOVA
****0.0000
(L)0.25
𝑚HD
out – 𝑚HD
L
ART Contrasts
****0.0000
𝑚HD
out – 𝑚HD
R
ART Contrasts
****0.0000
𝑚HD
L – 𝑚HD
R
ART Contrasts
0.7208
𝐿AS10
microphone
LME-ART-ANOVA
****0.0000
(L)0.67
𝑚HD
out – 𝑚HD
L
ART Contrasts
****0.0000
𝑚HD
out – 𝑚HD
R
ART Contrasts
****0.0000
𝑚HD
L – 𝑚HD
R
ART Contrasts
***0.0002
𝐿AS50
microphone
LME-ART-ANOVA
****0.0000
(L)0.74
𝑚HD
out – 𝑚HD
L
ART Contrasts
****0.0000
𝑚HD
out – 𝑚HD
R
ART Contrasts
****0.0000
𝑚HD
L – 𝑚HD
R
ART Contrasts
****0.0000
1Linear mixed effects Aligned Rank Transform (ART) ANOVA (LME-ART-ANOVA);
2*𝑝< 0.05; **𝑝< 0.01; ***𝑝< 0.001; ****𝑝< 0.0001
3Partial Omega squared (𝜔2
P) for linear mixed effects. (L) large effect 𝜔2
P ≥0.14 ; (M) medium effect 0.06 ≥𝜔2
P < 0.14; (S) small effect 0.01 ≥𝜔2
P < 0.06
Table A.2: Summary of LME-ART-ANOVA and posthoc contrast tests with microphone type as the fixed effect, and 1-h time
periods as the random effect for each acoustic metric at the NICU ward.
Metric
Term
Test1
𝑝-value2
𝜔2
P
3
𝐿AS
microphone
LME-ART-ANOVA
****0.0000
(L)0.91
𝑚NICU
in
– 𝑚NICU
out
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
L
– 𝑚NICU
R
ART Contrasts
0.3087
𝐿ASmax
microphone
LME-ART-ANOVA
****0.0000
(L)0.64
𝑚NICU
in
– 𝑚NICU
out
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
L
– 𝑚NICU
R
ART Contrasts
****0.0000
𝐿AS10
microphone
LME-ART-ANOVA
****0.0000
(L)0.89
𝑚NICU
in
– 𝑚NICU
out
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
L
– 𝑚NICU
R
ART Contrasts
0.8877
𝐿AS50
microphone
LME-ART-ANOVA
****0.0000
(L)0.91
𝑚NICU
in
– 𝑚NICU
out
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
in
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
L
ART Contrasts
****0.0000
𝑚NICU
out
– 𝑚NICU
R
ART Contrasts
****0.0000
𝑚NICU
L
– 𝑚NICU
R
ART Contrasts
**0.0022
Lam et al.: Preprint submitted to Elsevier
Page 15 of 16

---

## Page 16

Do neonates hear what we measure? Assessing neonatal ward soundscapes at the neonates’ ears
Table A.3: Summary of LME-ART-ANOVA and posthoc contrast tests with bed position as the fixed effect, and 1-h time
periods and microphone type as the random effects for each acoustic metric.
Metric
Test
Term
𝑝-value
𝜔2
P
𝐿AS
LME-ART-ANOVA
Bed position
****0.0000
(L)0.47
ART Contrasts
(HD-A) - (NICU-A)
****0.0000
(L)-2.16
ART Contrasts
(HD-A) - (NICU-B)
****0.0000
(L)-0.92
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)1.24
𝐿AS10
LME-ART-ANOVA
Bed position
****0.0000
(L)0.25
ART Contrasts
(HD-A) - (NICU-A)
****0.0000
(L)-1.34
ART Contrasts
(HD-A) - (NICU-B)
1.0000
(S)0.02
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)1.36
𝐿AS50
LME-ART-ANOVA
Bed position
****0.0000
(L)0.81
ART Contrasts
(HD-A) - (NICU-A)
****0.0000
(L)-4.50
ART Contrasts
(HD-A) - (NICU-B)
****0.0000
(L)-3.27
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)1.23
𝐿ASmax
LME-ART-ANOVA
Bed position
****0.0000
(S)0.04
ART Contrasts
(HD-A) - (NICU-A)
1.0000
(S)0.03
ART Contrasts
(HD-A) - (NICU-B)
****0.0000
(L)0.91
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)0.88
𝐿CS
LME-ART-ANOVA
Bed position
****0.0000
(L)0.48
ART Contrasts
(HD-A) - (NICU-A)
****0.0000
(L)-2.27
ART Contrasts
(HD-A) - (NICU-B)
0.5197
(M)0.13
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)2.40
𝐿CS10
LME-ART-ANOVA
Bed position
****0.0000
(L)0.34
ART Contrasts
(HD-A) - (NICU-A)
****0.0000
(L)-1.64
ART Contrasts
(HD-A) - (NICU-B)
****0.0000
(L)0.56
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)2.20
𝐿CS50
LME-ART-ANOVA
Bed position
****0.0000
(L)0.54
ART Contrasts
(HD-A) - (NICU-A)
****0.0000
(L)-2.62
ART Contrasts
(HD-A) - (NICU-B)
*0.0290
(L)-0.23
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)2.40
𝐿CSmax
LME-ART-ANOVA
Bed position
****0.0000
(M)0.06
ART Contrasts
(HD-A) - (NICU-A)
****0.0000
(L)-0.28
ART Contrasts
(HD-A) - (NICU-B)
****0.0000
(L)1.05
ART Contrasts
(NICU-A) - (NICU-B)
****0.0000
(L)1.33
Lam et al.: Preprint submitted to Elsevier
Page 16 of 16