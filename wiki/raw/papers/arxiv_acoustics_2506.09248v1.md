# Ultra-thin normal-shear-coupled metabarrier for low-frequency underwater sound insulation
**arXiv ID:** 2506.09248v1
**Source File:** arxiv_acoustics_2506.09248v1.pdf

## Page 1

arXiv:2506.09248v1  [physics.app-ph]  10 Jun 2025
Ultra-thin normal-shear-coupled metabarrier for low-frequency
underwater sound insulation
V. F. Dal Poggetto1,∗, M. Miniaci1,∗
Abstract
Underwater noise pollution caused by anthropogenic activities, such as offshore wind farms,
significantly affects marine life, hindering the intra- and inter-specific interactions of many
aquatic species. A common strategy to mitigate these effects is to enclose the noise source
within a physical barrier to achieve acceptable noise levels in the surrounding region. Un-
derwater barriers typically achieve noise reduction through sound absorption based on locally
resonant systems (e.g., foam and bubble elements) or sound reflecting systems (e.g., air
bubble curtains). Although locally resonant-based solutions can yield significant noise atten-
uation levels, their performance is usually narrow-band. On the other hand, sound-reflecting
systems require wider dimensions, presenting poor performance in the low-frequency range.
Thus, significant low-frequency underwater noise attenuation remains an open issue, espe-
cially when considering thin structures that perform over a broad frequency range. In this
work, we present the design of thin metamaterial-based acoustic barriers whose underwater
noise attenuation is owed to tailored anisotropic material properties. A topology optimization
approach is used to obtain a unit cell that maximizes the coupling between normal stresses
and shear strains (and vice-versa).
The resulting metabarrier presents a sub-wavelength
thickness-to-wavelength ratio in the low-frequency range (circa 1/70 below 1 kHz) and also
high sound transmission loss values at higher frequencies (almost 100 dB above 2 kHz). We
also investigate the effects of increased hydrostatic pressure, presenting structural modifi-
cations that enable real-world applications. The results presented in this work indicate an
efficient metamaterial-based solution for the mitigation of underwater noise, suggesting a
fruitful direction for the exploitation of anisotropy in acoustic insulation applications.
Keywords:
Metamaterials, Underwater acoustics, Topology optimization, Sound
transmission loss, mode coupling.
Email addresses: vinicius.fonseca-dal-poggetto@univ-lille.fr (V. F. Dal Poggetto),
marco.miniaci@univ-lille.fr; marco.miniaci@gmail.com (M. Miniaci)
1Univ. Lille, CNRS, Centrale Lille, Junia, Univ. Polytechnique Hauts-de-France, UMR 8520 - IEMN -
Institut d’Electronique de Microélectronique et de Nanotechnologie, F-59000 Lille, France

---

## Page 2

1. Introduction
The social focus on marine renewable energy has renewed the interest of researchers
and industry in new designs for compact and hydrostatic pressure resistant devices that
yield effective underwater noise reduction, especially at low frequencies. In these frequency
ranges, increasing human activity in marine environments, such as offshore wind farms, tidal
stream turbines, wave energy converters, shipping and military operations, is causing greater
disruption to marine life, affecting the behavior of aquatic species by, compromising their
communication, orientation, feeding, parental care, and prey detection skills [1]. This effect
is particularly grave in the low frequency range, where the primary frequencies of hearing and
vocalization of the mammalian auditory system are located [2]. However, reducing noise at
low frequencies with insulating devices much thinner than the wavelength of incident waves
(sub-wavelength behavior) has long been and still is a major scientific and technological
challenge. This is particularly true in underwater acoustics, where associated wavelengths
are significantly longer than in air and fluid-structure interaction plays a significant role [3, 4].
Thus, in order to efficiently reduce anthropogenic pressure in the underwater environment,
the design of novel resilient barriers with significant sound insulation properties in the low
frequency range is critical.
Whenever directly addressing the noise source is not possible, an alternative solution
to reduce noise is to place barriers between the source and the areas requiring protection.
The primary approaches for underwater acoustic insulation materials involve designing the
impedance match (or mismatch) of these barriers with respect to the acoustic impedance of
water, resulting in (i) absorptive or (ii) reflective behavior [5]. To achieve this, common de-
sign strategies include fluid- or solid-filled cavities, backings, resonators, periodic structures,
and metamaterials – composite materials made of periodic arrangements of sub-wavelength
structures – which have been widely explored to date [6, 7, 8].
When impedance matching is exploited, the use of barriers made of polymeric materials
enhanced with viscoelastic micro- or macro-inclusions, as well as viscoelastic coatings em-
bedded with periodic air pockets [9, 10, 5, 11] is among the most well known and diffuse
absorptive approaches. In this case, insulation performance results from intrinsic sound ab-
sorption derived from relaxation of molecular chains in the polymer matrix material and
frequency-dependent modifications of the barrier vibration characteristics (wave velocity,
resonance frequencies, and mode shapes). Relaxation of molecular chains provides rather
good performance at high frequencies, while its ability to absorb low-frequency sound re-
mains limited [9]. To improve performance, cavities of various shapes have been explored to
facilitate the conversion of acoustic waves to shear waves, a phenomenon known to improve
2

---

## Page 3

absorption due to high shear damping present in some materials [12]. Analytical and nu-
merical studies indicate that the shape and deformation of the inclusions play a crucial role;
however, the operational frequency bandwidth is constrained by the resonance frequencies of
the inclusions [13]. To address this limitation, researchers have proposed optimized geome-
tries and material compositions for resonating inclusions, along with tailored properties of
the host material, to improve attenuation efficiency and broaden the operational frequency
range [11].
Although relatively well-performing at mid and high frequencies, these approaches per-
form poorly below 1 kHz. Ensuring impedance matching between resonating elements (such
as Helmholtz-like resonators) and water has shown potential as an alternative, at least in
proximity of the resonance frequency of the resonators. Although extensively studied in the
context of airborne acoustics [14], their application in underwater environments has been
less explored. Duan et al. [15] numerically proved that an underwater quasi-Helmholtz res-
onator, including rubber coatings inside its resonant cavity, can lead to perfect absorption
in the 100 to 300 Hz frequency range. Duan et al. [16] developed a theoretical model to pre-
dict the sound absorption performance of a sub-wavelength absorber made of a perforated
face plate, a fluid-filled square honeycomb core with interior rubber coating, and a fixed
back plate based on the sound absorption theory of the micro-perforated panel and electroa-
coustic analogy. Multiple peaks of perfect absorption below 1 kHz have been numerically
reported. Furthermore, Qu et al. [6] proposed a structured tungsten-polyurethane compos-
ite, impedance-matched to water, that achieves a slow longitudinal sound speed through the
optimal distribution of Fabry-Pèrot resonances over a broad frequency range (4 to 20 kHz).
Other absorption-driven approaches include air or air/water-filled Helmholtz resonators,
multilayered coated plates to generate slow waves [17], the introduction of hard and air-filled
backings [18], and hydrosound dampers (nets with air-filled elastic balloons) [19]. In offshore
installations, such as pile driving for wind farms [20], air-filled Helmholtz resonators have
achieved noise reductions of approximately 20 dB at a central excitation frequency of 140
Hz [21]. Wochner et al. [22] measured up to a peak loss of 37 dB around 100 Hz (measured
using average one-third octave bands) in a Helmholtz resonator-based system with two fluids
(water and air). The main drawbacks of these approaches include their narrow-band nature
and the difficulty in accounting for the elastic deformation of the resonators induced by
hydrostatic pressure or by the oblique incidence of the acoustic wave, which can affect the
resonant behavior of the finite system [23].
The second approach, which relies on a strong impedance mismatch between the barrier
and surrounding water, primarily works by reflecting acoustic waves to prevent their prop-
3

---

## Page 4

agation through a given medium. Insulation of water sound through impedance mismatch
has the advantage of a more broadband effectiveness compared to using materials with band
gaps induced by local resonances. Common solutions of this type include (i) arrays of one
fluid immersed in another with contrasting properties, such as air bubbles in water, and
(ii) mechanical casings that enclose the noise source, such as those used around eolian piles
during driving, with the goal of confining the energy of the sound waves to the space be-
tween the noise source and the barrier. Lucke et al. [24] reported a peak-to-peak mean level
difference of 14 dB inside and outside an air curtain installed to protect porpoises from the
installation of wooden piles in Denmark. Würsig et al. reported [25] reductions of 8–10 dB
in the 400–800 Hz bands and 15–20 dB in the 1.6–6.4 kHz bands, indicating significantly
poorer performance at lower frequencies. Although commonly used, achieving attenuation
in the very low frequency range (< 600 Hz) may require air curtains with bubbles ranging in
radius from 8 mm near the surface to 50 mm at a depth of 30 m [26]. This poses a significant
limitation for the practical application of this concept because of the challenges of generating
and maintaining air bubbles in a controlled manner in an offshore environment.
Although shown in the ultrasonic regime, it is worth mentioning the works by Brunet et
al., who observed ultra-slow Mie resonances in meta-fluids made of concentrated suspensions
of macro-porous micro-beads engineered using soft matter techniques [27, 28], and Leroy et
al., who measured good acoustic attenuation in liquid foams over a broad high frequency
range (60–600 kHz), proving through a theoretical model that the attenuation mechanism is
derived from the existence of two non-dispersive bands in the dispersion relation for longi-
tudinal acoustic waves, separated by a negative density regime [29, 30].
Architected acoustic panels represent another potential solution to reduce underwater
noise acting as mechanical casings placed around noise sources. However, water belongs to
high-impedance media (Zw ≈1.5×106 N · s/m3), implying that barriers aimed at reflections
due to a higher impedance with respect to water cannot efficiently isolate sound at low
frequencies. For example, for the case of a 50 mm thick steel plate immersed in water, more
than 85% of the energy is transmitted if the frequency of the incident acoustic wave is below
500 Hz.
In the case of underwater casing systems for mitigation noise associated with pile instal-
lation, these are completely enclosed along the column of seawater. For instance, Jansen et
al. [31] proposed noise mitigation screens made of double-walled steel cylinder filled with air
submerged up to 25 m of depth. The proposed system works with combinations of (i) water
or air/water between the pile and the casing and (ii) water or air inside the casing, yielding
a frequency-dependent acoustic insertion loss (difference between transmission without and
4

---

## Page 5

with the barrier) with a slope of about 2 dB/octave, exceeding 20 dB above 4 kHz, being
limited to 8–11 dB when averaged over a large frequency range (50 Hz – 40 kHz). However,
the authors also state that the attenuation is less pronounced in the low frequency range
(100–250 Hz). Other technological solutions for underwater casing systems are also reported,
although with a lesser degree of maturity in terms of practical deployment [32].
Wang et al. [33] introduced a topological optimization approach for lattice materials
to create low acoustic impedance media, allowing "acoustic soft boundaries" compared to
water. By optimizing the topology of the material and applying a homogenization method,
key parameters for effective low-frequency sound insulation have been identified. The results
revealed that minimal acoustic impedance depends not only on the degree of anisotropy but
also on specific structural features that facilitate deformation. Two designs with ultra-thin
and deep sub-wavelength structures have been proposed relying on a bi-mode lattice material
possessing (i) strong anisotropy and a positive Poisson’s ratio or (ii) weak anisotropy and a
negative Poisson’s ratio. Chen et al. [34] explored the reflection of underwater sound waves
on orthotropic solids, whose acoustic impedance can be customized through mechanical
anisotropy, principal axes orientation, and velocity ratio of the quasi-transverse and quasi-
longitudinal waves supported by these materials.
Numerical simulations have shown an
optimal condition of an almost perfect reflection (97.7%) of the incident acoustic energy
in the case of normal incidence with an overall thickness of the lattice being two orders of
magnitude smaller than the water wavelength in the 1.5 – 3.5 kHz frequency range. Wang et
al. [35] measured a loss of sound transmission of approximately 16 dB within the 400 – 1200
Hz frequency range, overcoming the mutual exclusion of low acoustic impedance and high
mechanical properties by regulating the lattice orientation and incorporating a hierarchical
morphology in an anisotropic metamaterial. Wang et al. [36] proposed reverse engineering of
chiral metamaterials with optimized low acoustic impedance and appropriate stiffness using
a topology optimization approach, demonstrating high and broadband sound transmission
loss (STL) within the 1 to 5 kHz frequency range, as well as sufficient stiffness to ensure
stable acoustic performance under moderate hydrostatic pressure. Experiments carried out
in a water-filled impedance tube revealed, on average, a reduction of more than 95% of the
incident sound energy.
Despite the approaches described above, achieving broadband and efficient underwater
noise reduction at low frequencies (below 1000 Hz) remains a challenge, especially when us-
ing highly sub-wavelength structures that must also withstand hydrostatic pressure. In this
work, we address this challenge by introducing a periodic metamaterial with a unit cell de-
signed to enable a tailored interaction between normal and shear behavior along predefined
5

