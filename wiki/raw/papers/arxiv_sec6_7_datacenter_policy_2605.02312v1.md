# Should Small-Scale Data Centers Participate in the Day-Ahead Electricity Market?
**arXiv ID:** 2605.02312v1
**Source File:** arxiv_sec6_7_datacenter_policy_2605.02312v1.pdf

## Page 1

PREPRINT
1
Should Small-Scale Data Centers Participate in the Day-Ahead
Electricity Market?
Enea Figini, Student Member, IEEE and Mario Paolone, Fellow, IEEE
Abstract—The global race to artificial intelligence competitive
advantage is challenging electricity grids by demanding growing
data center capacity. Addressing this challenge requires syn-
ergistic operational strategies that integrate data centers into
electricity markets while supporting grid operation. This work
proposes a bilateral power purchase agreement between small-
scale data centers and distribution system operators, enabling
data center participation in the day-ahead electricity market.
To facilitate market participation, we develop a scenario-based,
risk-averse bidding strategy that leverages flexibility from local
energy resources, waste heat recovery, and data center workload.
The strategy jointly minimizes operational costs and carbon
emissions, creating a carbon-aware cost-effective framework for
data center integration in the electricity day-ahead market. The
method is evaluated on a study case comparing a conventional
time-of-use supply scheme with the proposed custom power pur-
chase agreement, showing a potential 22% cost reduction, thus
highlighting financial opportunities for small-scale data centers
day-ahead electricity market participation. Two additional case
studies illustrate the marginal effects of: (i) data center flexible
workload on energy costs and (ii) virtual de-rating of grid
transfer capacity.
Index Terms—Data center, electricity market, distributed en-
ergy resources, workload flexibility
I. NOMENCLATURE
Sets
D
Set of timesteps in a day.
W
Set of timesteps in a week.
T
Set of timesteps in the bidding problem.
Ω
Set of scenarios in the bidding problem.
C
Set of clusters in the data center.
R
Set of computational resources in the data
center.
Rmem
Set of memory resources.
Rcooled
Set of resources with Direct Liquid Cooling
(DLC).
Indices
t
Timestep index.
ω
Scenario index.
c
Data center cluster identifier.
res
Resource identifier.
i
Sampling index for the Organic Rankine Cy-
cle (ORC) heat to power piecewise approxi-
mation.
Parameters
The authors are with the Swiss Federal Institute of Technology (EPFL) in
1015 Lausanne, Switzerland (e-mail: {enea.figini, mario.paolone}@epfl.ch).
Preprint: 4th of May 2026.
Ns
Number of samples for the linear interpola-
tion of the input heat-to-output ORC power
curve.
P rated
gcp
Rated power of the Grid Connection Point
(GCP) connection.
P t
gcp,cap
Virtual transfer capacity at the GCP.
∆P t
gcp
GCP de-rating amount.
Pgcp,min
Guaranteed transfer capacity at the GCP.
tdaily,lim
Daily maximum duration of GCP de-rating.
tweekly,lim
Weekly maximum duration of GCP de-rating.
∆T
Time interval between timesteps in the bid-
ding problem.
α
Conditional Value at Risk (CVaR) confidence
level in the bidding problem.
β
CVaR weight in the bidding problem objec-
tive.
πcarbon
Carbon price.
πω, t
spot
Electricity spot price.
πω, t
short
Short imbalance price.
πω, t
long
Long imbalance price.
πheat
Heat selling price.
Scap
Renewable share target.
αr
Allowed fraction of violations of Scap.
κc,res
Cluster capacity of given resource.
Γinelastic
Guaranteed fraction of served inelastic de-
mand.
Γflexible
Guaranteed fraction of served flexible de-
mand.
γc,res
mem
Historical average of the memory-to-compute
ratio.
ηPUE
Data center power usage effectiveness.
ρc
inter
Intercept of the linear regression between
resource usage and IT power consumption.
ρc,res
coeff
Affine coefficient of the linear regression
between resource usage and IT power con-
sumption.
ρc
cooled,idle
Cluster idle power consumption of resources
with on-chip micro-fluidic cooling.
ηc,res
rec
Heat recovery efficiency.
( ˙qi, pi)
ORC heat-to-power samples.
ηbess
Battery Energy Storage System (BESS) one-
way efficiency.
Emin
bess, Emax
bess
Energy bounds for BESS operation.
P rated
bess
Rated BESS power.
arXiv:2605.02312v1  [eess.SY]  4 May 2026

---

## Page 2

PREPRINT
2
Lcycles
bess
Rated cycles of BESS.
Erated
bess
Rated capacity of BESS.
Πinvestment
bess
Investment cost of BESS.
CLCA
bess
Life-cycle emissions of BESS.
P rated
pv
Rated PV power.
iω, t
ghi
Forecasted
Global
Horizontal
Irradiance
(GHI).
ighi,ref
Reference GHI.
cω, t
gcp
Grid carbon intensity of electricity.
sω, t
gcp
Grid renewable share of electricity.
˙Qω, t
demand
District heating demand forecast.
Iω, t, c, res
Inelastic workload (WL) demand forecast.
F ω, c, res
Flexible WL demand forecast.
Variables
Πω
op
Total daily operational cost.
Πω, t
d-a
Day-ahead electricity supply cost.
Πω, t
imb
Imbalance settlement cost.
Πω, t
op,DERs
Distributed Energy Resources (DERs) opera-
tional cost.
Πω, t
heat
Heat revenue.
Cω, t
gcp
Electricity imports equivalent carbon emis-
sions.
Cω, t
op,DERs
DER operational equivalent carbon emis-
sions.
uω, t, c, res
Data center resource usage.
κt, c, res
v
Virtual capacity of resource.
P ω, t
dc
Data center power consumption.
˙Qω, t
rec
Total recovered heat.
˙Qω, t
orc,in
Recovered heat sent to ORC.
˙Qω, t
sold
Recovered heat sold to district heating.
˙Qω, t
lost
Recovered heat lost.
P ω, t
orc
ORC power output.
λω, t
i
ORC interpolation variables.
P ω, t
bess,d
BESS discharge power, on the direct-current
side of the converter.
P ω, t
bess,c
BESS charge power, on the direct-current
side of the converter..
zω, t
bess
Charge/discharge indicator for BESS.
Eω, t
bess
BESS stored energy.
P ω, t
bess,ac
BESS power on the AC side of the converter.
aω, t
bess
BESS operational aging variable.
Πω, t
bess
BESS operational cost.
Cω, t
bess
BESS equivalent carbon emissions.
P ω, t
pv
PV power generation.
P t
gcp,d-a
Day-ahead GCP power.
P ω, t
gcp,imb
Power imbalance at the GCP.
P ω, t
gcp,-
Long component of the imbalance power.
P ω, t
gcp,+
Short component of the imbalance power.
zω, t
imb
Imbalance indicator.
Eω, t
non-ren
Non-renewable energy consumed.
Eω
dc
Daily data center energy consumption.
II. INTRODUCTION
A. Context and Motivation
Rapid breakthroughs in Artificial Intelligence (AI) have
accelerated the global deployment of data centers. According
to the International Energy Agency (IEA) [1], total data center
capacity is projected to grow from approximately 100 GW
today to over 225 GW by 2035, while their electricity con-
sumption is expected to grow from 415 TW h in 2024 to
1 PW h in 2030. This growth is strongly driven by national
strategies aimed at gaining competitive advantages in technolo-
gies related to AI. For example, the European Commission
has published an action plan [2] that sets the goal of at least
tripling the capacity of data centers across Europe in seven
years, supported by an investment initiative of 200 billion
Euros. This massive growth is challenging electricity grids,
with Transmission System Operators (TSOs) in Ireland, the
Netherlands and Germany refusing to connect new large-scale
(e.g., > 100 MW data centers to the grid [3]. Some TSOs are
issuing data center-specific grid codes to regulate connections
[4].
Additionally, approximately 90% of AI workload (WL) is
currently training-based, while only about 10% is inference-
based. However, 90% of AI WL is expected to become
inference-based by 2030 [5]. Inference-based WL typically
requires low-latency processing close to end-users, making
small-scale edge data centers (e.g., < 20 MW) the preferred
solution. These data centers are generally connected to dis-
tribution power systems, which are already facing challenges
due to volatile distributed generation and fluctuating demand,
factors often associated to grid congestion [6]. Their con-
nection further complicates grid planning and operation for
Distribution System Operators (DSOs).
These trends highlight the need for data centers to operate
not only as electricity consumers but also as active/controllable
entities. To ensure their scalable deployment, their integration
must be supported by strategies that align data center opera-
tional flexibility with safe grid operation.
B. Literature Review and Gaps
Research on data center integration into electricity markets
explores many directions. This review provides an overview
of the main topics relevant to the scope of this work.
1) Interaction with Electricity Spot Market: Recent studies
have explored how data centers can participate in electricity
spot markets through optimized bidding and scheduling. In
[7], a multi-objective bidding strategy for WL scheduling is
proposed. Similarly, [8] and [9] investigate strategies for data
center aggregators that leverage geographical WL flexibility
(i.e., shifting computational tasks across multiple sites) to
minimize operational costs. A bidding strategy for data center
microgrids with wind and PV generation is presented in [10].
However, these approaches are typically not scenario-based
and overlook imbalance settlement costs, which are crucial
for realistic participation in spot markets.

