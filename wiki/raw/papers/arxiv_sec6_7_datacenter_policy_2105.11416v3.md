# Remunerating Space-Time, Load-Shifting Flexibility from Data Centers in Electricity Markets
**arXiv ID:** 2105.11416v3
**Source File:** arxiv_sec6_7_datacenter_policy_2105.11416v3.pdf

## Page 1

Remunerating Space-Time, Load-Shifting Flexibility
from Data Centers in Electricity Markets
Weiqi Zhang‡ and Victor M. Zavala‡*
‡Department of Chemical and Biological Engineering
University of Wisconsin-Madison, 1415 Engineering Dr, Madison, WI 53706, USA
Abstract
We study an electricity market clearing formulation that seeks to remunerate spatio-temporal,
load-shifting ﬂexibility provided by data centers (DaCes). Load-shifting ﬂexibility is a key asset for
power grid operators as they aim to integrate larger amounts of intermittent renewable power and
to decarbonize the grid. Central to our study is the concept of virtual links, which provide non-
physical pathways that can be used by DaCes to shift power loads (by shifting computing loads)
across space and time. We use virtual links to show that the clearing formulation treats DaCes
as prosumers that simultaneously request load and provide a load-shifting ﬂexibility service. Our
analysis also reveals that DaCes are remunerated for the provision of load-shifting ﬂexibility based
on nodal price differences (across space and time). We also show that DaCe ﬂexibility helps relieve
space-time price volatility and show that the clearing formulation satisﬁes fundamental economic
properties that are expected from coordinated markets (e.g., provides a competitive equilibrium
and achieves revenue adequacy and cost recovery). The concepts presented are applicable to other
key market players that can offer space-time shifting ﬂexibility such as distributed manufacturing
facilities and storage systems. Case studies are presented to demonstrate these properties.
Keywords: market clearing; virtual links; electricity; pricing; ﬂexibility; space-time
1
Introduction
The power grid is undergoing major structural changes due to the adoption of large amounts of
renewable power and the need to decarbonize operations. Multiple U.S. states have set ambitious re-
newable portfolio standards (RPS) that dictate the required level of renewable energy use in the near
future, including California (50% by 2030 according to California Public Utilities Commission 2019),
Minnesota and New York (around 25% by 2025 and 70 % by 2030 according to National Conference of
State Legislatures 2019). A critical challenge that emerges here is the unsteady, non-dispatchable, and
spatio-temporal nature of renewable power. Enabling high penetration of renewable power requires
new sources of load-shifting ﬂexibility (Wierman et al. 2017). Flexibility is a key asset in power system
operations that is often harnessed from consumers via demand response and price signals (Aghaei
and Alizadeh 2013).
*Corresponding Author: victor.zavala@wisc.edu
1
arXiv:2105.11416v3  [eess.SY]  16 Aug 2021

---

## Page 2