---

## Page 6

directions. An elasticity-based approach allowed us to ensure efficient underwater acoustic
waves reflection in broad frequency ranges. We start by demonstrating the effect that a cou-
pled normal–shear behavior has on fluid-immersed homogeneous anisotropic metabarriers.
Then, these results are utilized to formulate a topology optimization problem which maxi-
mizes such coupling. Unlike existing approaches, our optimization problem is proposed in
the static regime (zero frequency), depending only on the homogenized material properties
of the structured material but not on the properties of the surrounding fluid. The obtained
results, however, are shown to be valid to non-zero frequencies under various situations.
The paper is organized as follows: Section 2 presents the mathematical models and numer-
ical methods used to investigate the STL curves of fluid-immersed anisotropic metabarriers
and the formulation of the topology optimization problem that yields the optimized unit
cell. Section 3 presents the results of the optimization problem and its corresponding STL
curves for an increasing number of unit cells, including suitable modifications to account
for hydrostatic pressure. We also perform two-dimensional simulations to assess the acoustic
attenuation effects for a point source. In Section 4 we present our conclusions and an outlook
for future work.
2. Mathematical modeling and numerical methods
2.1. Normal-shear coupled behavior in anisotropic media
Fig. 1a reports a schematic representation of a noise source in an underwater medium
generating acoustic waves with a typical wavelength λ (top panel, Fig. 1a). Our objective
is to design a metamaterial-based acoustic barrier (henceforth named "metabarrier") that
interacts with the acoustic waves radiated by the noise source, reducing energy transmission
at selected frequencies and achieving efficient underwater noise mitigation (bottom panel,
Fig. 1a). Here, we do not account for energy absorption within the metabarrier. To this end,
we consider a metabarrier with an architected structure, whose periodicity is obtained by
the repetition of a specially designed unit cell. The metabarrier presents a finite repetition
of the unit cell in the x-direction (finite length h ≪λ) and an infinite number of unit cells
in the y-direction (theoretically periodic medium).
To achieve the effect of significant STL values using an architected medium, we propose
the exploitation of structural anisotropy. To illustrate this behavior, let us consider a two-
dimensional medium whose stress-strain relations are expressed in tensor notation as σij =
Cijklεkl, where σij is the Cauchy stress tensor, Cijkl is the fourth-order elasticity tensor and
εkl is the strain tensor [37]. For a fixed Cartesian coordinate system with axes xy, these
6

---

## Page 7

a
b
β
β
β
isotropic
anisotropic (four-
fold symmetry)
anisotropic (rotational 
symmetry)
x
y
x′
y′
Schematic 
representation of a 
wind turbine pile
λ
h<<λ
Metabarrier
x
y
x
y
Fig. 1: Underwater metabarrier. (a) A noise source produces acoustic waves (wavefronts represented
in blue) with a typical wavelength λ in an underwater medium (top panel). By enclosing the noise
source within a metamaterial-based acoustic barrier (metabarrier, represented in green) with length
h ≪λ, incident acoustic waves from the fluid partition at one side of the barrier are partially re-
flected, while a fraction of their energy is transmitted to the fluid partition at the other side (bottom
panel). (b) Typical examples of unit cells (top panel) with their respective behaviour (bottom panel)
of isotropic materials (left panel), anisotropic materials with four-fold symmetry (center panel),
and anisotropic materials with rotational symmetry (right panel), yielding direction-independent,
π/2-rotational symmetric, and π-rotational symmetric constitutive matrix components. The green
dashed line indicates the axis of symmetry (with respect to either reflection or rotation).
relations can be written in matrix form as





σx
σy
τxy





=


C11
C12
C13
C21
C22
C23
C31
C32
C33







εx
εy
γxy





,
(1)
where σx = σxx and σy = σyy are the normal stresses, τxy is the shear stress, Cij = Cji,
{i, j} = {1, 2, 3}, are terms of the constitutive matrix (C), εx = εxx and εy = εyy are normal
strains, and γxy = 2ϵxy is the in-plane shear strain. For a coordinate system x′y′ rotated
with respect to xy about an additional angle β (Fig. 1b, top left panel), it is possible to
obtain the corresponding matrix in the new coordinate system using an adequate coordinate
transformation matrix T of the form C′ = TTCT (see Appendix
A for details). As a
consequence, each component of the direction-dependent elasticity tensor in matrix form
C′
ij(β) can be analyzed separately.
The usual homogeneous structures employed in typical barriers [32] present isotropic
7

---

## Page 8

constitutive behavior, yielding decoupled normal stresses and shear strains (and vice versa)
for every direction. An example of a continuous homogeneous structure is shown in Fig. 1b
(top left panel), where we show (bottom left panel) the direction independence of the ratio
between constitutive components C′
13(β)/
p
C′
11(β)C′
33(β). In this case, the elasticity tensor
components are invariable with respect to the orientation angle β and C′
13(β) = C′
31(β) = 0,
indicating that normal-shear coupling is not possible for any angle.
In the case of structures with an architected unit cell, however, an anisotropic behavior
may be readily observed. Consider, for instance, the unit cell with four-fold symmetry shown
in Fig. 1b (top middle panel).
In this case, the illustrated elasticity tensor components
present a four-fold symmetry, displaying preferential angles (π/8 + nπ/4, n ∈N, illustrated
by the green dashed lines, bottom middle panel) for the coupling between normal and shear
stresses (C′
13(β)̸ = 0). This implies, however, that no coupling is present at an arbitrary
angle (e.g., β = 0).
Finally, by removing the condition of four-fold symmetry, it is possible to design a unit
cell that presents a non-zero value of normal-shear coupling at an arbitrary direction (e.g.,
β = 0). An example of a unit cell with such a condition is given in Fig. 1b (top right
panel), with its corresponding behavior showing π/2-rotational symmetry (dashed red and
yellow lines, bottom right panel), and as a consequence, non-zero normal-shear coupling for
the angle β = 0. This allows for the excitation of modes with a shear component due to
the incidence of longitudinal (acoustic) modes from the fluid, thus hindering the efficiency
of longitudinal wave mode propagation in the solid medium, reducing the transmission of
energy between incident and transmitted acoustic waves. Let us now verify the effect of a
coupled normal-shear behavior on the STL curves of homogeneous anisotropic structures.
2.2. Transfer matrix method
To investigate the effects of coupled normal-shear behavior, we utilize a transfer matrix
method [38] to relate quantities of interest (in this case, acoustic pressures) on both edges
of an acoustic barrier with homogeneous anisotropic material properties and a thickness h
in the x-direction (see Fig. 2a) immersed in a fluid, yielding the corresponding STL curves.
For the derivation of the transfer matrix method, we consider waves propagating in the
x-direction (same as the finite length of the metabarrier). The general form of structural
displacements is written as
u(x, t) = e−iωt(ˆu1pU1eik1x + ˆu1nU1e−ik1x + ˆu2pU2eik2x + ˆu2nU2e−ik2x) ,
(2)
where u = {ux, uy}T is a displacement vector in Cartesian coordinates, x is a coordinate
8

---

## Page 9

a
d
Pi(x,t)
Pr(x,t)
Pi’(x,t)
Pt(x,t)
u1pU1
^
^u1nU1
u2pU2
^
^u2nU2
x
x=0
x=h
b
Fluid medium
Metabarrier
Fluid medium
Unit cell
c
Fig. 2: Investigation on the STL properties of a fluid-immersed homogeneous anisotropic metabar-
rier under normal incidence of acoustic waves. (a) Anisotropic homogeneous acoustic barrier with
thickness h subjected to incident waves (Pi, P ′
i), emitting reflected (Pr) and transmitted acoustic
waves (Pt). The internal propagation of elastic waves is described by a pair of wave modes (U1,
U2) with positive- and negative-going components (indices p and n for each amplitude ˆu, respec-
tively).
(b) Computed STL in the normalized frequency range ωh/c0 ∈[0, 1] for the thickness
h = h = 10−2 and coupling factor δ = {0.9, 0.95, 0.995}.
(c) Same as (a) for δ = 0.999 and
h/h = {10−2, 10−1, 100}. The first and second peaks (dips) are represented by orange and purple
stars (diamonds), respectively, for the case h = 100. (d) Amplitude of normalized longitudinal (vx)
and transverse (vy) velocities for the peaks and dips indicated in (c).
whose origin is set at the fluid-structure interface between the metabarrier and incident
acoustic waves, i = √−1 is the imaginary unit number, ω is the circular frequency, t is
the time coordinate, U1 and U2 are generalized wave modes, k1 and k2 their corresponding
wavenumbers, and ˆu1p and ˆu1n (ˆu2p and ˆu2n) are, respectively, the complex amplitudes of
waves traveling in the positive (+x) and negative (−x) directions, related to wave mode U1
(U2). The values of complex amplitudes can be determined by setting appropriate boundary
conditions at the fluid-structure interface. Details on wavenumber and wave modes are given
in Appendix B.
At the fluid-structure interfaces between metabarrier and surrounding fluid, shear stresses
vanish [39], leading to a ratio of wave amplitudes given by
(
ˆu1n
ˆu2n
)
=
"
∆11
∆12
∆21
∆22
# (
ˆu1p
ˆu2p
)
,
(3)
9

---

## Page 10

where
∆11 = e−ik2h −eik1h
e−ik2h −e−ik1h , ∆12 = Cϕ2
z k2
Cϕ1
z k1
e−ik2h −eik2h
e−ik2h −e−ik1h ,
∆21 = Cϕ1
z k1
Cϕ2
z k2
e−ik1h −eik1h
e−ik2h −e−ik1h , ∆22 = eik2h −e−ik1h
e−ik2h −e−ik1h ,
(4)
with Cϕ
z = C31 cos ϕ + C33 sin ϕ, with ϕi = ∠Ui. Details are given in Appendix C.
The structural transfer matrix T(s) allows to relate longitudinal displacements (ux) and
normal stresses (σx) at the right (x = h) and left (x = 0) edges of the metabarrier as
(
ux
σx
)
x=h
= T(s)
(
ux
σx
)
x=0
=
"
T (s)
11
T (s)
12
T (s)
21
T (s)
22
# (
ux
σx
)
x=0
,
(5)
where T (s)
11 = T (s)
22 , det(T(s)) = T (s)
11 T (s)
22 −T (s)
12 T (s)
21 = 1 and T(s) is real-valued. This matrix is
computed as
T(s) = M(x = h)M−1(x = 0) ,
(6)
where M(x) is obtained as
M(x) =
"
cos ϕ1eik1x
cos ϕ1e−ik1x
cos ϕ2eik2x
cos ϕ2e−ik2x
Cϕ1
x ik1eik1x
−Cϕ1
x ik1e−ik1x
Cϕ2
x ik2eik2x
−Cϕ2
x ik2e−ik2x
#


1
0
∆11
∆12
0
1
∆21
∆22


,
(7)
with Cϕ
x = C11 cos ϕ + C13 sin ϕ. Details are given in Appendix C.
Let now the acoustic pressure waves (see Fig. 2a) be denoted as
Pi(x, t) = e−iωt ˆPieik0x,
Pt(x, t) = e−iωt ˆPteik0(x−h),
Pr(x, t) = e−iωt ˆPre−ik0x,
Pi′(x, t) = e−iωt ˆPi′e−ik0(x−h),
(8)
where Pi and Pi′ are, respectively, incident waves propagating in the +x and −x directions,
Pr and Pt are, respectively, reflected and transmitted waves (with respect to Pi), k0 = ω/c0
is the acoustic wavenumber, and c0 is the sound of speed in the fluid. The pressure Pi′ is
introduced due to the necessity of symmetry in the formulation, and the shift (x −h) in the
exponential terms of the waves at the right end of the metabarrier is adopted for analytical
convenience.
The continuity of accelerations and stresses at the fluid-structure interface between the
metabarrier and surrounding fluid allows to write the acoustic transfer matrix T(a), relating
10