---

## Page 3

PREPRINT
3
2) WL Modeling and Scheduling: Significant effort has
been put on modeling and scheduling job flexibility within data
centers. Most studies rely on M/M/n queue models to meet
Quality of Service (QoS) objectives [7], [11], while others re-
quire job-level scheduling [12]. The former generally assumes
WL and hardware homogeneity, whereas the latter becomes
computationally intractable for large-scale, day-ahead schedul-
ing [13]. The concept of Virtual Capacity Curves (VCCs),
introduced in [13] and further exploited in [14], provides
a promising trade-off by decoupling day-ahead optimization
from real-time WL scheduling using virtual capacity limits.
In [14], the authors propose a day-ahead planning problem
simultaneously designing the VCCs and the job scheduling
strategy while satisfying the constraints in [13]. The approach
is validated using load profiles from Google clusters, showing
VCCs can be used to efficiently leverage job flexibility in
large-scale data centers. These approaches, however, do not
fully address the interface with electricity markets (e.g., imbal-
ance settlement costs, coupled operation with local Distributed
Energy Resources (DERs), bidding strategy, etc.) and focus on
large-scale data centers with market access.
3) Market Accessibility and Operational Integration: Sev-
eral works have examined data centers participation to an-
cillary services or demand response mechanisms [15]–[17].
These studies generally assume that data centers are knowl-
edgeable market participants. In practice, however, most small-
scale data centers lack both expertise and direct market access
[18]. Bilateral agreements between Data Center Operators
(DCOs) and grid stakeholders (DSOs, TSOs, or energy sup-
pliers/retailers) are thus likely to represent the most realistic
entry point for data centers to participate in demand response
schemes and/or electricity markets.
4) Waste Heat Valorization: Finally, the sustainable op-
eration of data centers requires valorization of recovered
waste heat. Integration with district heating networks [19]
and electricity regeneration through Organic Rankine Cycles
(ORCs) [20], [21] have been studied, with recent Direct Liquid
Cooling (DLC) technologies capable of recovering medium-
grade heat further expanding these opportunities [22].
C. Contributions of This Work
This work addresses several gaps mentioned in Section II-B.
We propose a day-ahead bidding strategy that coordinates
small-scale data center flexibility to enable market partic-
ipation while accounting for carbon emissions, renewable
share and imbalance costs, which are often omitted in similar
approaches. A scenario-based, risk-averse Mixed Integer Lin-
ear Program (MILP) is formulated to schedule local Battery
Energy Storage System (BESS), PhotoVoltaic (PV) generation,
and ORC, as well as heat exports and flexible WL, building
on the VCCs concept from [13], [14] to make day-ahead
scheduling computationally tractable.
Additionally, we propose a bilateral Power Purchase Agree-
ment (PPA) between the DCO and DSO. It grants market
access to the DCO, while allowing the DSO to trigger a virtual
de-rating of the transfer capacity at the Grid Connection Point
(GCP), thus framing a simple demand response mechanism for
Data 
center
PV
BESS
District 
heating
ORC
DSO 
GCP 
Data center hub
Electricity flows
Heat flows
Fig. 1. Schematic representation of the system.
DSO-DCO collaboration. The framework is validated through
case studies based on the data of a local academic data center,
showing advantages for both parties.
III. PROBLEM STATEMENT
A. System Description
Given the context highlighted in II-A, the system under
study is illustrated in Fig. 1. A data center connected to a
distribution grid is co-located with local PV generation, a local
BESS and an ORC. Waste heat can be recovered from the
servers, used by the ORC to regenerate electricity and/or sold
to the local utility providing district heating services. Given
the paper’s focus on small-scale data centers connected to the
distribution grid (and thus likely neighboring urban areas), the
opportunity of recover heat to sell supply local district heating
is particularly interesting. This potential can be leveraged by
the DCO in the PPA negotiations.
B. Agreement Between the DCO and DSO
Small-scale data centers can represent a significant share
of the load in power distribution grids. Despite this, they
rarely participate in electricity markets and instead rely pre-
dominantly on standard PPAs with fixed pricing structures.
While such PPAs offer contractual simplicity and certainty
for DCOs and DSOs, their inherent price stability also limits
operational incentives. In particular, fixed-price PPAs do not
encourage improvements in power consumption predictability
or the provision of operational flexibility. As a result, the
potential of small-scale data centers to act as active and
dispatchable grid participants remains largely unexploited. We
propose and study a custom PPA between the DCO and DSO,
with the following features.
• DCO market access: Under the proposed agreement, the
data center is granted access to the day-ahead electricity
market. Given its size (i.e., < 20 MW), the data center
operates as a price-taker in the spot market. It performs a
day-ahead scheduling of resources within the data center
hub and submits a corresponding power profile bid to the