http://zavalab.engr.wisc.edu
Rapid expansion of the computing industry also poses signiﬁcant challenges to the power grid.
Power use from the information technology (IT) sector is experiencing fast growth (8% in 2016 and
projected at 13% in 2027) and the dynamics and spatial distribution of data centers (DaCes) now
represents a signiﬁcant demand on the grid. In addition, the computing infrastructure is undergo-
ing structural changes; speciﬁcally, motivated by economies of scale, large companies (e.g., Amazon,
Google, Alibaba, and Tencent) are centralizing DaCes. These DaCes form a computing infrastruc-
ture that is managed collectively via network operation centers (NOCs). NOCs have the ability to
shift computing loads/jobs (and associated power loads) across time (via job scheduling) and across
space (via service migration). As a result, NOCs can play an important role in providing space-time
load-shifting ﬂexibility to the power grid. These synergies are illustrated in Figure 1. Exploiting
load-shifting ﬂexibility also brings important environmental beneﬁts; for instance, Google recently
introduced a Carbon-Intelligent Compute Management system that schedules ﬂexible workloads
to minimize carbon footprint (by consuming power at time or locations with low carbon content)
(Radovanovic et al. 2021).
Space-time, load-shifting ﬂexibility can also be provided by other key electricity market play-
ers such as manufacturing and storage systems. In the context of manufacturing, there is an on-
going trend to deploy small-scale, modular production facilities as a way to harness distributed and
stranded resources (e.g., waste streams, biomass, and renewable power) and to gain more ﬂexibility
in both investment and operations (Allman and Zhang 2020). The deployment of modular manu-
facturing systems would decentralize power loads and potentially aid power grid operations. A key
example of this trend is that of ammonia and hydrogen manufacturing, which are currently pro-
duced at large centralized facilities (Smith et al. 2020). At the same time, it has been recently shown
that space-time electricity market dynamics incentivize the deployment of modular systems and to
decentralize loads; this is because exploiting space-time dynamics provides investors with a mech-
anism to mitigate risk (by exploiting price differences at across space and time (Shao and Zavala
2019).
There has been growing interest into investigating market mechanisms that harness space-time
ﬂexiblity from DaCes. Recent work by Wierman and co-workers has identiﬁed various forms of
DaCe ﬂexibility that can be of practical use such as load shifting, load shedding, and geographical
load balancing (Wierman et al. 2017). The work in Ghatikar et al. (2012) reviews how operations of
DaCes can provide demand response services. The work in Rao et al. (2010) analyzes how NOCs may
be incentivized to exploit price differences across electricity markets. The work in Tran et al. (2015)
sets up a Stackelberg game to simulate optimal load-shifting strategies that DaCes might follow to
real-time pricing signals. The work in Liu et al. (2013) uses a stochastic optimization framework
to study how DCs can predict coincidental peak-pricing and avoid high cost caused by peak hours
using temporal workload shifting. Research has also focused on harnessing DaCe ﬂexibility for the
speciﬁc purpose of exploiting the availability of renewable power (e.g., as a way to decarbonize
operations and mitigate variability). For example, Kim et al. (2017) shows that optimal placement and
participation of DaCes in power grid markets (as dispatchable loads) leads to important reductions in
power spillage and cost and to a better utilization of wind generation (thus enabling higher adoption
levels).
2

---

## Page 3

http://zavalab.engr.wisc.edu
ISO
Renewable Energy
Data Center
Power Plant
Building
Power Flow
Data Center
Data Flow
Figure 1: Interactions between the computing and power infrastructures.
Modeling DaCe ﬂexibility is challenging due to the complicated nature of their workloads (Wier-
man et al. 2017). Speciﬁcally, DaCes need to process complex mixtures of ﬂexible and inﬂexible loads
that vary signiﬁcantly over time. Work by Liu et al. (2014) has shown that load-shifting in DaCes
can be seen as a form of large-scale storage but also note that incentivizing the provision of DaCe
ﬂexibility in power markets is difﬁcult. It is also important to recognize that different DaCes possess
different types and degrees of spatial ﬂexibility; for instance, some DaCes might only possess local
ﬂexibility, while others might be equipped with geographical ﬂexibility. Similarly, some DaCes have
different levels of temporal ﬂexibility, which is dictated by the nature of their workloads (e.g., job
duration).
DaCes demand responses have been studied using various game-theoretic modeling frameworks.
For instance, Zhou et al. (2018) and Sun et al. (2016) study how to incentivize spatial and temporal
ﬂexibility participation from the DaCe side using online auctioning. A Nash bargaining framework
has been employed to study the design incentive mechanisms between data centers and load-serving
entities (Cao et al. 2018) and between data centers and tenants in order to encourage the utilization of
ﬂexibility (Guo et al. 2018). These studies have shown that the amount of ﬂexibility that data centers
are willing to offer is, in fact, highly dependent on electricity prices. However, the decision-making
process of DaCes is not properly taken into account in existing electricity market designs; as such,
electricity prices are limited in their ability to incentivize the provision of ﬂexibility.
Power grids in the U.S. are operated using a coordinated market design where an independent
system operator (ISO) collects bid information from power consumers and suppliers and uses this
information to solve a market clearing problem (an optimization problem). The solution of this prob-
lem seeks to determine power allocations and locational marginal prices (LMPs) that maximize the
social surplus (the collective proﬁt of all players) subject to myriad constraints of the underlying
physical assets (e.g., transmission, capacity). Clearing mechanisms in current use are largely based
3

---

## Page 4

http://zavalab.engr.wisc.edu
on the pioneering works of Schweppe Schweppe et al. (1988) and of Hogan (Hogan 1992, Hogan et al.
1996), the latter of which establish revenue adequacy for transmission congestion payments and uses
duality theory to determine proper remuneration mechanisms to participants using clearing prices.
Various market clearing formulations have been proposed to capture different characteristics of
speciﬁc types of assets. For instance, the work by Carrion and Arroyo (2006) proposes a clearing
problem to capture time-dependent limitations (start-up costs and ramping constraints) in thermal
units. The formulation proposed in Bouffard et al. (2005) aims to incorporate generation uncertainty
directly in the clearing procedure. Along the same lines, the works in Pritchard et al. (2010), Zavala
et al. (2017) propose stochastic clearing formulations to analyze whether LMPs properly reﬂect un-
certainty of power generation, while maintaining key economic properties in the face of such uncer-
tainty (e.g., revenue adequacy and cost recovery). The work in Gribik et al. (2011) proposed a pricing
methodology that captures the cost of using an off-line resource to meet operational constraints.
Several works have explored extending the standard price-quantity bid format non-conventional
market participants that are spatially and/or temporally ﬂexible, including energy storage systems
(De Vivero-Serrano et al. 2019) and prosumers (Ottesen et al. 2016). The work by Liu et al. (2015) ex-
tends bid formats for adjustable, shiftable, and arbitrage loads. Recently, the concept of price-region
bid format is introduced that captures general ﬂexibility providers with linearly-constrained feasible
region and convex piecewise linear cost (Bobo et al. 2021).
Zhang et al. (2020) have recently proposed a market clearing formulation that captures space-
time load-shifting ﬂexibility of DaCes. This ﬂexibility is captured in the market clearing process
using a load disaggregation procedure that can be represented using virtual links. Virtual links are
non-physical pathways that can be used by the ISO to shift power loads in space (i.e., by sending a
computing load to another geographical location) and time (i.e., by delaying a computing load). This
paradigm is compatible with existing market clearing procedures and reveals that virtual links form
an additional infrastructure layer (similar to that overseen by NOCs) that complements the transmis-
sion network. This paradigm also captures general spatially and temporally ﬂexible loads that can be
offered from other players such as distributed manufacturing facilities and storage systems. In this
work, we provide an in-depth theoretical analysis of market clearing formulations with virtual links.
This reveals mechanisms under which DaCes should be remunerated for their ﬂexibility and reveals
information that DaCes should share with the ISO in the bidding process. This also shows that ﬂexi-
ble consumers act as prosumers that simultaneously pay for requested load and that are paid for their
ﬂexibility service (there is an incentive to offer ﬂexibility in order to decrease total cost). Our analysis
also shows that virtual links provide a convenient mathematical construct to establish fundamental
market properties; speciﬁcally, we show that a market that harnesses space-time load-shifting ﬂexi-
bility increases the social surplus, achieves revenue adequacy, achieves cost recovery, and provides
a mechanism to mitigate space-time volatility of LMPs. The framework is applied to case studies to
illustrate the theoretical results and practical impact.
The paper is structured as follows; Section 2 presents basic market clearing formulations that
are used to introduce notation and concepts. Speciﬁcally, we consider a formulation that uses load
disaggregation to capture DaCe ﬂexibility and provide an equivalent representation that uses virtual
links. Section 3 presents a general market formulation that captures space-time virtual links along
4

---

## Page 5

http://zavalab.engr.wisc.edu
with its properties. Section 4 presents cases studies to illustrate the developments. Section 5 closes
with remarks on future directions.
2
Basic Market Formulations
The market clearing formulations under study incorporate several new elements that are not stan-
dard in the power systems literature. As such, we introduce the reader to these new concepts by
exploring a family of formulations of increasing complexity. This will also allows us to introduce
basic terminology, notation, and to highlight key concepts that motivate our work. The market set-
ting studied is for an energy-only setting, similar to those studied in recent market design work by
Pritchard et al. (2010), Kazempour et al. (2018), Zakeri et al. (2019), and Zavala et al. (2017).
2.1
Basic Notation and Terminology
We begin our discussion by introducing basic notation for a static network (there is no time asso-
ciated with it). The market considers a set of suppliers (owners of power plants) S and consumers
(owners of DaCes) D connected to a transmission network comprised of geographical nodes N and
transmission lines L (owned by transmission service providers).
Each supplier i ∈S is connected to the power grid at node n(i) ∈N. The supplier bids into
the market by offering power at bid price αp
i ∈R+ and offers available capacity ¯pi ∈[0, ∞). We
deﬁne Sn := {i ∈S | n(i) = n} ⊆S (set of suppliers connected to node n). The cleared allocation for
supplier i ∈S (load injected) are denoted as pi and must satisfy pi ∈[0, ¯pi]. We use p to denote the
collection of all cleared allocations.
A consumer j ∈D bids into the market by requesting power at bid price αd
j ∈R+ and requests
a maximum capacity ¯dj ∈[0, ∞). We deﬁne Dn := {j ∈D | n(j) = n} ⊆D (set of consumers
connected to node n). For simplicity, we assume that there is only one consumer at a given node
(Dn are singletons). The cleared allocation for consumer j ∈D (load withdrawn) is denoted as dj
and must satisfy dj ∈[0, ¯dj]. We use d to denote the collection of all cleared allocations. A standard
(inﬂexible) consumer requests that the cleared load dj is delivered at a single node n(j) ∈N. A
ﬂexible consumer (a DaCe owner), on the other hand, offers the possibility that the cleared load dj is
delivered at a set of possible nodes Nd ⊆N; in other words, the cleared load dj can be disaggregated
and individual portions are delivered at different nodes. We will see that this load disaggregation
scheme can be seen as a spatial, load-shifting mechanism that can be modeled using virtual links. For
simplicity, we will not make a distinction between DaCe owners and inﬂexible consumers. This is
because an inﬂexible consumer can be modeled as a ﬂexible consumer with Nd = {n(j)} (it offers
one node option for the load to be delivered).
Each transmission owner has a line l ∈L deﬁned by its sending node snd(l) ∈N and receiving
node rec(l) ∈N. The deﬁnitions of snd(l) and rec(l) are interchangeable because power can ﬂow in
either direction. The sending and receiving nodes of a link are also known as its supporting nodes.
For each node n ∈N, we deﬁne its set of receiving lines Lrec
n
:= {l ∈L | n = rec(l)} ⊆L and its
set of sending lines Lsnd
n
:= {l ∈L | n = snd(l)} ⊆L. Each line offers a bid price αf
l ∈R+ and
5

---

## Page 6

http://zavalab.engr.wisc.edu
capacity ¯fl ∈[0, ∞). Note that while in common market cleraing practice, transmission line costs are
not captured (i.e., αf
l = 0 for each line l), we add this generality in order to demonstrate the similarity
between transmission network and ﬂexibility network later.
Each cleared ﬂow fl must satisfy the
bounds fl ∈[−¯fl, ¯fl] and the collection f must obey the direct-current (DC) power ﬂow equations:
fl = Bl(θsnd(l) −θrec(l)),
(2.1)
where Bl ∈R+ is the line susceptance and θn ∈R is the phase angle at node n ∈N. The DC power
ﬂow model is a linear model and requires small phase angle differences across transmission lines
θsnd(l) −θrec(l) ∈[−∆¯θ′l, ∆¯θ′l]. The limits on phase angle differences and the capacity constraints for
ﬂows can be captured as:
−∆¯θl ≤θsnd(l) −θrec(l) ≤∆¯θl
(2.2)
where ∆¯θl := min{ ¯fl/Bl, ∆¯θ′l}.
We use πn ∈R+ to represent the cleared price at node n ∈N. The collection of cleared prices
is denoted as π; these are also known as nodal prices or LMPs and are used to charge/remunerate
market players. We observe that, in a typical market, suppliers and transmission owners offer a service
to the grid, while inﬂexible consumers request a service from the grid. This distinction is important
because we will see that ﬂexible consumers (DaCes) act as prosumers that simultaneously request a
service (request load) and offer a service (ﬂexibility for load to be delivered at different locations); as
such, a well-designed market should properly remunerate the provision of ﬂexibility by DaCes.
2.2
Basic Formulation with Inﬂexible Consumers
We begin our discussion by studying a clearing formulation with inﬂexible consumers:
max
d,p,f,θ
X
j∈D
αd
jdj −
X
i∈S
αp
i pi −
X
l∈L
αf
l |fl|
(2.3a)
s.t.
X
l∈Lrec
n
fl +
X
i∈Sn
pi =
X
l∈Lsnd
n
fl +
X
j∈Dn
dj,
(πn)
n ∈N
(2.3b)
fl = Bl(θsnd(l) −θrec(l)),
l ∈L
(2.3c)
d ∈Cd , p ∈Cp , θ ∈Cθ.
(2.3d)
Here, we deﬁne the feasible capacity sets Cd := {d | dj ∈[0, ¯dj] ∀j ∈D}, Cp := {p | pi ∈[0, ¯pi] ∀i ∈S}
and Cθ := {θ | θrec(l) −θsnd(l) ∈[−∆¯θl, ∆¯θl] ∀l ∈L}. The objective function (2.3a) is known as the
social surplus or total welfare, which captures the value of demand served (to be maximized) and the
cost of supply and transmission cost services (to be minimized). The transmission cost is typically
not included in the market clearing literature; this cost is included here to highlight an important
analogy between transmission costs and load-shifting costs for DaCes (to be discussed later). Specif-
ically, we will see that load-shifting creates an alternative, non-physical infrastructure network that
is analogous to the transmission network. Constraint (2.3b) is the power balance constraint at each
node n (Kirchoff’s current law).
The solution of the market clearing problem gives the primal allocations (p, d, f) and the dual allo-
cations π. The dual allocations are the dual variables associated with the power balance constraints
6

---

## Page 7

http://zavalab.engr.wisc.edu
(2.3b). We will see that these can be used locational marginal prices (LMPs) that clear the market.
We use (p, d, f, π) to denote the primal-dual allocation obtained from the solution of the clearing
formulation.
The social surplus (2.3a) is a non-smooth function because of the presence of absolute value terms.
As is standard practice Bertsimas and Tsitsiklis (1997), this can be reformulated as a standard linear
program by decomposing each line l into directed edges l+ = (snd(l), rec(l)), l−= (rec(l), snd(l)) and
replace the terms in (2.3) as fl ←fl+ −fl−, |fl| ←fl+ +fl−, and fl+ ≥0, fl−≥0. We use K to represent
the set of directed edges that results from this decomposition. Each edge k ∈K resulted from line
l(k) ∈L inherits the susceptance Bk := Bl(k), bid price αf
k := αf
l(k), and capacity ∆¯θk := ∆¯θl(k). We
deﬁne the proﬁt term for each directed edge in a similar way:
φf
k(πrec(k), πsnd(k), fk) := (πrec(k) −πsnd(k) −αf
k)fk
(2.4)
Using these deﬁnitions, the transmission cost can be expressed as:
X
l∈L
αf
l |fl| =
X
l∈L
αf
l (fl+ + fl−) =
X
k∈K
αf
kfk,
(2.5)
and the net ﬂows entering a node n can be expressed as:
X
l∈Lrec
n
fl −
X
l∈Lsnd
n
fl =
X
l∈Lrec
n
(fl+ −fl−) −
X
l∈Lsnd
n
(fl+ −fl−)
=

X
l∈Lrec
n
fl+ +
X
l∈Lsnd
n
fl−

−

X
l∈Lrec
n
fl−+
X
l∈Lsnd
n
fl+


=
X
k∈Krec
n
fk −
X
l∈Ksnd
n
fk.
(2.6)
This leads to the (equivalent) clearing problem:
min
d,p,f,θ
X
i∈S
αp
i pi +
X
k∈K
αf
kfk −
X
j∈D
αd
jdj
(2.7a)
s.t.
X
k∈Krec
n
fk +
X
i∈Sn
pi =
X
k∈Ksnd
n
fk +
X
j∈Dn
dj,
(πn)
n ∈N
(2.7b)
fl+ −fl−= Bl(θsnd(l) −θrec(l)),
l ∈L
(2.7c)
d ∈Cd , p ∈Cp , θ ∈Cθ
(2.7d)
In this formulation, we minimize the negative surplus (as opposed to maximize the surplus); this
equivalent representation will facilitate the analysis.
A well-designed market clearing formulation must satisfy the following economic properties:
• Competitive Equilibrium: The clearing formulation must deliver allocations and prices that rep-
resent a competitive equilibrium. Speciﬁcally, the market must deliver allocations that balance
supply and demand and that maximize the collective proﬁt for all players. This property also
ensures that the ISO does not interfere with the competitive nature of the market players.
7

---

## Page 8

http://zavalab.engr.wisc.edu
• Revenue Adequacy: The clearing formulation delivers allocations and prices such that the total
amount of money paid by service requesters (consumers) covers the total amount paid to all
service providers (suppliers and transmission). This also ensures that the ISO does not have
ﬁnancial gain.
• Cost Recovery: The clearing formulation delivers allocations and prices such that no cleared
player incurs a ﬁnancial loss (it recovers its operating cost).
Although not necessarily a fundamental property, it is often desired that prices delivered by the
market are consistent with bid prices provided by market players (e.g., prices are bounded by bid
prices provided by players). We will see that this property is intimately related to cost recovery;
speciﬁcally, for a service provider to not incur a ﬁnancial loss, its cleared price must be higher than
its bid price (its marginal cost); for a consumer, the cleared price must be lower than its bid price.
We thus see that prices must satisfy some inherent bounding properties in order for cost recovery to
occur.
Figure 2: Standard market clearing mechanism with inﬂexible loads.
We now show that the market clearing formulation satisﬁes the stated properties; our discussion
here will be informal and is intended to introduce the general logic behind the analysis of clearing
formulations (we will follow a similar logic in studying more complex formulations).
We ﬁrst need to deﬁne the mechanism that will be used to charge/remunerate players and we then
need to verify that such mechanism is compatible with the clearing formulation. We consider that
8

---

## Page 9

http://zavalab.engr.wisc.edu
each supplier i is remunerated with price πn(i) for each unit of power cleared (injected) and each
consumer j pays πn(j) for each unit of power cleared (withdrawn). Each transmission provider l is
remunerated using the unit price |πrec(l)−πsnd(l)|, which is the price difference between the supporting
nodes. The proﬁt functions for supplier i ∈S, consumer j ∈D, and transmission provider l ∈L are
thus:
φp
i (πn(i), pi) := (πn(i) −αp
i )pi
(2.8a)
φd
j(πn(j), dj) := (αd
j −πn(j))dj
(2.8b)
φf
l (πrec(l), πsnd(l), fl) := (|πrec(l) −πsnd(l)| −αf
l )|fl|
(2.8c)
When convenient, we use the short-hand notation φp
i , φd
j, and φf
l . We proceed by deﬁning the (partial)
Lagrange function of the clearing formulation (2.7):
L(π, d, p, f)
=
X
i∈S
αp
i pi +
X
k∈K
αf
kfk −
X
j∈D
αd
jdj −
X
n∈N
πn

X
k∈Krec
n
fk +
X
i∈Sn
pi −
X
k∈Ksnd
n
fk −
X
j∈Dn
dj


= −
X
j∈D
(αd
j −πn(j))dj −
X
i∈S
(πn(i) −αp
i )pi −
X
k∈K
(πrec(k) −πsnd(k) −αf
k)fk
= −
X
j∈D
φd
j −
X
i∈S
φp
i −
X
k∈K
φf
k,
(2.9)
and the Lagrange dual function:
D(π) :=
min
d∈Cd,p∈Cp,f∈F L(π, d, p, f).
(2.10)
where F := {f | ∃θ ∈Cθ s.t. fl+ −fl−= Bl(θsnd(l)−θrec(l)) ∀l ∈L} denotes the set of ﬂows that satisﬁes
constraints (2.7c). These deﬁnitions allow us to formulate the Lagrangian dual problem:
max
π
D(π).
(2.11)
Throughout our study we assume that strong duality holds for all proposed market clearing formula-
tions. For the setting discussed here, this guarantees that an optimal solution of the clearing problem
(2.7)) can also be found by solving the corresponding Lagrangian dual problem (2.11).
We now proceed to show that the solution of the clearing formulation constitutes a competitive
equilibrium. By deﬁnition, the solution satisﬁes the nodal balance constraints (2.7b). Furthermore,
given a set of prices π, the Lagrange dual function (2.10) can be decomposed into the independent
optimization problems maxdj∈[0, ¯dj] φd
j for each consumer j, maxpi∈[0,¯pi] φp
i for each supplier i, and
maxf∈F
P
k∈K φf
k for the transmission providers. Thus, the clearing formulation ﬁnds prices that
maximize the proﬁt function for each player. From strong duality we have that a solution of the
Lagrangian dual problem also solves the clearing problem and thus satisﬁes the power balance con-
straints (supply equals demand at each node).
To establish revenue adequacy, we need to show that the total revenue collected from consumers
matches the total revenue allocated to service providers:
X
j∈D
πn(j)dj =
X
i∈S
πn(i)pi +
X
k∈K
(πrec(k) −πsnd(k))fk.
(2.12)
9

---

## Page 10

http://zavalab.engr.wisc.edu
From the power balance constraints (2.7b) we have that:
X
k∈Krec
n
fk +
X
i∈Sn
pi −
X
k∈Ksnd
n
fk −
X
j∈Dn
dj = 0.
(2.13)
This implies that,
X
n∈N
πn

X
k∈Krec
n
fk +
X
i∈Sn
pi −
X
k∈Ksnd
n
fk −
X
j∈Dn
dj

= 0.
(2.14)
This expression can be written in the following equivalent form:
X
j∈D
πn(j)dj =
X
i∈S
πn(i)pi +
X
n∈N
πn

X
k∈Krec
n
fk −
X
k∈Ksnd
n
fk


=
X
i∈S
πn(i)pi +
X
k∈K
 πrec(k) −πsnd(k)

fk,
(2.15)
which establishes revenue adequacy.
We now establish cost recovery; in establishing a competitive equilibrium, we argue that the La-
grangian dual problem (2.10) maximizes the proﬁt function for each individual player. Furthermore,
since (p, d, f, θ) = (0, 0, 0, 0) is a feasible (trivial) solution we have that, at the optimal allocation, the
proﬁt function for each player must be non-negative and thus φp
i , φd
j, φf
l ≥0.
To see how cost recovery leads to price-boundedness, deﬁne the set of cleared suppliers S∗:=
{i ∈S | pi > 0} and the set of cleared consumers D∗:= {j ∈D | dj > 0}. From the argument behind
cost recovery we have φp
i (πn(i), pi) = (πn(i) −αp
i )pi ≥0 and φd
j(πn(j), dj) = (αd
j −πn(j))dj ≥0. For
i ∈S∗, we have pi > 0 and thus πn(i) ≥αp
i . Similarly, for j ∈D∗, we have dj > 0 and thus πn(j) ≤αd
j.
It is often observed that increasing transmission capacity of a line has the effect of reducing the
price difference between the connected nodes; in other words, transmission capacity reduces the spa-
tial variability of prices. In the limit when there is enough transmission capacity and the network
is well-connected, power should be allowed to move freely in the network (there is no market fric-
tion) and all nodal prices should collapse to a single value. On the other hand, when there is not
enough transmission capacity and/or the network is not well-connected, there will be large differ-
ences between nodal prices. Understanding the effect of transmission capacity on prices will become
relevant for the formulations studied in this paper; speciﬁcally, we will see that virtual links form an
alternative infrastructure network that can help overcome limitations of the transmission network.
To gain some intuition into how transmission capacity reduces spatial volatility, here we present
a simple analysis in the absence of DC constraints (2.7c); in such a case, the clearing formulation
reduces to:
min
d,p,f
X
i∈S
αp
i pi +
X
k∈K
αf
kfk −
X
j∈D
αd
jdj
(2.16a)
s.t.
X
k∈Krec
n
fk +
X
i∈Sn
pi =
X
k∈Ksnd
n
fk +
X
j∈Dn
dj,
(πn)
n ∈N
(2.16b)
d ∈Cd , p ∈Cp , f ∈Cf
(2.16c)
10