---

## Page 11

acoustic pressures on both sides of the metabarrier, as
( ˆPt
ˆPi′
)
= T(a)
( ˆPi
ˆPr
)
=
"
T (a)
11
T (a)
12
T (a)
21
T (a)
22
# ( ˆPi
ˆPr
)
,
(9)
where the terms of the acoustic transfer matrix T(a) are given by
T (a)
11 = T (s)
11 + i
2

−
k0
ρ0ω2T (s)
21 + ρ0ω2
k0
T (s)
12

, T (a)
12 = i
2
 k0
ρ0ω2T (s)
21 + ρ0ω2
k0
T (s)
12

,
T (a)
21 = −i
2
 k0
ρ0ω2T (s)
21 + ρ0ω2
k0
T (s)
12

, T (a)
22 = T (s)
22 + i
2
 k0
ρ0ω2T (s)
21 −ρ0ω2
k0
T (s)
12

,
(10)
with det(T(a)) = T (a)
11 T (a)
22 −T (a)
12 T (a)
21 = 1 due to the reciprocity of the system.
Assuming no incident waves at the right edge of the metabarrier ( ˆPi′ = 0) leads to
a reflection coefficient R = ˆPr/ ˆPi = −T (a)
21 /T (a)
22 , which allows to write the transmission
coefficient as
T =
ˆPt
ˆPi
= T (a)
11 T (a)
22 −T (a)
12 T (a)
21
T (a)
22
=
1
T (a)
22
.
(11)
Finally, the STL can be computed as [40]
STL(ω) = 10 log
 ˆPi
ˆPt
2
= 20 log

1
T
 .
(12)
It is interesting to note that there exists a set of frequencies where the condition of
full transmission (i.e., |T| = 1, zero STL) is observed.
This condition is achieved at
Im{T} =Im
n
1
T (a)
22
o
= 0, i.e.,
k0
ρ0ω2T (s)
21 −ρ0ω2
k0
T (s)
12 = 0 ,
(13)
which implies a real-valued T (a)
22 at these frequencies (since T (s)
22 is real-valued). As a conse-
quence, at |T| = 1, we have the equality T (a)
22 = T (s)
22 = ±1. As det(T(s)) = 1 and T (s)
22 = T (s)
11 ,
this also implies in T (s)
12 T (s)
21 = (T (s)
22 )2 −1. Since at these frequencies T (s)
22 = ±1, this also
implies T (s)
12 T (s)
21 = 0, which combined with Eq. (13), also implies that both T (s)
12 = 0 and
T (s)
21 = 0. As a consequence, at each frequency where |T| = 1 (zero STL), we have T(s) =
T(a) = ±I, which implies ˆPt = ± ˆPi, ux(x = h) = ±ux(x = 0), and σx(x = h) = ±σx(x = 0).
Thus, we conclude that full transmission conditions are associated with a formation of sym-
metric modes at the metabarrier. A similar derivation of STL maxima condition is however
less direct, since in these cases the condition |T| = 0 is not achieved (which would imply
11

---

## Page 12

infinite STL). We now proceed to utilize the derived transfer matrix method to evaluate the
effect of couple normal-shear behavior on the STL curves.
2.3. Effect of normal-shear coupling on STL curves
The proposed transfer matrix method can be used to present an illustrative example,
computing the STL curves of a homogeneous two-dimensional structure whose constitutive
matrix C presents components with values C11 = 1 GPa, C33/C11 = 0.9 and a specific mass
density of ρ = 1000 kg/m3. The ratio between the acoustic wave speed in the fluid and the
solid is assumed as c0/
p
C11/ρ = 0.9 and the ratio between their specific mass densities as
ρ0/ρ = 0.9, thus similar to the ratio between the material properties of water and typical
polymers. We compute and investigate the STL curves for a barrier with a finite thickness
h over the normalized frequency range ω∗= ωh/c0 ∈[0, 1], for h = 10−2.
Following our previous discussion on anisotropy, we also define a mode coupling factor δ
which relates normal stresses and shear strains (and vice-versa) as the the ratio between the
C13 = C31 terms of the constitutive matrix and the product C11C33 as
δ =
C13
√C11C33
,
(14)
yielding δ ∈(−1, 1). In the case of an isotropic medium, C13 = C31 = 0 and one obtains
δ = 0. This parameter is also typically associated to the degree of structural instability and
used in the context of longitudinal-shear mode conversion [41].
The STL curves computed for h = 100 and δ = {0.9, 0.95, 0.995} are shown in Fig. 2b.
For the value δ = 0.9, the presence of a local maximum of 2.6 is noticed at ω∗= 0.83. For
δ = 0.95, we notice the presence of a maximum STL of 4.7 located at ω∗= 0.55, with the
occurrence of a zero STL value (dip) at ω∗= 0.96, which shows that increasing the value
of δ presents the effects of (i) increasing the first peak STL value and (ii) red-shifting its
frequency. Finally, for δ = 0.995, a total of 5 STL peaks is noticed, also with an increase in
the number of dips (total of 4) in the same frequency range. Noticeably, the first peak is now
located at ω∗= 0.17 with an STL value of 13.8. Thus, increasing δ from 0.9 to 0.995 leads
to a (i) five-fold increase in the first STL peak and (ii) 80% reduction in its corresponding
normalized frequency. As a consequence, an infinite STL value would be achieved close to
the zero frequency, for δ →1−.
We also investigate the variation of the STL curves computed for the fixed value of
δ = 0.999 and increasing values of h ∈[10−2, 100], as shown in Fig. 2c (bottom panel) For
h = 10−2, a maximum STL value of 7.0 is computed at ω∗= 1, which suggests that even
12

---

## Page 13

ultra-thin structures may present significant STL values, even if the first peak is located at
higher frequencies. It is important to notice that remaining in the sub-wavelength regime
(thickness much smaller than typical wavelength) is of interest, which then requires small
values of h. On the other hand, sufficiently large values of h are required to ensure that
the homogenization hypotheses are valid, which may pose conflicting design objectives (sub-
wavelength regime vs. homogenized material properties). For h = 10−1, a maximum STL
value of 20.7 is achieved at ω∗= 0.75, indicating the red-shift of STL peaks for an increase
in the thickness. Finally, for h = 100, a total of 10 STL peaks and dips are observed in this
frequency range, with a first STL peak of 20.7 dB at ω∗= 0.075. Interestingly, this represents
a maintenance in the STL level of the first peak with respect to the case h = 10−1, however
with a ten-fold reduction in its frequency for a ten-fold thickness increase, thus suggesting
that the first peak of the STL curve can be tuned using the thickness of the metabarrier.
Finally, we indicate the first two peaks (dips) in the STL curve for h = 100 using orange
and purple stars (diamonds), respectively. The profiles of the absolute normalized velocities
(and equivalently, displacements and accelerations) are shown in Fig. 2d.
The modes corresponding to the selected peaks (orange and purple stars) present a sig-
nificant decrease between the longitudinal velocities (vx, black lines) at the left (x = 0) and
right (x/h = 1) ends of the metabarrier. This implies a decrease in the velocity (and accel-
eration) transmissibility between the input and transmitted ends, which justifies the sharp
peaks in the STL curves. On the other hand, the modes corresponding to the dips in the
STL curves (orange and purple diamonds) present symmetric profiles of longitudinal and
transverse absolute velocities, resulting in unit transmissibility between the left and right
edges of the metabarrier. The n-th dip presents a phase variation of nπ, n ∈N, resulting
in complete in-phase or out-of-phase behavior between both edges of the metabarrier. As
a consequence, the transmitted and incident acoustic waves present the same amplitude,
differing at most from a phase shift performed by the metabarrier.
2.4. Optimization problem and unit cell design
The previous discussion suggests that a suitable optimization objective to obtain the pe-
riodic unit cell that forms a metabarrier which yields maximum STL at a minimal operating
frequency is the maximization of the mode coupling factor δ. The desired value of δ →1−
would yield an infinite STL at zero frequency. However, this value cannot be achieved, as it
represents a structural singularity.
Thus, in order to obtain the periodic metamaterial unit cell, we propose a topology
13

---

## Page 14

optimization problem which aims to minimize the objective function φ, given by
minimize
q∈{0,1}nq
φ(q) =
 |C13|/√C11C33 −1
2 ,
subjected to
ω1 > ωmin ,
(15)
where q is a binary vector composed of nq design variables representing the presence of
material or voids in the unit cell, and ω1 is the first resonant frequency of the system for free
boundary conditions excluding rigid body motion, which must be above a certain threshold
(ωmin). The proposed objective function aims to minimize the distance between |δ| and 1,
while the first resonance frequency restriction is imposed to ensure a connectivity between
the pixels of the candidate unit cell, thus discarding solutions that present disconnected (i.e.,
"floating") regions.
Each square unit cell used in the topology optimization process is described by a distri-
bution of 2q×2q pixels. The continuity between the pixels of contiguous unit cells is ensured
by the correspondence of pixels between opposing edges. Additionally, a π/2-rotational sym-
metry can be enforced in the internal region of the unit cell to ensure normal-shear coupling.
This yields a total of nq = 2q2 −2q −1 pixels, which can then be encoded into a corre-
sponding binary vector q (Fig. 3a, middle panel). The represented unit cell can then be
discretized using regular square finite elements under the assumption of plane strain [42],
allowing to compute the effective constitutive matrix of the homogenized unit using the
method described in [43]. The dynamic behavior of the homogenized unit cell is valid in the
long wavelength limit (k →∞, i.e., its validity decreases for increasing frequency values). It
is also important to note that since the homogenization procedure only concerns the static
properties of the unit cell, the evaluation of binary vectors in the optimization problem (see
Eq. (15)) presents a low computational cost, which allows to make an efficient use of genetic
algorithms [44] to determine an optimal solution.
3. Results
3.1. Result of optimization problem
We apply the optimization procedure considering a structure composed of a plastic ma-
terial with Young’s modulus E = 3 GPa, Poisson’s ratio ν = 0.3, and specific mass density
ρ = 1150 kg/m3. The unit cell has a length a = 10 mm, which is amenable to fabrication.
An example of a discretized unit cell, with a distribution of 2q×2q pixels, is shown in Fig. 3a.
The continuity between the pixels of contiguous unit cells and the internal π/2-rotational
14

---

## Page 15

symmetry are represented as "Matching boundaries" (green contour) and "Anti-symmetry"
(region inside the dashed red contour).
 
 
Smoothed 
unit cell
Optimization
result
δ=0.9879
δ=0.9852
p<0.5
p>0.5
2.67 kHz
c
a
Matching 
boundaries
2q
Anti-
symmetry
Encoded binary vector
2q2-2q-1 entries
Genetic Algorithm
Unit cell
q=
search optimal q
1 1 1 0 1 1 0 0 0 1 0 1 1
b
ux
uy
ux
uy
u
-1     0   +1 
u
-1     0   +1 
Fig. 3: Optimization of the metabarrier unit cell. (a) Periodic unit cell (top panel) with a discretized
geometry indicating 2q × 2q pixels with either material (1) or void (0), with enforce π/2-rotational
symmetry in the internal region (Anti-symmetry) and periodic boundaries (Matching boundaries).
This description in encoded into a binary vector q (middle panel), which then is utilized in a genetic
algorithm optimization (bottom panel).
(b) Result of the optimization procedure (top panel),
obtained for q = 5, yielding a normalized stiffness ratio δ = 0.9879. After obtaining a smooth
approximate representation (bottom panel), this value is decreased to δ = 0.9852. (c) Dispersion
diagram (continuous lines) for the obtained unit cell (length a = 10 mm), with polarization values p
indicating either completely longitudinal (p = 0) or transverse motion (p = 1). The wave modes are
computed and shown at the X-point (k = π/a) of the first branch (2.67 kHz) and k ≈0.14π/a point
of the second branch (5.00 kHz). The dashed lines indicate the dispersion curves corresponding to
the medium with effective homogenized properties for the first (k1) and second branches (k2).
The result obtained using q = 5, yielding a total of 2q × 2q = 100 pixels and nq = 39
optimization variables (i.e., 239 = 5.5 × 1011 possible designs), and ωmin = 0.1 rad/s is
presented in Fig. 3b (top panel), displaying the discretized geometry of the unit cell and
the obtained δ value (δ = 0.9879). The obtained geometry then undergoes a smoothing
procedure to yield a geometry amenable to fabrication (Fig. 3b, bottom panel). As a result
of the geometrical modifications, a slightly smaller value of δ is obtained (δ = 0.9852).
We then apply periodic Bloch-Floquet conditions to the resulting unit cell [45] and
compute its dispersion diagram in the ΓX direction, with Γ located at k = 0 and X lo-
cated at k = π/a. For each wavenumber, we also compute a polarization metric given by
p(ux, uy) =
R
S |uy|2 dS/
R
S |ux|2 + |uy|2 dS, where ux and uy are the x- and y-direction dis-
placement components of a given wave mode and S is the unit cell two-dimensional domain.
15