---

## Page 4

PREPRINT
4
DSO, which acts as an interface with the market plat-
form. Following market clearing, the DCO is financially
responsible for deviations from the cleared day-ahead
schedule. Imbalances are therefore settled according to
imbalance prices, incentivizing accurate load forecasting
and schedule tracking.
• Dynamic rating of the GCP: In exchange for market
access, the DSO retains the right to apply a day-ahead
virtual de-rating of the data center GCP, reducing the
maximum import capacity during selected hours. The de-
rating signal is communicated day-ahead and must be
incorporated into the DCO’s bidding process.
To ensure contractual fairness and operational predictabil-
ity, the de-rating profile is bounded by a minimum
capacity guarantee and cumulative de-rating daily and
weekly budgets. Defining the de-rating amount in (1),
we formalize three contractual limits (2)-(4).
∆P t
gcp = P rated
gcp −P t
gcp,cap
(1)
P t
gcp,cap ≥Pgcp,min, ∀t
(2)
X
t∈D
∆P t
gcp∆T ≤(P rated
gcp −Pgcp,min)tdaily,lim
(3)
X
t∈W
∆P t
gcp∆T ≤(P rated
gcp −Pgcp,min)tweekly,lim
(4)
A minimum import capacity is guaranteed in (2), while
(3) and (4) limit the cumulative daily and weekly de-
rating that can be imposed by the DSO.
In Section IV, we propose a stochastic optimization-based
bidding strategy for data center hubs with such PPA. In
Section V, we study the potential of such agreement using real
data from an academic data center at EPFL in Switzerland, and
show that it can benefit both DCOs and DSOs.
IV. DAY-AHEAD BIDDING STRATEGY
A. Objective
The objective in (5) minimizes the expected daily oper-
ational costs across scenarios ω ∈Ω, while incorporating
risk-aversion through the α-level Conditional Value-at-Risk
(CVaR) [23]. The relative importance of risk-aversion can be
set by the user through the parameter β ∈[0, 1]1. We highlight
decision variables in bold.
min
(1 −β) E(Πω
op) + β CVaRα(Πω
op)
(5)
Daily operational costs Πω
op are defined as the sum over
t ∈T of Πω,t
op , defined in (6). They include electricity costs
(with day-ahead and imbalance components), energy resources
aging costs, operational carbon emissions costs (with grid
imports and energy resources aging components) and revenues
generated by selling waste heat.
Πω,t
op =Πω,t
d-a + Πω,t
imb + Πω, t
op, DERs −Πω,t
heat
+πcarbon

Cω,t
gcp + Cω, t
op, DERs

(6)
1Note that β can be tuned via pareto front studies. We do not show such
studies in this paper because of page limits.
Note that πcarbon represents the cost of carbon emissions,
expressed in ¤/gCO2 eq, where ¤ is the universal currency
symbol.
B. Data Center Model
1) Computational Resources: We define the data center as
a set of clusters C. Each cluster c has its own configura-
tion and resources, with capacity κc, res. Clusters can contain
Central Processing Units (CPUs) and Graphics Processing
Units (GPUs). Memory resources are split in two categories,
Rmem = {MEM-CPU, MEM-GPU}, as CPUs and GPUs
typically use different types of memory. We define the set
of computational resources types R = {CPU, GPU}. Within
clusters, resources of a given nature should be homogeneous
(e.g., a single CPU model per cluster). The usage of resources
per cluster uω, t,c,res is the decision variable in the data center
model.
2) Workload: Following [13], we model the data center WL
by defining two broad categories: (i) inelastic WL (i.e., jobs
that must be executed upon arrival and, therefore, offer no
scheduling flexibility) and (ii) flexible WL (i.e., jobs that must
be completed within a given time window, allowing flexibility
regarding their start time). The inelastic WL’s per cluster
resource demand Iω,t,c,res is assumed to be forecastable as a
time series, 24h-ahead. For flexible WL, we focus on WL that
has to be completed within a day. We assume that the daily
cumulative demand of computational resources F ω,c,res can be
forecasted 24h-ahead. These assumptions are supported by the
work conducted in [13].
uω, t, c, res ≥Iω,t,c,res
(7a)
X
t∈T

uω, t, c, res −Iω,t,c,res
≥F ω,c,res
∆T
(7b)
X
t∈T

uω, t, c, res −Iω,t,c,res
≤F ω,c,res
∆T
(7c)
When verified for all ω ∈Ω, t ∈T , c ∈C, res ∈R,
(7a) and (7b) ensure the satisfaction of the two WL categories
strictly, while (7c) avoids over-using resources (and, in this
case, (7b) and (7c) could be joined in a single equality con-
straint). However, to embed QoS considerations, we replace
(7a) and (7b) by the Chance Constraints (CCs) (8a) and
(8b) (i.e., we relax 7a and 7b). Practically, both CCs are
implemented using violation indicator variables and ensuring
the likelihood of violations does not exceed the allowed
quotas.
P(7a) ≥Γinelastic
(8a)
P(7b) ≥Γflexible
(8b)
The usage of memory resources is tracked and modeled using
a linear mapping (9) to the related resource (e.g., MEM-CPU
usage is proportional to CPU usage) using historical average
ratios γc, res
mem .
uω, t, c, res =γc, res
mem uω, t, c, rel-res,
∀ω ∈Ω, t ∈T , c ∈C, res ∈Rmem
(9)

---

## Page 5

PREPRINT
5
The usage of resources must be less or equal to the available
capacity for each resource and cluster, leading to (10).
uω, t, c, res ≤κc, res, ∀ω ∈Ω, t ∈T , c ∈C, res ∈R
(10)
3) Power Consumption: The power consumption of the
data center is modeled as a function of resource usage
uω, t, c, res. In this work, we assume an affine relation (11)
between resource usage and cluster IT-equipment power con-
sumption [13], [24]. Note that ηPUE is the Power Usage
Effectiveness (PUE) of the data center and includes the
consumption of non-IT equipment (e.g., fans, pumps, etc). In
what follows, we omit the explicit quantifiers ∀ω ∈Ω, t ∈T
for compactness. All constraints (with the exception of CCs)
involving scenario- and time-dependent variables hold for all
ω ∈Ωand t ∈T .
P ω,t
dc
=ηPUE
X
c∈C
 ρc
inter +
X
res∈R∪Rmem
ρc, res
coeff uω, t, c, res
(11)
4) Heat Recovery: We consider the case of data centers
equipped with DLC for computational resources, as this
technology is more efficient and allows for the recovery of
medium-grade heat, which can in turn be exploited by the
ORCs to regenerate electricity (see Fig. 1). Therefore, reusable
heat comes from the power losses of the resources that are
cooled using this technology (e.g., CPUs and GPUs). We
define the recovered heat in (12). Note that, in practice, the
idle consumption of cooled resources in each cluster ρc
rec,idle
can be estimated empirically by measuring the heat recovered
with the cluster operating in idle mode.
˙Qω, t
rec =
X
c∈C
ηc, res
rec
 