---

## Page 11

http://zavalab.engr.wisc.edu
where Cf = {f|fk ∈[0, ¯fk]} and ¯fk = Bk¯θk. Consider now a couple of instances for the clearing
formulation (2.16) with line capacities ¯fk and ¯f′
k satisfying ¯fk < ¯f′
k for some k ∈K. Let π∗, π′∗be the
optimal prices for the corresponding instances; we would like to show that the prices satisfy:
π′∗
rec(k) −π′∗
snd(k) ≤π∗
rec(k) −π∗
snd(k).
(2.17)
The Lagrange function of (2.16) has the same form as that of (2.9). The Lagrange dual function is:
D(π) =
min
d∈Cd,p∈Cp,f∈Cf
L(π, d, p, f).
(2.18)
For ﬁxed prices π, the Lagrange function is separable and be decomposed into the individual proﬁt-
maximization subproblems:
max
d
(αd
j −πn(j))dj
(2.19a)
s.t.
0 ≤dn ≤¯dj
(2.19b)
max
pi
(πn(j) −αp
i )pi
(2.20a)
s.t.
0 ≤pi ≤¯pi
(2.20b)
max
f
X
k∈K
(πrec(k) −πsnd(k) −αf
k)fk.
(2.21)
These subproblems have explicit solutions and this allows us to write the Lagrangian dual function
as:
D(π) = −
X
j∈D
|αd
j −πn(j)|+ ¯dj −
X
i∈S
|πn(i) −αp
i |+¯pi −
X
k∈K
|πrec(k) −πsnd(k) −αf
k|+ ¯fk
(2.22)
where | · |+ = max{·, 0}. The Lagrangian dual problem is:
max
π
D(π).
(2.23)
Deﬁning D′(π) as the Lagrangian dual function for the problem with expanded capacity ¯f′
k; we
have that h′(π) ≤D(π) for any π due to the larger feasible region of the inner problem. Now let
(d∗, p∗, f∗, π∗) be an optimal solution for maxπ D(π), and deﬁne ∆k(π) := πrec(v) −πsnd(v) −αf
k. We
consider a couple of cases; for the ﬁrst case, assume ∆k(π∗) ≤0, we thus have D′(π∗) = D(π∗) and
thus the optimal prices remain the same; for the second case, assume ∆k(π∗) > 0 and let π be arbi-
trary prices such that ∆k(π) > ∆k(π∗) > 0. We now observe that π cannot be optimal; from the setup
above we have that:
D(π) −D′(π) = ∆k(π)( ¯f′
k −¯fk)
(2.24a)
D(π∗) −D′(π∗) = ∆k(π∗)( ¯f′
k −¯fk),
(2.24b)
11

---

## Page 12

http://zavalab.engr.wisc.edu
this implies that:
D′(π) −D′(π∗) = D(π) −D(π∗) + ( ¯f′
k −¯fk)(∆k(π∗) −∆k(π)) < 0,
(2.25)
which holds because ∆k(π∗) −∆k(π) < 0 and D(π) ≤D(π∗) (by optimality of π∗).
This simple analysis provides some intuition into how the addition of transmission ﬂexibility can
help mitigate nodal price differences. We will see later that a similar behavior can be obtained by in-
corporating spatial load-shifting ﬂexibility provided by DaCes. Moreover, we will see that temporal
load-shifting ﬂexibility can be used to mitigate temporal price differences.
2.3
Basic Formulation with Flexible Consumers
We now expand the previous clearing formulation by incorporating ﬂexible consumers; speciﬁcally,
we consider ﬂexible consumers that offer load-shifting ﬂexibility by exploiting the availability of
multiple DaCes placed at different nodes. For simplicity in the presentation, here we consider a single
ﬂexible consumer. Suppose that this consumer submits a bid for requested load ¯d with bid price αd;
the requested load can be served/delivered at a set of nodes Nd ⊆N. Each node n ∈Nd receives
a partial load dn ≥0; the total load served to the consumer is P
n∈Nd dn and satisﬁes P
n∈Nd dn ≤¯d
(total load served cannot exceed the requested load). The clearing problem is:
min
d,p,f,θ
X
i∈S
αp
i pi +
X
k∈K
αf
kfk −αd X
n∈Nd
dn
(2.26a)
s.t.
X
k∈Krec
n
fk +
X
i∈Sn
pi =
X
k∈Ksnd
n
fk + dn
(πn),
n ∈Nd
(2.26b)
X
k∈Krec
n
fk +
X
i∈Sn
pi =
X
k∈Ksnd
n
fk
(πn),
n ∈N\Nd
(2.26c)
0 ≤
X
n∈Nd
dn ≤¯d
(2.26d)
dn ≥0,
n ∈Nd
(2.26e)
fl+ −fl−= Bl(θsnd(l) −θrec(l)),
l ∈L
(2.26f)
p ∈Cp , θ ∈Cθ
(2.26g)
From the structure of the surplus function we see that the formulation aims to maximize the total load
delivered to the ﬂexible consumer. From the power balances, we see that nodes offered by the ﬂexible
consumer (Nd) can receive load, while those not offered (N \ Nd) cannot. The proﬁt function for the
ﬂexible consumer is deﬁned as φd(π, d) := P
n∈Nd(αd −πn)dn. This indicates that the consumer is
charged for power based on the prices of all the nodes offered. This remuneration mechanism is
fundamentally different from that of an inﬂexible consumer (which is charged based on the price at a
single node). As such, when a consumer offers load to be delivered at multiple nodes, it is expected
that the ISO can exploit this ﬂexibility to maximize the consumer proﬁt (if this is not the case, there
is no incentive for the consumer to offer ﬂexibility).
12

---

## Page 13

http://zavalab.engr.wisc.edu
We now establish the fundamental market properties for (2.26) to highlight differences with the
previous market setting. The partial Lagrange function is:
L(π, d, p, f) =
X
i∈S
αp
i pi +
X
k∈K
αf
kfk −αd X
n∈Nd
dn −
X
n∈N\Nd
πn

X
k∈Krec
n
fk −
X
i∈Sn
pi −
X
k∈Ksnd
n
fk


−
X
n∈Nd
πn

X
k∈Krec
n
fk −
X
i∈Sn
pi −
X
k∈Ksnd
n
fk −dn


=
−
X
j∈Nd
(αd −πn(j))dj −
X
i∈S
(πn(i) −αp
i )pi −
X
k∈K
(πrec(k) −πsnd(k) −αf
k)fk,
(2.27)
and the Lagrangian dual problem is:
max
π
D(π) :=
min
d,p,f,θ
L(π, d, p, f)
(2.28a)
s.t.
0 ≤
X
j∈Nd
dj ≤¯d
(2.28b)
dn ≥0,
n ∈Nd
(2.28c)
fl+ −fl−= Bl(θsnd(l) −θrec(l)),
l ∈L
(2.28d)
p ∈Cp , θ ∈Cθ
(2.28e)
The Lagrange dual function D(π) can be decomposed to individual proﬁt maximization problems:
max
d
X
j∈Nd
(αd −πn(j))dj
(2.29a)
s.t.
0 ≤
X
j∈Nd
dj ≤¯d
(2.29b)
dn ≥0,
n ∈Nd
(2.29c)
max
pi
(πn(j) −αp
i )pi
(2.30a)
s.t.
0 ≤pi ≤¯p
(2.30b)
max
f,θ∈Cθ
X
k∈K
(πrec(k) −πsnd(k) −αf
k)fk
(2.31a)
s.t.
fl+ −fl−= Bl(θsnd(l) −θrec(l)),
l ∈L
(2.31b)
It is straightforward to show that the proﬁt maximization problems for suppliers (2.30) and transmis-
sion providers (2.31) are the same as those of the base formulation with inﬂexible consumers (under
DC constraints). The main difference that arises here lies in the proﬁt maximization problem for the
consumer (2.29); the structure of this problem conﬁrms that the ﬂexible consumer should be charged
13

---

## Page 14

http://zavalab.engr.wisc.edu
based on the nodal prices and the corresponding components of the disaggregated load; moreover,
the total load served should not exceed the requested capacity.
We now establish the properties for the market clearing formulation; the logic is similar as that
followed before but we highlight some basic differences that arise from the provision of ﬂexibility.
Market clearance is guaranteed by satisfaction of the power balance constraints (2.26b), (2.26c). Fur-
thermore, (2.29)-(2.31) show that the formulation (2.26) delivers an optimal price and allocation that
maximize proﬁt for the ﬂexible consumer, each of the suppliers, and the transmission network. From
the balance constraints (2.26b), (2.26c) we have:
0 =
X
n∈N
πn

X
k∈Krec
n
fk +
X
i∈Sn
pi −
X
k∈Ksnd
n
fk −
X
j∈Dn
dj


(2.32)
Basic manipulations reveal that this expression implies revenue adequacy.
To establish cost recovery, we note again that (p, d, f, θ) = (0, 0, 0, 0) is a feasible solution and thus
the proﬁt function of all players is non-negative. Non-negative proﬁts implies that φp
i (πn(i), pi) =
(πn(i) −αp
i )pi ≥0 and φd(π, d) = P
j∈Nd(αd −πn(j))dj ≥0. If supplier i satisﬁes pi > 0, then
πn(i) ≥αp
i . To establish upper bounds, suppose by contradiction that there exists n ∈Nd such that
αd −πn < 0 and dn > 0; then, d is not optimal (d does not attain the maximum proﬁt for the ﬂexible
consumer); we can construct d′ by letting d′
n′ = dn′ for n′ ∈D\{j} and d′
n = 0. We thus have that d′
satisﬁes all constraints and gives a higher proﬁt; as such, dn > 0 implies πn ≤αd. We thus see that the
introduction of ﬂexibility affects price boundedness; speciﬁcally, for markets with inﬂexible loads, a nodal
price can only be upper bounded by the bid price of the load connected to it. This is not the case for
markets with ﬂexible loads; speciﬁcally, the price for any node in Nd can be bounded by the load bid
price αd. Therefore, the key insight here is that load-shifting ﬂexibility provides a new mechanism
for the ISO to control price behavior.
Figure 3: Disaggregation model (left) and equivalent representation using virtual links (right).
14

---

## Page 15

http://zavalab.engr.wisc.edu
2.4
Basic Formulation with Virtual Links
We have seen that there natural incentive for ﬂexible consumers to offer alternative nodes to the ISO
in order to access alternative nodal prices. However, the market clearing formulation previously
explored does not provide intuition on how DaCe ﬂexibility is remunerated. To address this issue,
we propose a mathematically-equivalent formulation that treats DaCes as prosumers that simultane-
ously request power and offer load-shifting ﬂexibility. To do this, we introduce the notion of virtual
links; speciﬁcally, as shown in Figure 3, load disaggregation can be seen as a non-physical transport
(shift) of load from a reference node to a set of alternate nodes.
Suppose the ﬂexible consumer submits a bid for requested load ¯d at a hub (reference) node nh ∈N
with bid price αd and offers at set of alternate nodes Nd ⊆N such that nh ∈Nd. We use δnh,n ∈R+
to denote the amount of load that is shifted from the hub node nh to the alternate node n ∈Nd; we
refer to the load-shifting pathway as a virtual link. This leads to the following clearing formulation:
min
d,p,f,θ,δ
X
i∈S
αp
i pi +
X
k∈K
αf
kfk −αdd
(2.33a)
s.t.
X
k∈Krec
n
fk +
X
i∈Sn
pi =
X
k∈Ksnd
n
fk +









d −P
j∈Nd δnh,j,
n = nh
δnh,n,
n ∈Nd\{nh}
0,
n ∈N\Nd
(πn)
(2.33b)
0 ≤d ≤¯d
(2.33c)
δn ≥0,
n ∈Nd
(2.33d)
d −
X
n∈Nd
δnh,n ≥0
(2.33e)
fl+ −fl−= Bl(θsnd(l) −θrec(l)),
l ∈L
(2.33f)
p ∈Cp , θ ∈Cθ
(2.33g)
It is not difﬁcult to observe that formulations (2.26) and (2.33) are equivalent. Speciﬁcally, there exists
a bijection between dn in (2.26) and (d, δnh,n) in (2.33) such that each pair satisﬁes:
dnh = d −
X
n∈Nd
δnh,n
dn = δnh,n,
n ∈Nd\{nh}.
A feasible solution (d, p, f, θ, δ) of (2.33) implies existence of a feasible solution (d, p, f, θ) for (2.26)
with the same value of (f, θ, p) (and viceversa). In addition, both solutions attain the same optimal
15

---

## Page 16

http://zavalab.engr.wisc.edu
objective value. The partial Lagrange function for (2.33) is:
L(d, p, θ, δ)
=
X
i∈S
αp
i pi +
X
k∈K
αf
kfk −αdd −πnh
 X
k∈Krec
nh
fk +
X
i∈Snh
pi −
X
k∈Ksnd
nh
fk −d +
X
n∈Nd
δnh,n

−
X
n∈Nd\{nd}
πn
 X
k∈Krec
n
fk +
X
i∈Sn
pi −
X
k∈Ksnd
n
fk −δnh,n

−
X
n∈N\Nd\{nd}
πn
 X
k∈Krec
n
fk +
X
i∈Sn
pi −
X
k∈Ksnd
n
fk