---

## Page 16

As a result, p = 0 (p = 1) represents purely longitudinal (transverse) motion. The band
diagram computed using the FE method is shown in Fig. 3c in the [0, 5] kHz frequency range
using continuous lines, with polarization values indicated in a color scale ranging from p = 0
(dark blue) to p = 1 (dark green).
The first obtained branch presents p ∈[0.403, 0.414], demonstrating a predominant longi-
tudinal behavior (p < 0.5), although with a high degree of hybridization between longitudinal
and transverse motion. The wave mode corresponding to this branch at the point X is also
shown (colorbar represents displacement values, ux and uy), illustrating this coupled behav-
ior at 2.67 kHz. Above this frequency (indicated with a horizontal red dashed line), the
first branch is no longer present in the considered frequency range. Likewise, the second
branch presents p ∈[0.585, 0.589], exhibiting a predominant transverse behavior (p > 0.5)
with a significant hybridization between longitudinal and transverse motion. A wave mode
corresponding to this branch is shown at 5 kHz, displaying a rigid-body-like vertical motion
due to the small wavenumber at this point (k ≈0.14π/a). Therefore, it is possible to observe
that even though the coupling between normal/shear stresses/strains was optimized in the
static regime (i.e., ω = 0), this also implies in coupled longitudinal-transverse motion .
It is also interesting to note that the behavior predicted by the homogenized structure
with effective properties (see Appendix B), represented by the dashed green and purple lines
in Fig. 3c, correlates well with the finite element-based solution up to 2.3 kHz, when the
first branch starts presenting a significant dispersive behavior. We now proceed to evaluate
the STL properties of a metabarrier composed of repetitions of the unit cell obtained in the
optimization procedure.
16

---

## Page 17

3.2. Metabarrier STL curves
The unit cell resulting from the optimization process (Fig. 3b) presents inconvenient gaps
in its left and right ends, resulting in finite structures with cavities at their edges. To remedy
this issue, we may swap the left and right halves of the unit cell keeping their orientation
(regions inside the red and green contours in Fig. 4a, respectively), which does not affect
the dispersion relation of the material due to its periodicity. This unit cell is then repeated
along the x-direction to obtain finite structures with a thickness equal to h = Na, where
N ∈N ∗is the number of utilized unit cells.
The resulting finite structures are utilized to evaluate the STL (see Eq. (12)) when
immersed in water, as illustrated in Fig. 4b, considering a periodic medium in the y-direction.
The numerical procedure for computing the STL curves is described in Appendix D, which
we perform considering a solid structure filled with air fluid. The effect of the consideration
of the internal fluid is a slight blue-shift in the STL curves with respect to the case without
fluid (this comparison is presented in Appendix E). The material properties of water (air) are
the specific mass density ρw = 998 kg/m3 (ρa = 1.2 kg/m3), with a speed of sound cw = 1481
m/s (ca = 343 m/s). These results are shown in Fig. 4c for an increasing number of unit
cells, N = 1, 2, · · · , 6. Displacement profiles corresponding to selected peaks and dips are
also shown considering longitudinal and transverse displacements (ux and uy, respectively),
normalized with respect to the largest computed displacement (i.e., |u| =
p
|ux|2 + |uy|2).
The vertical dashed red line indicates the start of the frequency region where a single wave
mode is present (corresponding to the horizontal dashed red line in Fig. 3c).
We begin our analysis with N = 1, a particularly interesting case due to its very thin
profile. In the shown frequency range, this structure presents a maximum STL of 29.0 dB at
2.07 kHz (displacement profile i-p). At this frequency, the structure presents a remarkable
subwavelength performance, since the ratio between the thickness h = a and the associated
wavelength λ = cw/f yields the ratio h/λ ≈1/70. The STL curve reaches a first dip at 4.7
kHz, presenting a symmetric displacement profile with respect to the y-axis (displacement
i-d), which justifies a unit ratio between displacements and also acoustic pressures, yielding
a zero STL (a complete explanation is given in Section 2.3). However, no visible correlation
can be described with respect to the dispersion diagram shown in Fig. 3c due to the lack of
periodicity in this case, which considers a single unit cell.
For the case N = 2, a first STL peak of 24.4 dB is computed at 0.83 kHz, with a
displacement profile (ii-p) indicating a behavior equivalent to that of the first peak computed
at N = 1 (i-p), however with a longer wavelength for both ux and uy (i.e., the displacement
profiles become distributed along two unit cells, instead of one).
The second STL peak
17

---

## Page 18

Air
Periodic boundary conditions
...
Incident
Transmitted
Water
b
c
Structure/water interface
...
Water
d
a
x
y
i-p
i-d
ux
uy
ux
uy
u
+1
0
-1
ux
ux
ux
uy
ii-p
iii-d
iii-p
ux
uy
ux
uy
iv-d
iv-p
ux
ux
v-d
v-p
vi-d
vi-p
ux
ux
ii-d
ux
uy
u
+1
0
-1
u
+1
0
-1
uy
uy
u
+1
0
-1
uy
uy
u
+1
0
-1
uy
uy
u
+1
0
-1
Fig. 4: Metabarrier STL curves. (a) Redefinition of the unit cell (swapping regions inside the red
and green contours, left to right) to obtain edges without gaps. (b) Sequential arrangement of
unit cells filled with air and submerged into water. The medium is theoretically infinite in the
y-direction, which allows to enforce periodic boundary conditions at the bottom and top edges of
the overall unit cell. The ratio between the power of the transmitted and incident acoustic waves
is then computed to obtain the STL curves. (c) STL curves for an increasing number of unit cells
(N = 1, 2, · · · , 6). The peak (dips) displacement profiles are marked from i-p to vi-p (i-d to vi-d),
shown in a normalized scale with respect to the largest absolute displacement. (d) Summary of
values for STL peaks (left panel) and frequencies (right panel).
presents an attenuation of 31.8 dB at 2.63 kHz. We do not show this displacement profile
since the formation of modes around 2.67 kHz will be discussed ahead. Also, a single dip is
formed between these peaks at 1.47 kHz, displaying a symmetric displacement profile with
respect to the y-axis (ii-d), which has the same type of symmetry displayed by the first STL
18

---

## Page 19

dip with N = 1 (i-d). Thus, it is possible to notice that similar behaviors are observed for
the first peak and first dip for an increasing number of unit cells (N = 1, 2), indicating the
preservation of the behavior of equivalent peaks and dips, however with a significant red-shift
in frequency.
For the case N = 3, three STL peaks are computed with a 23.5, 25.2, and 89.8 dB
attenuation, at the frequencies 0.57, 1.49, and 4.00 kHz, respectively. The first two peaks
(not shown here for the sake of brevity) present a similar behavior to the previously computed
peaks for the cases N = 1 and N = 2, however with a longer wavelength (3 unit cells instead
of 1 or 2). Also, the most notable difference between the first and the second peaks is the
normalized longitudinal displacements, which change from half a wavelength, at the first
peak, to three wavelengths, in the second peak. Interestingly, the third peak, presenting
a much more considerable attenuation, displays a displacement profile similar to a Bragg-
scattering (iii-p), which can be explained due to the frequency range where it occurs (i.e.,
above 2.67 kHz), corresponding to a band gap which is partial with respect to the first
propagative branch (see Fig. 3c). In this case, the dips are located at 1.03 and 1.93 kHz. It
is interesting to notice that the displacement profile associated with the second dip (iii-d)
displays a similar behavior to the wave mode computed at the X-point (see Fig. 3c) at its
center unit cell.
For the remaining considered cases (N = 4, 5, 6) we only report the dips that are closest
to the frequency corresponding to the wave mode at the X-point (2.67 kHz) and the first
peak observed immediately above this frequency. The corresponding dips (iv-d, v-d, and vi-
d, respectively) present similar displacement profiles, with a behavior explained by the wave
mode at the X-point of the first propagative branch (see Fig. 3c). Indeed, for a sufficient
number of unit cells, a vibration mode is expected precisely at the frequency corresponding to
this wave mode, in the case of unit cells with vacuum in their cavities (situation corresponding
to the computed band diagrams). We have verified this by computing the STL curve for
a total of N = 10 unit cells, checking the existence of the last dip at this region at 2.6
kHz. It is also interesting to note that the displacement profiles corresponding to the peaks
(iv-p, v-p, and vi-p, respectively) present similar behaviors to that of the dips, however with
a spatial decay, which suggests a Bragg-scattering behavior considering the first branch of
the dispersion diagram. The existence of the second branch at the same frequency range,
however, impedes the formation of a complete band gap at this direction. We also note here
the STL values and frequencies for the sequential peaks occurring at each case, respectively,
(i) N = 4: 23.2, 22.8, 29.1, and 42.4 dB at 0.44, 1.12, 1.93, and 3.14 kHz; (ii) N = 5: 23.0,
21.4, 26.9, 30.4, and 102.3 dB at 0.37, 0.90, 1.52, 2.20, and 3.17 kHz; and (iii) N = 6: 22.9,
19

---

## Page 20

20.5, 25.5, 27.9, 32.4, and 49.5 dB at 0.31, 0.76, 1.25, 1.81, 2.37, and 3.06 kHz. At each case,
the dips are formed at (i) N = 4: 0.81, 1.42, and 2.31 kHz; (ii) N = 5: 0.67, 1.13, 1.84, and
2.46 kHz; and (iii) N = 6: 0.57, 0.95, 1.53, 2.06, and 2.56 kHz.
We summarize the data concerning the attenuation and frequency of each maxima for the
computed STL curves, respectively, in Figs. 4d and e, for an increasing number of unit cells.
It is interesting to notice that, although for certain cases some peaks present a pronounced
attenuation behavior similar to an anti-resonance (e.g., third peak for N = 3 and fifth
peak for N = 5), the general trend concerning attenuation levels is to present a practically
constant value. On the other hand, for a sufficient number of unit cells, the frequency at
which these peaks occur presents an almost linear behavior starting from the first peak.
At this point, the question may arise whether the STL properties in this type of medium
are only due to the high degree of hybridization observed (p ≈0.5) in the wave modes shown
by the dispersion diagram (Fig. 3c). To verify that this is not the case, we have performed an
additional optimization procedure resulting in a structure with a perfect coupling between
longitudinal and shear motion (p ≈0.5 for all wave vectors in the [0, 5] khz frequency range).
In fact, the STL curves computed for this type of structure (see Appendix F) present smaller
peak values. Thus, this demonstrates that the fundamental aspect that guarantees large STL
values is the mode coupling factor δ.
20

---

## Page 21