ρc
rec,idle +
X
res∈Rcooled
ρc, res
coeff uω, t, c, res
!
(12)
Recovered heat can be (i) used by the ORC, (ii) sold to
local utilities operating district heating or (iii) dumped and
lost (13).
˙Qω, t
rec = ˙Qω, t
orc, in + ˙Qω, t
sold + ˙Qω, t
lost
(13)
Note that, in practice, residual heat at the output of the ORC
could be used for district heating purposes if its temperature
is high enough. In this formulation, we assume the residual
heat of the ORC cannot be used by the district heating.
C. Energy Resources Models
1) ORC Model: The ORC uses recovered heat to generate
electrical power. The relation between the two, if the ORC
is operated at maximum efficiency, is non-linear [25]. We
thus sample the curve Porc( ˙Qorc, in) and get the sample set
{( ˙qi, pi) : i ∈[0, 1, ..., Ns], pi = Porc( ˙qi)}. The samples
are then used to formulate (14), where (14a) constrains the
interpolation variables λω,t
i
, (14b) interpolates the input heat
and (14c) defines the upper bound for the output power. While
not made explicit here, Special Ordered Set of type 2 (SOS2)
piecewise constraints are used to ensure that two consecutive
λω,t
i
at maximum can be non-zero simultaneously [26], [27].
N
X
i=0
λω,t
i
= 1,
λω,t
i
≥0,
(14a)
˙Qω,t
orc, in =
N
X
i=0
˙qi λω,t
i
,
(14b)
P ω,t
orc ≤
N
X
i=0
pi λω,t
i
(14c)
We highlight that we only define an upper bound for the
output power, implying that, for a given heat input, the ORC
can be controlled to track any setpoint between zero and the
upper bound.
2) BESS Model: We model the energy dynamics of the
BESS using a bucket model in (15a). The BESS state-of-
energy and power limits are ensured by (15b) and (15c),
respectively. Finally, we account for the BESS one-way ef-
ficiency ηbess in (15d), where P ω, t
bess, d and P ω, t
bess, c denote the
discharge and charge power of the battery. We guarantee
their mutual exclusivity through binary activation constraints
via Big-M formulation (15e)–(15g), where zω, t
bess is a binary
indicator variable (here, P rated
bess
plays the role of the Big-M
constant since BESS power is constrained by its rated value).
Finally, we ensure, through (15h) along with the inherent
inclusion of BESS losses via (15d), that the BESS does not get
charged or discharged on average. This ensures that the BESS,
in expectation, remains a neutral energy buffer, guaranteeing
its availability for subsequent daily operation.
Eω, t + ∆T
bess
= Eω, t
bess + ∆TP ω, t
bess ,
(15a)
Emin
bess ≤Eω, t
bess ≤Emax
bess,
(15b)
−P rated
bess ≤P ω, t
bess ≤P rated
bess ,
(15c)
P ω, t
bess, ac = η−1
bessP ω, t
bess, c −ηbessP ω, t
bess, d,
(15d)
P ω, t
bess = P ω, t
bess, c −P ω, t
bess, d
(15e)
P ω, t
bess, c ≤zω, t
bessP rated
bess
(15f)
P ω, t
bess, d ≤(1 −zω, t
bess)P rated
bess
(15g)
E
 X
t∈T
P ω,t
bess

= 0
(15h)
We model the aging of the BESS due to cycling, as it
corresponds to the operational aging of the asset. To do so, we
assume the aging of the asset to be linear with the system’s
energy throughput. This is made explicit in (16a), where Lcycles
bess
and Erated
bess are the rated number of cycles and the rated capacity
of the asset, respectively. Then, the operational cost of the
battery Πω,t
bess and its operational carbon footprint Cω,t
bess (scope
3 emissions) are computed in (16b) and (16c). Note that Πω,t
bess
and Cω,t
bess are part of the total operational costs and emissions
of the data center hub DERs in the objective (5).
aω, t
bess =
|P ω, t
bess |∆T
2Lcycles
bess Erated
bess
,
(16a)
Πω,t
bess = aω, t
bessΠinvestment
bess
,
(16b)
Cω,t
bess = aω, t
bessCLCA
bess
(16c)

---

## Page 6