=(πnh −αd)d −
X
n∈Nd
(πnh −πn)δnh,n −
X
i∈S
(πi −αp
i )pi −
X
k∈K
(πrec(k) −πsnd(k) −αf
k)fk,
(2.34)
and the Lagrangian dual problem is:
max
π
min
d,p,f,θ
L(π, d, p, θ)
(2.35a)
s.t.
0 ≤d ≤¯d
(2.35b)
δnh,n ≥0,
n ∈Nd
(2.35c)
d −
X
n∈Nd
δnh,n ≥0
(2.35d)
fl+ −fl−= Bl(θsnd(l) −θrec(l)),
l ∈L
(2.35e)
p ∈Cp , θ ∈Cθ
(2.35f)
The Lagrange function (2.34) reveals that virtual links are a service offered by the consumer. The
market remunerates the consumer for the provision of this service via the proﬁt P
n∈Nd(πnh−πn)δnh,n.
This highlights that load-shifting is incentivized whenever there is a nodal price πn that is lower than
the price at the hub node πnh. This is analogous to how transmission is remunerated (based on nodal
price differences). The market also charges the consumer via the the proﬁt (αd −πnh)d; consequently,
the ﬂexible consumer acts as a prosumer and has total proﬁt:
(αd −πnh)d +
X
n∈Nd
(πnh −πn)δnh,n = (αd −πnh)(d −
X
n∈Nd
δnh,n) +
X
n∈Nd
(αd −πn)δnh,n
(2.36)
This is the same proﬁt function shown in (2.27), where the proﬁt is determined by the difference
between the bid price and the price at the nodes where the loads are shifted to (this further reinforces
the equivalence between the load disaggregation formulation and the formulation with virtual links).
The load disaggregation formulation shows the total remuneration for DaCes, while the formulation
with virtual links reveals how the market remunerates the provision of load-shifting services. We
observe that all market and price properties established for the load disaggregation model hold for
the virtual link model (since the models are equivalent); as such, these are not established again.
2.5
Basic Formulation with General Virtual Links (Spatial)
We now generalize the concept of virtual links as a means to offer spatial load-shifting ﬂexibility ser-
vices; this will reveal strong connections between the non-physical network formed by virtual links
16

---

## Page 17

http://zavalab.engr.wisc.edu
and the physical transmission network. Speciﬁcally, we will see that virtual links form an additional
infrastructure layer that is not restricted by DC power ﬂow laws.
We let V be the set of all virtual links; each virtual link v ∈V has an associated bid price αδ
v ∈R+
and capacity ¯δv ∈[0, ∞). The cleared load shifts (virtual ﬂows) are deﬁned as δv ∈R+ and are
subject to capacity constraints δv ∈[0, ¯δv]. We deﬁne Vsnd
n
:= {v ∈V | snd(v) = n} ⊆V, Vrec
n
:=
{v ∈V | rec(v) = n} ⊆V to be the set of sending and receiving virtual links at node n. Each ﬂexible
consumer j ∈D is associated with a set of virtual links Vj ⊆V. For each v ∈Vj, snd(v) = nh(j)
since each consumer can only bid ﬂexibility going from its hub node to other alternative nodes. We
note that the bid price of the virtual link can represent cost of shifting load (e.g., opportunity cost of
migrating a computing load). This can also help capture the fact that shifts to certain nodes can be
more expensive (e.g., due to distance or to capture preferred locations by the market players). The
shift cost is analogous to the service cost of power transmission.
In a base setting with inﬂexible consumers, the load cleared (withdrawn) at a node n is ˆdn =
P
j∈Dn dj. This does not hold if we consider ﬂexible consumers, as a requested load at a given node
might be withdrawn at another node. We thus have that the load withdrawn at node n is:
ˆdn =
X
j∈Dn
dj +
X
v∈Vin
n
δv −
X
v∈Vout
n
δv.
(2.37)
As load shifting is introduced to the market clearing, the clearing process needs to ensure that a
certain DaCe does not absorb a load that exceeds its available computing capacity. Moreover, the
clearing process needs to ensure that a certain DaCe does not shift load that exceeds how much it
actually possesses. This logic can be captured using the computing capacity constraints:
0 ≤
X
j∈Dn
dj +
X
v∈Vrec
n
δv −
X
v∈Vsnd
n
δv ≤¯dmax
n
,
n ∈N
(2.38)
where ¯dmax
n
denotes the capacity of the DaCe located at n.
The market clearing problem with spatial virtual links is:
min
d,p,f,θ,δ
X
i∈S
αp
i pi +
X
k∈K
αf
kfk +
X
v∈V
αδ
vδv −
X
j∈D
αd
jdj
(2.39a)
s.t.
X
k∈Krec
n
fk +
X
i∈Sn
pi +
X
v∈Vsnd
n
δv =
X
k∈Ksnd
n
fk +
X
j∈Dn
dj +
X
v∈Vrec
n
δv, (πn) n ∈N
(2.39b)
fl+ −fl−= Bl(θsnd(l) −θrec(l)),
l ∈L
(2.39c)
0 ≤
X
j∈Dn
dj +
X
v∈Vrec
n
δv −
X
v∈Vsnd
n
δv ≤¯dmax
n
, (ωl
n, ωu
n)
n ∈N
(2.39d)
d ∈Cd, p ∈Cp, θ ∈Cθ, δ ∈Cδ
(2.39e)
where the set Cδ := {δ | δv ∈[0, ¯δv] ∀v ∈V} captures the capacity constraints for virtual links.
Comparing this formulation with the previous formulation (2.33), we observe that the social surplus
(2.39a) now captures the operational cost of virtual links; moreover, the balance constraints (2.39b)
now include spatial virtual shifts. The dual variables associated with the computing capacity con-
straints (2.39d) are denoted ωl
n and ωu
n, respectively. Note that the operational cost of virtual links
17

---

## Page 18

http://zavalab.engr.wisc.edu
resembles that of operational costs of physical transmission and, as the name suggest, these capture
costs associated with load shifting (e.g., data transfer costs). In this market, each consumer j ∈D is
charged with the electricity price at the hub node and also remunerated by the shifting service pro-
vided through virtual links. As shown in Section 2.4, the market pays off virtual links by the price
difference between the sending and receiving nodes.
2.6
Basic Formulation with General Virtual Links (Temporal)
The concept of virtual links naturally arises from the ability of DaCes to offer geographical load-
shifting ﬂexibility; however, this concept can also be used to capture temporal ﬂexibility. This is
key because DaCes are also able to schedule tasks over time in a way that they ﬁnd most efﬁ-
cient/proﬁtable. The key is to capture temporal shifting ﬂexibility by using virtual links considering
a time horizon as a linear network (with nodes deﬁning time locations). We thus have that virtual
links transport load from a given time location to another time location in the future.
To see how to incorporate temporal virtual links in the clearing model, we consider a time horizon
given by the time nodes T = {t1, t2, ..., tT }. For simplicity, we consider a network with a single spatial
node (no transmission network is present in this setting). For each time node t ∈T , the DaCe bids
a price αd
t and a capacity ¯dt that represents the amount of load requested. Similarly, we consider
a supplier that bids a price αp
t and a capacity ¯pt at time t ∈T . The clearing formulation will ﬁnd
optimal levels for load satisfaction dt and generation pt for each time t ∈T .
Each virtual link v ∈V branches from a time node t to a later time node t′. The virtual link bids
into the market at a price αδ
v and capacity δt. The load at each time t ∈T is associated with a set of
virtual links Vt ⊆V. For each v ∈Vt, we have snd(v) = t (since each consumer can only bid ﬂexibility
going from the current time to a later time). The market clearing process will ﬁnd the optimal time
shift ﬂows δv for each v ∈V. A distinguishing feature of temporal virtual links (compared to spatial
virtual links) is that they are naturally unidirectional. The temporal model needs to establish balance
constraints for each time node. The load cleared/withdrawn at t is:
ˆdt = dt +
X
v∈Vin
t
δv −
X
v∈Vout
t
δv.
(2.40)
Interestingly, we note that this power balance is similar to that of an energy storage system. This
indicates that storage systems act as transporters/carriers of load and thus can be remunerated as
ﬂexibility providers. This also highlights that virtual links provide a mechanism to remunerate tech-
nologies that can provide load-shifting ﬂexibility (e.g., buildings, manufacturing, batteries).
18

---

## Page 19

http://zavalab.engr.wisc.edu
The clearing formulation for this setting is:
min
d,p,δ
X
t∈T
αp
t pt +
X
v∈V
αδ
vδv −
X
j∈D
αd
jdj
(2.41a)
s.t.
pt = dt +
X
v∈Vin
t
δv −
X
v∈Vout
t
δv,
t ∈T
(2.41b)
0 ≤dt +
X
v∈Vrec
t
δv −
X
v∈Vsnd
t
δv ≤¯dmax
t
, (ωl
t, ωu
t )
t ∈T
(2.41c)
0 ≤pt ≤¯pt,
t ∈T
(2.41d)
0 ≤dt ≤¯dt,
t ∈T
(2.41e)
0 ≤δv ≤¯δv,
v ∈V
(2.41f)
The load at each time t is charged at the corresponding cleared price and also remunerated by the
shifting service provided through virtual links; the consumer ﬂexibility is remunerated based on the
price difference between the sending and receiving times. In other words, a load shift will occur
provided there is a price difference. We can see that the temporal formulation is directly analogous
to the spatial formulation; as such, we can use virtual links to unify space-time shifting.
Figure 4: Illustration of space-time load shifting using virtual links.
19

---

## Page 20

http://zavalab.engr.wisc.edu
3
Market Formulation with Space-Time Virtual Links
In this section, we establish properties for a general clearing framework with space-time virtual links
(3.42). This formulation uniﬁes all the formulations that we have previously discussed. We will show
that this clearing formulation satisﬁes revenue adequacy, cost recovery, and provides a competitive
equilibrium. Moreover, we explore the effect of consumer ﬂexibility on space-time price behavior;
speciﬁcally, we will show that virtual links mitigate volatility.
Central to our results is the observation that virtual links can be used to treat space and time
load-shifting ﬂexibility in a uniﬁed manner, as shown in Figure 4. In this illustration, the spatial
nodes of the network are extended into a time dimension using a set of time nodes, thus becoming
a space-time network (a graph). Each time slice of the space-time graph represents the state of the
network at the corresponding time. This space-time network representation is analogous to those
used in dynamic network ﬂow models.
Consider a space-time clearing setting with spatial nodes N and temporal nodes T . A node
in this space-time graph is deﬁned as the pair (n, t) ∈N × T (we refer to (n, t) as a space-time
node). Participation of suppliers, consumers and transmission services is extended to include a time
dimension. Speciﬁcally, participants bid prices αp
i,t, αd
j,t, αf
k,t and capacities ¯pi,t, ¯dj,t, ¯fk,t at each time
t ∈T (bids are a function of time). The cleared allocations dj,t, pi,t, fk,t and θk,t are also indexed in
time.
Virtual links connect space-time nodes; each v ∈V is associated with a sending space-time node
snd(v) = (nsnd(v), tsnd(v)) and a receiving space-time node rec(v) = (nrec(v), trec(v)). We deﬁne Vsnd
n,t :=
{v ∈V | snd(v) = (n, t)} ⊆V, Vrec
n,t := {v ∈V | rec(v) = (n, t)} ⊆V to be the set of sending and
receiving virtual links at space-time node (n, t). This setting captures the special case in which v is a
spatial virtual link if it connects nodes at different locations but same time (nsnd(v)̸ = nrec(v), tsnd(v) =
trec(v)). Similarly, the setting captures the special case in which v is a temporal virtual link if it connects
nodes at different times but at the same location (tsnd(v)̸ = trec(v), nsnd(v) = nrec(v)). The load j ∈D at
each space-time node (n(j), t(j)) is associated with a set of virtual links Vj and we have V = S
j∈D Vj.
The clearing formulation with space-time virtual links is:
min
d,p,f,θ,δ
X
t∈T
 X
i∈S
αp
i,tpi,t +
X
k∈K
αf
k,tfk,t −
X
j∈D
αd
j,tdj,t

+
X
v∈V
αδ
vδv
(3.42a)
s.t.
X
k∈Krec
n
fk,t +
X
i∈Sn
pi,t +
X
v∈Vsnd
n,t
δv =
X
k∈Ksnd
n
fk,t +
X
j∈Dn
dj,t +
X
v∈Vrec
n,t
δv,
(πn,t)
n ∈N, t ∈T
(3.42b)
fl+,t −fl−,t = Bl(θsnd(l),t −θrec(l),t),
l ∈L, t ∈T
(3.42c)
0 ≤
X
j∈Dn
dj,t +
X
v∈Vrec
n,t
δv −
X
v∈Vsnd
n,t
δv ≤¯dmax
n,t ,
(ωl
n,t, ωu
n,t)
n ∈N, t ∈T
(3.42d)
(d, p, θ, δ) ∈C
(3.42e)
20

---

## Page 21

http://zavalab.engr.wisc.edu
Figure 5: Market clearing mechanism with ﬂexible loads using space-time virtual links.
where C := Cd × Cp × Cθ × Cδ captures the capacity constraints for all variables:
Cd := {d | dj,t ∈[0, ¯dj,t] ∀j ∈D, t ∈T }
(3.43a)
Cp := {p | pi,t ∈[0, ¯pi,t] ∀i ∈S, t ∈T }
(3.43b)
Cθ := {θ | θrec(k),t −θsnd(k),t ∈[−∆¯θk,t, ∆¯θk,t] ∀k ∈K, t ∈T }
(3.43c)
Cδ := {δ | δv ∈[0, ¯δv] ∀v ∈V}
(3.43d)
The social surplus (3.42a) captures the entire time horizon. Constraints (3.42b) are nodal balances for
each space-time node (we denote the duals of these constraints as πn,t). Constraints (3.42c) are DC
power ﬂows for all times. Constraints (3.42d) are computing capacity constraints for DaCes at space-
time node (n, t). The duals associated with these constraints are denoted ωl
n,t ∈R+ and ωu
n,t ∈R+.
The market clearing setting is illustrated in Figure 5.
21

---

## Page 22