3.3. Influence of hydrostatic pressure on the design of the metabarrier
After having presented the underlying physical phenomena responsible that generate sig-
nificant STL in the low-frequency range, we now turn to a practical implementation concern-
ing a fixed number of unit cells. To this end, we proceed with the design of our metabarrier
by choosing a fixed number of unit cells with considerable sub-wavelength thickness as well as
remarkable STL features. We choose N = 3 (see Fig. 4c, middle left panel), whose thickness-
to-wavelength ratio is h/λ ≈1/50 in the operating frequency of 1 kHz, also presenting a
considerable STL (≈90 dB) at 4 kHz.
An immediate concern considering the applicability of the metabarrier is the stress levels
that might arise due to the hydrostatic pressure after its submersion in water. In particular,
prohibitive stress concentrations might occur due to the geometrical variations presented by
the optimized unit cell. To this end, we propose a solution which consists in increasing the
unit cell overall thickness by adding layers of a homogeneous material with thickness hw to
a desired number of unit cells (Fig. 5a), resulting in a total length h = 3a + 2hw.
To determine a suitable value of hw, we perform a quasi-static analysis by imposing a
pressure at the lateral walls of the metabarrier given by p0 = ρwgd, where g = 9.81 m/s2
is the gravitational acceleration and d is the depth in which the structure is submerged.
The bottom and top edges of this unit cell present an anti-symmetric condition (opposing
displacements). A non-linear FE analysis is performed considering large displacements with a
Total Lagrangian formulation [46], since a priori linearity is not guaranteed and geometrical
buckling might occur.
We then evaluate the stress distribution in the structure for the
maximum depth of d = 50 m [47] (i.e., p0 = 0.49 MPa). For the initial case hw = 0 (i.e.,
no additional thickness), the maximum computed von Mises stress is 108.6 MPa (Fig. 5b,
left panel). We then increase the thickness hw until this maximum von Mises stress reaches
a value close to 50% of the material’s tensile strength (55 MPa, no yield strength available
from the manufacturer’s datasheet). We then end up with a final thickness of hw = 1.0 mm
for a maximum von Mises stress of 27.4 MPa (Fig. 5b, right panel). We also verify that
the maximum von Mises stress is indeed highly concentrated, while the overall mean von
Mises stress levels are considerably lower. It is also worth to notice that the maximum lateral
displacements at the left and right edges, computed for the values hw = {0, 0.1, 0.5, 1.0} mm,
are negligible with respect to the unit cell total length, presenting, respectively, the values
0.48, 0.38, 0.22, and 0.03 mm.
Next, we verify the influence of the additional thickness on the STL curves by re-
computing these for increasing values of hw with d = 0 (i.e., only the influence of hw is
assessed at these analyses). In this case, we still consider the y-direction lattice length to
21

---

## Page 22

a
hw=0
hw=1.0 mm
hw
b
c
d
increasing  
stresses
increasing 
thickness
increasing 
thickness
N=3
p0
a
θ
increasing θ
1
2
3
4
5
e
hw
p0
θ
increasing θ
Fig. 5: Effects of hydrostatic pressure on the stress distribution and STL curves. (a) Finite structure
obtained by adding two layers with a thickness hw made of a homogeneous isotropic material to the
previously obtained unit cell configuration, chosen with N = 3. This structure is submerged into
water, undergoing a hydrostatic pressure p0 on its lateral walls. (b) The value of hw is increased
from hw = 0 to hw = 1.0 mm, indicating the decrease of the maximum von Mises stress from 108.6
(top panel) to 27.4 MPa (bottom panel). (c) STL curves for increasing values of hw, indicating a
blueshift (redshift) in the frequency range below (above) 2.7 kHz. This difference in behaviour is
owed to the diverse attenuation formation mechanisms in each frequency range. (d) STL curves for
the case hw = 1.0 mm for increasing depth values d = {0, 10, 20, 30, 40, 50} m, indicating a redshift
in the STL curves due to the development of compressive stresses. (e) STL variation with respect
to increasing incidence angle (θ), showing an improvement in performance in the low-frequency
range and a red-shift of the highest STL peak for increasing incidence angles, followed by a decrease
attenuation.
be equal to a, since the maximum vertical displacements at the bottom and top edges of
the metabarrier unit cell are equal to 94.5, 82.8, 49.9, and 6.2 µm, respectively. The re-
sults, shown in Fig. 5c, show that increasing the lateral thickness hw has a two-fold effect
on the STL curves, which present (i) a blue-shift effect in the region below 2.67 kHz and
(ii) a red-shift effect in the region above 2.67 kHz. This observation is in agreement with
22

---

## Page 23

the previous statement that the formation mechanism for the STL peaks and dips is dif-
ferent for the regions divided by the frequency corresponding to the wave mode formed at
the X-point (see Fig. 3c), namely, Bragg-scattering-like (higher frequencies) and due to the
effective medium properties (lower frequencies). This is also verified by re-computing the
effective constitutive matrix for each case, from which we obtain the values of δ equal to
0.9851, 0.9848, and 0.9847, respectively, for hw equal to 0.1, 0.5, and 1.0 mm. Such decrease
in the value of δ explains both the red-shift and the slight decrease in the STL peaks below
2.67 kHz. At the low-frequency region it is also possible to verify that the behavior of the
cases 0.5 and 1.0 mm are similar, which is explained by their approximate δ value. On the
other hand, the STL curves obtained at higher frequencies present the opposed behavior,
which however cannot be directly correlated to the band diagram presented in Fig. 3c due to
the broken periodicity of the system caused by the introduction of the additional thickness.
We also note that the STL peaks concerning the case hw = 1.0 mm now present the values
23.5, 21.5, and 84.3 dB, respectively, at 0.73, 1.71, and 3.27 kHz.
The last investigation we perform concerning this metabarrier unit cell design is the
influence of the hydrostatic pressure on the STL curves. To this end, we consider the inclusion
of an additional stiffness matrix [42] caused by the stresses induced by hydrostatic pressure.
Figure 5d presents this variation with respect to the values d = {0, 10, 20, 30, 40, 50} m. It is
possible to observe a red-shift effect concerning the whole STL curve. This effect is explained
by the compressive stresses induced in the structure, which cause an overall softening of the
metabarrier, thus decreasing its characteristic frequencies. We note that for the case d = 50
m, the highest peak is shifted down to 2.86 kHz (12.5% reduction with respect to 3.27 kHz
for d = 0), presenting a mild variation in the peak value (smaller than 2.7%).
Finally, the performance of the metabarrier with respect to varying incidence angles is
computed. The results, shown in Fig. 5e, indicate that in the first frequency region (below
2.67 kHz), the STL curves present a mild red-shift, especially at higher frequencies (close
to 2 kHz), however presenting also a significant increase in attenuation for larger incidence
angles (close to 40 dB at θ = 80o). Also, for the second frequency region (above 2.67 kHz),
the STL peak presents a decreased attenuation and a much more significant red-shift effect,
however remaining above 60 dB for all computed cases. Once again, the different behaviors
displayed by the structure when considering these frequency ranges are due to the different
mechanisms that yield attenuation in each case.
23

---

## Page 24

3.4. Finite two-dimensional circular structure
To validate our findings, we now verify the proposed unit cell’s performance in protecting
an underwater region from noise generated by a point source. To this end, we dispose the unit
cell in a circular manner, enclosing a center point C describing a radial distance r in a two-
dimensional square space of length L, as shown in Fig. 6a. An additional perfectly matched
layer (PML) of length ∆L is included to minimize reflections from the system boundaries,
thus approximating an infinite medium in the xy plane. The considered medium is square
due to the chosen PML FE implementation [48].
In order to comply with the curved geometry, the metabarrier unit cell must be slightly
modified with respect to its original (rectangular) design. Hence, we position the left (right)
edge of the unit cell at x = ri (x = re) and its x-centerline aligned with y = 0.
We
then compute the angle α described by C with respect to a pair of points located at the
center of the bottom (y = −a/2) and top edges (y = +a/2) of the unit cell, whose x
coordinate is given by x = (ri + re)/2, as depicted in Fig. 6b. This angle is thus defined as
α = 2 tan−1(a/(ri + re)), yielding a total number of nc = 2π/α, nc ∈N ∗, unit cells in the
angular direction, creating a structure with cyclic symmetry.
Due to fabrication constraints, we set the outer radius of the structure as re = 120 mm.
As the thickness h = 32 mm of the metabarrier is fixed from the previous design, its inner
radius is thus set as ri = re −h = 88 mm. From these quantities, we compute α = 0.0961
rad, leading to a total number of nc = 65.4 unit cells, which cannot be implemented (non-
integer number). We therefore approximate this number to nc = 64 unit cells to ensure a
π/2-rotational symmetry on the metabarrier (to alleviate directional biasing associated with
meshing), thus yielding a corrected angle α = 2π/64 = 0.0982 rad (≈2% deviation). The
initial geometry of the unit cell, described in the (x, y) coordinates, is then mapped into a
polar coordinate system (r, θ) following (x →r, y →θ), thus obtaining the final configuration
(x′ = r cos θ, y′ = r sin θ). The manufactured structure is presented in Fig. 6c.
We then proceed to perform a FE analysis of the resulting metabarrier embedded in
an underwater medium with L = 1000 mm, considering a PML with length ∆L = 250
mm. The structural response of the metabarrier and the pressure distribution in the cavity
(region encircled by the metabarrier) and external domain are computed using the FE model
described in [49]. The pressure distribution in the fluid, p(r, ω), r ∈[re, L/2], is obtained by
imposing a unit acoustic force (representing a monopole source) at the center point C, while
zero Dirichlet boundary conditions are assigned to the outer edges of the PML (required for
numerical accuracy). In this case, standing waves are formed inside the cavity, which does
not allow to separate incident and reflected waves to compute the STL. Instead, we compute
24

---

## Page 25

the insertion loss (IL) associated with the inclusion of the metabarrier as
IL = 20 log

˜p(r, ω)
p(r, ω)
 ,
(16)
where ˜p(r, ω) is the pressure distribution obtained without the metabarrier. These results are
represented in Fig. 6d, where r is taken as directed along the x-axis of the two-dimensional
domain, for simplicity. Also, for the sake of comparison, we overlay the STL curve (in red)
obtained for the rectangular unit cell at a normal incidence angle (see Fig. 5).
These results show that the IL is significantly more influenced by the excitation frequency
ω than by the distance r. Also, although there is an excellent agreement between the IL (col-
ored surface) and the STL curve (red line), two differences can be immediately noticed upon
their comparison, which is illustrated comparing these curves for r = re. First, an overall
blue-shift of the rectangular STL is noticed, being less noticeable for increasing frequencies.
We note, for instance, that the first two dips (with non-zero frequencies) shift from 1.27 to
1.58 kHz and from 2.16 kHz to 2.39 kHz, respectively, representing increases of 24% and 11%
in frequency. A similar behavior is observed for the peaks, which, for the case of the highest
peak, shifts from 3.27 to 3.47 kHz, representing an increase of 6% in frequency. Second, the
zero STL previously computed close to the zero frequency is now lifted, generating a IL of
14.4 dB at 0.01 kHz, with a subsequent dip of 8.7 dB at 0.16 kHz. Finally, we also note a
significant increase in the attenuation for some of the computed STL peaks. The first and
second peaks (previously indicated in Fig. 5c) now present attenuation levels of 36.2 and 28.4
dB, respectively representing increases of 54% and 32%. The third peak has a practically
constant value of 84.0 dB (less than 0.4% reduction).
We also compute the displacement and pressure fields at the frequencies 0.16, 2.39, and
3.47 kHz, corresponding to the first dip, second dip, and third peak, as shown in Fig. 6d,
respectively, using a pink diamond, blue diamond, and green star. Fig. 6e shows the corre-
sponding normalized displacements (top panel) and pressure fields (normalized with respect
to point C, top panel). For the non-zero IL dip (pink diamond), it is possible to notice sig-
nificant displacements at the inner part of the metabarrier, while a mild decrease in pressure
occurs between the cavity and the outer region. For zero-IL dip (blue diamond), absolute
displacements present similar values at the inner and outer faces of the metabarrier, leading
to a negligible acoustic attenuation. On the other hand, for the indicated peak (green star),
absolute displacements are significantly concentrated at the inner face of the metabarrier,
resulting in strong pressure decreases at the outer region.
25

---

## Page 26

