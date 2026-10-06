# Multiresonant Layered Acoustic Metamaterial (MLAM) solution for broadband low-frequency noise attenuation through double-peak sound transmission loss response
**arXiv ID:** 2107.07762v1
**Source File:** arxiv_sec4_acoustic_noise_2107.07762v1.pdf

## Page 1

Multiresonant Layered Acoustic Metamaterial (MLAM) solution for broadband
low-frequency noise attenuation through double-peak sound transmission loss response
D. Rocaa,c, J. Cantea,c, O. Lloberas-Vallsa,d, T. P`amiesb,d, J. Olivera,d,∗
a Centre Internacional de M`etodes Num`erics en Enginyeria (CIMNE)
Campus Nord UPC, Ed. C1, C/ Gran Capit`a s/n, 08034 Barcelona (Spain)
b Laboratori d’Enginyeria Acustica i Mec`anica (LEAM)
Campus Terrassa UPC, C/ Colom 11, 08222 Terrassa (Spain)
c Universitat Polit`ecnica de Catalunya (UPC), Escola Superior d’Enginyeries Industrial Aeroespacial i Audiovisuals de Terrassa (ESEIAAT)
Campus Terrassa UPC, C/ Colom 11, 08222 Terrassa (Spain)
d Universitat Polit`ecnica de Catalunya (UPC), Escola T`ecnica Superior d’Enginyers de Camins, Canals i Ports de Barcelona (ETSECCPB)
Campus Nord UPC, Ed. C1, C/ Jordi Girona 1, 08034 Barcelona (Spain)
Abstract
The problem of noise control and attenuation is of interest in a broad range of applications, especially in the low-frequency range,
below 1000 Hz. Acoustic metamaterials allow us to tackle this problem with solutions that do not necessarily rely on high amounts
of mass, however most of them still present two major challenges: they rely on complex structures making them diﬃcult to manu-
facture, and their attenuating capabilities are limited to narrow frequency bandwidths. Here we propose the Multiresonant Layered
Acoustic Metamaterial (MLAM) concept as a novel kind of acoustic metamaterial based on coupled resonances mechanisms. Their
main advantages hinge on providing enhanced sound attenuation capabilities in terms of a double-peak sound transmission loss
response by means of a layered conﬁguration suitable for large scale manufacturing.
Keywords: Acoustic Metamaterials, Coupled resonances, Layered-based panel, Sound transmission loss, MLAM
1. Motivation
For years, the notion of metamaterials has attracted the in-
terest among the scientiﬁc community for their potential range
of applications. Their attractiveness resides on the ability to ex-
hibit customized behavior, speciﬁcally in the manipulation of
waves, by engineering their internal structure. While the con-
cept was originated in the ﬁeld of electromagnetism, with meta-
materials that showed both negative permittivity and permeabil-
ity [24], the idea rapidly extended to other areas. In regards of
the present work, the focus is on the manipulation of acous-
tic waves, aiming at designing a metamaterial with enhanced
sound attenuation capabilities in the low-frequency region, i.e.
between 100 and 1000 Hz, where most common noise sources
occur (see Fig. 1).
The ﬁrst notions of acoustic metamaterials emerged two
decades ago, when Ping Sheng and co-workers demonstrated
the concept of local resonance with a metamaterial composed
of rubber-coated lead spheres, acting as internal resonators, em-
bedded in an epoxy matrix [14]. Several other works followed,
aiming at exploiting the local resonance phenomena involved
in the production of frequency band gaps for improved acoustic
attenuation in selected frequency regions. Beyond the early de-
signs based on the combination of rubber-coated inclusions in a
polymer matrix [4, 22, 25], examples including membranes as
∗Corresponding author
Email address: oliver@cimne.upc.edu (J. Oliver)
internal resonators [8, 11, 27], as well as periodic arrangements
of pillars on a plate [1–3], have been explored, among oth-
ers. Non-periodic acoustic metamaterial conﬁgurations based
on irregularities and random structures have also been studied
in the past years [5, 21].
The main challenges faced by most of the proposed resonance-
based acoustic metamaterials so far are: (1) the frequency bandgaps
they typically produce are narrowband, and (2) they cannot be
easily manufactured. The former issue is related to the local
resonance phenomenon itself so it mainly aﬀects the low fre-
quency range (for higher frequencies, Bragg scattering eﬀects
typically produce wider bandgaps). In order to produce wider
frequency bandgaps, one needs to increase the internal resonat-
ing mass in the metamaterial, which makes them lose their lightweight
capabilities that makes them competitive against other classical
approaches. Several works found in the literature have tried to
overcome this issue, for instance, by employing multiple res-
onators [26, 29, 30] or combining local resonance with other
damping mechanisms [10, 12, 15, 23]. However, the problem
has not been entirely addressed. Multiple resonators typically
lead to a collection of separated narrowband frequency bandgaps. As
for the enhancements obtained through the introduction of dis-
sipation phenomena, they are somewhat limited to very speciﬁc
damping ranges (which may not be easily obtained, in practice,
with conventional materials).
As for manufacturability, most of the proposed acoustic meta-
materials resort to combine diﬀerent material components, whose
assembly presents a challenge for their practical implementa-
1
arXiv:2107.07762v1  [physics.app-ph]  16 Jul 2021

---

## Page 2