http://zavalab.engr.wisc.edu
3.1
Market Properties
To establish market properties for (3.42), we formulate the partial Lagrange function of (3.42):
L(d, p, f, θ, δ, π, ω) =
X
t∈T
 X
i∈S
αp
i,tpi,t +
X
k∈K
αf
l,tfl,t −
X
j∈D
αd
j,tdj,t

+
X
v∈V
αδ
vδv
−
X
t∈T
X
n∈N
πn,t
 X
k∈Krec
n
fk,t +
X
i∈Sn
pi,t +
X
v∈Vsnd
n,t
δv −
X
k∈Ksnd
n
fk,t −
X
j∈Dn
dj,t −
X
v∈Vrec
n,t
δv

+
X
n∈N,t∈T
ωu
n,t
 X
j∈Dn
dj,t +
X
v∈Vrec
n,t
δv −
X
v∈Vsnd
n,t
δv −¯dmax
n,t

−
X
n∈N,t∈T
ωl
n,t
 X
j∈Dn
dj,t +
X
v∈Vrec
n,t
δv −
X
v∈Vsnd
n,t
δv

=
−
X
j∈D,t∈T
φd
j,t(ˆπn(j),t, αd
j,t, dj) −
X
v∈V
φδ
v(ˆπrec(v), ˆπsnd(v), αδ
v, δv)
−
X
k∈K,t∈T
φf
k,t(πrec(k),t, πsnd(k),t, αf
k,t, fk,t) −
X
i∈S,t∈T
φp
i,t(πn(i),t, αp
i,t, pi)
(3.44)
where we deﬁne ωn,t := ωu
n,t −ωl
n,t and ˆπn,t := πn,t + ωn,t. The proﬁts for demands, virtual links,
suppliers, and transmission links are (see Figure 6):
φd
j,t(ˆπn(j),t, αd
j,t, dj) := (αd
j,t −ˆπn(j),t)dj,t
(3.45a)
φδ
v(ˆπrec(v), ˆπsnd(v), αδ
v, δv) := (ˆπsnd(v) −ˆπrec(v) −αδ
v)δv
(3.45b)
φp
i,t(πn(i),t, αp
i,t, pi,t) := (πn(i),t −αp
i,t)pi,t
(3.45c)
φf
k,t(πrec(k),t, πsnd(k),t, αf
k,t, fk,t) := (πrec(k),t −πsnd(k),t −αf
k,t)fk,t
(3.45d)
We can thus see that the Lagrange function (3.44) is the negative sum of proﬁt functions for all par-
ticipants with price adjustment for DaCes due to the capacity constraints (3.42d). The presence of
capacity constraints for DaCes introduces technical difﬁculties in the analysis (as they couple de-
mands and virtual links). To see this, we note that the total proﬁt for the DaCes is:
X
t∈T

X
j∈D
(αd
j,t −ˆπn(j),t)dj,t

+
X
v∈V
(ˆπsnd(v) −ˆπrec(v) −αδ
v)δv
=
X
j∈D,t∈T
αd
j,t −
X
v∈V
αδ
vδv −
X
n∈N,t∈T
ˆπn,t



X
j∈Dn
dj,t +
X
v∈Vrec
n,t
δv −
X
v∈Vsnd
n,t
δv


.
(3.46)
The proﬁt functions for the DaCes use ˆπ = π + ω as prices (instead of the LMPs π). The dual
variable ω adjusts the incentive for load-shifting to prevent shifting that exceeds computing capacity
bounds or available loads to shift. Speciﬁcally, if ωsnd(v) > 0, the upper bound of ˆdsnd(v) is active
(meaning that local loads are reaching their upper limit at snd(v)); thus, ωsnd(v) provides incentive
to shift. If ωsnd(v) < 0, the local loads are exactly zero, and ωsnd(v) eliminates the incentive to shift.
Similarly, if ωrec(v) > 0, the upper bound of ˆdrec(v) is active, meaning that local loads reach the max-
imum at the receiving node; thus, ωsnd(v) eliminates the incentives to shift. If ωrec(v) < 0, the local
22

---

## Page 23

http://zavalab.engr.wisc.edu
loads are zero at the receiving node, and ωrec(v) provide incentives for shifting. An alternative way of
interpreting ω is as an internal price factor for DaCes; speciﬁcally, ω is the demand-supply relationship
of loads within the DaCe network. If loads are not desired at a space-time node, then ω > 0 (the
load will be pushed away from the node and therefore is not as valuable); if loads are desired at a
space-time node, ω < 0 (the load will be attracted to the node and therefore it is valuable).
Figure 6: Payment, remuneration, and proﬁt of market players.
Since we assume that strong duality holds, an optimal solution of (3.42) can be obtained by solving
the Lagrangian dual problem:
max
π,ω
min
(d,p,θ,δ)∈C,f∈F L(d, p, f, θ, δ, π, ω)
(3.47)
where F captures the DC power ﬂow constraints (3.42c). For ﬁxed duals π, ω, the Lagrange function
can be decomposed into the individual proﬁt maximization problems:
max
pi,t∈[0,¯pi,t]φp
i,t(πn(i),t, αp
i,t, pi,t)
(3.48a)
max
dj,t∈[0, ¯dj,t]φd
j,t(ˆπn(j),t, αd
j,t, dj,t)
(3.48b)
max
δv∈[0,¯δv]φδ
v(ˆπrec(v), ˆπsnd(v), αδ
v, δv)
(3.48c)
max
θt∈Cθt,fk,t∈Ft
X
k∈K
φf
k,t(πrec(k),t, πsnd(k),t, αf
k,t, fk,t)
(3.48d)
We now proceed to establish fundamental properties for the clearing formulation.
Theorem 3.1. The clearing formulation (3.42) provides an allocation and prices that represent a competitive
equilibrium.
23

---

## Page 24

http://zavalab.engr.wisc.edu
Proof. The market is cleared by construction, because the balance constraints (3.42b) are satisﬁed
at any solution. Furthermore, (3.48) shows that the market clearing formulation (3.42) delivers an
optimal price and allocation that maximize the proﬁt for all players. □
Theorem 3.2. The clearing formulation (3.42) delivers an allocation and prices that satisfy revenue adequacy.
Proof. The following power balance holds at each space-time node:
X
k∈Krec
n
fk,t +
X
i∈Sn
pi,t +
X
v∈Vsnd
n,t
δv −
X
k∈Ksnd
n
fk,t −
X
j∈Dn
dj,t −
X
v∈Vrec
n,t
δv = 0
Multiplying both sides by the corresponding space-time nodal price and summing over all space-
time nodes, we obtain:
X
n∈N,t∈T
πn,t
 X
k∈Krec
n
fk,t +
X
i∈Sn
pi,t +
X
v∈Vsnd
n,t
δv −
X
k∈Ksnd
n
fk,t −
X
j∈Dn
dj,t −
X
v∈Vrec
n,t
δv

= 0.
This can be rewritten as:
X
j∈D,t∈T
πn(j),tdj,t
=
X
i∈S,t∈T
πn(i),tpi,t +
X
n∈N,t∈T
πn,t
 X
k∈Krec
n
fk,t +
X
v∈Vsnd
n,t
δv −
X
k∈Ksnd
n
fk,t −
X
v∈Vrec
n,t
δv

=
X
i∈S,t∈T
πn(i),tpi,t +
X
k∈K,t∈T
(πrec(k),t −πsnd(k),t)fk,t +
X
v∈V
(πsnd(v) −πrec(v))δv
The summation on the left-hand side represents the total payment by all loads, while the summations
on the right-hand side represent the revenue for suppliers, transmission service provides, and virtual
links (service providers), respectively. This establishes revenue adequacy. □
Theorem 3.3. The clearing formulation (3.42) delivers an allocation and prices that guarantee cost recovery
for all players.
Proof. Consider the allocation (p∗, d∗, f∗, δ∗
v) and duals (π∗, ω∗); we need to show that
φp
i,t(π∗
n(i),t, αp
i,t, p∗
i,t) ≥0
(3.49a)
φd
j,t(ˆπ∗
n(j),t, αd
j,t, d∗
j) ≥0
(3.49b)
φδ
v(ˆπ∗
rec(v), ˆπ∗
snd(v), αδ
v, δ∗
v) ≥0
(3.49c)
X
k∈K
φf
k,t(π∗
rec(k),t, π∗
snd(k),t, αf
k,t, f∗
k,t) ≥0.
(3.49d)
For the inner problem of (3.47), (p, d, f, θ, δ) = (0, 0, 0, 0, 0) is a feasible point (for any (π, ω)). For ﬁxed
(π, ω), the inner problem is equivalent to maximizing individual proﬁt functions in (3.48); therefore,
(3.49) hold. □
One can easily show that increasing load-shifting ﬂexibility leads to a higher total social surplus.
The intuition is that, with more ﬂexibility is offered by DaCes, the ISO has more options to match
demand and supplies across space-time. We use the notation M(V, ¯δ) to represent the market clearing
problem (3.42) in parametric form; the problem is a function of the set of virtual links V and virtual
link capacities ¯δ. We denote the corresponding optimal social surplus value as φ(V, ¯δ). The following
result formalizes this observation.
24

---

## Page 25

http://zavalab.engr.wisc.edu
Theorem 3.4. The social surplus satisﬁes φ(V, ¯δ) ≥φ(V+, ¯δ+) if V ⊆V+ and ¯δv ≤¯δ+
v for all v ∈V.
Proof. Let (d, p, f, θ, δ) be a feasible solution of M(V, ¯δ); the nodal balance constraints, and capacity
constraints for d, p, θ remain unchanged for M(V+, ¯δ+) and therefore are satisﬁed by (d, p, f, θ, δ).
The solution δv satisﬁes the virtual link capacity constraints of M(V+, ¯δ+) because v ∈V ⊆V+, and
0 ≤δv ≤¯δv ≤¯δ+
v . Therefore, (d, p, f, θ, δ) is feasible for M(V+, ¯δ+) and φ(V+, ¯δ+) ≤φ(V, ¯δ). □
3.2
Pricing Properties
We now investigate how virtual links affect price behavior. We begin by showing that the nodal
prices are bounded by the bid prices of cleared players. We denote (p∗, d∗, f∗, θ∗, δ∗) and (π∗, ω∗) as
the optimal primal-dual allocation. At each space-time node, we deﬁne the set of cleared suppliers
S∗
n,t := {i ∈Sn | p∗
i,t > 0}, and loads D∗
n,t := {j ∈Dn | d∗
j,t > 0}.
Theorem 3.5. If S∗
n,t and D∗
n,t are non-empty for (n, t) ∈N × T , the optimal prices satisfy:
max
i∈S∗
n,t
αp
i,t ≤π∗
n,t ≤min
j∈D∗
n,t
(αd
j,t −ω∗
n(j),t)
(3.50)
Proof. From Theorem 3.3 we have that: φd
j,t(π∗
j(n),t, αd
j,t, d∗
j,t) ≥0, φp
i,t(π∗
i(n),t, αp
i,t, p∗
i,t) ≥0 holds for
any j ∈Dn,t, i ∈Sn,t; consequently,
(αd
j,t −ˆπ∗
n(j),t)d∗
j,t ≥0
(π∗
n(i),t −αp
i,t)p∗
i,t ≥0.
For any j ∈D∗
n,t we have that d∗
j,t > 0; we thus have αd
j,t −ω∗
n(j),t ≥π∗
n,t. Similarly, π∗
n,t ≥αp
i,t for any
i ∈S∗
n,t and thus:
max
i∈S∗n
αp
i,t ≤π∗
n,t ≤min
j∈D∗n
(αd
j,t −ω∗
n(j),t)
This result shows that cleared suppliers and consumers deﬁne the bounds for the LMP values.
On the load side, we see that the price bound is on the adjusted price (effect of the shifting capacity
constrains). If ω∗
n(j),t > 0 we have that the load is not desired at the node and therefore its value
αd
j,t −ω∗
n(j),t is decreased; if ω∗
n(j),t < 0 we have that the load is desired at the node and therefore its
value αd
j,t −ω∗
n(j),t is increased. If the net dual If the computing capacity constraints are not active,
the LMPs are bounded by the load bid prices.
From cost recovery for virtual links, we have (ˆπ∗
snd(v) −ˆπ∗
rec(v) −αδ
v)δ∗
v ≥0 and thus:
δ∗
v > 0
⇒
ˆπ∗
snd(v) −ˆπ∗
rec(v) ≥αδ
v.
(3.51)
This indicates that a virtual link is used only if the price difference between the receiving node and
sending node is high enough to overcome its load-shifting cost (bid price). On the other hand, if the
price difference is lower than the bid price, the virtual link will not be used. In short, the virtual link
25

---

## Page 26