PREPRINT
6
3) PV Generation Model: We model PV generation using
the simplified linear PV performance model described in (17),
and PV generation can be curtailed.
P ω, t
pv
≤
iω, t
ghi
ighi, ref
P rated
pv
(17)
D. Electricity Supply Model
1) Electricity Market: We model the electricity spot market
as well as the imbalance costs faced by the market player (i.e.,
the DCO), which is therefore modeled as a passive player in
the balancing markets. We base our model on the european
(and swiss) electricity markets. In (18b), we decompose the
power at the GCP (18a) into a day-ahead scenario-independent
power component P t
gcp, d-a and an imbalance power component
P ω, t
gcp, imb. The day-ahead power component is billed at the
spot price πω,t
spot in (18d). In (18c), the imbalance power is
decomposed into a long P ω, t
gcp,- and short P ω, t
gcp,+ component to
match the settlement structure of imbalance costs, detailed in
(18e). The mutual exclusivity of P ω, t
gcp,-, P ω, t
gcp,+ is guaranteed
through (18f)–(18g), where zω, t
imb is a binary indicator variable
and P rated
gcp
is the rated power of the GCP. Finally, (18h)
constrains the GCP power using dynamic virtual transfer
capacity values P t
gcp, cap set by the grid operator, according
to the bilateral agreement in Section III-B.
P ω, t
gcp = P ω, t
dc
−P ω, t
orc + P ω, t
bess, ac −P ω, t
pv
(18a)
P ω, t
gcp = P t
gcp, d-a + P ω, t
gcp, imb,
(18b)
P ω, t
gcp, imb = P ω, t
gcp,+ −P ω, t
gcp,-,
(18c)
Πω,t
d-a = πω,t
spotP t
gcp, d-a∆T,
(18d)
Πω,t
imb = ∆T(πω,t
shortP ω, t
gcp,+ −πω,t
longP ω, t
gcp,-)
(18e)
P ω, t
gcp,+ ≤zω, t
imb P rated
gcp
(18f)
P ω, t
gcp,- ≤(1 −zω, t
imb )P rated
gcp
(18g)
P ω, t
gcp ≤P t
gcp, cap
(18h)
2) Carbon Emissions: We compute the scope 2 carbon
emissions due to electricity imports in (19).
Cω, t
gcp = cω,t
gcpP ω, t
gcp ∆T
(19)
E. Heat Market Model
We assume that the data center is connected to a district
heating network operated by the local utility provider. The
data center and the utility provider have a simple fixed unit
price contract, allowing the data center to sell medium-grade
heat. The revenue stream from sold heat is computed in (20a).
The amount of heat that can be sold is limited by the district
heating demand (20b).
Πω,t
heat = πheat ˙Qω,t
sold∆T
(20a)
˙Qω, t
sold ≤˙Qω, t
demand
(20b)
F. Renewable Share
We track the renewable share of the data center energy
consumption. Since local generation is fully renewable (from
the PV and the ORC), we track the non-renewable electricity
Eω, t
non-ren that flows into the system from the GCP (21a). Note
that 0 ≤sω, t
gcp ≤1 is the renewable share of the electricity
imported from the grid. We formulate a CC on the non-
renewable energy consumption (21b), where Eω
non-ren is the
non-renewable energy at the end of the day and Eω
dc is the total
daily energy consumption of the data center. This constraint
ensures that the renewable share cannot be smaller than the
set target Scap in more than 100αr% of the scenarios, where
αr denotes the allowed fraction of violations. Note that (21b)
can induce infeasibility and, therefore, Scap must be selected
with care. Practically, we implement the corresponding CC
by introducing violation indicators and ensuring that the
probability of a violation occuring is below αr.
Eω, t + 1
non-ren = Eω, t
non-ren + (1 −sω, t
gcp )P ω, t
gcp ∆T
(21a)
P(Eω
non-ren ≥(1 −Scap)Eω
dc) ≤αr
(21b)
G. Final Problem Formulation
We formulate the full optimization problem (22).
min
(5)
s.t.
(6)
(7c) to (21b)
(22)
Note that, once the day-ahead bidding process is performed,
we can construct VCCs for the CPUs and GPUs of each
cluster. In (23), we propose a conservative construction, where,
for each timestep, the VCC is set to the maximum resource
usage across all scenarios. We note that, in practice, the VCCs
are derived after solving the proposed method and their precise
construction should be adapted to the performance of the real-
time control layer.
κt, c, res
v
=maxω∈Ω(uω, t, c, res),
∀t ∈T , c ∈C, res ∈R
(23)
V. STUDY CASES
We present the case of an academic 200 kW-rated data
center located at EPFL, in Lausanne, Switzerland. The grid
connection power rating is 300 kW. An ORC with a rated
maximum input heat flow of 100 kW, 200 kW of PV gener-
ation and a BESS with a 250 kW rated power and 250 kW h
capacity are co-located with the data center. The data center,
the ORC, the PV and the BESS are controllable.
The simulations ran on a MacBook Pro with Apple M2 Max
Chip, 32 GB of RAM, using the GUROBI solver.
A. Data Availability
Unless specified otherwise, hourly data from January 2023
to August 2025 is used.

---

## Page 7

PREPRINT
7
1) Electricity Imports:
We recover the electricity spot
prices and imbalance prices for Switzerland from the ENTSO-
E transparency platform [28]. We recover the day-ahead fore-
casts of renewable generation for Germany, Italy, France and
Austria, as candidate explanatory variables for the spot price.
We use [29] to get the dynamic carbon intensity (GWP100a)
and renewable share of electricity in canton Vaud, Switzerland.
2) Carbon Cost: The cost of a gram of CO2 eq emitted
(πcarbon) can be set in various ways2. In this paper, we use
πcarbon = 265 EUR/tCO2 eq, the mean social cost of carbon
from [30].
3) Heat Price: According to [31], district heating heat is
sold at 0.15 EUR/kWh to end-consumers. We assume the data
center has secured a deal to sell its recovered heat to the district
heating operator at 0.03 EUR/kWh.
B. Scenario Generation
While forecasting is not the focus of this work, its per-
formance impacts the results of the stochastic optimization
method. We thus describe the methods we use for the sake of
reproducibility.
1) Solar Irradiance: We use the service from [32] to
recover up to 40 day-ahead irradiance scenarios.
2) Spot Prices, Renewable Share and Carbon Intensity:
We implement a Gradient Boost Regression (GBR) forecasting
method [33] to forecast the spot prices, the renewable share
and the carbon intensity of the electricity imported by the data
center under study. We follow the following steps, for each of
the stochastic variables, independently.
• We augment the data set adding candidate features,
such as day-ahead renewable forecasts from neighboring
countries, lagged data of the stochastic variable (week-
ahead lag and day-ahead lag) and day of the week. We
standardize the data to zero means and unit variances.
• We split the data into a training and a test data set, with
the day to plan as the first test date.
• Using the training data set, we identify the five domi-
nant features by running a first GBR with all candidate
features. We drop all the other candidates.
• We run GBR using the selected features only. We store
the non-standardized residuals of the training set.
• The expected value of the stochastic variable is predicted
for the target day and rescaled to its original units.
• We build N scenarios by bootstrap subsampling N days
in the set of residuals. This preserves the realistic time-
coupling of residuals in the scenarios.
3) Imbalance Prices: Long and short imbalance price data
are collected for the period from January 2023 to August
2025 [28]. Given the high volatility typically observed in
imbalance prices, we adopt a simplified modeling approach
in which imbalance costs are assumed to be proportional to
the spot price. The proportionality factors are calibrated such
that, when the approximation is applied to the historical data
2For example, the EU Emissions Trading System (ETS) sets prices via
traded allowances, while voluntary carbon markets offer credits for avoidance
or removal (e.g., direct air capture or reforestation), with prices varying from
hundreds to thousands of Euros per ton of CO2 eq.
set, 40% of the observations result in an underestimation of
the actual imbalance prices.
4) Data Center WL: As anticipated earlier, we use data
from a data center providing its services to the research
community at EPFL3. We recover node-level statistics for
power consumption, CPU usage, GPU usage, CPU memory
used, GPU memory used. The node configuration determines
to which cluster a given node belongs. The capacity of the
clusters is detailed in Table I. The data have a granularity of
2 min and span from October 16th 2024 to August 4th 2025.
TABLE I
CLUSTER CAPACITIES OF THE DATA CENTER UNDER STUDY
Cluster
Nodes
GPU
CPU cores
GPU-MEM
CPU-MEM
A100
32
256
1024
10240
32768
H100
10
80
960
6400
15360
V100
16
64
576
2048
6160
Using the nodes configurations, we aggregate resources into
clusters and downsample the data to an hourly resolution.
We then fit three linear models to map resource usage to
cluster-level power consumption, determining the coefficients
in (11). In addition, we compute the average ratio of memory
to computational resource usage γres, c
mem , which is required in
(9). Finally, we use the GBR method (cf. V-B2) to generate
scenarios for hourly inelastic WL resources request and daily
flexible WL resources request.
5) Scenario Combination and Clustering: To be consistent
with [32], we generate 40 scenarios for each stochastic pa-
rameter (i.e., spot prices, renewable share, carbon intensity,
solar irradiance, inelastic CPU/GPU demand and flexible
CPU/GPU demand). We generate 500’000 combinations of
these scenarios (assuming the parameters are independent) and
cluster them using K-Means with 60 clusters. Then, for each
cluster, we select the closest scenario (using the L2−norm) to
the centroid and assign its probability according to the cluster
population.
C. Study Cases Discussion
We evaluate the proposed bidding strategy and PPA across
three case studies. The first one provides a statistical analysis
of the performance of the bidding strategy with different PPAs
over the month of July 2025. The second aims at quantifying
the value of flexible WL in the day-ahead electricity mar-
ket. The final case study analyzes the impact of virtual de-
rating on day-ahead planning. In the first two case studies,
ex-ante and ex-post operational metrics are compared. Ex-
post performance is assessed by enforcing the day-ahead bid
determined in the stochastic optimization planning stage and
re-optimizing operational decisions using the realized values
of Global Horizontal Irradiance (GHI), spot prices, carbon
intensity, renewable share and WL.
1) Study Case I — on the Advantages of the Proposed PPA:
In this study case, we evaluate the contractual framework
proposed in Section III-B from the perspective of the data
center. We compare key operational metrics for two PPAs:
3https://www.epfl.ch/research/facilities/rcp/