1
100
1k
0
20
40
60
80
100
120
140
160
180
200
220
Frequency (Hz)
Sound Pressure Level (dB)
10
10k
100k
120 dB
100 dB
80 dB
60 dB
40 dB
20 dB
0 dB
Region of 
interest
Figure 1:
Sound pressure level and frequency range for common noise
sources. Each solid black curve is associated to a decibel level at which each
sound source is perceived by human hearing at diﬀerent frequencies. As an ex-
ample, traﬃc noise at 70 dB is perceived around this same level at frequencies
in the range of 200-2000 Hz, but below 100 Hz the perceived intensity rapidly
decreases, becoming practically inaudible below 30 Hz. The shaded area indi-
cates the frequency range of interest, where most common noise sources can be
found, and their perceived intensities are higher.
tion, for instance, in a mass production chain. Furthermore,
ideas based on a single material component, which typically
provide a solution to this problem, rely on additive manufac-
turing technologies due to their topological and geometrical
complexity and characteristics [6, 13, 16]. This kind of tech-
nology, while presenting itself as a potential promising manu-
facturing option in the future, still faces many challenges nowa-
days, especially in terms of processing times and dimensional
tolerances (see Section 4.2 for a further insight on that), which
are of utmost importance in order to produce eﬀective acoustic
metamaterials in a practical manner.
As an attempt to oﬀer a solution to these problems, a
Multiresonant Layered Acoustic Metamaterial (MLAM) is pro-
posed in the present work. Its constant thickness, thin layer-
based conﬁguration allows it to be easily manufactured by presently
available well-known techniques.
These could refer, for in-
stance, to a process involving lamination and die cutting. While
multi-layer panels based on acoustic metamaterials have been
proposed in the past, they typically rely on membrane-type meta-
materials in which diﬀerent material components are combined
in the same layer, which still represents an issue in terms of the
manufacturing process (see, for instance, Refs. [17, 28]). Fur-
thermore, in order to improve its attenuating capabilities in tar-
get frequency ranges, the internal resonances of diﬀerent layers
of the MLAM proposed here are coupled, which translates into
an extended eﬀective attenuation band exhibiting a double-peak
Anechoic 
termination
Loudspeaker
Front tube
Rear tube
Sample 
(panel)
Microphones
1
3
4
2
Figure 2: Experimental setting schematic representation of the two impedance
tubes. The loudspeaker generates acoustic pressure plane waves on the front
tube, with a fraction being reﬂected back by the sample panel and the remain-
ing being transmitted through it to the rear tube. The rear tube contains an
anechoic termination to avoid spurious reﬂections. Four microphones measure
the acoustic pressure at the designated positions, which can be used to obtain
the STL of the sample panel.
sound transmission loss (STL) response. The physical back-
ground behind the coupled resonances mechanism, as well as
its eﬀects in terms of the system’s dispersion characteristics,
is described theoretically in Gao and Wang [7] through simple
spring-mass systems, but without providing an actual practical
implementation. Here, we present a practical realization of the
concept and analyse the consequences in terms of the STL re-
sponse.
In this article, we show a methodology to numerically com-
pute the STL response of metamaterial-based panels under normal-
incidence acoustic waves. This methodology will be used to
characterize the proposed MLAM attenuating capabilities, high-
lighting the beneﬁts of the coupled resonances mechanism when
compared to other conventional conﬁgurations. Finally, the con-
cept will be validated through an impedance tube measurement
of a 3D-printed MLAM early prototype.
2. Materials and methods
2.1. Experimental test
The experimental test considered to evaluate the performance
of the prototype panel consists of an impedance tube measure-
ment of its normal-incidence STL. This method has been used
in previous works with the same purpose, to evaluate the per-
formance of LRAM-based panels [20]. Since a detailed descrip-
tion of the whole methodology can be found in Roca et al. [20],
here we will focus only on the most relevant aspects of it.
The impedance tube setup (depicted in Fig. 2) consists of
two tube parts with the same constant inner section. On one
end of the front tube, a loudspeaker (VISATON FRS 8-4 Ohm,
with a nominal diameter of 8 cm, 30 W, and linear frequency
response from 200 and 20000 Hz) connected to a six channel
ampliﬁer (ECLER MPA 6-80) emits a pink noise (noise source
on the whole audible frequency spectrum with equal amount of
energy for each octave). The last 30 cm on the opposite end of
the rear tube are ﬁlled with a polyurethane foam acting as an
anechoic termination. The sample panel is placed between the
two tubes, pressed against a soft sealing material that prevents
2

---

## Page 3