http://zavalab.engr.wisc.edu
bid price (shifting cost) deﬁnes the minimum incentive to activate virtual links.
We have shown that each virtual link v ∈V solves the problem
max
δv∈[0,¯δv]φδ
v(πrec(v), πsnd(v), αδ
v, δv).
(3.52)
The optimal solution of this problem satisﬁes:
ˆπ∗
snd(v) −ˆπ∗
rec(v) > αδ
v
⇒
δ∗
v = ¯δv
(3.53a)
δ∗
v ∈(0, ¯δv)
⇒
ˆπ∗
snd(v) −ˆπ∗
rec(v) = αδ
v
(3.53b)
These results are analogous to congestion (friction) behavior observed in physical transmission net-
works. Speciﬁcally, the price difference between the supporting nodes of a virtual link equals the
shifting cost when the virtual ﬂow has not hit is capacity bound; this implies that, when the shift cost
is zero, the prices of the supporting nodes will be the same (this helps homogenize LMPs). On the
other hand, when the virtual ﬂow hits it capacity limit, the price difference is bounded by the shift
cost; since the shift cost is non-negative, we can see that price at the receiving node will be less than
(or equal) that of the sending node. In other words, the receiving node cannot be higher (otherwise
there is no incentive to shift load).
A key difference between virtual ﬂows and physical ﬂows is that the former are not subject to any
DC network constraints; as such, the only source of congestion for the virtual links is their capacity
constraint. Note also that virtual ﬂows can travel in space-time; while physical ﬂows can only travel
in space; as such, virtual ﬂows can be used to mitigate space-time price variability.
We note that DaCes receive the adjusted prices π + ω (due to the presence of computing capacity
constraints); the duals ω thus play a key role that we now explain. Because ωu
n,t · ωl
n,t = 0 for any
space-time node n, t (they are complementary), we have the following interpretation for possible
values of ω:
• ωn,t = 0: ωu
n,t = 0 and ωl
n,t = 0. The incentive for submitting or shifting a load into space-time
node (n, t) is dependent on the LMPs π alone.
• ωn,t > 0: ωu
n,t > 0 and ωl
n,t = 0. The upper bound is active, which means the computing
resource is scarce at (n, t). Loads submitted at and shifted into (n, t) will compete for this scarce
computing resource. On the other hand, virtual links ﬂowing outward are incentivized to shift
more load.
• ωn,t < 0: ωu
n,t = 0 and ωl
n,t < 0. The lower bound is active, which means no loads are physically
cleared at (n, t). The DaCe thus have a higher incentive to submit loads at (n, t), and virtual
links have a higher incentive to shift loads into (n, t). On the other hand, virtual links shifting
out will compete for loads to shift.
We now explore the effect of increasing DaCe ﬂexibility on the clearing outcomes. For simplicity,
we write the Lagrangian dual problem as:
max
π,ω
D(π, ω),
(3.54)
26

---

## Page 27

http://zavalab.engr.wisc.edu
where:
D(π, ω) :=
min
(d,p,θ,δ)∈C,f∈F L(d, p, f, θ, δ, π, ω)
(3.55)
To establish properties that describe the impact of adding virtual link capacity on the prices, we
inspect what happens to the solution of the clearing problem if we increase the capacity of one virtual
link v ∈V by some amount ϵ > 0. The capacity of v is expressed as ¯δv = ¯δ0
v +ϵ, where ¯δ0
v is the original
(base) capacity. We denote the Lagrangian dual problem with capacity ¯δv = ¯δ0
v + ϵ as:
max
π,ω Dϵ(π, ω).
(3.56)
We refer to this problem as M(ϵ) and denote a primal-dual solution as (p∗ϵ, d∗ϵ, f∗ϵ, θ∗ϵ, δ∗ϵ, π∗ϵ, ω∗ϵ).
Note that (p∗0, d∗0, f∗0, θ∗0, δ∗0, π∗0, ω∗0) is an optimal solution of the base problem M(0).
We proceed to analyze the effect of incorporating additional ﬂexibility of DaCes. We begin with
the case of adding capacity to a virtual link that is not congested. Intuitively, adding capacity to
such a link should not beneﬁt the DaCe. Our analysis shows that the unit proﬁt for the shift (price
difference between its supporting nodes minus its shift cost) does not change. The following result
establishes this property.
Theorem 3.6. If δ∗0
v < ¯δ0
v then, for any ϵ > 0, we have that:
ˆπ∗ϵ
snd(v) −ˆπ∗ϵ
rec(v) −αδ
v = ˆπ∗0
snd(v) −ˆπ∗0
rec(v) −αδ
v.
(3.57)
Proof. Proof: If δ∗0
v < ¯δ0
v, then ˆπ∗0
snd(v) −ˆπ∗0
rec(v) ≤αδ
v, and thus:
φδ∗0
v
= (ˆπ∗0
snd(v) −ˆπ∗0
rec(v) −αδ
v)δ∗0
v = 0.
This means Dϵ(π∗0, ω∗0) = D0(π∗0, ω∗0) since all other proﬁt values remain unchanged, which implies
that (p∗0, d∗0, δ∗0, f∗0, θ∗0) also solves of Dϵ(π∗0, ω∗0). We now look at an arbitrary (π, ω)̸ = (π∗0, ω∗0).
By optimality of M(0), we have that Dϵ(π∗0, ω∗0) = D0(π∗0, ω∗0) ≥D0(π, ω). For any (π, ω), any
feasible point of D0(π, ω) is feasible for Dϵ(π, ω). This implies Dϵ(π, ω) ≤D0(π, ω) ≤Dϵ(π∗0, ω∗0);
thus, (p∗0, d∗0, f∗0, θ∗0, δ∗0, π∗0, ω∗0) solves M(ϵ). This implies that (3.57) holds. □
We now focus on the more interesting case of adding capacity to a congested virtual link. Specif-
ically, we show that the unit proﬁt decreases with capacity.
Theorem 3.7. If δ∗0
v = ¯δ0
v then, for any ϵ > 0, we have that:
ˆπ∗ϵ
snd(v) −ˆπ∗ϵ
rec(v) −αδ
v ≤ˆπ∗0
snd(v) −ˆπ∗0
rec(v) −αδ
v.
(3.58)
Furthermore, for any ϵ2 > ϵ1 > 0,
ˆπ∗ϵ2
snd(v) −ˆπ∗ϵ2
rec(v) −αδ
v ≤ˆπ∗ϵ1
snd(v) −ˆπ∗ϵ1
rec(v) −αδ
v
(3.59)
Proof. Proof: If (3.58) holds, then (3.59) holds by setting ¯δv = ¯δ0
v + ϵ1 as the base case, and setting
ϵ = ϵ2−ϵ1. We now prove (3.58); let ∆∗
v := ˆπ∗0
snd(v)−ˆπ∗0
rec(v)−αδ
v > 0 be the unit proﬁt of virtual link v in
the base solution. Assume that (π, ω) satisﬁes ∆v(ˆπ) > ∆∗
v, where ∆v(ˆπ) := ˆπsnd(v) −ˆπrec(v) −αδ
v is the
27

---

## Page 28

http://zavalab.engr.wisc.edu
unit proﬁt of v at price ˆπ. We show that (π, ω) is not optimal. By optimality of M(0), D0(π∗0, ω∗0) ≥
D0(π, ω) for any (π, ω). At (π∗0, ω∗0), δ∗0
v
= ¯δ0
v + ϵ since ∆∗
v > 0, and the optimal values of all other
proﬁt terms remain unchanged. Thus,
D0(π∗0, ω∗0) −Dϵ(π∗0, ω∗0) = ∆∗
v(¯δ0
v + ϵ) −∆∗
v¯δ0
v = ∆∗
vϵ
The same reasoning holds for (π, ω) that satisﬁes ∆v(ˆπ) > 0; we have:
D0(π, ω) −Dϵ(π, ω) = ∆v(ˆπ)ϵ,
then we have:
Dϵ(π∗0, ω∗0) −Dϵ(π, ω)
=(D0(π, ω) −Dϵ(π, ω)) −(D0(π∗0, ω∗0) −Dϵ(π∗0, ω∗0)) + (D0(π∗0, ω∗0) −D0(π, ω))
=∆v(ˆπ)ϵ −∆∗
vϵ + D0(π∗0, ω∗0) −D0(π, ω)
=(∆v(ˆπ) −∆∗
v)ϵ + D0(π∗0, ω∗0) −D0(π, ω)
>0
where the last inequality holds because ∆v(ˆπ) > ∆∗
v, D0(π∗0, ω∗0) ≥D0(π, ω), and (π∗0, ω∗0) solves
M(0). Since this holds for arbitrary (π, ω) such that ∆v(ˆπ) > ∆∗
v, we conclude that:
ˆπ∗ϵ
snd(v) −ˆπ∗ϵ
rec(v) ≤ˆπ∗0
snd(v) −ˆπ∗0
rec(v),
which implies (3.58). □
Theorem 3.7 indicates that increasing virtual link capacity has the effect of reducing the price
difference between space-time nodes that support the virtual links. We note, however, that the ability
of virtual links to reduce price volatility might be affected by computing capacity constraints (as the
duals ω might distort the prices in a manner that is difﬁcult to predict). Moreover, we note that
Theorem 3.7 does not guarantee convergence of the price difference to a speciﬁc value. To address
these issues, we now proceed to show that, when the capacity of a virtual link is sufﬁciently large,
the price difference between the supporting nodes is bounded by the link shift cost. As such, the
price difference can be made arbitrarily small as the shift cost is made arbitrarily small. In order to
study this convergence behavior, we apply subgradient analysis to problem (3.47). A brief review of
subgradient analysis and nonsmooth optimization is provided in the Appendix A.
We recall that minimizing the Lagrange function with respect to allocation variables is equivalent
to individual proﬁt maximization; we exploit this property to write out the optimal proﬁt of each
player as a function of (π, ω):
φd∗
j,t(ˆπn(j),t) = max{(αd
j,t −ˆπn(j),t) ¯dj,t, 0} = |αd
j,t −ˆπn(j),t|+ ¯dj,t
(3.60a)
φp∗
i,t(πn(i),t) = max{(πn(i),t −αp
i,t)¯pi,t, 0} = |πn(i),t −αp
i,t|+¯pi,t
(3.60b)
φδ∗
v (ˆπsnd(v), ˆπrec(v)) = max{(ˆπsnd(v) −ˆπrec(v) −αδ
v)¯δv, 0} = |ˆπsnd(v) −ˆπrec(v) −αδ
v|+¯δv
(3.60c)
φf∗
t (π) = maxft∈Ft
X
k∈K
(πrec(k),t −πsnd(k),t −αf
k,t)fk,t
(3.60d)
28

---

## Page 29

http://zavalab.engr.wisc.edu
where | · |+ := max{·, 0}. The Lagrangian dual function is thus:
D(π, ω) = −
X
t∈T
 X
j∈D
φd∗
j,t +
X
i∈S
φp∗
i,t + φf∗
t

−
X
v∈V
φδ∗
v .
(3.61)
Using linearity of subdifferential operator, we calculate the subgradient of this function with respect
to each element of an arbitrary price π as follows:
∂πn,tD = −



X
j∈Dn
∂πn,tφd∗
j,t +
X
i∈Sn
∂πn,tφp∗
i,t +
X
v∈Vrec
n,t∪Vsnd
n,t
∂πn,tφδ∗
v + ∂πn,tφf∗
t


.
Here, + denotes the Minkowski sum and the individual subgradient terms are:
∂πn(i),tφp∗
i,t =









{0}, ˆπn(i) < αp
i
{¯pi}, ˆπn(i) > αp
i
[0, ¯pi], ˆπn(i) = αp
i
∂πn(j),tφd∗
j,t =









{−¯dj}, πn(j) < αd
j
{0}, πn(j) > αd
j
[−¯dj, 0], πn(j) = αd
j
∂πrec(v)φδ∗
v =









{0}, ˆπsnd(v) −ˆπrec(v) −αδ
v < 0
{−¯δv}, ˆπsnd(v) −ˆπrec(v) −αδ
v > 0
[−¯δv, 0], ˆπsnd(v) −ˆπrec(v) −αδ
v = 0
∂πsnd(v)φδ∗
v =









{0}, ˆπsnd(v) −ˆπrec(v) −αδ
v < 0
{¯δv}, ˆπsnd(v) −ˆπrec(v) −αδ
v > 0
[0, ¯δv], ˆπsnd(v) −ˆπrec(v) −αδ
v = 0
It is difﬁcult (if not impossible) to derive an analytic form for ∂πn,tφf∗
t
(due to the presence of DC
constraints). For the following analysis, however, we only need to assume that ∂πn,tφf∗
t
is bounded.
We now show the effect of increasing virtual shift capacity; in short, the virtual link capacity has a
critical point beyond which the difference of π + ω between the connected space-time nodes will be
bounded by its bid price. Once the virtual link capacity reaches this critical point, additional capacity
will not be used by the market.
Theorem 3.8. Assume ∂πn,tφf∗
t
is bounded for any π; then, for any v ∈V, ∃Mv > 0 such that, if ϵ > Mv:
ˆπ∗ϵ
snd(v) −ˆπ∗ϵ
rec(v) ≤αδ
v
Proof. Proof: Consider an arbitrary virtual link v, the optimality conditions require that:
0 ∈∂πsnd(v)Dϵ(π∗ϵ, ω∗ϵ)
0 ∈∂πrec(v)Dϵ(π∗ϵ, ω∗ϵ)
29

---

## Page 30

http://zavalab.engr.wisc.edu
Each term in the subgradient is an interval of possibly zero length. When the capacity of v in-
creases, all terms remain constant except for the subgradient terms ∂πsnd(v)φδ∗
v and ∂πrec(v)φδ∗
v . This
allows us to write the sum of all other terms as constant intervals, which we denote [a−, a+] for
∂πsnd(v)Dϵ and [b−, b+] for ∂πrec(v)Dϵ, respectively. Then the subgradients can be expressed as
∂πsnd(v)Dϵ = −

[a−, a+] + ∂πsnd(v)φδ∗
v

∂πrec(v)Dϵ = −

[b−, b+] + ∂πrec(v)φδ∗
v