f=0.16 kHz
α
x,r
y
a
e
r
Water
PML
L
ΔL
log|p|
-2                    0                    2
b
C
h
a
...
...
x
y z
d
ri
re
c
|u|
0                                         1
f=2.39 kHz
f=3.47 kHz
Fig. 6: (a) Two-dimensional square medium with side length L, where a curved metabarrier, centered
around C, is immersed in water. The radial distance r is measured with respect to C. An additional
PML layer (side length ∆L) is included in the external boundary of the fluid medium. (b) The x-
(y-)coordinates of the initially rectangular unit cell (top panel) are used to generate corresponding
radial r (angular α) coordinates and obtain a section of a circular shape, yielding an internal
radius ri and an external radius re (bottom panel). (c) Manufactured structure with ri = 88 mm
and re = 120 mm. (d) IL computed for an input at point C, varying with respect to the radial
distance r and frequency f. The STL curve obtained for the rectangular unit cell is also shown,
for comparison, in red. Frequencies corresponding to selected dips are marked using pink and blue
diamonds (0.16 and 2.39 kHz, respectively), while a selected peak is marked using a green star
(3.47 kHz). (e) Normalized displacement profiles (top panel) and pressure distribution (bottom
panel) for the frequencies indicated in (d). IL dips are associated with non-zero pressure decreases
in the vicinity of the metabarrier, while IL peaks lead to significant pressure decrease outside the
metabarrier.
26

---

## Page 27

4. Conclusions
In conclusion, we have proposed a strategy to exploit structural anisotropy in the design
of metamaterial-based acoustic barriers yielding efficient underwater noise reduction. Us-
ing our proposed transfer matrix approach, we have calculated the STL curves considering
an anisotropic homogeneous medium immersed in a fluid. The first peak of these curves
presents (i) an increasing maximum value and (ii) a decreasing frequency, as a conveniently
defined mode coupling factor approaches unity. We have also shown that the thickness of
the anisotropic barrier has a lesser influence on the maximum STL value, suggesting that
this can be used to tune the frequency of the STL peaks. This effect is contrary to Bragg-
scattering band gaps, whose efficiency in wave attenuation is proportional to the number of
unit cells (and therefore thickness) of the structure.
These results were then used to propose a topology optimization problem with the ob-
jective of maximizing the mode coupling factor, approaching it to a unit value. The disper-
sion relation obtained using the optimized unit cell indicates a high degree of longitudinal-
transverse polarization, which, however, was demonstrated not to be responsible for increas-
ing maximum STL values.
A partial band gap (with respect to one of the propagative
branches) is also obtained. The STL curves computed for an increasing number of unit
cells immersed in water confirm the previous conclusions regarding the effect of increasing
thickness values on the STL curves. Interestingly, a sub-wavelength behavior is reported for
a single unit cell (thickness-to-wavelength ratio circa 1/70). Furthermore, the effect of the
partial band gap is confirmed, achieving almost 90 dB using three unit cells (30 mm).
The effects of hydrostatic pressure on the configuration of three unit cells require the
inclusion of additional layers of homogeneous material (1 mm each) on each side, which is
sufficient to reduce stress levels by a four-fold. Including these layers leads to (i) a blue-shift of
the STL curves for low frequencies and (ii) a red-shift of the STL curves for higher frequencies,
without, however, degrading STL levels. Likewise, the hydrostatic-induced stresses lead to
a red-shift in STL curves due to their compressive nature. The STL curves also present (i)
increases in peaks for low frequencies and (ii) blue-shifts for higher frequencies for increasing
incidence angles.
Finally, we proposed a convenient transformation for the unit cell, morphing its shape
from a rectangular to a circular design. We have also shown the manufacturability of the
structure for an external radius of 120 mm and thickness 32 mm. The IL curves obtained
for this configuration, considering a monopole source at the center of an unbounded domain,
confirm the previously computed STL curves, lifting the zero-frequency dip and increasing
the attenuation of the STL peaks. Thus, not only the proposed structure seems suitable for
27

---

## Page 28

technological exploitation, but its underlying mechanism of anisotropy (with the associated
rational design) also indicates a fruitful direction for further investigation in acoustics.
CRediT authorship contribution statement
VFDP: Conceptualization, Data curation, Formal analysis, Investigation, Methodology,
Software, Visualization, Writing – original draft. MM: Funding acquisition, Project ad-
ministration, Resources, Supervision, Validation, Writing – review and editing
Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal
relationships that could have appeared to influence the work reported in this paper.
Acknowledgements
VFDP and MM are supported by the European Union’s Horizon Europe programme in
the framework of the ERC StG POSEIDON under Grant Agreement No. 101039576.
28

---

## Page 29

References
[1] C. M. Duarte, L. Chapuis, S. P. Collin, D. P. Costa, R. P. Devassy, V. M. Eguiluz,
C. Erbe, T. A. C. Gordon, B. S. Halpern, H. R. Harding, M. N. Havlik, M. Meekan, N. D.
Merchant, J. L. Miksis-Olds, M. Parsons, M. Predragovic, A. N. Radford, C. A. Radford,
S. D. Simpson, H. Slabbekoorn, E. Staaterman, I. C. Van Opzeeland, J. Winderen,
X. Zhang, F. Juanes, The soundscape of the Anthropocene ocean, Science 371 (6529)
(2021) eaba4658.
[2] N. R. Council, D. on Earth, L. Studies, O. S. Board, C. on Potential Impacts of Ambient
Noise in the Ocean on Marine Mammals, Ocean Noise and Marine Mammals, National
Academies Press, 2003.
URL https://books.google.fr/books?id=OlupYZ1F3_oC
[3] D. Ross, Mechanics of underwater noise, Elsevier, 2013.
[4] E. Dong, P. Cao, J. Zhang, S. Zhang, N. X. Fang, Y. Zhang, Underwater acoustic
metamaterials, National Science Review 10 (6) (2023) nwac246.
[5] J. Dong, P. Tian, Review of underwater sound absorption materials, IOP Conference
Series: Earth and Environmental Science 508 (1) (2020) 012182.
[6] S. Qu, N. Gao, A. Tinel, B. Morvan, V. Romero-García, J.-P. Groby, P. Sheng, Un-
derwater metamaterial absorber with impedance-matched composite, Science Advances
8 (20) (2022) eabm4206.
[7] N. Gao, Z. Zhang, J. Deng, X. Guo, B. Cheng, H. Hou, Acoustic metamaterials for
noise reduction: a review, Advanced Materials Technologies 7 (6) (2022) 2100698.
[8] C. Croënne, J. O. Vasseur, L. Roux, C. Audoly, A.-C. Hladky, A review of acoustic
metamaterials for naval and underwater defense applications: from historical concepts
to new trends, Acta Acustica 9 (2025) 24.
[9] W. Kuhl, Sound Absorption and Sound Absorbers in Water. (Dynamic Properties of
Rubber and Rubberlike Substances in the Acoustic Frequency Region), Department of
the Navy, Bureau of Ships, 1950.
[10] A.-C. Hladky-Hennion, J.-N. Decarpigny, Analysis of the scattering of a plane acoustic
wave by a doubly periodic structure using the finite element method: Application to
29

---

## Page 30

alberich anechoic coatings, The Journal of the Acoustical Society of America 90 (6)
(1991) 3356–3367.
[11] Y. Fu, I. I. Kabir, G. H. Yeoh, Z. Peng, A review on polymer-based materials for
underwater sound absorption, Polymer Testing 96 (2021) 107115.
[12] C. Lin, G. S. Sharma, D. Eggler, L. Maxit, A. Skvortsov, I. MacGillivray, N. Kessis-
soglou, Sound radiation from a cylindrical shell with a multilayered resonant coating,
International Journal of Mechanical Sciences 232 (2022) 107479.
[13] S. M. Ivansson, Numerical design of alberich anechoic coatings with superellipsoidal
cavities of mixed sizes, The Journal of the Acoustical Society of America 124 (4) (2008)
1974–1984.
[14] V. Romero-García, N. Jimenez, G. Theocharis, V. Achilleos, A. Merkel, O. Richoux,
V. Tournat, J.-P. Groby, V. Pagneux, Design of acoustic metamaterials made of
Helmholtz resonators for perfect absorption by using the complex frequency plane,
Comptes Rendus. Physique 21 (7-8) (2020) 713–749.
[15] M. Duan, C. Yu, F. Xin, T. J. Lu, Tunable underwater acoustic metamaterials via
quasi-Helmholtz resonance: From low-frequency to ultra-broadband, Applied Physics
Letters 118 (7) (2021).
[16] M. Duan, C. Yu, F. Xin, T. J. Lu, Deep subwavelength hybrid metamaterial for low-
frequency underwater sound absorption by quasi-helmholtz resonance, AIP Advances
13 (2) (2023).
[17] Y. Zhang, J. Pan, K. Chen, J. Zhong, Subwavelength and quasi-perfect underwater
sound absorber for multiple and broad frequency bands, The Journal of the Acoustical
Society of America 144 (2) (2018) 648–659.
[18] H. Zhao, J. Wen, H. Yang, L. Lv, X. Wen, Backing effects on the underwater acoustic
absorption of a viscoelastic slab with locally resonant scatterers, Applied Acoustics 76
(2014) 48–51.
[19] K.-H. Elmer, J. Savery, New hydro sound dampers to reduce piling underwater noise,
INTER-NOISE and NOISE-CON Congress and Conference Proceedings 249 (2) (2014)
5551–5560.
30

---

## Page 31

[20] J. Elzinga, A. Mesu, E. van Eekelen, M. Wochner, E. Jansen, M. Nijhof, Installing
offshore wind turbine foundations quieter: A performance overview of the first full-
scale demonstration of the AdBm underwater noise abatement system, in: Offshore
Technology Conference, OTC, 2019, p. D021S019R003.
[21] Y. Peng, A. Tsouvalas, A. Metrikine, E. Belderbos, Modelling and development of a
resonator-based noise mitigation system for offshore pile driving, in: Proceedings of the
25th International Congress on Sound and Vibration, 2018.
[22] M. Wochner, K. Lee, A. McNeese, P. Wilson, Underwater noise mitigation from pile
driving using a tuneable resonator system, in: Proc. 22nd International Congress on
Acoustics ICA, Buenos Aires, Argentina, 2016.
[23] S. Su, S. Wu, Finite element analysis of acoustic performance of water-filled Helmholtz
resonator with the effect of elastic cavity walls, Journal of Physics: Conference Series
2458 (1) (2023) 012017.
[24] K. Lucke, P. A. Lepper, M.-A. Blanchet, U. Siebert, The use of an air bubble curtain to
reduce the received sound levels for harbor porpoises (phocoena phocoena), The Journal
of the Acoustical Society of America 130 (5) (2011) 3406–3412.
[25] B. Würsig, C. Greene Jr, T. Jefferson, Development of an air bubble curtain to reduce
underwater noise of percussive piling, Marine environmental research 49 (1) (2000) 79–
93.
[26] A. Tsouvalas, Underwater noise emission due to offshore pile installation: A review,
Energies 13 (12) (2020) 3037.
[27] T. Brunet, A. Merlin, B. Mascaro, K. Zimny, J. Leng, O. Poncelet, C. Aristégui,
O. Mondain-Monval, Soft 3d acoustic metamaterial with negative index, Nature ma-
terials 14 (4) (2015) 384–388.
[28] B. Tallon, A. Kovalenko, O. Poncelet, C. Aristégui, O. Mondain-Monval, T. Brunet,
Experimental demonstration of negative refraction with 3d locally resonant acoustic
metafluids, Scientific Reports 11 (1) (2021) 4627.
[29] J. Pierre, B. Dollet, V. Leroy, Resonant acoustic propagation and negative density in
liquid foams, Physical review letters 112 (14) (2014) 148307.
31

---

## Page 32