sound from leaking while not fully restricting the panel’s mo-
tion on the longitudinal direction. This particular setting devi-
ates from the standard method described in ASTM E1050-98,
where the sample typically ﬁlls the inside of the tubes’ sec-
tion. However, it allows more ﬂexibility in the sample’s shape
while still proving to capture local resonance mechanisms on
metamaterial-based panel conﬁgurations [9, 20]. Finally, two
pairs of 0.5 in. prepolarized microphones (electret condenser
model GRAS 40AE) with an integrated circuit piezoelectric
(ICP) preampliﬁer (model GRAS 26CA) are located at diﬀer-
ent tube positions. They measure the acoustic pressure at these
points, from which the STL can be computed. The tubes’ sec-
tion size of 8 cm × 8 cm and the separation distance between
each pair of microphones of 7.6 cm guarantee an applicability
range between 200 and 2000 Hz for normal-incidence acoustic
plane waves.
The procedure to compute the STL starts with the measured
pressure values at the four microphone positions, which can be
written in the frequency domain as
P1(ω) = A(ω)eiκx1 + B(ω)e−iκx1, x1 = −17.6 cm;
(1)
P2(ω) = A(ω)eiκx2 + B(ω)e−iκx2, x2 = −10 cm;
(2)
P3(ω) = C(ω)eiκx3 + D(ω)e−iκx3, x3 = d + 10 cm;
(3)
P4(ω) = C(ω)eiκx4 + D(ω)e−iκx4, x4 = d + 17.6 cm,
(4)
where A and B are the complex pressure amplitudes of the inci-
dence and reﬂected waves on the front tube, respectively, C and
D are the complex pressure amplitudes of the transmitted and
reﬂected waves on the rear tube, respectively, d is the panel’s
thickness, and κ is the wavenumber, deﬁned as
κ = ω
c ,
(5)
with ω being the frequency and c the speed of sound in air. Each
xk in the Eqs. (1)-(4) refers to the relative position of the k-th
microphone with respect to the panel’s incidence surface.
The anechoic termination condition allows us to neglect the
eﬀect of the reﬂected wave on the rear tube (i.e., D = 0), thus
the transmission coeﬃcient T of the sample panel can be ob-
tained simply as
T(ω) = C(ω)
A(ω),
(6)
where A and C are computed according to:
A(ω) = i
¯P1e−iκx2 −¯P2e−iκx1
2 sin κ(x2 −x1) ,
(7)
C(ω) = i
¯P3e−iκx3 −¯P4e−iκx3
2 sin κ(x4 −x3) .
(8)
with ¯Pk being the calibrated complex Fourier transformed pres-
sure measured for the k-th microphone. The calibration process
to correct the amplitude and phase of the pressure amplitudes
follows the standard ASTM E1050-98 and is described also in
Roca et al. [20].
PML
Acoustic 
domain 2
PML
Acoustic 
domain 1
Solid domain 
(unit cell)
z
x
y
Transmission 
surface Γt
Incidence 
surface Γi
Figure 3: Schematic representation of the problem setting for numerically com-
puting the STL of a panel with a periodically repeating unit cell. Two perfectly
matched layers (PML) are considered at the ends of the acoustic domains to
simulate an inﬁnite extension of the domain in all directions. The STL is ob-
tained by computing the average amplitude of the incidence and transmitted
pressure ﬁelds on the designated surfaces Γi and Γt, respectively.
The STL can ﬁnally be obtained by inserting Eqs. (7) and (8)
into Eq. (6) and using the formula:
STL(ω) = −10 log10 |T|2.
(9)
2.2. Numerical simulations
The objective of the numerical simulations here is to com-
pute the STL of an acoustic metamaterial panel characterized
by a unit cell that inﬁnitely repeats in the transverse directions. To
properly account for this STL parameter, the acoustic domains
(ﬁlled with air, where acoustic pressure plane waves propagate),
must be also inﬁnite on each side of the solid panel. To per-
form such analysis, the schematic representation in Fig. 3 is
considered. The domain is split into an acoustic domain (the
air), where the pressure ﬁeld is the primary unknown, and a
solid domain (the metamaterial panel), where the displacement
ﬁeld is the primary unknown.
(a) Acoustic domain:
In the acoustic domain, the pressure ﬁeld is solved in terms
of the frequency, ω, from the Helmholtz equation
∇2pt + κ2pt = 0,
(10)
where κ is the wavenumber, as previously deﬁned in Eq. (5),
and
pt = ps + pb
(11)
is the total pressure ﬁeld, deﬁned as the sum of the scattered
pressure ﬁeld, ps (the actual unknown), and the background
pressure ﬁeld, pb.
To simulate a normal-incidence acoustic plane wave, the
background pressure ﬁeld in the acoustic domain 1 (the inci-
dence side) is imposed to
pb = p0e−iκx,
∀x < 0
(12)
where p0 = 0.02 Pa (this value corresponds to a sound pressure
3

---

## Page 4

A
B
B
A
C1
C2
D
a
a
w
h1
(b)
(c)
(d)
h2
w
a
a
a
a
w
b
Layer C2
Layer C1
Layers B/D
z
y
x
y
z
(a)
tA
tB
tC
tD
tC
tB
tA
Figure 4: (a) Representation of the MLAM layered structure with an example of its diﬀerent types of layers. (b) Detailed geometrical parameters and structure of
the U-shaped unit cell in the ﬁrst resonating layer (C1). (c) Detailed geometrical parameters and structure of the U-shaped unit cell in the second resonating layer
(C2). (d) Detailed geometrical parameters and structure of the unit cell in the the separating and connecting layers (B and D).
4

---

## Page 5

level of 60 dB, but is taken simply as a reference, since it does
not aﬀect the resulting STL). In the acoustic domain 2 (trans-
mission side), pb = 0.
At both ends of the acoustic domain (in the x-direction),
perfectly matched layers (PMLs) are imposed to avoid wave re-
ﬂections, hence simulating the medium’s inﬁnite extension.
(b) Solid domain:
In the solid domain, the displacement ﬁeld, u, is solved
from the momentum balance equation in the frequency domain,
∇· σ + ρω2u = 0,
(13)
where ρ is the material’s density ﬁeld and σ is the stress tensor
ﬁeld. In this context, small displacements and strains can be
assumed, so a linear elastic material model is considered. In
particular,
σ = C : ∇Su,
(14)
where ∇S denotes the symmetric gradient operator and C is the
fourth-order constitutive tensor, which can be expressed, using
Voigt’s notation, in terms of the material’s Young’s modulus, E,
and Poisson’s ratio, ν, as
CVoigt =

λ + 2µ
λ
λ
0
0
0
λ
λ + 2µ
λ
0
0
0
λ
λ
λ + 2µ
0
0
0
0
0
0
µ
0
0
0
0
0
0
µ
0
0
0
0
0
0
µ