Let Mv = max{−a−−¯δ0
v, b+ −¯δ0
v, 0} and suppose ϵ > Mv. Given arbitrary duals (π, ω) that satisfy
ˆπsnd(v) −ˆπrec(v) > αδ
v, we show that π does not satisfy the optimality condition for M(ϵ) if ϵ > Mv. If
πsnd(v) + ωsnd(v) −πrec(v) −ωrec(v) −αδ
v > 0, then the subgradients at the supporting nodes become:
∂πsnd(v)Dϵ ⊆[−a+ −¯δ0
v −ϵ, −a−−¯δ0
v −ϵ]
∂πrec(v)Dϵ ⊆[−b+ + ¯δ0
v + ϵ, −b−+ ¯δ0
v + ϵ]
By deﬁnition of Mv, we have:
−a−−¯δ0
v −ϵ < −a−−¯δ0
v + a−+ ¯δ0
v = 0
−b+ + ¯δ0
v + ϵ > −b+ + ¯δ0
v + b+ −¯δ0
v = 0
This means that the lower bound of ∂πrec(v)Dϵ is strictly positive, and the upper bound of ∂πsnd(v)g is
strictly negative. Therefore, 0 /∈∂πrec(v)Dϵ, 0 /∈∂πsnd(v)g, which implies (π, ω) is not optimal. □
Theorem 3.8 shows that the price difference is eventually bounded by the shift cost in the limit of
high virtual link capacity. This result is key, as it shows that virtual links can help homogenize prices
(by controlling price differences). It is important to highlight that the price differences exploited by
virtual links traverse space and time and thus spatial and temporal price variability can be mitigated.
The ability to control price differences across space and time is a key beneﬁt over power transmission
(which only exploits spatial price differences). Moreover, one could argue that it is easier to expand
virtual link capacity (by installing more DaCes) than it is to install more transmission lines.
A rigorous proof of price convergence is established here for the market clearing formulation
(3.42), which is quite general but also does not account for other features encountered in practice (e.g.,
ramping constraints and AC power ﬂows). A rigorous analysis of more sophisticated formulations
is challenging and is left as a topic of future work. However, we have observed empirically that
similar properties are observed in more complex formulations (in the next section we illustrate how
temporal virtual links mitigate price volatility introduced by ramping constraints).
4
Computational Studies
In this section we present case studies to demonstrate the various beneﬁts of using the virtual link
paradigm for capturing DaCe ﬂexibility. All our models were implemented in JuMP Dunning et al.
(2017) and were solved using Gurobi Optimization (2019). We ﬁrst analyze a small-scale model to
illustrate the key results and then analyze a large-scale model to show that the results and insights
30

---

## Page 31

http://zavalab.engr.wisc.edu
are scalable. All scripts needed to reproduce the results can be found in https://github.com/
zavalab/JuliaBox/tree/master/VirtualLinks.
Figure 7: Scheme for 7-bus system (small generators co-located with DaCes not shown).
4.1
7-Bus Spatial System
We consider a 7-bus system at a ﬁxed time, sketched in Figure 7. Four DaCes, owned and operated
by a single market player, are distributed at nodes {2, 3, 6, 7}. Their bid prices and capacities are
{10, 10, 15, 15} $/MWh and {13, 17, 17, 13} MWh, respectively. Each DaCe has a computing capacity
of 20 MWh and is co-located with a small and expensive generator with bid price αp = 3 $/MWh
and capacity 5 MWh. In addition, nodes 2 and 4 are connected to a large generator with bid price
αp = 1 $/MWh and capacity 20 MWh. The transmission network topology is highlighted using solid
lines in Figure 7. Each line has a capacity of 10 MWh and a bid cost 0.1 $/MWh.
We considered three scenarios with different virtual link capacity levels. The results are summa-
rized in Table 1. Scenario 1 represents the base case in which no virtual links are used. Scenario 2
accounts for virtual links (1, 7) and (7, 1), both with capacity 5 MWh and bid cost 0.3 $/MWh. Sce-
nario 3 is a replicate of scenario 2, except the capacity is set as 10 MWh. Scenario 4, on top of virtual
links in scenario 2, includes additional virtual links (1, 3) and (3, 1), both with capacity 5 MWh and
bid cost 0.3 $/MWh. Scenario 5 is a replicate of scenario 4, except the capacity is set as 10 MWh.
Scenario 6 is a replicate of scenario 5, except that the computing capacity for each DaCe is increased
from 20 MWh to 25 MWh. Scenario 7 is a replicate of scenario 6, except that the bid costs of all virtual
links are reduced to 0.
Results for price behavior are summarized in Table 1. Here, φ represents the social surplus in
units of USD ($). In the base case, the LMPs show clustered patterns, where nodes in the same
31

---

## Page 32