---

## Page 8

PREPRINT
8
(i) the proposed PPA and (ii) Time-of-Use (ToU) fixed tariffs
representative of 2025 [34]. For the sake of simplicity, the
analysis is restricted to energy supply, transmission/imbalance
costs and BESS aging costs. For (i), the data center pays the
market-cleared spot prices and the settled imbalance costs,
while for (ii) it faces fixed ToU tariffs. Importantly, while
the supply agreements are different, both cases leverage the
method proposed in this paper. We run the method for 23
days in July 2025. To isolate the impact of the agreements,
no virtual de-rating request from the DSO is considered
(thereby estimating the maximum gains that the data center
can achieve). We consider 50% of flexible WL in this study
case and will use these results as a baseline for the study case
in Section V-C2.
Fig. 2.
Distribution of ex-post operational costs and carbon footprint:
proposed PPA vs. ToU.
In Fig. 2, we show the empirical Probability Distribution
Functions (PDFs) of the operational costs and carbon footprint
across days (estimated with Kernel Density Estimation (KDE)
on the observed daily metrics). One can observe that using our
method within the proposed PPA shifts the costs PDF to the
left, suggesting a cost reduction in most cases. However, one
can also observe that the right-side tail of the PDF is extended,
suggesting rare occasions of large energy supply costs (likely
caused by extreme imbalance costs events). Interestingly, the
footprint PDF is shifted to the right, suggesting an increase in
the footprint of the system. Intuitively, this can be attributed
to less cost reduction opportunities in the baseline (since the
tariffs are less dynamic), which lead to more opportunities of
reducing carbon emissions without negatively impacting the
costs. It is important to remember that the cost of carbon
emissions is a parameter of the day-ahead bidding strategy
(see Section V-A2).
To quantify the differences between the two supply agree-
ments, we describe the PDFs in Table II. From ex-post results,
we expect the custom supply agreement to lead to a reduction
in expected operational costs of approximately 22%, and a
footprint increase of approximately 6%. In the custom PPA
case, we observe an underestimation of the two metrics in
Fig. 3. Ex-post energy supply operational costs and footprint: no WL elasticity
vs. 50% of flexible WL.
their ex-ante forecasts, likely due to an underestimation of
imbalance prices.
2) Study Case II — on the Value of Flexible WL in the
Spot Market: In this section, we quantify the economic value
of flexible WL in the day-ahead planning phase. We use the
flexible demand scenarios for computational resources (i.e.,
CPUs and GPUs) generated in study case V-C1. The daily
flexible demand is uniformly distributed over the correspond-
ing inelastic demand scenario, ensuring the total daily demand
for computational resources remains unchanged. This allows
us to isolate the impact of WL flexibility.
From Fig. 3 and Table II, we conclude that the expected
cost reduction from flexible WL is approximately 15 EUR
per day. Based on the scenarios analyzed, the average flexible
demand amounts to about 6000 CPUh and 1500 GPUh per day.
Using the pricing reported in [35], their corresponding value is
about 660 EUR. Thus, the observed savings represent less than
2.5% of the total value of the WL, assuming it were inelastic.
This marginal reduction offers little economic incentive to
users, making it unlikely that such discounts would encourage
flexible resource bookings.
These results suggest that, under current pricing schemes,
WL flexibility does not provide enough value in the spot
market alone to motivate data center operators to propose
flexible rates. However, other factors (such as system relia-
bility, local policies, participation to other electricity markets,
or environmental goals) could justify flexible billing schemes.
3) Study Case III — on the Impact of Virtual De-Rating:
We assess the impact of virtual power de-rating of the GCP
on day-ahead planning. The DSO anticipates a period of high
local demand between 17 h and 21 h and tries to alleviate
system stress. In this regard, it issues a day-ahead request of
virtual de-rating of the data center’s grid connection power.
Specifically, we assume the nominal connection capacity of
300 kW to be temporarily reduced to:
• 75 kW at 17:00,
• 25 kW at 18:00,

---

## Page 9