[30] J. Pierre, C. Gaulon, C. Derec, F. Elias, V. Leroy, Investigating the origin of acoustic
attenuation in liquid foams, The European Physical Journal E 40 (2017) 1–11.
[31] H. Jansen, C. de Jong, B. Jung, Experimental assessment of the insertion loss of an
underwater noise mitigation screen for marine pile driving, in: Proceedings of the 11th
European Conference on Underwater Acoustics-ECUA 2012, 2-6 July 2012, Edinburgh,
UK, 2012.
[32] S. Koschinski, K. Lüdemann, Development of noise mitigation measures in offshore
wind farm construction, Commissioned by the Federal Agency for Nature Conservation
(2013) 1–102.
[33] Y. Wang, H. Zhao, H. Yang, J. Liu, D. Yu, J. Wen, Topological design of lattice mate-
rials with application to underwater sound insulation, Mechanical Systems and Signal
Processing 171 (2022) 108911.
[34] Y. Chen, B. Zhao, X. Liu, G. Hu, Highly anisotropic hexagonal lattice material for low
frequency water sound insulation, Extreme Mechanics Letters 40 (2020) 100916.
[35] Y. Wang, H. Zhao, H. Yang, H. Zhang, T. Li, C. Wang, J. Liu, J. Zhong, D. Yu, J. Wen,
Acoustically soft and mechanically robust hierarchical metamaterials in water, Physical
Review Applied 20 (5) (2023) 054015.
[36] C. Wang, H. Zhao, Y. Wang, J. Zhong, D. Yu, J. Wen, Topology optimization of chiral
metamaterials with application to underwater sound insulation, Applied Mathematics
and Mechanics 45 (7) (2024) 1119–1138.
[37] W. M. Lai, D. Rubin, E. Krempl, Introduction to Continuum Mechanics, Butterworth-
Heinemann, 2009.
[38] N. Jiménez, O. Umnova, J.-P. Groby, Acoustic waves in periodic structures, metamate-
rials, and porous media, Springer, 2021.
[39] M. Oudich, X. Zhou, M. Badreddine Assouar, General analytical approach for sound
transmission loss analysis through a thick metamaterial plate, Journal of Applied
Physics 116 (19) (2014).
[40] L. Kinsler, A. Frey, A. Coppens, J. Sanders, Fundamentals of Acoustics, Wiley, 2000.
URL https://books.google.fr/books?id=FecSEAAAQBAJ
32

---

## Page 33

[41] J. M. Kweun, H. J. Lee, J. H. Oh, H. M. Seung, Y. Y. Kim, Transmodal Fabry-Pérot
resonance: theory and realization with elastic metamaterials, Physical review letters
118 (20) (2017) 205901.
[42] R. D. Cook, Concepts and applications of finite element analysis, John Wiley & Sons,
2007.
[43] J. Pinho-da Cruz, J. Oliveira, F. Teixeira-Dias, Asymptotic homogenisation in linear
elasticity. part i: Mathematical formulation and finite element modelling, Computa-
tional Materials Science 45 (4) (2009) 1073–1080.
[44] D. Goldberg, Genetic Algorithms, Pearson Education India, 2013.
URL https://books.google.fr/books?id=6gzS07Sv9hoC
[45] B. R. Mace, E. Manconi, Modelling wave propagation in two-dimensional structures
using finite element analysis, Journal of Sound and Vibration 318 (4-5) (2008) 884–902.
[46] K.-J. Bathe, Finite element procedures, Klaus-Jurgen Bathe, 2006.
[47] A. C. A. Vasconcelos, S. V. Valappil, D. Schott, J. Jovanova, A. M. Aragón, A
metamaterial-based interface for the structural resonance shielding of impact-driven
offshore monopiles, Engineering Structures 300 (2024) 117261.
[48] A. Bermúdez,
L. Hervella-Nieto,
A. Prieto,
R. Rodrıguez,
An optimal finite-
element/PML method for the simulation of acoustic wave propagation phenomena,
Variational Formulations in Mechanics: Theory and Applications,(January) (2006).
[49] J.-M. Mencik, M. Ichchou, Wave finite elements in guided elastodynamics with internal
fluid, International Journal of Solids and Structures 44 (7-8) (2007) 2148–2167.
[50] W. S. Slaughter, The linearized theory of elasticity, Springer Science & Business Media,
2012.
[51] F. Bloch, Über die Quantenmechanik der Elektronen in Kristallgittern, Zeitschrift für
Physik 52 (7-8) (1929) 555–600.
[52] Y. Yang, B. R. Mace, M. J. Kingan, Prediction of sound transmission through, and
radiation from, panels using a wave and finite element method, The Journal of the
Acoustical Society of America 141 (4) (2017) 2452–2460.
33

---

## Page 34

Appendix A. Constitutive equations in a general anisotropic two-dimensional
medium
The terms of the constitutive matrix can be expressed with respect to general coordinates
x′y′z, rotated with respect to the original xyz coordinates by an angle β around the z-axis
using the relation
C′ = TTCT ,
(A.1)
where T is a coordinate transformation matrix, expressed by [42]
T =


cos2 β
sin2 β
sin β cos β
sin2 β
cos2 β
−sin β cos β
−2 sin β cos β
2 sin β cos β
cos2 β −sin2 β

.
(A.2)
In the case of an isotropic two-dimensional medium, C13 = C31 = C23 = C32 = 0, and
the ratio between the remaining constants is such that C′
13 = C′
31 = C′
23 = C′
32 = 0, as well,
for any angle β. On the other hand, anisotropic media may present C13 = C31̸ = 0 and
C23 = C32̸ = 0, thus evidencing the coupling between normal stresses and shear strains (and
vice-versa).
Appendix B. Wave propagation in a homogeneous anisotropic medium
The equations of motion for a two-dimensional medium free of external forces can be
written in tensor notation as [50]
σji,j = ρ¨ui ,
(B.1)
where the partial derivatives with respect to the spatial coordinate j and time coordinate t
are denoted, respectively, as (◦),j = ∂(◦)
∂j and (¨◦) = ∂2(◦)
∂t2 , and ρ is the material specific mass
density.
Equations (1) and (B.1) can be combined and rewritten by considering an infinitesimal
strain tensor (εkl = εlk = 1
2(uk,l + ul,k)), yielding
Cxu,xx + Cxyu,xy + Cyu,yy = ρ¨u,
(B.2)
where the matrix and vector components are described as
Cx =
"
C11
C13
C31
C33
#
, Cxy =
"
C13 + C31
C12 + C33
C21 + C33
C23 + C32
#
, Cy =
"
C33
C32
C23
C22
#
, u =
(
ux
uy
)
.
(B.3)
34

---

## Page 35

Consider now a Bloch solution for the displacements in the form [51]
u(r, t) = Ue−iωteik·r,
(B.4)
where U = {Ux, Uy}T is a wave mode, ω is the circular frequency, k = {kx, ky}T is the
two-dimensional wave vector, and r = {x, y}T is the two-dimensional coordinate vector.
Substituting Eq. (B.4) in (B.2) yields
(k2
xCx + kxkyCxy + k2
yCy −ω2ρI)U = 0 ,
(B.5)
where I a order-2 identity matrix.
The previous equation can be solved as a quadratic
eigenvalue problem for kx (ky) for a specified value of ky (kx). Rewriting the wavenum-
ber components kx = k cos θ and ky = k sin θ, for a given wavenumber k and propagation
direction θ, leads to the eigenproblem
(k2D −ω2ρI)U = 0 ,
(B.6)
where D = D(C, θ) = Cx cos2 θ + Cxy sin θ cos θ + Cy sin2 θ is a direction-dependent stiffness
matrix. By considering the symmetry of the constitutive matrix, the terms of D can be
written as
D11 = C11 cos2 θ + C13 sin 2θ + C33 sin2 θ ,
D12 = D21 = C13 cos2 +C12 + C33
2
sin 2θ + C23 sin2 θ ,
D22 = C33 cos2 +C23 sin 2θ + C22 sin2 θ .
(B.7)
The dispersion relation k = k(ω) in a homogeneous anisotropic medium can then be
obtained for a given propagation direction θ by computing the determinant of Eq. (B.6).
Considering a non-singular determinant of matrix D (i.e., D11D12 −D12D21̸ = 0) yields
two pairs of non-dispersive solutions k(ω) = ±k1(ω) = ±ω/c1(ω) and k(ω) = ±k2(ω) =
±ω/c2(ω), where the wave speeds c1,2 are given by
c1,2(C, θ) =
s
1
ρ
2(D11D22 −D12D21)
(D11 + D22) ±
p
(D11 −D22)2 + 4D12D21
,
(B.8)
and the subscript 1 (2) refers to the solution containing the + (−) sign.
This pair of wavenumbers (k1, k2) can be substituted back into Eq. (B.6) to obtain the
35

---

## Page 36

normalized mode shapes Ui = {cos ϕi, sin ϕi}T, i = {1, 2}, related by
Uy
Ux

1,2
= tan ϕ1,2 = D11[(D11 + D22) ±
p
(D11 −D22)2 + 4D12D21)] −2(D11D22 −D12D21)
−D12[(D11 + D22) ±
p
(D11 −D22)2 + 4D12D21]
.
(B.9)
For the simplified case of a four-fold symmetric unit cell (i.e., with respect to both x and
y axes), one has C13 = C31 = 0; considering waves propagating in the x-direction (θ = 0),
the well-know solutions kl(ω) = ω
p
ρ/C11 and ks(ω) = ω
p
ρ/C33 for longitudinal and shear
waves, respectively, are retrieved. The corresponding wave modes, described as Ul = {1, 0}T
and Us = {0, 1}T, indicate a full decoupling between the corresponding motions.
This
simplification is no longer valid for θ = 0 whenever C13̸ = 0.
Appendix C. Derivation of transfer matrix method
The shear stresses τxy in the metabarrier can be written combining Eqs. (1)–(2) as
τxy(x) = ˆu1pCϕ1
z ik1eik1x −ˆu1nCϕ1
z ik1e−ik1x + ˆu2pCϕ2
z ik2eik2x −ˆu2nCϕ2
z ik2e−ik2x ,
(C.1)
where Cϕ
z = C31 cos ϕ + C33 sin ϕ, with ϕi = ∠Ui. Time dependencies, including the e−iωt
terms, are henceforth omitted for the sake of brevity.
At the fluid-structure interfaces between metabarrier and surrounding fluid, shear stresses
vanish [39], i.e.,
τxy(x = 0) = 0, τxy(x = h) = 0,
(C.2)
which can be substituted into the previous equation, leading to
"
Cϕ1
z k1
Cϕ2
z k2
Cϕ1
z k1eik1h
Cϕ2
z k2eik2h
# (
ˆu1p
ˆu2p
)
−
"
Cϕ1
z k1
Cϕ2
z k2
Cϕ1
z k1e−ik1h
Cϕ2
z k2e−ik2h
# (
ˆu1n
ˆu2n
)
= 0 , (C.3)
thus allowing to obtain a relation between the complex amplitudes of negative- and positive-
going waves as
(
ˆu1n
ˆu2n
)
=
"
∆11
∆12
∆21
∆22
# (
ˆu1p
ˆu2p
)
,
(C.4)
where
∆11 = e−ik2h −eik1h
e−ik2h −e−ik1h , ∆12 = Cϕ2
z k2
Cϕ1
z k1
e−ik2h −eik2h
e−ik2h −e−ik1h ,
∆21 = Cϕ1
z k1
Cϕ2
z k2
e−ik1h −eik1h
e−ik2h −e−ik1h , ∆22 = eik2h −e−ik1h
e−ik2h −e−ik1h .
(C.5)
36

---

## Page 37

Next, we apply a similar procedure considering normal stresses, which can be written as
σx(x) = ˆu1pCϕ1
x ik1eik1x −ˆu1nCϕ1
x ik1e−ik1x + ˆu2pCϕ2
x ik2eik2x −ˆu2nCϕ2
x ik2e−ik2x,
(C.6)
where Cϕ
x = C11 cos ϕ + C13 sin ϕ and the time dependence is once again omitted.
A state vector containing the x-direction displacement (ux) and normal stress (σx) can
now be evaluated in the x-coordinate as
(
ux
σx
)
x
=
"
cos ϕ1eik1x
cos ϕ1e−ik1x
cos ϕ2eik2x
cos ϕ2e−ik2x
Cϕ1
x ik1eik1x
−Cϕ1
x ik1e−ik1x
Cϕ2
x ik2eik2x
−Cϕ2
x ik2e−ik2x
#











ˆu1p
ˆu1n
ˆu2p
ˆu2n











, (C.7)
which can be combined with Eq. (C.4) to express the state vector as
(
ux
σx
)
x
= M(x)
(
ˆu1p
ˆu2p
)
,
(C.8)
where
M(x) =
"
cos ϕ1eik1x
cos ϕ1e−ik1x
cos ϕ2eik2x
cos ϕ2e−ik2x
Cϕ1
x ik1eik1x
−Cϕ1
x ik1e−ik1x
Cϕ2
x ik2eik2x
−Cϕ2
x ik2e−ik2x
#


1
0
∆11
∆12
0
1
∆21
∆22