,
(15)
with λ =
νE(1 + iη)
(1 + ν)(1 −2ν), µ = E(1 + iη)
2(1 + ν) ,
where η is used here as an isotropic loss factor to account for
damping in the system (notice that i refers to the imaginary
number, so the tensor C becomes complex valued for η , 0). It
should be remarked that damping does not play a major role
into the expected material behaviour (it is introduced simply
to characterize a more realistic response), so this simple model
provides just a measure of each material’s dissipation capacity,
regardless of the speciﬁc sources (it takes into account, for in-
stance, visco-elastic or thermo-viscous eﬀects).
(c) Acoustic-structure interface:
On the boundaries between the solid and acoustic domains,
the eﬀect of the pressure ﬁeld on the solid domain is accounted
for as an external traction force
σ · n = −ptn,
(16)
where n is the outward unit vector of the solid’s boundary sur-
face. Additionally, compatibility of the normal component of
the displacements is considered through
n · ∇pt = ω2ρau · n,
(17)
where ρa is the air’s density.
(d) Periodic boundary conditions:
Given the periodic conﬁguration of the acoustic metama-
terial structure, the analysis is focused on a single unit cell
while still accounting for the inﬁnite transverse extension of
the panel. In general, this is achieved through imposing Floquet
boundary conditions in the y and z-directions, both on the solid
and the acoustic domains:
pt(x(+)) = pt(x(−))eiκ·(x(+)−x(−))
(18)
u(x(+)) = u(x(−))eiκ·(x(+)−x(−))
(19)
where x(−) and x(+) refer to the source and corresponding desti-
nation points, respectively, of the periodic boundaries.
For this particular case, in which we consider waves prop-
agating in the x-direction (normal-incidence, i.e. κy = κz = 0),
conditions expressed by Eqs. (18) and (19) turn into standard
periodic boundary conditions.
(e) STL computation:
Equations (10) and (13) are solved considering a FEM dis-
cretization using the standard coupled acoustic-solid model in
COMSOL. Once the pressure and displacement ﬁelds are ob-
tained, for a given frequency, the corresponding STL is com-
puted as in Eq. (9), with the transmission coeﬃcient, T, ob-
tained through
T =
R
Γt ptdΓ
R
Γi pbdΓ
,
(20)
where Γi and Γt denote the incidence and transmission surfaces,
respectively, as depicted in Fig. 3.
3. Proposed design
The MLAM design concept is based on a stack of constant
thickness layers of homogeneous materials. Each of these lay-
ers is characterized by its speciﬁc material properties, thick-
ness and unit cell’s design/topology (see Fig. 4(a)). In order to
operate properly (i.e., exhibit the coupled resonances and the
double-peak eﬀects), diﬀerent layers with particular purposes
are required:
a) Resonating layers (e.g. layers Ci in Fig. 4(a)). They rep-
resent the core layers of the MLAM structure, as they
contain the resonating elements responsible for trigger-
ing local resonance eﬀects, causing the STL attenuation
peaks. In this kind of layers, the unit cell’s topology and
dimensions play an important role in determining the lo-
cation of these peaks on the frequency spectrum. The
5

---

## Page 6

Material
Density
ρ (kg/m3)
Young’s modulus
E (MPa)
Poisson’s
ratio ν
Loss
factor η
Layers
Polyamide (PA)
1050
1650
0.4
0.005
A, B
Steel
7800
200000
0.3
0
C1, C2
Silicone rubber
1050
0.15
0.47
0.02
D
Parameter
MLAM
UMLAM
SLAM
HP
HP+
tA (mm)
1 / 1
1 / 1
2.9 / 2.9
9.5
38
tB (mm)
0.5 / 0.5
0.5 / 4 / 0.5
1 / 1
-
-
tC1 (mm)
0.75
0.75
0.75
-
-
tC2 (mm)
0.75
0.75
-
-
-
tD (mm)
4
-
-
-
-
a (mm)
40
40
40
-
-
b (mm)
1
1
1
-
-
w (mm)
4
4
4
-
-
h1 (mm)
8
8
6
-
-
h2 (mm)
4
4
-
-
-
Total thickness (mm)
8.5
8.5
8.55
9.5
38
Surface density (kg/m2)
9.96
9.96
9.95
9.98
39.9
Table 1: Material properties and geometrical parameters considered for obtaining the STL curves in Fig. 5. Each material is assigned to the corresponding layer
types (as deﬁned in Fig. 4) indicated in the layers column. The deﬁnition of all the geometric parameters can also be found in Fig. 4. The last two rows in the table
provide detailed information regarding each panel conﬁguration’s total thickness and surface density, respectively.
simple “U-shaped” design considered for the proposed
prototype (see Fig. 4(b)-(c)) is enough to guarantee a
good STL response in the frequency range below 1 kHz. In
this case, the overall performance of the STL is improved
when choosing denser materials for the resonating layers,
since it allows them to be more compact and thin.
b) Connecting layers (e.g. layer D in Fig. 4(a)). As the name
suggests, the purpose of these layers is to connect pairs
of resonating layers, and so they must be stacked be-
tween them as depicted in Fig. 4(a). Their presence in
the MLAM structure is key to enable the coupling res-
onances eﬀects. In this case, their associated unit cells’
pattern must be compatible with that of the resonating
layers’, making sure the corresponding unit cells’ bound-
aries match (see Fig. 4(c)). The speciﬁc dimensions and
material choice for this kind of layers is also important to
guarantee a good coupling eﬀect. This can be adjusted
through the eﬀective stiﬀness of the layer. If the con-
necting layer is too stiﬀ, the resonating layers become
eﬀectively uncoupled and the corresponding STL atten-
uation peaks wouldn’t be connected (see Fig. 5). Thus,
softer (rubber-like) materials would be preferred in this
case to guarantee the coupling with a more compact and
thin conﬁguration.
c) Separating layers (e.g. layers B in Fig. 4(a)). These lay-
ers are adjacent to resonating layers since their whole
purpose is to enable the vibration of their resonating ele-
ments. For this reason, their unit cells’ pattern must again
be compatible with that of the resonating layers. To cause
minimal interference with the overall performance of the
MLAM structure, these layers should be ideally thin and
stiﬀenough to isolate each unit cell’s vibration from the
others (otherwise, it can cause undesired eﬀects on their
associated local resonances due to triggering unit cell’s
deformation modes in the frequency range of interest).
d) Skin layers (e.g. layers A in Fig. 4(a)). These layers are
homogeneous solid covers (with no associated unit cell
pattern), present for supporting the whole stack, and also
for protection purposes. Since they do not play a major
role in the MLAM performance, they should have enough
stiﬀness to avoid interference with the STL response. For
some applications in which the MLAM panel is attached
to some structure (e.g. a wall), the corresponding skin
layer could be removed (hence attaching the separating
layer directly onto the structure) while still exhibiting the
relevant eﬀects on the STL response.
4. Results
4.1. Double-peak STL response
In Fig. 5, we show the STL response of three diﬀerent layered-
based acoustic metamaterial conﬁgurations: (a) one with a sin-
gle resonating layer (SLAM), (b) another with two uncoupled
resonating layers (UMLAM), and (c) the MLAM concept (i.e.,
with two coupled resonating layers). For each case, Fig. 5 shows
the equivalent spring-mass systems: (a) a mass-in-mass con-
ﬁguration describing a conventional acoustic metamaterial, (b)
two diﬀerent inner masses inside the same outer mass (i.e., an
acoustic metamaterial with two internal resonators), and (c) two
diﬀerent mass-in-mass units contained in the same supercell
structure (i.e., two coupled acoustic metamaterial units). The
general idea behind the MLAM realization of its equivalent
spring-mass system (c) is that the cells represent the correspond-
ing resonating layers (C1 and C2), the masses at each end are
6