PREPRINT
9
TABLE II
QUANTITATIVE DESCRIPTION OF OPERATIONAL FOOTPRINT AND COST
Supply scheme
Ex-post costs (EUR)
Ex-ante costs (EUR)
Ex-post emissions (kgCO2eq)
Ex-ante emissions (kgCO2eq)
-
Q25%
Mean
Q75%
σ
Q25%
Mean
Q75%
σ
Q25%
Mean
Q75%
σ
Q25%
Mean
Q75%
σ
ToU
171
197
216
31
169
195
219
32
79
98
105
28
73
91
105
24
Custom
128
153
165
38
126
144
154
26
86
104
109
33
77
96
109
27
Custom, no WL flex
150
168
186
29
144
161
172
24
83
104
110
31
80
97
109
26
• 25 kW at 19:00,
• 50 kW at 20:00 (until 21:00).
We evaluate the impact of de-rating on system planning in
two scenarios: 50% flexible WL and no flexible WL, and
compare both to a baseline without virtual de-rating (with
50% flexible WL). Figure 4 shows the effect of the virtual
de-rating on day-ahead power profiles. On the right-side of
the figure, we observe that the de-rating constraint is satisfied
in the day-ahead bid. In the left-side of the figure, we see that
the BESS and ORC compensate most of the shortfall caused
by the virtual power de-rating. Interestingly, the ORC has a
crucial role in the case without WL flexibility, highlighting its
contribution in highly constrained operating conditions (e.g.,
de-rating and no WL flexibility)4. In the baseline, the expected
Fig. 4. Dispatch for 18.07.2025, no de-rating vs. de-rating with and without
WL flexibility.
energy supply cost is 101 EUR. With virtual de-rating it
increases by 10% (i.e., +11 EUR) with workload flexibility
and 33% (i.e. +34 EUR) without. This increase is mainly
caused by the additional aging induced on the BESS and the
reduced exports of heat. Given that this increase is similar to
the daily savings enabled by the custom contract (as shown
in Table II, larger than 30 EUR in expectation), we conclude
that the proposed contract is economically attractive for the
data center, as long as the triplet (P t
gcp,cap, tdaily,lim, tweekly,lim)
of the PPA are carefully selected.
If flexible workload is available, the bidding strategy lever-
ages VCCs, as shown in Fig. 5. Most WL is scheduled
during daytime hours, driven by high solar generation and low
spot prices. In contrast, costly morning hours and periods of
reduced grid capacity exhibit low virtual capacity, reflecting a
low inclination to schedule WL during these periods. During
4The heat price selected in Section V-A3 makes it generally more advan-
tageous to deliver recovered heat to the district heating network rather than
to the ORC system, if the district heating network needs that heat.
real-time operation, the workload scheduler should use the
VCCs to avoid overscheduling WL during constrained hours.
Fig. 5.
Resource usage and VCC for 18.07.2025, de-rating with WL
flexibility.
VI. CONCLUSION
In this work, we presented a practical risk-averse day-ahead
bidding strategy for small-scale data centers gaining access to
the spot electricity market through a custom PPA with the
local DSO. The strategy accounts for imbalance costs and
carbon emissions. It leverages flexible WL, BESS, local PV
generation, and waste heat recovery to minimize data center
operational costs.
Through three study cases based on an academic datacenter
in Lausanne, Switzerland, we analyzed the proposed PPA
combined with our bidding strategy. In the first study case,
we compared the proposed market scheme to a classic ToU
billing scheme and showed that it is expected to reduce energy
supply costs by 22%, thus showing that there are opportunities
for small-scale data centers in the day-ahead electricity market.
The second study case assessed the value of WL flexibility
and showed that the marginal gains it enables are unlikely to
motivate data centers to propose custom billing schemes for
flexible WL (from the energy supply perspective). Finally, the
third study case showed that virtual GCP transfer capacity de-
rating requests by the DSO should not significantly impact
operational costs if the supply agreement is well-designed.
We believe this work can benefit both DSOs and DCOs,
as the proposed bilateral billing scheme provides value to
both parties. The main limitation of the study is its focus on
the day-ahead scheduling phase, which requires simplifying
assumptions, particularly in WL modeling. Future work will
extend this approach toward real-time control strategies for
data centers, building on the bidding framework proposed here.
ACKNOWLEDGMENTS
This work is supported by the Heating Bits EPFL project
financed by the Solutions4Sustainability initiative. Data on

---

## Page 10