.
(C.9)
Combining {ux, σx}T
x=h = M(x = h){ˆu1p, ˆu2p}T and {ux, σx}T
x=0 = M(x = 0){ˆu1p, ˆu2p}T
allows to relate the displacements and stresses at the edges of the metabarrier as
(
ux
σx
)
x=h
= T(s)
(
ux
σx
)
x=0
=
"
T (s)
11
T (s)
12
T (s)
21
T (s)
22
# (
ux
σx
)
x=0
,
(C.10)
where T(s) = M(x = h)M−1(x = 0) represents a real-valued structural transfer matrix.
Also, T (s)
11 = T (s)
22 and det(T(s)) = T (s)
11 T (s)
22 −T (s)
12 T (s)
21 = 1 due to the reciprocity between both
propagation directions. The complete expression of the terms in matrix T(s) is too long to
be conveniently expressed, in which case, a numerical solution is preferred. We now proceed
to the coupling between the structure and surrounding fluid.
The coupling between the solid metabarrier and the surrounding fluid can be considered
by ensuring acceleration and stress continuity conditions at both edges of the metabarrier.
37

---

## Page 38

The continuity of accelerations can be stated as [39]
(Pi + Pr),x

x=0 = ρ0ω2ux

x=0,
(Pt + Pi′),x

x=h = ρ0ω2ux

x=h,
(C.11)
and the continuity of stresses at the interface can be written as
−(Pi + Pr)

x=0 = σx|x=0,
−(Pt + Pi′)

x=h = σx|x=h.
(C.12)
Combining Eqs. (8)–(C.12) yields
"
ik0
ρ0ω2
−ik0
ρ0ω2
−1
−1
#
P =
(
ux
σx
)
,
(C.13)
where P = { ˆPi, ˆPr}T for {ux, σx}T
x=0 and P = { ˆPt, ˆPi′}T for {ux, σx}x=h.
Combining
Eqs. (C.10) and (C.13) leads to
( ˆPt
ˆPi′
)
= T(a)
( ˆPi
ˆPr
)
=
"
T (a)
11
T (a)
12
T (a)
21
T (a)
22
# ( ˆPi
ˆPr
)
,
(C.14)
where the terms of the acoustic transfer matrix T(a) are given by
T (a)
11 = T (s)
11 + i
2

−
k0
ρ0ω2T (s)
21 + ρ0ω2
k0
T (s)
12

, T (a)
12 = i
2
 k0
ρ0ω2T (s)
21 + ρ0ω2
k0
T (s)
12

,
T (a)
21 = −i
2
 k0
ρ0ω2T (s)
21 + ρ0ω2
k0
T (s)
12

, T (a)
22 = T (s)
22 + i
2
 k0
ρ0ω2T (s)
21 −ρ0ω2
k0
T (s)
12
 (C.15)
and det(T(a)) = T (a)
11 T (a)
22 −T (a)
12 T (a)
21 = 1 due to the reciprocity of the system.
Appendix D. Sound transmission loss computation with finite elements
The formulation presented in this section is derived from [52]. The computational ap-
proach for the computation of the STL considering a fluid-filled structure is illustrated in
Fig. D.1, whose FE discretization is shown for illustration purposes. The solid region is
indicated by gray elements, while fluid-filled cavities are indicated in blue.
The incident (Pi), reflected (Pr), transmitted acoustic wave (Pt), and FE displacements
38

---

## Page 39

Pi(x,t)
Pr(x,t)
Pt(x,t)
θ
θ
θ
t
b
l
r
i
Fig. D.1: Metabarrier STL behaviour under oblique incidence angles and a diffuse field.
(uq, q = {x, y}) are described as
Pi(x, y, t) = e−iωt X
Gy
ˆPi(Gy)eik(0)
x xei(k(0)
y +Gy)y ,
Pr(x, y, t) = e−iωt X
Gy
ˆPr(Gy)e−ikxa(Gy)xei(k(0)
y +Gy)y ,
Pt(x, y, t) = e−iωt X
Gy
ˆPt(Gy)e+ikxa(Gy)(x−h)ei(k(0)
y +Gy)y ,
uq = e−iωt X
Gy
ˆuq(Gy)ei(k(0)
y +Gy)y ,
(D.1)
where Gy = n(2π/a), n ∈Z, is the reciprocal wavenumber in the y-direction for a lattice
of length a, ˆp(Gy) is the spatial Fourier component corresponding to the quantity p (Pi, Pr,
Pt, or uq), k(0)
x
and k(0)
y
refer to the wavenumbers in the x- and y-directions in the fluid,
computed as k(0)
x
= k0 cos θ and ky = k0 sin θ, where k0 = ω/c0 is the acoustic wavenumber
for a sound speed value of c0, and kxa(Gy) is computed such that k2
xa(Gy) + (ky + Gy)2 = k2
0.
The shift (x −h) in the exponential term of the transmitted wave is denoted for analytical
convenience.
The continuity of accelerations (see Eq. (C.11)) at the incident face (index l in Fig. D.1)
leads to
ˆPr(Gy) =
k(0)
x
kxa(Gy)
ˆPi(Gy) + i ρeω2
kxa(Gy) ˆu(l)
x (Gy) ,
(D.2)
where ρe is the specific mass density of the surrounding fluid (outside the finite structure),
and the superscript (l) refers to nodes at the incident face (left) of the metabarrier.
Analogously, at the transmitted face, one obtains
ˆPt(Gy) = −i ρeω2
kxa(Gy) ˆu(r)
x (Gy) ,
(D.3)
39

---

## Page 40

where the superscript (r) refers to nodes at the transmitted face (right) of the metabarrier.
The pressure produced at the input (left) and output (right) faces of the structure can
be written, using Eqs. (D.1)–(D.3), respectively as
Pin = Pi(x = 0) + Pr(x = 0) =
X
Gy

1 +
k(0)
x
kxa(Gy)

ˆPi(Gy) + i ρeω2
kxa(Gy) ˆu(l)
x (Gy)

ei(k(0)
y +Gy)y ,
Pout = −Pt(x = h) =
X
Gy

i ρeω2
kxa(Gy) ˆu(r)
x (Gy)

ei(k(0)
y +Gy)y ,
(D.4)
where the time dependence is henceforth omitted for the sake of brevity.
The consistent nodal forces produced by the incident, reflected, and transmitted pressure
waves, can then be computed as
F =
X
Sl
Z
Ω
NT
x Pin dΩ+
X
Sr
Z
Ω
NT
x Pout dΩ,
(D.5)
where P
Sl and P
Sr refer to the FE assembly process performed over the left and right
edges of the periodic domain, and Nx is a matrix containing the x-direction interpolation
shape functions for the plane elements. Combining Eqs. (D.4) and (D.5) and recalling that
ˆPi(Gy) = 0 for Gy̸ = 0 (case of a single incident plane wave) leads to
F =
 X
Sl
Z
Ω
2NT
x eik(0)
y y dΩ

ˆPi(Gy = 0) +
X
Gy
X
Sl
i ρeω2
kxa(Gy)
Z
Ω
NT
x ˆu(l)
x (Gy)ei(k(0)
y +Gy)ydΩ
+
X
Gy
X
Sr
i ρeω2
kxa(Gy)
Z
Ω
NT
x ˆu(r)
x (Gy)ei(k(0)
y +Gy)ydΩ.
(D.6)
In the previous equation, the first term corresponds to the immediate force exerted by
the incident acoustic wave, while the second and third terms account for the additional
fluid loading due to the reflected and transmitted acoustic waves, respectively. Particular
attention is given to these terms due to integrals performed over the input and ouptut (left
and right, respectively) domains.
The spatial Fourier components of the x-direction displacements (ˆux(Gy)) can be com-
puted by applying the orthogonality property in the last equation presented in Eq. (D.1) to
obtain
ˆux(Gy) = 1
a
Z
Ω
ux e−i(k(0)
y +Gy)y dΩ,
(D.7)
where Ωis a edge of the unit cell (e.g., left, right). This equation can be rearranged consid-
40

---

## Page 41

ering a FE-interpolation in the form
ux = Nxu ,
(D.8)
where Nx is a matrix containing the x-direction interpolation shape functions and u is a
vector containing the nodal displacements corresponding to the spatial Fourier coefficients.
Thus, the previous equation can be rewritten as
ˆux(Gy) = 1
aB(Gy)u ,
(D.9)
where B(Gy) is a matrix relating nodal displacements and spatial Fourier components, given
by
B(Gy) =
X
S
Z
Ω
Nxe−i(k(0)
y +Gy)y dΩ,
(D.10)
with P
S representing the assembly process considering the edge of the elements at a given
face S. This expression can be substituted into Eq. (D.6), which allows it to be rewritten as
F = Fp + ω2(Min
f + Mout
f )u ,
(D.11)
where Fp =
  P
Sl
R
Ω2NT
x eik(0)
y y dΩ
 ˆPi(Gy = 0) and the fluid-loading associated matrices writ-
ten as Min
f = iρe
a
P
Gy
1
kxa(Gy)BH
in(Gy)Bin(Gy) and Mout
f
= iρe
a
P
Gy
1
kxa(Gy)BH
in(Gy)Bout(Gy),
with the matrices Bin(Gy) and Bout(Gy) evaluated, respectively, at the incident (left, S = Sl)
and transmitted (right, S = Sr) faces.
The next step to obtain the STL curves is now considering a periodic medium in the
y-direction. Notice that the structure may contain fluid-filled acoustic cavities (blue regions
in Fig. D.1), in which case, its dynamic stiffness matrices can be written partitioned as [49]
"
Ks −ω2Ms
iωρiC
iωρiCT
−ρi(Ka −ω2Ma)
# (
u
ψ
)
=
(
Fs
1
iωFa
)
(D.12)
Appendix E. Comparison between results
Figure E.2 compares the STL curves computed considering different methods and the
existence of air-filled cavities in the metabarrier unit cell. Fig. E.2a shows the STL curves
computed using the analytical method for homogenized structures (Section 2.2) and numer-
ical FE-based method for architected structures (Appendix D). It is possible to notice that
the agreement between both methods is improved as the number of unit cells (N) increases,
41

---

## Page 42

extending the frequency range of agreement between these methods. This observation is in
agreement with the hypothesis considered in the homogenization method, which assumes a
periodic medium of infinite extent (i.e., the boundary effects, which are more significant for
a small number of unit cells, are not considered). Also, we show in Fig. E.2b the differences
in the computed STL curves considering vacumm- (void) and air-filled internal cavities of
the unit cells of the metabarrier. Notice that in both cases, the external fluid is water. The
effect of the inclusion of air in the internal cavities is the redshift of the STL curve, although
not significantly.
a
b
Fig. E.2: Comparison between STL curves obtained using (a) analytical and FE-based methods
and (b) FE-based methods without (void) and with air in the internal cavities of the metabarrier
unit cell.
Appendix F. Optimization results for alternative objective function
An alternative optimization approach is proposed to verify that the effect of achieving
high STL values is not owed only to the high degree of polarization between longitudinal and
transverse modes (i.e., p ≈0.5). In this case, the chosen objective function (see Eq. (15)) to
be minimized was chosen as φ(q) = max(cos2(ϕ1), cos2(ϕ2)). Thus, the optimization algo-
rithm seeks to bring both ϕ1 and ϕ2 as close as possible to 0, i.e., keeping only shear modes.
As this would not be a feasible solution, the algorithm yields a structure with ϕ1,2 = ±3π/4,
i.e., perfectly polarized (p = 0.5) modes. The resulting structure obtained through the topo-
logical optimization is shown in Fig. F.3a (inset) with the corresponding dispersion relation,
which confirms the almost ideal degree of polarization (p ≈0.5). Conversely, the STL curves
considering a strucutre with effective properties (obtained through the homogenization pro-
cedure), shown in Fig. F.3b for an increasing number of unit cells (N), indicate that the
42

---

## Page 43

peak STL levels are close to 15 dB. This value is significantly lower than the ones observed in
Fig. 4c. This difference can be explained due to the lower value of coupling between normal
stresses and shear strains (and vice-versa), given in this case by δ = 0.9208.
a
b
Fig. F.3: Results for the optimized structure obtained using an alternative objective function.
(a) Band diagram relative to the obtained structure (inset) showing almost ideally hybridized
longitudinal and shear polarization (p ≈0.5).
(b) STL curves obtained for the homogeneous
structure with effective properties for an increasing number of unit cells (N).
43