---

## Page 7

0
200
400
600
800
1000
Frequency (Hz)
0
20
40
60
80
STL (dB)
Homogeneous panel, HP (10 kg/m2)
Homogeneous panel, HP+ (40 kg/m2)
A
D
C1
C2
A
B
B
A
B
C1
C2
A
B
B
A
C1
A
B
B
(a) Single resonator acoustic metamaterial (SLAM)
(b) Uncoupled two-resonator acoustic metamaterial (UMLAM)
(c) Coupled two-resonator acoustic metamaterial (MLAM)
≡
≡
≡
0
20
40
60
80
STL (dB)
0
200
400
600
800
1000
Frequency (Hz)
0
20
40
60
80
STL (dB)
0
200
400
600
800
1000
Frequency (Hz)
SLAM (10 kg/m2)
𝛼
𝛽
𝛾
𝛼
𝛽
𝛾
0.25M
0.25M
m1
m2
m1
m2
0.125M
Kc = 0.2K
0.125M
m0
m1 + m2
2
m0 =
k0
K
K
K
K
Kc
0.2M
0.2M
0.2M
0.2M
m1 = 0.15M
m2 = 0.2M
K
K
0.2M + m0
2
k1
(b)
k2
(b)
k1
(c)
k2
(c)
0.2M + m0
2
SLAM (spring-mass model)
UMLAM (10 kg/m2)
UMLAM (spring-mass model)
MLAM (10 kg/m2)
MLAM (spring-mass model)
Figure 5: On the left, the three diﬀerent layered-based acoustic metamaterial conﬁgurations are depicted, with their respective layer types composition, along with
an equivalent spring-mass system representation. On the right, the corresponding STL curves for each case are shown and compared to the results for homogeneous
panels of the same surface density (10 kg/m2) and four times that (40 kg/m2). The shaded areas in the plots correspond to frequency regions in which the metamaterial
conﬁgurations exhibit levels of attenuation higher than those obtained with comparable homogeneous panels with four times more mass. For reference, the thin
continuous lines on the right plots represent the STL curves for each equivalent spring-mass system.
7

---

## Page 8

Materials (3D-printing)
Density
ρ (kg/m3)
Young’s modulus
E (MPa)
Poisson’s
ratio ν
Layers
Polyamide (PA)
1010
1800
0.4
A, B
Steel
7860
147000
0.3
C1, C2
Rubber-like
1200
85
0.48
D
tA (mm)
tB (mm)
tC1 (mm)
tC2 (mm)
tD (mm)
a (mm)
b (mm)
w (mm)
h1 (mm)
h2 (mm)
2 / 2
1 / 1
2
2
15
40
1
10
3
8
Table 2: Material properties and geometrical parameters for the MLAM prototype used in the experiments and the corresponding numerical simulations. Each
material is assigned to the corresponding layer types (as deﬁned in Fig. 4) indicated in the layers column. The deﬁnition of all the geometric parameters can also be
found in Fig. 4. The material properties are obtained from the datasheets of the manufacturer.
assumed as the skin layers (A), and the roles of springs K and
Kc are taken by the separating layers (B) and connecting layer
(D), respectively. Analogous considerations can be assumed for
the spring-mass systems (a) and (b) with the SLAM and UM-
LAM conﬁgurations, respectively.
The material properties and geometric characteristics of each
panel conﬁguration are detailed in Tab. 1. For comparative pur-
poses, all three acoustic metamaterial panels have almost the
same total thickness and mass. Notice that the only diﬀerence
between the UMLAM and the MLAM is the material choice
for the layer between the two resonating layers. For the uncou-
pled conﬁguration (UMLAM), the same polymer-like material
of the separating layers (type B layers) is considered, while a
softer rubber-like material (with the same density) is chosen for
the MLAM case, making it a truly connecting layer (type D
layer), and hence exhibiting the coupled resonances eﬀect and
the double-peak STL response. In the SLAM conﬁguration, the
skin and separating layers’ thicknesses have been increased to
match the global mass and thickness of the other two conﬁg-
urations. To properly analyse the STL response, the obtained
curves for each case in Fig. 5 are compared with the corre-
sponding results for reference homogeneous panel (HP) conﬁg-
urations of the same surface density (of 10 kg/m2) and 4 times
that (40 kg/m2, named HP+). As an example, these could refer
to steel panels of 1.28 mm and 5.12 mm thick, respectively, or
polyamide (PA) panels of 9.5 mm and 38 mm thick (consider-
ing the densities provided in Tab. 1).
Additionally, to support the physical insight provided by
the equivalent spring-mass systems, the STL plots in Fig. 5
also show their corresponding STL curves. To obtain these re-
sults, the conditions of incident, reﬂected and transmitted plane
waves have been imposed in terms of non-dimensional displace-
ments and forces acting on the end masses:
ˆuL = (1 −R)eiωt,
ˆuR = Teiωt;
(21)
ˆfL = i ˆωγ(1 + R)eiωt,
ˆfR = −i ˆωγTeiωt.
(22)
Here, the subscripts “L” and “R” refer to the “left” and “right”
end masses, respectively. Variables R and T are the reﬂection
and transmission coeﬃcients, ˆω = ω/Ω0 (with Ω2
0 = K/M),
and γ = ˙mair/MΩ0 (with ˙mair ∼ρaircair being a reference air
mass ﬂow rate). While no straightforward (direct) association
between the springs and masses can be made with the corre-
sponding 3D realization parameters, both systems can be made
equivalent (in terms of their STL response) with an appropri-
ate choice of the variables γ = 0.008 and Ω0 = 600 Hz, along
with the total mass M distribution detailed in Fig. 5 (this selec-
tion of parameters comes from attempting to ﬁt the spring-mass
model results to those for its corresponding 3D implementa-
tion). In this case, the values considered for k0, k(b)
i
and k(c)
i
(i = 1, 2), deﬁned in Fig. 5, come from matching the frequen-
cies of their corresponding resonance STL peaks. Notice that,
for the MLAM case, a lower stiﬀness for the connecting spring,
Kc = 0.2K, has been required to achieve the resonance coupling
eﬀect.
As expected, the more conventional acoustic metamaterial
conﬁguration, i.e. consisting of a single resonator/unit cell de-
sign, produces an STL response characterized by an attenua-
tion peak followed by a transmission dip on frequencies that,
for plane waves at normal incidence, coincide with the asso-
ciated bandgap limits [18, 19] (see Fig. 5(a)). The idea of ex-
ploiting the local resonance eﬀects of diﬀerent resonators can
be conceived as a way to obtain higher levels of attenuation
in an extended frequency range. However, the use of multiple
resonators is not enough to guarantee a broader range of atten-
uation in the panel’s STL response. To properly exploit them,
the resonators also need to be coupled, otherwise they will pro-
duce several narrowband attenuation peaks isolated from one
another (i.e., with transmission dips in-between). Through the
resonators’ coupling, their locally resonant bandgaps are joined
into a continuous larger gap (translating into the double-peak
STL response). This can be appreciated comparing the STL re-
sponses in Figs. 5(b) and 5(c).
Notice that through the resonating layers’ coupling, one ef-
fectively makes the transmission dip that typically appears after
the STL peaks produced by local resonances (see γ in Fig. 5(b)
appearing between peaks α and β), to occur before the ﬁrst at-
tenuation peak (see now γ appearing before peaks α and β in
Fig. 5(c)), creating an extended single, continuous attenuation
band between the two attenuation peaks. When comparing the
results with those of a homogeneous panel 4 times heavier, the
MLAM conﬁguration clearly shows how we can get the same
eﬀective attenuation levels in the whole range between 400 Hz
and 500 Hz. In both other cases, the comparative STL levels
are only achieved in very narrow, isolated frequency bands (of
less than 30 Hz). It is also worth noting that this enhanced STL
response occurs at lower frequencies for the MLAM conﬁgu-
ration compared to the equivalent single resonator and two un-
8