http://zavalab.engr.wisc.edu
Table 1: Results for 7-bus system. Symbol φ denotes the social surplus. The surplus and dual vari-
ables are in units of USD ($).
Scenario
φ
[π1, π2, π3]
π4
[π5, π6, π7]
[ω2, ω3, ω6, ω7]
P dj (MWh)
1
522
[3, 1, 2]
1
[14.9, 15, 15]
[0, 0, 0, 0]
50
2
577.36
[5, 1, 3]
2.9
[14.87, 15, 14.93]
[0, 0, 0, 0]
55
3
605.533
[10, 1, 5.5]
1
[10.233, 10.367, 10.3]
[0, 0, 0, 0]
56
4
582.467
[3, 2.4, 2.7]
2.6
[14.867, 15, 14.933]
[0, 0, 0, 0]
55
5
618.133
[10, 1, 5.5]
5.4
[10.233, 10.367, 10.3]
[0, 4.2, 0, 0]
57.5
6
639.133
[3.3, 2.7, 3]
2.9
[3.533, 3.667, 3.6]
[0, 0, 0, 0]
60
7
644.533
[3, 1, 3]
1
[2.933, 3.067, 3]
[0, 0, 0, 0]
60
Table 2: DaCe load payments and revenues for different players (in $)
Scenario
Total Load Payments
Transmission
Suppliers
Virtual Links
Total Revenue
1
373
180
193
0
373
2
490.13
181.8
258.67
49.67
490.13
3
493.63
273.8
216.83
3
493.63
4
459.03
133.8
264.67
60.57
459.03
5
508.63
185.8
306.33
16.5
508.63
6
203.03
17.8
179.83
5.4
203.03
7
181.13
80.8
100.33
0
181.13
Table 3: Proﬁt for market players (in $, S# denotes supplier at node #)
Scenario
DaCe Load
Virtual Links
Transmission
S2
S4
1
50
0
175
0
0
2
55
48.17
176.77
0
38
3
56
0
268.33
0
0
4
55
58.17
128.67
28
32
4
57.5
0
180.33
0
88
4
60
0
12.33
34
38
5
60
0
75.33
0
0
32

---

## Page 33

http://zavalab.engr.wisc.edu
cycle share similar prices. We also observe a large price difference between nodes in the separate
cycles. In scenarios 2 and 3, the virtual link connects across the two cycles (via node 1 and node
7) to exploit the price difference in between. We see that the price gap between node 1 and node 7
is reduced to 0.3 $/MWh in scenario 3, exactly the bid price of the virtual link, as predicted by the
pricing properties. We also run scenario 3 with ¯δ = 1000 MWh, which gives back the same primal
and dual optimal solutions except for the price at node 4 due to degeneracy. We note that the LMP
at node 3 also approaches the LMPs of the other cycle even though there is no virtual link connected
at node 3 yet. Similarly, the LMPs of nodes 5 and 6 come down to around 10 $/MWh with node 7
without virtual links directed connected. Because of the DC power ﬂow constraints, the addition of
virtual links alter the LMPs of not just the connected nodes, but also neighboring nodes in the same
cluster. The values of ω for scenarios 1 and 2 are zero, meaning that computing capacity constraints
are inactive. Scenario 5 shows a case where the addition of a virtual link within cluster {1, 2, 3} does
not change the prices (compared with scenario 3), even if the price difference between the connected
nodes is much higher than the bid cost. The reason is that computing capacity constraint is active
at the destination node of the newly added virtual link (node 3) , as shown by the nonzero value
of ω3. However, if the computing capacity constraints are not binding (as in scenarios 6 and 7), the
price difference within the cluster {1, 2, 3} becomes much smaller. In scenario 6, the price gaps across
virtual links (|π1 −π3| and |π1 −π7|) are exactly the bid cost of the virtual links, meaning that the price
gaps converge to the best case. As an extreme case, scenario 7 shows that the prices [π1, π3, π7] become
homogeneous when the bid costs are zero. These results are consistent with the pricing properties
established and show how virtual links provide a mechanism to help mitigate spatial variability of
prices.
Table 2 summarizes results for load payments and revenues. These results verify that revenue ad-
equacy holds for our proposed market clearing formulation. Table 3 summarizes results for proﬁts for
different market stakeholders. The results verify that the clearing formulation satisﬁes cost recovery
in all scenarios. Furthermore, we notice that virtual link proﬁts are strictly positive and comparable to
proﬁts of load clearing in scenarios 2 and 4, but zero otherwise. This shows that virtual links provide
an extra revenue stream when price volatility is high (there exist large price differences to exploit).
Another interesting observation from scenarios 2 and 4 is that, when the amount of total cleared load
is the same, more ﬂexibility leads to lower load payments and higher virtual link revenue because
the extra ﬂexibility from a new virtual link provides more ways to clear the DaCe loads. This is not
necessarily true when the total amount of cleared loads is different, though, because clearing more
load might need to use more expensive power suppliers from the grid. When too much ﬂexibility is
provided, however, DaCes could beneﬁt from a lower price, as shown by scenarios 6 and 7 in Table
2, but will lose the virtual link revenue streams (because of low price volatility).
4.2
1-Bus Temporal System
We now consider a single DaCe co-located with one generator over a time horizon of 4 points. The
setup is a modiﬁcation of the temporal case shown in Zhang et al. (2020). The system is sketched in
Figure 8. At each time interval, the DaCe can receive loads shifted from the previous time interval
33

---

## Page 34

http://zavalab.engr.wisc.edu
Figure 8: Scheme for 4-time system.
and delay loads to some later time interval, thus providing temporal ﬂexibility (similar to that of a
storage system). As boundary conditions, the DaCe does not receive loads at t = t1, and does not
delay loads at t = 4. The load capacity and bid costs of loads and supplies change with time. The
system thus has T = 4 time nodes and we consider 4 virtual links V := {(1, 2), (1, 3), (1, 4), (3, 4)}.
The supplier capacities are set to ¯p = {50, 50, 50, 50}, load capacities to ¯d = {70, 25, 70, 40}, supplier
bidding costs to αp = {10, 20, 10, 15}, and load bidding prices to αd = {30, 60, 40, 50}. We ﬁx the
bidding cost for virtual links as αδ = {3, 3, 3, 3}. To create extreme temporal prices differences (often
seen in real systems), we also incorporate a set of ramp limit constraints |pt+1 −pt| ≤15.
Table 4: Results for one-bus network with temporal shifting ﬂexibility.
Scenario
¯δ (MWh)
φ ($)
π ($/MWh)
d (MWh)
p (MWh)
δ (MWh)
1
[0,0,0,0]
4400
[30,-30,40,15]
[40,25,40,40]
[40,25,40,40]
[0,0,0,0]
2
[8,0,0,0]
4856
[30,-30,40,15]
[56,25,48,40]
[48,33,48,40]
[8,0,0,0]
3
[10,0,0,0]
4970
[30,20,40,15]
[60,25,50,40]
[50,35,50,40]
[10,0,0,0]
4
[21,0,0,0]
5040
[23,20,40,15]
[70,25,50,40]
[50,45,50,40]
[20,0,0,0]
5
[21,20,0,0]
5040
[23,20,40,15]
[70,25,50,40]
[50,45,50,40]
[20,0,0,0]
6
[11,0,11,0]
5090
[23,20,40,20]
[70,25,50,40]
[50,35,50,50]
[10,0,10,0]
7
[11,0,11,10]
5197
[30,20,40,27]
[61,25,60,40]
[50,36,50,50]
[11,0,0,10]
8
[11,0,11,20]
5197
[30,20,40,37]
[61,25,60,40]
[50,36,50,50]
[11,0,0,10]
9
[21,0,11,20]
5260
[23,20,40,37]
[70,25,60,40]
[50,45,50,50]
[20,0,0,10]
Nine scenarios with different temporal shifting capacities are presented in Table 4. The results
are analogous to those observed in the spatial 7-bus case and highlights how virtual links facilitate
treating space and time dimensions in a uniﬁed manner. Speciﬁcally, the social surplus and the total
amount of delivered loads increase with increasing shifting capacity. Price variability also becomes
smaller with increasing shifting capacity. In the limit of high shifting capacity, prices converge and the
differences between time nodes are bounded by the shifting cost, similar to the results of scenario 3 in
the 7-bus system. Note that scenarios 1 and 2 has a negative LMP caused by the ramping limit, which
is relieved by virtual links in other scenarios. Another interesting observation arises from scenarios
1 to 3, where a virtual link between t1 and t2 increases the amount of load cleared at t3. These
34

---

## Page 35

http://zavalab.engr.wisc.edu
Table 5: Total payments and revenue for market players (in units of $).
Scenario
Load Payments
Suppliers
Virtual Links
Total Revenue
1
2650
2650
0
2650
2
3450
2970
480
3450
3
4900
4800
100
4900
4
4710
4650
60
4710
5
4710
4650
60
4710
6
4910
4850
60
4910
7
5810
5570
240
5810
8
6210
6070
140
6210
9
5990
5900
90
5990
Table 6: DaCe loads and virtual link and supplier proﬁts (in units of $).
Scenario
Loads Proﬁt
Virtual Links Proﬁt
Suppliers Proﬁt
1
3650
0
750
2
3650
456
750
3
2400
70
2500
4
2890
0
2150
5
2890
0
2150
6
2690
0
2400
7
1920
177
3100
8
1520
77
3600
9
2010
0
3250
35

---

## Page 36

http://zavalab.engr.wisc.edu
results show how temporal ﬂexibility is able to relieve ramping constraints (analogous to how spatial
ﬂexibility relieves network transmission constraints). However, because temporal shifts only move
in the direction of increasing time, their effects on price gaps are also unidirectional. Speciﬁcally,
temporal shifts can only exploit lower prices in later times; for instance, scenarios 4 and 5 show that
adding virtual link (1, 3) does not change the solution since the price at node 2 is higher than that at
node 3.
Table 5 summarizes the payment and revenue results for the temporal case. We observe that
revenue adequacy is satisﬁed for all scenarios. Table 6 summarizes the proﬁt results for the temporal
case. We observe that the clearing formulation satisﬁes cost recovery, since no participant incurs a
negative proﬁt in all scenarios. Furthermore, similar to the spatial system, the revenues and proﬁts
generated via virtual links become larger when there is more price volatility in the system.
4.3
Space-Time IEEE-30 Bus System
We now consider a modiﬁed version of the IEEE 30-bus system. The network topology is presented
in Figure 9. Each square node is connected to a load with varying demand capacity in time. The loads
bid with the same price (200 $/MWh) and different capacity levels. A total of six of these loads are
DaCes owned by the same entity, distributed at 6 different nodes as shown in Figure 9. We run the
space-time market clearing model over T = 24 hours. Virtual links are assigned as follows: a virtual
link is assigned from one DaCes at one time, either to itself at a later time, or to another DaCe at the
same time or a later time. Each virtual link has a bid price of 0 $/MWh and capacity of 20 MWh. The
two suppliers are designated with a ﬁxed cost and capacity over the time horizon.
1
2
5
6
7
8
9
10
11
12
13
14
15
19
21
22
24
25
27
28
30
3
4
16
17
18
20
23
26
29
Figure 9: Scheme of IEEE 30-bus system. Squared nodes are connected to a load. Dashed curves are
virtual links (not all virtual links are shown for clarity).
36

---

## Page 37

http://zavalab.engr.wisc.edu
The LMPs of the 30-bus system over the time horizon are plotted in Figure 10. We observe that
virtual links are able to drastically reduce both spatial and temporal price volatility. Speciﬁcally,
with no virtual links, we can observe prices reaching 200 $/MWh in 8 out of 24 time intervals, and
negative prices at 4 time intervals. Table 7 provide summarizing statistics for LMPs for both cases.
The range, standard deviation and average deviation are all much smaller for the case with virtual
links than the case with no virtual links. In addition, the case of no virtual links has a mean value
that is much higher than its median value, meaning that the LMP distribution is positively skewed
when there are no virtual links. The price convergence behavior can also be observed from the LMP
distribution shown in Figure 11. With virtual links, the LMPs become have less spread and exhibit a
higher frequency at around 50 $/MWh, compared to the case with no virtual links.
(a) No virtual links
(b) With virtual links
Figure 10: Price trajectories of all buses over time. Dashed lines denote nodes with DaCes.
Figure 11: Space-time LMPs distribution.
37

---

## Page 38

http://zavalab.engr.wisc.edu
Table 7: Summarizing statistics for LMPs of IEEE 30-bus case study (in units of $/MWh).
LMP Statistics
No virtual links
With virtual links
Mean
56.6
43.77
Median
44.21
44.22
Maximum
200.0
55.95
Minimum
-5.85
18.42
Standard Deviation
31.36
5.29
Average Deviation
21.3
2.32
5
Conclusions and Future Work
We have presented a market clearing formulation to capture space-time, load-shifting ﬂexibility pro-
vided by data centers. Load-shifting ﬂexibility is captured using the concept of virtual links, which
are non-physical pathways that can transfer power geographically and over time. We show that the
proposed market clearing formulation satisﬁes fundamental properties (it provides a competitive
equilibrium and satisﬁes revenue adequacy and cost recovery). Our analysis reveals that DaCes act
as prosumers that are remunerated for their provision of ﬂexibility; this remuneration is analogous to
that of transmission service providers (based on nodal price differences) but is unique in that it can
traverse space-time. Moreover, we show that load-shifting ﬂexibility can help mitigate space-time
price volatility; speciﬁcally, we show that prices can be made homogeneous as we increase ﬂexibility.
This new feature can be achieved because virtual links provide alternative pathways that can help
relieve physical transmission congestion. We present case studies that illustrate these effects. As
part of future work, we are interested in understanding how data center ﬂexibility could be used to
mitigate risk and maximize reliability. To do so, it is necessary to develop stochastic market clearing
formulations. Moreover, we are interested in understand the effect of load-shifting ﬂexibility on AC
power ﬂow systems and in understanding strategic bidding by DaCes that help exploit space-time
price differences.
Acknowledgments
We acknowledge support from the U.S. National Science Foundation under award 1832208.
References
Jamshid Aghaei and Mohammad-Iman Alizadeh. Demand response in smart electricity grids equipped with
renewable energy sources: A review. Renewable and Sustainable Energy Reviews, 18:64–72, 2013.
Andrew Allman and Qi Zhang. Dynamic location of modular manufacturing facilities with relocation of indi-
vidual modules. European Journal of Operational Research, 286(2):494–507, 2020.
38

---

## Page 39

http://zavalab.engr.wisc.edu
Adil Bagirov, Napsu Karmitsa, and Marko M M¨akel¨a. Introduction to Nonsmooth Optimization: theory, practice
and software. Springer, 2014.
Dimitris Bertsimas and John N Tsitsiklis. Introduction to linear optimization. Athena Scientiﬁc Belmont, MA,
1997.
Lucien Bobo, Lesia Mitridati, Josh A Taylor, Pierre Pinson, and Jalal Kazempour. Price-region bids in electricity
markets. European Journal of Operational Research, 2021.
Franc¸ois Bouffard, Francisco D Galiana, and Antonio J Conejo. Market-clearing with stochastic security-part i:
formulation. IEEE Trans. Power Syst., 20(4):1818–1826, 2005.
Xuanyu Cao, Junshan Zhang, and H. Vincent Poor. Data center demand response with on-site renewable
generation: A bargaining approach. IEEE/ACM Transactions on Networking, 26(6):2707–2720, 2018.
M. Carrion and J.M. Arroyo. A computationally efﬁcient mixed-integer linear formulation for the thermal unit
commitment problem. IEEE Transactions on Power Systems, 21(3):1371–1378, 2006.
California Public Utilities Commission. California renewables portfolio standard. https://www.cpuc.ca.
gov/renewables/, 2019. Accessed 2019-07-01.
Gustavo De Vivero-Serrano, Kenneth Bruninx, and Erik Delarue. Implications of bid structures on the offering
strategies of merchant energy storage systems. Applied Energy, 251:113375, 2019.
Iain Dunning, Joey Huchette, and Miles Lubin. Jump: A modeling language for mathematical optimization.
SIAM Review, 59(2):295–320, 2017.
Girish Ghatikar, Venkata Ganti, Nance Matson, and Mary Ann Piette. Demand response opportunities and
enabling technologies for data centers: Findings from ﬁeld studies, 2012.
Paul R. Gribik, Dhiman Chatterjee, Nivad Navid, and Li Zhang. Dealing with uncertainty in dispatching and
pricing in power markets. 2011 IEEE Power and Energy Society General Meeting, 2011.
Yuanxiong Guo, Hongning Li, and Miao Pan. Colocation data center demand response using nash bargaining
theory. IEEE Transactions on Smart Grid, 9(5):4017–4026, 2018.
LLC Gurobi Optimization. Gurobi optimizer reference manual, 2019. URL http://www.gurobi.com.
William W. Hogan. Contract networks for electric power transmission. Journal of Regulatory Economics, 4(3):
211–242, Sep 1992.
W.W. Hogan, E.G. Read, and B.J. Ring. Using mathematical programming for electricity spot pricing. Interna-
tional Transactions in Operational Research, 3(3-4):209–221, 1996.
Jalal Kazempour, Pierre Pinson, and Benjamin F Hobbs. A stochastic market design with revenue adequacy
and cost recovery by scenario: Beneﬁts and costs. IEEE Transactions on Power Systems, 33(4):3531–3545,
2018.
Kibaek Kim, Fan Yang, Victor M. Zavala, and Andrew A. Chien. Data centers as dispatchable loads to harness
stranded power. IEEE Transactions on Sustainable Energy, 8(1):208–218, 2017.
Yanchao Liu, Jesse T Holzer, and Michael C Ferris. Extending the bidding format to promote demand response.
Energy Policy, 86:82–92, 2015.
Zhenhua Liu, Adam Wierman, Yuan Chen, Benjamin Razon, and Niangjun Chen. Data center demand re-
sponse: Avoiding the coincident peak via workload shifting and local generation. Performance Evaluation,
70(10):770 – 791, 2013. Proceedings of IFIP Performance 2013 Conference.
Zhenhua Liu, Iris Liu, Steven Low, and Adam Wierman. Pricing data center demand response. ACM SIGMET-
RICS Performance Evaluation Review, 42(1):111–123, 2014.
39

---

## Page 40

http://zavalab.engr.wisc.edu
National Conference of State Legislatures. State renewable portfolio standards and goals. http://www.
ncsl.org/research/energy/renewable-portfolio-standards.aspx, 2019. Accessed 2019-
07-01.
Stig Ødegaard Ottesen, Asgeir Tomasgard, and Stein-Erik Fleten. Prosumer bidding and scheduling in elec-
tricity markets. Energy, 94:828–843, 2016.
Geoffrey Pritchard, Golbon Zakeri, and Andrew Philpott. A single-settlement, energy-only electric power
market for unpredictable and intermittent participants. Operations Research, 58(4-part-2):1210–1219, 2010.
Ana Radovanovic, Ross Koningstein, Ian Schneider, Bokan Chen, Alexandre Duarte, Binz Roy, Diyue Xiao,
Maya Haridasan, Patrick Hung, Nick Care, et al. Carbon-aware computing for datacenters. arXiv preprint
arXiv:2106.11750, 2021.
Lei Rao, Xue Liu, Le Xie, and Wenyu Liu. Minimizing electricity cost: Optimization of distributed internet
data centers in a multi-electricity-market environment. 2010 Proceedings IEEE INFOCOM, 2010.
Fred C Schweppe, Michael C Caramanis, Richard D Tabors, and Roger E Bohn.
Spot pricing of electricity.
Springer Science & Business Media, 1988.
Yue Shao and Victor M Zavala. Space-time dynamics of electricity markets incentivize technology decentral-
ization. Computers & Chemical Engineering, 127:31–40, 2019.
Collin Smith, Alfred K Hill, and Laura Torrente-Murciano. Current and future role of haber–bosch ammonia
in a carbon-free energy landscape. Energy & Environmental Science, 13(2):331–344, 2020.
Qihang Sun, Shaolei Ren, Chuan Wu, and Zongpeng Li. An online incentive mechanism for emergency de-
mand response in geo-distributed colocation data centers. In Proceedings of the Seventh International Con-
ference on Future Energy Systems, pages 3:1–3:13, New York, NY, USA, 2016. ACM.
Nguyen H. Tran, Dai H. Tran, Shaolei Ren, Zhu Han, Eui-Nam Huh, and Choong Seon Hong. How geo-
distributed data centers do demand response: A game-theoretic approach. IEEE Transactions on Smart
Grid, page 1, 2015.
Adam Wierman, Zhenhua Liu, Iris Liu, and Hamed Mohsenian-Rad. Opportunities and challenges for data
center demand response. IEEE Transactions on Smart Grid, 9:4017–4026, 2017.
Golbon Zakeri, Geoffrey Pritchard, Mette Bjorndal, and Endre Bjorndal. Pricing wind: a revenue adequate,
cost recovering uniform price auction for electricity markets with intermittent generation. INFORMS
Journal on Optimization, 1(1):35–48, 2019.
Victor M. Zavala, Kibaek Kim, Mihai Anitescu, and John Birge. A stochastic electricity market clearing formu-
lation with consistent pricing properties. Operations Research, 65(3):557–576, 2017.
Weiqi Zhang, Line A Roald, Andrew A Chien, John R Birge, and Victor M Zavala. Flexibility from networks
of data centers: A market clearing formulation with virtual links. Electric Power Systems Research, 189:
106723, 2020.
Ruiting Zhou, Zongpeng Li, and Chuan Wu. An online emergency demand response mechanism for cloud
computing. ACM Trans. Model. Perform. Eval. Comput. Syst., 3(1):5:1–5:25, February 2018.
40

---

## Page 41

http://zavalab.engr.wisc.edu
Appendices
A
Review on Non-Smooth Analysis
In this section we review tools of nonsmooth analysis that we use to establish price bounding prop-
erties. This discussion is based on Bagirov et al. (2014).
A.1
Deﬁnitions
We consider a function f : Rn →R that is convex but not necessarily differentiable. A vector g ∈Rn
is a subgradient of f at point x ∈Rn if for any y ∈Rn
f(y) ≥f(x) + gT (y −x).
(A.62)
The right hand side of (A.62) is a globally valid lower bound function for f that attains the exact
function value at point x. The subdifferential ∂f(x) of f at x is deﬁned as the set of all subgradients
at x:
∂f(x) = {g | f(y) ≥f(x) + gT (y −x) ∀y ∈Rn}.
(A.63)
In general, since convexity implies local Lipschitz continuity, ∂f(x) is a nonempty, convex and com-
pact set. As a special case, if f is continuously differentiable at x, then the gradient ∇f(x) is deﬁned
at x and the subdifferential becomes a singleton:
∂f(x) = {∇f(x)}.
(A.64)
A.2
Subgradient Calculus
We now summarize a set of basic rules for subgradient calculus. If f(x) = Pn
i=1 αifi(x), where αi ≥0
and fi is convex. Then the subdifferential of f is
∂f(x) =
n
X
i=1
αi∂fi(x)
(A.65)
where the + operator is the Minkowski sum operator for sets:
A + B = {a + b | a ∈A, b ∈B}
(A.66)
In our analysis we frequently encounter functions of the following form:
f(x) =
max
i∈{1,2,...n}{fi(x)}
(A.67)
where each fi : Rn →R is convex. The subdifferential of f is
∂f(x) = conv
[
i∈I(x)
∂fi(x)
(A.68)
41

---

## Page 42

http://zavalab.engr.wisc.edu
where conv(·) is the convex hull operator and I(x) := {i | fi(x) = f(x)} denotes the set of active
functions. When fi’s are differentiable, we have
∂f(x) = conv{∇fi(x) | i ∈I(x)}
(A.69)
Note that all the subgradient calculus rules reviewed above reduce to multivariate calculus if f is
continuously differentiable at x (all ∂fi can be replaced by ∇fi(x)).
A.3
Optimality Conditions
For convex f, x∗is a global minimizer of f if and only if 0 ∈∂f(x∗). For the case in which f is contin-
uously differentiable at x∗, the optimality conditions reduce to ∇f(x∗) = 0, which are necessary and
sufﬁcient optimality conditions for convex minimization problems.
42