PREPRINT
10
data center usage and power consumption was provided by
the Research Computing Platform of EPFL.
REFERENCES
[1] Davide D’Ambrosio, Hugh Hopewell, Vincent Jacamon, Alex Martinos,
Nicholas Salmon, and Brent Wanner, “Energy and AI,” Tech. Rep., Apr.
2025. [Online]. Available: https://www.iea.org/reports/energy-and-ai
[2] European
Commission,
“About
the
EU
Emissions
Trading
System.”
[Online].
Available:
https://climate.ec.europa.eu/eu-action/
carbon-markets/eu-emissions-trading-system-eu-ets/about-eu-ets en
[3] Ember, “Europe’s AI ambitions at risk of gridlock.” [Online]. Available:
https://ember-energy.org/chapter/chapter-1-grids-for-data-centres/
[4] IEEE SA, “Review of Industry Efforts and Standards of Grid Readiness
For Data Center Deployment,” Jan. 2026.
[5] A. Garg, C. Booten, O. VanGeet, S. Pless, K. Stenger, J. Vidal,
R. Jackson, L. Lavin, and K. Prabakar, “Considerations for Distributed
Edge Data Centers and Use of Building Loads to Support Large
Interconnections,” Renewable Energy, 2025.
[6] IEA, “Grid congestion is posing challenges for energy security and tran-
sitions,” 2025. [Online]. Available: https://www.iea.org/commentaries/
grid-congestion-is-posing-challenges-for-energy-security-and-transitions
[7] B.
Chen,
Y.
Che,
Z.
Zheng,
and
S.
Zhao,
“Multi-objective
robust optimal bidding strategy for a data center operator based
on
bi-level
optimization,”
Energy,
vol.
269,
p.
126761,
Apr.
2023. [Online]. Available: https://linkinghub.elsevier.com/retrieve/pii/
S036054422300155X
[8] P. Zhang, K. Li, F. Wang, Z. Zhen, and T. Wang, “Optimal
Bidding Strategy for Data Center Aggregators Considering Spatio-
Temporal
Transfer
Characteristics,”
in
2020
IEEE/IAS
Industrial
and
Commercial
Power
System
Asia
(I&CPS
Asia).
Weihai,
China: IEEE, Jul. 2020, pp. 1667–1675. [Online]. Available: https:
//ieeexplore.ieee.org/document/9208528/
[9] W. Zhang, L. A. Roald, A. A. Chien, J. R. Birge, and V. M.
Zavala,
“Flexibility
from
networks
of
data
centers:
A
market
clearing formulation with virtual links,” Electric Power Systems
Research, vol. 189, p. 106723, Dec. 2020. [Online]. Available:
https://linkinghub.elsevier.com/retrieve/pii/S0378779620305265
[10] L. Liu, X. Shen, Z. Chen, Q. Sun, and R. Wennersten, “Optimal Energy
Management of Data Center Micro-Grid Considering Computing
Workloads Shift,” IEEE Access, vol. 12, pp. 102 061–102 075, 2024.
[Online]. Available: https://ieeexplore.ieee.org/document/10606267/
[11] L. Rao, X. Liu, L. Xie, and W. Liu, “Minimizing Electricity Cost:
Optimization of Distributed Internet Data Centers in a Multi-Electricity-
Market Environment,” in 2010 Proceedings IEEE INFOCOM.
San
Diego, CA, USA: IEEE, Mar. 2010, pp. 1–9. [Online]. Available:
http://ieeexplore.ieee.org/document/5461933/
[12] Z. Liu, Y. Chen, C. Bash, A. Wierman, D. Gmach, Z. Wang, M. Marwah,
and C. Hyser, “Renewable and Cooling Aware Workload Management
for Sustainable Data Centers.”
[13] A. Radovanovi´c, R. Koningstein, I. Schneider, B. Chen, A. Duarte,
B. Roy, D. Xiao, M. Haridasan, P. Hung, N. Care, S. Talukdar,
E. Mullen, K. Smith, M. Cottman, and W. Cirne, “Carbon-Aware
Computing for Datacenters,” IEEE Transactions on Power Systems,
vol. 38, no. 2, pp. 1270–1280, Mar. 2023. [Online]. Available:
https://ieeexplore.ieee.org/document/9770383/
[14] S. Hall, F. Micheli, G. Belgioioso, A. Radovanovi´c, and F. D¨orfler,
“Carbon-Aware
Computing
for
Data
Centers
with
Probabilistic
Performance Guarantees,” IEEE Transactions on Power Systems, pp.
1–14, 2025. [Online]. Available: https://ieeexplore.ieee.org/document/
11250739/
[15] Robert Basmadjian, Juan Felipe Botero, Giovanni Giuliani, Xavier
Hesselbach, Sonja Klingert, and Hermann de Meer, “Making Data Cen-
ters Fit for Demand Response: Introducing GreenSDA and GreenSLA
contracts.” 2016.
[16] Ali Pahlevan, Marina Zapater, Ayse Coskun, and David Atienza,
“ECOGreen: Electricity Cost Optimization for Green Datacenters in
Emerging Power Markets,” 2021.
[17] A.
Abada,
M.
St-Hilaire,
and
A.
Wei
Shi,
“Balancing
Power
Grids and Maximizing Revenue: A Novel Approach to Rebate
Auctions for Cloud Workload Migrations,” IEEE Access, vol. 12, pp.
172 969–172 979, 2024. [Online]. Available: https://ieeexplore.ieee.org/
document/10747803/
[18] M. T. Takci, M. Qadrdan, J. Summers, and J. Gustafsson, “Data
centres
as
a
source
of
flexibility
for
power
systems,”
Energy
Reports, vol. 13, pp. 3661–3671, Jun. 2025. [Online]. Available:
https://linkinghub.elsevier.com/retrieve/pii/S2352484725001623
[19] L.
Socci,
A.
Rocchetti,
A.
Verzino,
A.
Zini,
and
L.
Talluri,
“Enhancing
third-generation
district
heating
networks
with
data
centre waste heat recovery: analysis of a case study in Italy,”
Energy,
vol.
313,
p.
134013,
Dec.
2024.
[Online].
Available:
https://linkinghub.elsevier.com/retrieve/pii/S0360544224037915
[20] J. Wang, H. Deng, Y. Liu, Z. Guo, and Y. Wang, “Coordinated
optimal scheduling of integrated energy system for data center based
on computing load shifting,” Energy, vol. 267, p. 126585, Mar.
2023. [Online]. Available: https://linkinghub.elsevier.com/retrieve/pii/
S0360544222034727
[21] S. Zakeralhoseini and J. Schiffmann, “Experimentally validated pre-
design maps and performance estimation methods for small-scale
turbopumps for organic rankine cycles,” Journal of the Global Power
and Propulsion Society, vol. 9, no. May, pp. 17–32, May 2025.
[Online]. Available: https://doi.org/10.33737/jgpps/195408
[22] R. Van Erp, R. Soleimanzadeh, L. Nela, G. Kampitsis, and E. Matioli,
“Co-designing electronics with microfluidics for more sustainable
cooling,” Nature, vol. 585, no. 7824, pp. 211–216, Sep. 2020. [Online].
Available: https://www.nature.com/articles/s41586-020-2666-1
[23] R. T. Rockafellar and S. Uryasev, “Optimization of conditional
value-at-risk,” The Journal of Risk, vol. 2, no. 3, pp. 21–41, 2000.
[Online]. Available: http://www.risk.net/journal-of-risk/technical-paper/
2161159/optimization-conditional-value-risk
[24] M.
Dayarathna,
Y.
Wen,
and
R.
Fan,
“Data
Center
Energy
Consumption Modeling: A Survey,” IEEE Communications Surveys
& Tutorials, vol. 18, no. 1, pp. 732–794, 2016. [Online]. Available:
http://ieeexplore.ieee.org/document/7279063/
[25] U. Muhammad, M. Imran, D. H. Lee, and B. S. Park, “Design and
experimental investigation of a 1 kW organic Rankine cycle system
using R245fa as working fluid for low-grade waste heat recovery from
steam,” Energy Conversion and Management, vol. 103, pp. 1089–1100,
Oct. 2015. [Online]. Available: https://linkinghub.elsevier.com/retrieve/
pii/S0196890415006962
[26] E. M. L. Beale and J. J. H. Forrest, “Global optimization using
special ordered sets,” Mathematical Programming, vol. 10, no. 1,
pp. 52–69, Dec. 1976. [Online]. Available: http://link.springer.com/10.
1007/BF01580653
[27] M. L. Bynum, G. A. Hackebeil, W. E. Hart, C. D. Laird, B. L. Nicholson,
J. D. Siirola, J.-P. Watson, and D. L. Woodruff, Pyomo — Optimization
Modeling in Python, ser. Springer Optimization and Its Applications.
Cham: Springer International Publishing, 2021, vol. 67. [Online].
Available: http://link.springer.com/10.1007/978-3-030-68928-5
[28] L.
Hirth,
J.
M¨uhlenpfordt,
and
M.
Bulkeley,
“The
ENTSO-E
Transparency Platform – A review of Europe’s most ambitious
electricity data platform,” Applied Energy, vol. 225, pp. 1054–1067,
Sep. 2018. [Online]. Available: https://linkinghub.elsevier.com/retrieve/
pii/S0306261918306068
[29] Emissium, “Emissium Docs.” [Online]. Available: https://docs.emissium.
tech
[30] K. Rennert, F. Errickson, B. C. Prest, L. Rennels, R. G. Newell, W. Pizer,
C. Kingdon, J. Wingenroth, R. Cooke, B. Parthum, D. Smith, K. Cromar,
D. Diaz, F. C. Moore, U. K. M¨uller, R. J. Plevin, A. E. Raftery,
H. ˇSevˇc´ıkov´a, H. Sheets, J. H. Stock, T. Tan, M. Watson, T. E. Wong,
and D. Anthoff, “Comprehensive evidence implies a higher social cost
of CO2,” Nature, vol. 610, no. 7933, pp. 687–692, Oct. 2022. [Online].
Available: https://www.nature.com/articles/s41586-022-05224-9
[31] EWB, “Tarife Fernw¨arme,” Jan. 2024. [Online]. Available: https://www.
ewb.ch/angebot/waerme-kaelte/fernwaerme/tarife-fernwaerme.php
[32] A.
Paxian,
B.
Mannig,
M.
Tivig,
K.
Reinhardt,
K.
Isensee,
A. Pasternack, A. Hoff, K. Pankatz, S. Buchholz, S. Wehring,
P.
Lorenz,
K.
Fr¨ohlich,
F.
Kreienkamp,
and
B.
Fr¨uh,
“The
DWD
climate
predictions
website:
Towards
a
seamless
outlook
based on subseasonal, seasonal and decadal predictions,” Climate
Services,
vol.
30,
p.
100379,
Apr.
2023.
[Online].
Available:
https://linkinghub.elsevier.com/retrieve/pii/S2405880723000407
[33] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y.
Liu, “LightGBM: A Highly Efficient Gradient Boosting Decision Tree.”
[34] Romande ´energie, “Tarifs d’´electricit´e.” [Online]. Available: https:
//www.romande-energie.ch/electricite/votre-electricite#prix
[35] EPFL, “Operational and unit costs for RCP,” Sep. 2024. [Online]. Avail-
able:
https://www.epfl.ch/campus/services/finance/wp-content/uploads/
2024/09/Grille-RCP-validee-1.pdf