---

## Page 9

coupled resonators cases, which is an additional advantage.
4.2. Experimental validation
In order to validate the MLAM concept experimentally, a
3D-printed prototype of the conﬁguration depicted in Fig. 4 was
tested following the procedure described in Section 2.1. The
material properties and geometrical parameters for this case
are given in Tab. 2. It should be noticed that, at present, there
are limited options in terms of materials available for the 3D-
printing technology and, in most cases, there are additional de-
sign constraints that need to be taken into account. For instance,
the minimum thickness of the layers. Furthermore, since sili-
cone rubber was not available as a material choice for the con-
necting layer, the closest alternative was a powder-based mate-
rial that, in its ﬁnal form (achieved through a Multi-Jet Fusion
process), it exhibits some rubber-like behaviour. While being
certainly softer than most conventionally polymer-based ma-
terials, this material’s stiﬀness is still 1-2 orders of magnitude
higher than that of common silicone rubber materials, which re-
quired a noticeable increase of the connecting layer’s thickness
to compensate, and make the coupled resonances work. Once
each diﬀerent layer component was 3D-printed, they were glued
together forming a MLAM stack. The tackled frequency range
of attenuation for the prototype is around 1000 Hz (in contrast
to the 400-500 Hz range considered in Fig. 5 numerical simula-
tions) due to the material options and geometric tolerances for
the available manufacturing process.
Four diﬀerent tests were performed on the same prototype,
with Fig. 6 showing the average of the obtained results. The re-
sults show more than 20 dB increase over a range of 200 Hz be-
tween two clearly deﬁned peaks at 1000 Hz and 1100 Hz. These
experimental results are consistent with the expected STL curves
obtained from the numerical simulation, especially when con-
sidering an appropriate amount of damping, with a loss factor
of η = 0.02 (expressly chosen to match to the experimental re-
sults). The experiment setting does not reproduce the ideal con-
ditions of the numerical simulations, which explains some of
the diﬀerences between both curves (like, for instance, the ap-
pearance of small spurious peaks between 800 and 900 Hz). The
lower STL level achieved in the experimental test for lower fre-
quencies (minus 10 dB compared to the simulation results) is
likely due to small sound leaks, caused by a non-perfect iso-
lation inside the tube and to the particular sample holding ap-
proach. Finally, dimensional tolerances during the manufactur-
ing process (and possible inaccuracies in the material properties
provided by the manufacturer that have been used in the simu-
lations) may be cause of small frequency shifts in the expected
STL peaks. Despite these small discrepancies the experimental
results clearly show the expected enhanced STL response, with
an extended eﬀective attenuation band due to two joined STL
peaks in the predicted frequency range.
5. Conclusions
Results for the MLAM design proposed show great poten-
tial for it to become a practical lightweight, sound attenuating
600
700
800
900
1000
1100
1200
1300
1400
Frequency (Hz)
0
10
20
30
40
50
60
70
80
90
100
STL (dB)
Experimental
Simul. (η = 0.00)
Simul. (η = 0.02)
25 mm
170 mm
Figure 6: Sound transmission loss curve, obtained experimentally for the
MLAM prototype, compared to the corresponding numerical simulation re-
sults for η = 0 (no damping) and η = 0.02. The inset on the top left depicts
a side view and a front view of the actual 3D-printed prototype employed with
the whole panel dimensions (detailed layer composition, including geometrical
parameters and materials, are given in Tab. 2).
solution at lower frequency ranges. Its main advantage over
other conventional acoustic metamaterial conﬁgurations stems
from its layer-based structure, that makes it suitable for large-
scale production through well-established manufacturing pro-
cesses. Additionally, by taking advantage of the coupled res-
onances phenomenon combined with the acoustic metamate-
rials’ local resonance eﬀects, it manages to produce STL re-
sponses exhibiting wider eﬀective attenuation bands at lower
frequencies, compared to equivalent single-resonator or uncou-
pled multi-resonator based acoustic metamaterials.
While the proposed designs in the present work provide a
ﬁrst notion of what are the capabilities of the MLAM tech-
nology, along with its validation through an early 3D-printed
prototype, there are still issues to tackle. Early studies suggest
that there is a compromise between extending the attenuation
bandwidth (by separating the resonance frequencies) and the
STL level achieved. This aﬀects also the coupling mechanism,
which is not triggered when these resonances are separated be-
yond a certain value. For the samples presented in Fig. 4, at-
tenuation bandwidths of up to 200 Hz can still be achieved, but
with signiﬁcantly lower STL performances. However, this limit
is linked to material and geometrical features of the MLAM
design, and a more detailed analysis would be a topic for fu-
ture research. In this regard, exploring the eﬀects of coupling
several MLAM panels or investigating the role of the layers’
design and topology into optimizing the STL response could
lead to more eﬃcient performances (either by increasing the
attenuation level or further extending the eﬀective attenuation
9

---

## Page 10

band). Also, it would be interesting to perform experimental
tests on prototypes produced with more suitable manufacturing
techniques (for instance, lamination combined with die cutting)
to analyze possible challenges and limitations of the technology
that would be considered in future, more optimized MLAM de-
signs.
Acknowledgements
This research has received funding from the European Re-
search Council (ERC) under the European Union’s Horizon 2020
research and innovation program (Proof of Concept Grant call
reference ERC-2019-PoC-25-04-2019, Proposal No. 874481)
through the project “Computational design and prototyping of
acoustic metamaterials for tailored insulation of noise” (META-
COUSTIC). The authors also acknowledge the ﬁnancial sup-
port received by the Spanish Ministry of Economy and Com-
petitiveness, through the Research Grant DPI2017-85521-P for
the project “Computational Design of Acoustic and Mechani-
cal Metamaterials” (METAMAT) and the “Severo Ochoa Pro-
gramme for Centres of Excellence in R&D” (CEX2018-000797-
S). The authors would like to acknowledge Prof. Mahmoud
Hussein, for the insights behind the physics of the coupled res-
onances mechanism. Finally, the authors would like to grate-
fully acknowledge Dr. Jordi Romeu and the LEAM group for
facilitating the realization of the experimental part of this work.
References
[1] M. Badreddine Assouar and Mourad Oudich. Enlargement of a locally
resonant sonic band gap by using double-sides stubbed phononic plates.
Applied Physics Letters, 100(12):123506, mar 2012. ISSN 0003-6951.
doi: 10.1063/1.3696050.
[2] M. Badreddine Assouar, Matteo Senesi, Mourad Oudich, Massimo
Ruzzene, and Zhilin Hou. Broadband plate-type acoustic metamaterial
for low-frequency sound attenuation. Applied Physics Letters, 101(17):
173505, oct 2012. ISSN 0003-6951. doi: 10.1063/1.4764072.
[3] Osama R Bilal, Andr´e Foehr, and Chiara Daraio. Observation of trampo-
line phenomena in 3D-printed metamaterial plates. Extreme Mechanics
Letters, 15:103–107, sep 2017. ISSN 23524316. doi: 10.1016/j.eml.
2017.06.004.
[4] Emilio P. Calius, Xavier Bremaud, Bryan Smith, and Andrew Hall.
Negative mass sound shielding structures: Early results.
physica sta-
tus solidi (b), 246(9):2089–2097, sep 2009.
ISSN 03701972.
doi:
10.1002/pssb.200982040.
[5] Paolo Celli, Behrooz Yousefzadeh, Chiara Daraio, and Stefano Gonella.
Bandgap widening by disorder in rainbow metamaterials. Applied Physics
Letters, 114(9):091903, mar 2019. ISSN 0003-6951. doi: 10.1063/1.
5081916.
[6] Claus Claeys, Elke Deckers, Bert Pluymers, and Wim Desmet.
A
lightweight vibro-acoustic metamaterial demonstrator: Numerical and
experimental investigation. Mechanical Systems and Signal Processing,
70-71:853–880, mar 2016. ISSN 08883270. doi: 10.1016/j.ymssp.2015.
08.029.
[7] Yuqiang Gao and Lifeng Wang. Ultrawide coupled bandgap in hybrid
periodic system with multiple resonators. Journal of Applied Physics,
127(20):204901, may 2020. ISSN 0021-8979. doi: 10.1063/1.5142066.
[8] Morgan Hiraiwa, M. Abi Ghanem, S. P. Wallen, Amey Khanolkar, A. A.
Maznev, and Nicholas Boechler. Complex Contact-Based Dynamics of
Microsphere Monolayers Revealed by Resonant Attenuation of Surface
Acoustic Waves. Physical Review Letters, 116(19):198001, may 2016.
ISSN 0031-9007. doi: 10.1103/PhysRevLett.116.198001.
[9] Kin Ming Ho, Z. Yang, X.X. Zhang, and Ping Sheng. Measurements of
sound transmission through panels of locally resonant materials between
impedance tubes.
Applied Acoustics, 66(7):751–765, jul 2005.
ISSN
0003682X. doi: 10.1016/j.apacoust.2004.11.005.
[10] Mahmoud I. Hussein and Michael J. Frazier. Metadamping: An emergent
phenomenon in dissipative metamaterials. Journal of Sound and Vibra-
tion, 332(20):4767–4774, sep 2013. ISSN 0022460X. doi: 10.1016/j.jsv.
2013.04.041.
[11] Amey Khanolkar, Samuel Wallen, Maroun Abi Ghanem, Jennifer Jenks,
Nicolas Vogel, and Nicholas Boechler. A self-assembled metamaterial for
Lamb waves. Applied Physics Letters, 107(7):071903, aug 2015. ISSN
0003-6951. doi: 10.1063/1.4928564.
[12] A.O. Krushynska, V.G. Kouznetsova, and M.G.D. Geers. Visco-elastic
eﬀects on wave dispersion in three-phase acoustic metamaterials. Jour-
nal of the Mechanics and Physics of Solids, 96:29–47, nov 2016. ISSN
00225096. doi: 10.1016/j.jmps.2016.07.001.
[13] Alexandre Leblanc and Antoine Lavie.
Three-dimensional-printed
membrane-type acoustic metamaterial for low frequency sound attenu-
ation. The Journal of the Acoustical Society of America, 141(6):EL538–
EL542, jun 2017. ISSN 0001-4966. doi: 10.1121/1.4984623.
[14] Z. Liu, X. Zhang, Y. Mao, Y. Zhu, Z. Yang, C. T. Chan, and P. Sheng.
Locally Resonant Sonic Materials. Science, 289(5485):1734–1736, sep
2000. ISSN 00368075. doi: 10.1126/science.289.5485.1734.
[15] James M. Manimala and C. T. Sun. Microstructural design studies for
locally dissipative acoustic metamaterials. Journal of Applied Physics,
115(2):023518, jan 2014. ISSN 0021-8979. doi: 10.1063/1.4861632.
[16] Olivia McGee, Huan Jiang, Feng Qian, Zian Jia, Lifeng Wang, Han
Meng, Dimitrios Chronopoulos, Yanyu Chen, and Lei Zuo. 3D printed ar-
chitected hollow sphere foams with low-frequency phononic band gaps.
Additive Manufacturing, 30:100842, dec 2019. ISSN 22148604. doi:
10.1016/j.addma.2019.100842.
[17] Christina J. Naify, Chia-Ming Chang, Geoﬀrey McKnight, and Steven R.
Nutt. Scaling of membrane-type locally resonant acoustic metamaterial
arrays. The Journal of the Acoustical Society of America, 132(4):2784–
2792, oct 2012. ISSN 0001-4966. doi: 10.1121/1.4744941.
[18] D. Roca, O. Lloberas-Valls, J. Cante, and J. Oliver.
A computational
multiscale homogenization framework accounting for inertial eﬀects: Ap-
plication to acoustic metamaterials modelling.
Computer Methods in
Applied Mechanics and Engineering, 330:415–446, mar 2018.
ISSN
00457825. doi: 10.1016/j.cma.2017.10.025.
[19] D Roca, D Yago, J Cante, O Lloberas-Valls, and J Oliver. Computational
design of locally resonant acoustic metamaterials. Computer Methods
in Applied Mechanics and Engineering, 345:161–182, mar 2019. ISSN
00457825. doi: 10.1016/j.cma.2018.10.037.
[20] D. Roca, T. P`amies, J. Cante, O. Lloberas-Valls, and J. Oliver. Exper-
imental and Numerical Assessment of Local Resonance Phenomena in
3D-Printed Acoustic Metamaterials. Journal of Vibration and Acoustics,
142(2):1–9, apr 2020. ISSN 1048-9002. doi: 10.1115/1.4045774.
[21] Matthieu Rupin, Fabrice Lemoult, Geoﬀroy Lerosey, and Philippe Roux.
Experimental Demonstration of Ordered and Disordered Multiresonant
Metamaterials for Lamb Waves.
Physical Review Letters, 112(23):
234301, jun 2014.
ISSN 0031-9007.
doi: 10.1103/PhysRevLett.112.
234301.
[22] Ping Sheng, X.X. Zhang, Zhengyou Liu, and C.T. Chan. Locally resonant
sonic materials. Physica B: Condensed Matter, 338(1-4):201–205, oct
2003. ISSN 09214526. doi: 10.1016/S0921-4526(03)00487-3.
[23] Lucas Van Belle, Claus Claeys, Elke Deckers, and Wim Desmet. The
impact of damping on the sound transmission loss of locally resonant
metamaterial plates. Journal of Sound and Vibration, 461:114909, nov
2019. ISSN 0022460X. doi: 10.1016/j.jsv.2019.114909.
[24] Viktor G. Veselago.
The electrodynamics of substances with si-
multaneously negative values of ϵ and µ.
Soviet Physics Us-
pekhi, 10(4):509–514, apr 1968.
ISSN 0038-5670.
doi:
10.1070/
PU1968v010n04ABEH003699.
[25] Eric C Wester, Xavier Br´emaud, and Bryan Smith. Meta-Material Sound
Insulation. Building Acoustics, 16(1):21–30, jan 2009. ISSN 1351-010X.
doi: 10.1260/135101009788066555.
[26] Yong Xiao, Jihong Wen, and Xisen Wen. Sound transmission loss of
metamaterial-based thin plates with multiple subwavelength arrays of at-
tached resonators. Journal of Sound and Vibration, 331(25):5408–5423,
dec 2012. ISSN 0022460X. doi: 10.1016/j.jsv.2012.07.016.
10

---

## Page 11

[27] Z. Yang, Jun Mei, Min Yang, N. H. Chan, and Ping Sheng. Membrane-
Type Acoustic Metamaterial with Negative Dynamic Mass.
Physical
Review Letters, 101(20):204301, nov 2008.
ISSN 0031-9007.
doi:
10.1103/PhysRevLett.101.204301.
[28] Z. Yang, H. M. Dai, N. H. Chan, G. C. Ma, and Ping Sheng. Acous-
tic metamaterial panels for sound attenuation in the 50–1000 Hz regime.
Applied Physics Letters, 96(4):041906, jan 2010. ISSN 0003-6951. doi:
10.1063/1.3299007.
[29] Hao-Jiang Zhao, Hong-Wei Guo, Ming-Xing Gao, Rong-Qiang Liu,
and Zong-Quan Deng. Vibration band gaps in double-vibrator pillared
phononic crystal plate. Journal of Applied Physics, 119(1):014903, jan
2016. ISSN 0021-8979. doi: 10.1063/1.4939484.
[30] Xiaoling Zhou, Longqi Wang, Li Qin, and Fujun Peng. Improving sound
insulation in low frequencies by multiple band-gaps in plate-type acous-
tic metamaterials.
Journal of Physics and Chemistry of Solids, 146
(November 2019):109606, nov 2020. ISSN 00223697. doi: 10.1016/j.
jpcs.2020.109606.
11