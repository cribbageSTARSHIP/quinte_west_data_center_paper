# Greening Multi-Tenant Data Center Demand Response
**arXiv ID:** 1504.07308v1
**Source File:** arxiv_sec1_grid_impacts_1504.07308v1.pdf

## Page 1

arXiv:1504.07308v1  [cs.GT]  27 Apr 2015
1
Greening Multi-Tenant Data Center Demand Response
Niangjun Chen, Xiaoqi Ren, Shaolei Ren, Adam Wierman
Abstract
Data centers have emerged as promising resources for demand response, particularly for emergency demand response (EDR),
which saves the power grid from incurring blackouts during emergency situations. However, currently, data centers typically
participate in EDR by turning on backup (diesel) generators, which is both expensive and environmentally unfriendly. In this
paper, we focus on “greening” demand response in multi-tenant data centers, i.e., colocation data centers, by designing a pricing
mechanism through which the data center operator can efﬁciently extract load reductions from tenants during emergency periods
to fulﬁll energy reduction requirement for EDR. In particular, we propose a pricing mechanism for both mandatory and voluntary
EDR programs, ColoEDR, that is based on parameterized supply function bidding and provides provably near-optimal efﬁciency
guarantees, both when tenants are price-taking and when they are price-anticipating. In addition to analytic results, we extend the
literature on supply function mechanism design, and evaluate ColoEDR using trace-based simulation studies. These validate the
efﬁciency analysis and conclude that the pricing mechanism is both beneﬁcial to the environment and to the data center operator
(by decreasing the need for backup diesel generation), while also aiding tenants (by providing payments for load reductions).
I. INTRODUCTION
Data centers have emerged as a promising demand response opportunity. However, data center demand response today is not
environmentally friendly since data centers typically participate by turning on backup (diesel) generators. In this paper, we focus
on designing a pricing mechanism for a crucial class of data centers for demand response – multi-tenant colocation data centers
– that allows the data center operator to encourage load shedding among tenants in response to demand response signals; thus
greening data center demand response by reducing the need for use of backup (diesel) generation.
Data center demand response. Power-hungry data centers have been quickly expanding in both number and scale to support
the exploding IT demand, consuming 91 billion kilowatt-hour (kWh) electricity in 2013 in the U.S. alone [29]. While traditionally
viewed purely as a negative, the massive energy usage of data centers has recently begun to be recognized as an opportunity. In
particular, because the energy usage of data centers tends to be ﬂexible, they are promising candidates for demand response, which
is a crucial tool for improving grid reliability and incorporating renewable energy into the power grid. From the grid operator’s
perspective, a data center’s ﬂexible power demand serves as a valuable energy buffer, helping balance grid power’s supply and
demand at runtime [43].
To this point, data center is a promising, but still largely under-utilized opportunity for demand response. However, this is
quickly changing as data centers play an increasing role in emergency demand response (EDR) programs. EDR is the most
widely-adopted demand response program in the U.S., representing 87% of demand reduction capabilities across all reliability
regions [25]. Speciﬁcally, during emergency events (e.g., extreme weather or natural disasters), EDR coordinates many large
energy consumers, including data centers, to shed their power loads, serving as the last protection against cascading blackouts that
could potentially result in economic losses of billions of dollars [27], [31]. The U.S. EPA has identiﬁed data centers as critical
resources for EDR [11], which was attested to by the following example: on July 22, 2011, hundreds of data centers participated
in EDR by cutting their electricity usage before a large-scale blackout would have occurred [27].

---

## Page 2

2
While data centers are increasingly contributing to EDR, they typically participate by turning on their on-site backup diesel
generators, which is neither cost effective nor environmentally friendly. For example, in California (a major data center market),
a standby diesel generator often produces 50-60 times more nitrogen oxides (a smog-forming pollutant) compared to a typical
power plant for each kWh of electricity, and diesel particulate represents the state’s most signiﬁcant toxic air pollution problem
[34].
In addition, relying on diesel generation for EDR presents emerging challenges which, if left unaddressed, may forfeit data
center’s EDR capability. First, as EDR is becoming more frequent, the current ﬁnancial compensation offered by power grid to data
centers (for committed energy reduction during EDR) may not be enough to cover the growing cost of diesel generation. Second,
data center operators are aggressively cutting the huge capital investment in their power infrastructure (e.g., 10-15$/watt [6], [22]),
by down-sizing the capacity of diesel generator and uninterrupted power supply (UPS) system [39]. Such under-provisioning of
diesel generator may compromise data center’s EDR capability. Therefore, to retain and encourage data center’s participation in
EDR without contaminating the environment, it is critical and urgent that data centers seek alternative ways to shed load.
Consequently, modulating server energy for green EDR (as well as other demand response programs such as regulation service
[20]) has received an increasing amount of attention in recent years, e.g., [1], [2], [7], [14], [20], [24], [41], [43]. These studies
leverage various widely-available IT computing knobs (e.g., server turning on/off and workload migration) in data centers and
provide algorithms to optimize them for participation in demand response markets. Importantly, these are not simply theoretical
studies. For example, a ﬁeld study by Lawrence Berkeley National Laboratory (LNBL) has illustrated that data centers can reduce
energy consumption by 10-25% in response to demand response signals, without noticeably impacting data center’s normal
operation [15].
Demand response in collocation data centers. While existing studies on data center demand response show promising
progress, they are primarily focused on owner-operated data centers (e.g., Google) whose operators have full control over both
servers and facilities. Unfortunately, such companies may actually be the least likely to participate in demand response programs,
because many of their workloads are extremely delay sensitive and their data centers have been optimized for delay.
In this paper, we focus on another type of data centers — multi-tenant colocation data centers (e.g., Equinix). These have
been investigated much less frequently, but are actually better targets for demand response then owner-operated data centers. In a
colocation data center (simply called “colocation” or “colo”), multiple tenants deploy and keep full control of their own physical
servers in a shared space, while the colo operator only provides facility support (e.g., high-availability power and cooling). Colos
are less studied than owner-operated data centers, but they are actually more common in practice. Colos offer data center solutions
to many industry sectors, and serve as physical home to many private clouds, medium-scale public clouds (e.g., VMware) [8],
and content delivery providers (e.g., Akamai). Further, a recent study shows that colos consume nearly 40% data center energy in
the U.S., while Google-type data centers collectively account for less than 8%, with the remaining going to enterprise in-house
data centers [29].
In addition to consuming a signiﬁcant amount of energy (more than Google-type data centers), colos are often located in
places more useful for demand response. While many mega-scale owner-operated data centers are built in rural areas, colos are
mostly located in metropolitan areas (e.g., Los Angeles, New York) [9], which are the very places where EDR is most needed.
Further, workloads in colos are highly heterogenous, and many tenants run non-mission-critical workloads (e.g., lab computing
[37]) that have very high scheduling ﬂexibilities, different delay sensitivities, peak load periods, etc., which is ideal for demand
response participation.
For all these reasons, colos are key participants in EDR programs. Compared to owner-operated data centers that can leverage
various computing knobs, however, greening colos’ participation in EDR by reducing reliance on diesel generator is signiﬁcantly
more challenging, because of colo operators’ lack of control over their tenants’ servers. On the other hand, many tenants in colos
run servers hosting highly-ﬂexible and non-critical workloads with a great potential for shedding loads when called upon [37].

---

## Page 3

3
Thus, tenants’ load shedding potentials, if appropriately exploited, can altogether form a green alternative to diesel generation
for colo EDR. Nonetheless, tenants manage their own servers independently and may not have incentive to cooperate with the
operator for EDR, thus raising the research question: how can a colo operator efﬁciently incentivize its tenants’ load shedding for
EDR?1
Contributions of this paper. In this paper, we focus on “greening” colocation demand response by extracting load reduction
from tenants instead of relying on backup diesel generation. We study both mandatory EDR, a type of EDR program in which
participants sign contracts and are obliged to reduce loads when requested [31], and voluntary EDR, where participants voluntarily
reduce loads for ﬁnancial compensation upon grid request. In both cases, we propose a new pricing mechanism with which colo
operators can extract load shedding from tenants. In particular, our proposed approach, called ColoEDR, can effectively provide
incentives for tenants to reduce energy consumption during EDR events, complementing (and even substituting for) the high-cost
and environmentally-unfriendly diesel generation.
ColoEDR works as follows. After an EDR signal arrives at the colo operator, tenants bid using a parameterized supply
function, and then the colo operator announces a market clearing price which, when plugged into the bids, speciﬁes how much
energy tenants will reduce and how much they will be paid. Participation by the tenants is straightforward, since they are required
to bid only one parameter, which can be viewed as a proxy of how much ﬂexibility in energy usage they have at that moment.
This participation can be automated and so can be easily incorporated into current practice, and mimics the way generation
resources participate in electricity markets more broadly. For example, colo operators at Verizon Terremark already communicate
with tenants in preparation for an EDR event.
The main technical contribution of the paper is the analysis of the efﬁciency of the supply function mechanism proposed in
ColoEDR. In particular, while there is a large literature studying supply function bidding [5], [10], [16]–[18], our setting here
is novel and different because the colo operator can either satisfy the EDR request using ﬂexibility from the tenants (as in prior
supply funding literature) or through its backup diesel generator. Thus, the diesel generator is an outside option that allows for
elasticity in the amount of response extracted from the tenants. Further, the colo operator can combine and balance between its
two options (i.e., tenant load shedding and backup generator) in order to minimize costs. This creates a multi-stage game and
adds a considerable complexity as compared to the standard setting without an outside option, e.g., [18].
Despite the added complexity, our analysis precisely characterizes the equilibrium outcome, both when tenants are price-
taking and when they are price-anticipating. In both cases, our results highlight that ColoEDR suffers little performance loss
compared to the socially optimal outcome, both from the operator’s and the tenants’ perspectives. However, our analysis does
highlight one possible drawback of ColoEDR. In the worst case, it is possible that ColoEDR may result in using signiﬁcantly
more on-site diesel generation than would the socially optimal. However, this bad event occurs only in cases where one tenant
has an overwhelmingly dominant amount of servers and has a unit cost (for energy reduction) just below that of on-site diesel
generation. Such an exploitation of market power is unlikely to be possible in practical multi-tenant colocation data centers.
In addition to our theoretical analysis, we investigate a case study of colocation demand response in §VI using trace-based
experiments. The results further validate the design of ColoEDR, and show that it achieves the mandatory energy reduction for
EDR while beneﬁting tenants through ﬁnancial incentives and decreasing the operator’s cost. Moreover, our simulation study
shows that the efﬁciency loss in practical settings is even lower than what is suggested by the analytic bounds. This is especially
true for the amount of on-site generation, which the analytic results suggest can (in the worst-case) be signiﬁcantly larger than
socially optimal but in realistic settings is very close to the social optimal.
1Tenants receive UPS-protected power from colo operator and share cooling systems. In other words, tenants’ total energy consumption is not directly
provided by grid and includes non-separable cooling energy, which makes tenants ineligible for direct participation in EDR [31].

---

## Page 4

4
II. PROBLEM FORMULATION
Our focus is to design a mechanism for a colo operator to extract tenant load reductions in response to to an EDR signal.
Thus, we need to begin by describing a model for a colo operator.
Recall that the colo operator is responsible for non-IT facility support (e.g., high-availability power, cooling). We capture
the non-IT energy consumption using Power Usage Effectiveness (PUE) γ, which is the ratio of the total colocation energy
consumption to the IT energy consumption. Typically, γ ranges from 1.1 to 2.0, depending on factors such as outside temperature.
When the operator receives an EDR signal from the LSE, it has two options for satisfying the load reduction. First, without
involving the tenants, the colo operator can use its on-site backup diesel generator.2 We denote the amount of energy reduction
by diesel generation by y and the cost per kWh of diesel generation (e.g., for fuels) by α.
Alternatively, the colo operator could try to extract IT load reductions from the tenants. We consider a setting where there
are N tenants, i ∈N = {1, 2, · · · , N}. When shedding energy consumption, a tenant i will incur some costs and we denote
the cost from shedding si by a function ci(si). These costs could be due to wear-and-tear, performance degradation, workload
shifting, etc. For the purposes of our model, we do not specify which technique reduces the IT load, only its cost. For details on
how one might model such costs, see [4], [12], [30], [42]. A standard, natural assumption on the costs is the following.
Assumption 1. For each n, the cost function cn(sn) is continuous, with cn(sn) = 0 if sn ≤0. Over the domain sn ≥0, the
cost function cn is convex and strictly increasing.
Intuitively, convexity follows from the conventional assumption that the unit cost increases as tenants reduce more energy
(e.g., utilization becomes higher when servers are off, leading to a faster increase in response time of tenants’ workloads).
III. PRICING TENANT LOAD SHEDDING IN MANDATORY EDR
EDR is the last line of protection against cascading power failures, and represents 87% of demand reduction capabilities
across all the U.S. reliability regions [25]. In general, there are two types of EDR programs: mandatory and voluntary (also called
economic) [31]. We focus on mandatory EDR ﬁrst, and return to voluntary EDR in Section V.
For mandatory EDR, participants typically sign contracts with a load serving entity (LSE) in advance (e.g., 3 years ahead
in PJM [31]) and receive ﬁnancial rebates for their committed energy reduction even if no EDR signals are triggered during the
participation year, whereas non-compliance (i.e., failure to cut load as required during EDR) incurs heavy penalty [31]. If an LSE
anticipates that an emergency will occur, participants are notiﬁed, usually at least 10 minutes in advance, and obliged to fulﬁll
their contracted amounts of energy reduction for the length of the event, which may span a few minutes to a few hours.
In mandatory EDR, the colo operator has two options for obtaining load reductions in response to an EDR signal that speciﬁes
the reduction amount – tenants or on-site generation. Thus, it must balance between paying tenants for reduction and using on-site
generation in order to minimize cost. Note that tenants’ load reduction can also reduce the usage of diesel generator, mitigating
environmental impacts. Nonetheless, the challenge is that the operator does not know the tenant cost functions, and so cannot
determine the cost-minimizing price.
Consequently, the operator has two options: (i) predict the tenant supply function and compute prices based on the predictions,
or (ii) allow tenants to supply some information about their cost functions through bids. Clearly, there is a tradeoff here between
the accuracy of predictions and the manipulation possible in the bids. Both of these approaches have been looked at in the literature
[3], [10], [18], [24], [28], though not in the context of colo demand response. In general, the broad conclusion is that approach
(i) is appropriate when predictions are accurate and one bidder has market power (e.g., is signiﬁcantly larger than other bidders).
While market power is a considerable issue for the participation of owner-operated data centers in demand response programs due
2Other alternatives, e.g., battery [39], usually only last for < 5 minutes. So, diesel generation is the typical method [11].

---

## Page 5

5
to their large size compared to other participants, it is not an issue within a speciﬁc colo that houses multiple tenants (typically
of comparable sizes), and so we adopt approach (ii) in this paper.
Speciﬁcally, we design a mechanism, named ColoEDR, where tenants bid using parameterized supply functions and then,
given the bids, the operator decides how much load to shed via tenants and how much to shed via on-site generation. In the
following, we describe the mechanism and then contrast our approach with other potential alternatives.
Note that, throughout this paper, we focus on one EDR event, and thus we omit the time index. In the case of multiple
consecutive EDR events, ColoEDR will be executed once at the beginning of each event, as is standard in the literature [24],
[33].
A. An overview of ColoDR
The operation of ColoEDR is summarized below, and then discussed in detail in the text that follows.
1) The colo operator receives an EDR reduction target δ and broadcasts the supply function S(bn, p) to tenants according to (1);
2) Participating tenants respond by placing their bids bn;
3) The colo operator decides the amount of on-site generation y and market clearing price p to minimize its cost, using equations
(2) and (3);
4) EDR is exercised. ∀n ∈N, tenant n sheds S(bn, p), and receives pS(bn, p) reward.
Given the overview above, we now discuss each step in more detail.
Step 1. Upon receiving an EDR notiﬁcation of an energy reduction target δ, the colo operator broadcasts a parameterized
supply function S(b, p) to tenants (by, e.g., signalling to the tenants’ server control interfaces, which are widely existing today).
The form of S(b, p) is the following parameterized family3:
S(bn, p) = δ −bn
p .
(1)
where p is offered reward for each kWh of energy reduction and bn is the bidding values that can be chosen by tenant n. This
form is inspired by [18], where it is shown that by restricting the supply function to this parameterized family, the mechanism
can guide the ﬁrms in the market reach to an equilibrium with desirable properties.4 Note that, to be consistent with the supply
function literature, we exchangeably use “price” and “reward rate” wherever applicable.
Step 2. Next, according to the supply function, each participating tenant submits its bid bn to the colo operator. This bid
speciﬁes that, at each price p, it is willing to reduce S(bn, p) unit of energy. The bid is chosen by tenants individually to maximize
their own utility and can be interpreted as the amount of IT service revenue that tenant n is willing to forgo. Note that bn can be
chosen to ensure that tenant n will not be required to reduce more energy than its capacity. To see this, note that since the operator
is cost-minimizing, p(b, y) ≤α always holds, i.e., the market clearing price is lower than the unit cost of diesel generation.
Hence, if Kn is the capacity of reduction for tenant n, as long as bn ≥α(δ −Kn), then
S(bn, p) = δ −bn
p ≤δ −bn
α ≤Kn.
An important note about the tenant bids is that the supply function is likely of a different form than the true cost function cn,
and so it is unlikely for the tenants to reveal their cost functions truthfully. This is necessary in order to provide a simple form
for tenant bids. Bidding their true cost functions is too complex and intrusive. However, a consequence of this is that one must
3The supply function allows tenants to have negative supply, i.e., tenants consume more energy intentionally, which is neither proﬁt maximizing nor practical.
We show in §IV that energy reduction of each tenant is always nonnegative in both equilibrium and social optimal outcomes.
4 [18] studies the case where ﬁrms bid to supply an inelastic demand, which is equivalent to ﬁxing the diesel generation y = 0 in our case. Allowing the
operator to choose y in a cost-minimizing manner leads to signiﬁcantly different results, as will be shown in §IV-A and §IV-B.

---

## Page 6

6
carefully analyze the emergent equilibrium to understand the efﬁciency of the pricing mechanism. We study both the cases of
price-taking and price-anticipating equilibrium in §IV.
Step 3. After tenants have submitted their bids, the colo operator decides the amount of energy y to produce via on-site
generation and the clearing price p. Given y, the market clearing price has to satisfy ΣnS(p(b), bn) + y = δ, thus
p(b, y) =
P
n bn
(N −1)δ + y .
(2)
To determine the amount of local generation y, the operator minimizes the cost of the two load-reduction options, i.e.,
y = arg min
0≤y≤δ
(δ −y) · p(b, y) + αy.
(3)
Step 4. Finally, EDR is exercised and tenants receive ﬁnancial compensation from the colo operator via the realized price in
(2), shed load S(p, bn), and on-site generation produces (3).
B. Discussion
To the best of our knowledge, this paper represents the ﬁrst attempt to design a supply function bidding mechanism for
colocation demand response. Although alternative mechanisms may be applicable, there are compelling advantages to the supply
function approach. First, bidding for the tenants is simple – they only need to communicate one number, and it is already common
practice for operators to communicate with tenants before EDR events, so the overhead is small. Second, the colo operator collects
just enough information (i.e., how much energy reduction each tenant will contribute to EDR), while tenants’ private information
(i.e., how much performance penalty/cost each for energy reduction) is masked by the form of the supply function and hence not
solicited. Third, ColoEDR guarantees that the colo operator will not incur a higher cost than the case where only diesel generator
is used. Further, ColoEDR pays a uniform price to all participating tenants and hence ensures fairness.
The most natural alternative design to supply function bidding is a VCG-based mechanism, as is suggested in [46]. While
VCG-based mechanisms have the beneﬁts of incentive compatibility, however, these mechanisms violate all the four properties
discussed above. Under such approaches, tenants must submit very complex bids describing their precise cost functions, the true
private cost of tenants is disclosed, payment made to tenants may be unbounded, and prices to different tenants are differentiated
and thus raises unfairness issues.
Due to these shortcomings, VCG-based mechanisms are typically not adopted in complex resource allocation settings such
as power markets, where supply-function based designs are common [18]. In fact, nearly all generation markets use a variation
of supply function bidding.
IV. EFFICIENCY ANALYSIS OF ColoEDR FOR MANDATORY EDR
Given the ColoEDR mechanism described above, our task now is to characterize its efﬁciency. There are two potential causes
of inefﬁciency in the mechanism: the cost minimizing behavior of the operator and the strategic behavior (bidding) of the tenants.
In particular, since the forms of the tenant’s cost functions are likely more complex than the supply function bids, tenants cannot
bid their true cost function even if they wanted to. This means that evaluating the equilibrium outcome is crucial to understanding
the efﬁciency of the mechanism.
Further, the equilibrium outcome that emerges depends highly on the behavior of the tenants – whether they are price-taking,
i.e., they passively accept the offered market price p as given when deciding their own bids; or price-anticipating, i.e., they
anticipate how the price p will be impacted by their own bids. We investigate both models, in §IV-A and §IV-B, respectively.

---

## Page 7

7
In both cases, the goal of our analysis is to assess the efﬁciency of ColoEDR. To this end, we adopt a notion of a (socially)
optimal outcome, and focus on the following social cost minimization problem.
SCM :
min αy +
X
i∈N
ci(si)
(4a)
s.t.
y + γ ·
X
i∈N
si = δ
(4b)
si ≥0, ∀i ∈N,
y ≥0.
(4c)
where si and ci are tenant i’s energy reduction and corresponding cost, respectively.
The objective in SCM can be interpreted as the tenants’ cost plus the colo operator’s cost. Note that the internal payment
transfer between the colo operator and tenants cancels, and does not impact the social cost. Also, note that payment from the LSE
to the colo operator is not included in the social cost objective, since it is independent of how the operator obtains the amount of
δ load reduction. Additionally, we do not include the option of ignoring the event and taking the penalty, since the penalties for
lack of participation are typically extreme. Finally, the Lagrangian multiplier of (4b) can be interpreted as the social optimal price
p∗, i.e., given this price as reward for energy reduction, each tenant will individually reduce their energy by sn that corresponds
to the social cost minimization solution in (4).
Before moving to the analysis, in order to simplify notation, we suppress the PUE γ by, without loss of generality, setting
γ = 1. This is equivalent to a change of notation y′ = y/γ, δ′ = δ/γ, and α′ = αγ, i.e., translating the diesel generation, unit
cost of diesel generation, and EDR energy reduction target into their respective equivalent amounts in terms of server energy.
A. Price-Taking Tenants
When tenants are price-taking, they maximize their net utility, which is the difference between the payment they receive and
the cost of energy reduction, given the assumption that they consider their action does not impact the price.
Pn(bn, p)
= pSn(bn, p) −cn(Sn(bn, p))
(5a)
= pδ −bn −cn

δ −bn
p

.
(5b)
Here, the price-taking assumption implies that the variable p is considered to be as is. The market equilibrium for price-taking
tenants is thus deﬁned as follows.
Deﬁnition 1. A triple (b, p, y) is a (price-taking) market equilibrium if each tenant maximizes its payoff deﬁned in (5), market
is cleared by setting price p according to (2), and the amount of on-site generation is decided by (3), i.e.,
Pn(bn; p) ≥Pn(¯bn; p)
∀¯bn ≥0,
n = 1, . . . , N.
(6)
p =
P
i∈N bi
(N −1)δ + y .
(7)
y = arg min
0≤y≤δ
(δ −y) · p(b, y) + αy.
(8)
1) Market Equilibrium Characterization: The key to our analysis is the observation that the equilibrium can be charac-
terized by an optimization problem. Once we have this optimization, we can use it to characterize the efﬁciency of the equilibrium
outcome. This approach parallels that used in [18]; however, the optimization obtained has a different structure due to local diesel
generation. Additionally, though we use an optimization to characterize the equilibrium, the game is not a potential game.
Our ﬁrst result highlights that, given any choice for on-site generation, a unique market equilibrium exists for the tenants,
and can be characterized via a simple optimization.

---

## Page 8

8
Proposition 1. Under Assumption 1, when tenants are price-taking, for any on-site generation level 0 ≤y < δ, there exists
a market equilibrium, i.e., a vector bt = (bt
1, . . . , bt
N) ≥0 and a scalar p > 0 that satisﬁes (2), and the resulting allocation
sn = S(bn, p) is the optimal solution of the following
min
s
X
i∈N
ci(si)
(9a)
s.t.
X
i∈N
si = (δ −y),
(9b)
si ≥0, ∀i ∈N.
(9c)
This result is a key tool for understanding the overall market outcome. Intuitively, the operator running ColoEDR is more
likely (than the social optimal) to use on-site generation, since this reduces the price paid to tenants. The following proposition
quantiﬁes this statement.
Proposition 2. Under Assumption 1, it is optimal for price-taking tenants to use on-site generation if and only if
α <
(Σnbn)
(N −1)δ , 5
(10)
However, when the operator is proﬁt maximizing, it will turn on on-site generation if and only if
α <
N
N −1
(Σnbn)
(N −1)δ .
(11)
This proposition is an important building block because the most interesting case to consider is when it is optimal to use
some on-site generation and some tenant load shedding, i.e., δ > y∗> 0. Otherwise the EDR demand should be entirely fulﬁlled
by tenants, and the analysis reduces to the case of an inelastic demand, as studied in [18]. Thus, subsequently, we make the
following assumption, which ensures that on-site generation is valuable.
Assumption 2. The unit cost of on-site generation is cheap enough that the optimal on-site generation is non-zero, i.e., α satisﬁes
(10).
Note that, when Assumption 2 holds, by ﬁrst-order optimality condition of (3) we have
y =
r
(Σi∈N bi)Nδ
α
−(N −1)δ,
(12)
and so the market clearing price for the tenants given on-site generation is
p =
P
i∈N bi
(N −1)δ + y =
r
(Σi∈N bi)α
Nδ
.
(13)
Using these allows us to prove a complete characterization of the market equilibrium under price-taking tenants. This theorem
is the key to our analysis of market efﬁciency.
Theorem 3. When Assumptions 1 and 2 hold there is a unique market equilibrium, i.e., a vector bt = (bt
1, . . . , bt
N) ≥0, yt > 0
and a scalar pt > 0 that satisﬁes (6)-(8), and the resulting allocation (st, yt) where st
n = S(bt
n, pt) is the optimal solution of
5We adopt the convention that 0
0 = 0 and x
0 = +∞when x > 0. Therefore, when N = 1, unless the bid is 0, the condition is always satisﬁed.

---

## Page 9

9
the following problem
min
s,y
X
n
cn(sn) +
α
2Nδ (y + (N −1)δ)2
(14a)
s.t.
X
n
sn = δ −y,
(14b)
sn ≥0, ∀n,
y ≥0.
(14c)
2) Bounding Efﬁciency Loss: We now use Theorem 3 to bound the efﬁciency loss due to strategic behavior in the market.
Denote the socially optimal on-site generation by y∗, the optimal price that leads to the optimal allocation si, ∀i ∈N by p∗, and
let yt and pt be the allocation under the price-taking assumption.
Our ﬁrst result highlights that, due to the cost-minimizing behavior of the operator, the equilibrium outcome uses more on-site
generation and pays a lower price to the tenants than the social optimal.
Proposition 4. Suppose that Assumptions 1 and 2 hold. When tenants are price-taking, the operator running ColoEDR uses
more on-site generation and pays a lower price for power reduction to its tenants than the social optimal. Speciﬁcally, yt ≥y∗
and
N−1
N p∗≤pt ≤p∗.
Now, we move to more detailed comparisons. There are three components of market efﬁciency that we consider: social welfare,
operator cost, and tenant cost.
First, let us consider the social cost.
Theorem 5. Suppose that Assumptions 1 and 2 hold. Let (st, yt) be the allocation when tenants are price-taking, and (s∗, y∗)
be the optimal allocation. Then the welfare loss is bounded by: P
n cn(st
n) + αyt ≤P
n cn(s∗
n) + αy∗+ αδ/2N.
Importantly, this theorem highlights that the market equilibrium is quite efﬁcient, especially if the number of tenants is large
(the efﬁciency loss decays to zero as O(1/N)). However, the market could maintain good overall social welfare at the expense
of either the operator or the tenants. The following results show this is not true.
Let costo(p, y) be the operator’s cost, i.e.,
costo(p, y) = p(δ −y) + αy.
(15)
Then, we have the following results.
Theorem 6. Suppose that Assumptions 1 and 2 are satisﬁed. The cost of colo operator with price-taking tenants is smaller than
the cost in the socially optimal case. Further, we have costo(p∗, y∗) −αδ/N ≤costo(pt, yt) ≤costo(p∗, y∗).
B. Price-Anticipating Tenants
In contrast to the price-taking model, price-anticipating tenants realize that they can change the market price by their bids,
i.e., that p is set according to (13), and adjust their bids accordingly. Clearly, this additional strategic behavior can lead to larger
efﬁciency loss. But, in this section, we show that the extra loss is surprisingly small, especially when a large number of tenants
participate in ColoEDR.
Given bids from the other tenants, each price-anticipating tenant n optimizes the following cost over bidding value bn
Qn(bn, b−n) = p(b)Sn(bn, p) −cn(Sn(bn, p))

---

## Page 10

10
where we use b−n to denote the vector of bids of tenants other than n; i.e., b−n = (b1, . . . , bn−1, bn+1, . . . , bN). Thus,
substituting (1) and (13), we have
Qn(bn; b−n) =
r
(Σnbn)αδ
N
−bn −cn
 
δ −
bn
√
Σmbm
r
Nδ
α
!
.
(16)
Note that the payoff function Qn is similar to the payoff function Pn in the price-taking case, except that the tenants anticipate
that the colo operator will set the price p according to p = p(b, y) from (13).
Deﬁnition 2. A triple (b, p, y) is a (price-anticipating) market equilibrium if each tenant maximizes its payoff deﬁned in (16),
the market is cleared by setting the price p according to (2) and the amount of on-site generation is decided by (3), i.e.,
Qn(bn; bn) ≥Qn(¯bn; bn)
∀¯bn ≥0,
n = 1, . . . , N
(17)
p =
P
n bn
(N −1)δ + y .
(18)
y = arg min
0≤y≤δ
(δ −y) · p(b, y) + αy.
(19)
Note that our analysis in this section requires one additional technical assumption about the tenant cost functions.
Assumption 3. The marginal cost of all the tenants at 0 is greater than
α
2N , i.e., ∂+cn(0)
∂sn
≥
α
2N , ∀n.
This assumption is quite mild, especially if the number of tenants N is large. Intuitively, it says that the unit cost of on-site
generation is competitive with the cost of tenants reducing their server energy.
1) Market Equilibrium Characterization: Our analysis of market equilibria proceeds along parallel lines to the price-
taking case. We again show that there exists a unique equilibrium and, furthermore, that the tenants and operator behave in
equilibrium as if they were solving an optimization problem of the same form as the aggregate cost minimization (4), but with
“modiﬁed” cost functions.
Theorem 7. Suppose that Assumption 1-3 are satisﬁed, then there exists a unique equilibrium of the game deﬁned by
(Q1, . . . , Qn) satisfying (17)-(19). For such an equilibrium, the vector sa deﬁned by sa
n = S(p(ba), ba
n) is the unique optimal
solution to the following optimization:
min
X
n
ˆcn(sn) +
α
2Nδ (y + (N −1)δ)2
(20a)
s.t.
X
n
sn = δ −y
(20b)
y ≥0, sn ≥0,
n = 1, . . . , N,
(20c)
where, for sn ≥0,
ˆcn(sn) =1
2

cn(sn) + sn α
2N

+ 1
2
Z sn
0
s∂+cn(z)
∂z
−α
2N
2
+ 2∂+cn(z)
∂z
zα
Nδ dz,
(21)
and for sn < 0,
ˆcn(sn) = 0.
Although the form of ˆcn(sn) looks complicated, there is a simple linear approximation that gives useful intuition.
Lemma 8. Suppose that Assumption 1-3 are satisﬁed. For all modiﬁed cost ˆcn, n ∈1, . . . , N, for any 0 ≤sn ≤δ,
cn(sn) ≤ˆcn(sn) ≤cn(sn) + sn α
2N ,
Furthermore, when the left or right derivatives of ˆc(·) is deﬁned, it can be bounded by
∂−cn(sn)
∂sn
≤∂−ˆc(sn)
∂sn
≤∂+ˆc(sn)
∂sn
≤∂+cn(sn)
∂sn
+ α
2N .

---

## Page 11

11
The form of Lemma 8 shows that the difference between the modiﬁed cost function in (21) and the true cost diminishes as N
increases, and this is the key observation that underlies our subsequent results upper bounding the efﬁciency loss of ColoEDR.
2) Bounding Efﬁciency Loss: We now use Theorem 7 to bound the efﬁciency loss due to strategic behavior. Note that, by
comparing to both the socially optimal and the price-taking outcomes, we can understand the impact of both strategic behavior
by the operator and the tenants.
Our ﬁrst result focuses on comparing the price-anticipating and price-taking equilibrium outcomes. It highlights that price-
anticipating behavior leads to tenants receiving higher price while providing less load shedding.
Theorem 9. Suppose Assumption 1-3 hold. Let (pt, yt) be the equilibrium price and on-site generation when tenants are price-
taking, and (pa, ya) be those when tenants are price-anticipating, then we have, yt ≤ya ≤yt +δ/2 and pt ≤pa ≤pt +α/2N.
Next, combining Theorem 9 and Proposition 4 yields the following comparison between the price-anticipating and socially
optimal outcomes.
Corollary 10. Suppose Assumption 1-3 hold. When tenants are price-anticipating, an operator running ColoEDR uses more
on-site generation and pays lower market price than in the socially optimal case, i.e., ya ≥y∗and N−1
N p∗≤pa ≤p∗.
Now, we move to more detailed comparisons. There are three components of market efﬁciency that we consider: social welfare,
operator cost, and tenant cost.
First, let us consider the social cost.
Theorem 11. Suppose that Assumption 1-3 hold. Let (sa, ya) be the allocation when tenants are price-anticipating, and (s∗, y∗)
be the optimal allocation. The welfare loss is bounded by: P
n cn(sa
n) + αya ≤P
n cn(s∗
n) + αy∗+ αδ/N.
Similarly to the price-taking case, the efﬁciency loss in the price-anticipating case decays to zero as O(1/N), only with a
larger constant. Also, as in the case of price-taking tenants, we again see that neither the tenants nor the operator suffers signiﬁcant
efﬁciency loss.
Theorem 12. Suppose that Assumption 1-3 hold. The cost of colo operator for price-anticipating tenants is smaller than the cost
in the socially optimal case. Further, we have
costo(p∗, y∗) −αδ
N ≤costo(pa, ya) ≤costo(p∗, y∗),
costo(pa, ya) −αδ
N ≤costo(pt, yt) ≤costo(pa, ya)
Finally, let us end by considering the amount of on-site generation used in equilibrium. Here, in the worst-case, the equilibrium
on-site generation for price-anticipating tenants can be arbitrarily worse than the socially optimal, i.e., the socially optimal can
use no on-site generation while the equilibrium outcome uses only on-site generation.
Theorem 13. Suppose that Assumption 1-3 hold. For any ε > 0, N ≥1, there exist cost functions c1, . . . , cN, such that the
on-site generation in the market equilibrium compared to the optimal is given by ya −y∗≥δ −ε.
This is a particularly disappointing result since a key goal of the mechanism is to obtain load shedding from the tenants.
However, the proof emphasizes that this is unlikely to occur in practice. In particular, the worst-case scenario is that there exists
a dominant (monopoly) tenant, which is unlikely in a multi-tenant colo, that has a cost function asymptotically linear with unit
cost roughly matching the on-site generation price α. We conﬁrm this in a case study in Section VI.

---

## Page 12

12
C. Discussion
The main results for the price-taking and price-anticipating analyses are summarized in Table I. Note that simpliﬁed bounds
are presented in the table, to ease interpretation, and the interested reader should refer to the theorems in §IV-A and §IV-B for
the tightest bounds. Also, note that the benchmark for social cost we consider is an ideal, but not achievable, mechanism.
Tenants
Price Ratio
Colo Saving
Welfare Loss
Price-taking
[ N−1
N , 1]
[0, αδ/N]
[0, αδ/2N]
Price-anticipating
[ N−1
N , 1]
[0, αδ/N]
[0, αδ/N]
TABLE I
PERFORMANCE GUARANTEE OF ColoEDR COMPARED TO THE SOCIAL OPTIMAL ALLOCATION.
To summarize the results in Table I brieﬂy, note ﬁrst that ColoEDR always beneﬁts the operator, since the price paid to
tenants to reduce energy is always less than the socially optimal price, and the total cost incurred by operator for energy reduction
is also less than that of the social optimal. Secondly, ColoEDR also gives the tenants approximately the social optimal payment,
since the operator’s additional beneﬁt is bounded above by αδ/N. This naturally means that the loss in payment for tenants
compared to the social optimal is also αδ/N, which approaches 0 as N grows. Third, regardless of tenants being price-taking or
price-anticipating, ColoEDR is approximately socially cost-minimizing as the number of tenants grows.
However, while ColoEDR is good in terms of operator, tenant, and social cost, it may not use the most environmentally
friendly form of load reduction: in the worst case, the upper bound on the extra on-site generation that ColoEDR uses is not
decreasing with N. However, the analysis highlights that this worst-case occurs when there exists a dominant tenant with unit
cost of energy reduction that is consistently just below the cost of diesel over a large range of energy reduction. As our case
study in §VI shows, this is unlikely to occur in practice. So, ColoEDR can be expected to use an environmentally friendly mix
in most realistic situations.
V. PRICING TENANT LOAD SHEDDING IN VOLUNTARY EDR
We now turn from mandatory EDR to voluntary EDR and show how the analysis and design of ColoEDR can be extended.
Under voluntary EDR, a colo operator is offered a certain compensation rate for load reduction and can cut any amounts of energy
at will without any obligation. Voluntary EDR often supplements mandatory EDR, and both are widely adopted in practice [25],
[31]. Since the colo operator can freely decide on the amount of energy to cut based on the compensation rate [31], the amount of
energy reduction responses from tenants is fully elastic, differing from mandatory EDR where the total energy reduction (including
diesel generation if necessary) needs to satisfy a constraint δ.
In the following, we formulate the problem and generalize ColoEDR for the voluntary EDR setting. Furthermore, we illustrate
that the efﬁciency analysis, though more complicated, parallels that of mandatory EDR.
A. Problem Formulation
During a voluntary EDR event, the LSE offers a reward of u for each unit of energy reduction (or diesel generation if
applicable). In our setting, the colo operator aims at maximizing its proﬁt through extracting loads from tenants using parameterized
supply function bidding, as considered for mandatory EDR.
A key difference with the case of mandatory EDR is that, since the reduction is voluntary, diesel generation need not be
considered. In particular, if the reward offered the the LSE for reduction is larger than the cost of diesel, then the operator can
contribute its whole diesel capacity and, if the reward is smaller than the cost of diesel, no diesel need be used. Compared to
the mandatory EDR setting, operator need to use more diesel generation when tenants’ bids are high in order to meet the ﬁxed
reduction target δ; in the voluntary EDR case, the operator can simply reduce the DR contribution by tenants when their bids are
high. Thus, the optimization of diesel generation by the operator is separable from the optimization of tenant reduction.

---

## Page 13

13
This yields a situation where the net proﬁt (from tenant reduction) received by the colo operator is:
u · d −p · d
(22)
where p is the unit price the colo operator pays to the tenants to solicit d units of reduction in aggregate, which arises from N
tenants where tenant i has reduction capacity Di.
a) An overview of ColoEDR: It is straightforward to adapt ColoEDR to this setting. We outline its operation in four
steps below, which parallel the steps in the case of mandatory EDR.
1) The colo operator receives the voluntary EDR reduction price u and broadcasts the supply function S(bn, p) to tenants according
to
Si(bi, p) = Di −bi
p ,
(23)
where Di is the capacity of tenant i for reduction determined exogenously.
2) Participating tenants respond by placing their bids bn in order to maximize their own payoff;
3) The colo operator decides the total amount of reduction from tenants d and market clearing price p to maximize its utility.
Given the bids b = (b1, . . . , bn), if the operator decides to offer d amount of energy reduction to the utility, then the market
clearing price p will be
p =
Pn
i=1 bi
Pn
i=1 Di −d.
(24)
Hence to maximize the operator’s proﬁt, the operator will chooose d such that
d =
arg max
0≤d≤Pn
i=1 Di
(u −p)d =

u −
Pn
i=1 bi
Pn
i=1 Di −d

d.
(25)
It follows from the ﬁrst order optimality of (25) that
d =
n
X
i=1
Di −
r
(Pn
i=1 bi)(Pn
i=1 Di)
u
,
(26)
which gives that the price set by a proﬁt maximizing operator will be
p =
s
u Pn
i=1 bi
Pn
i=1 Di .
(27)
4) Voluntary EDR is exercised. ∀n ∈N, tenant n sheds S(bn, p), and receives pS(bn, p) reward.
b) Discussion: The key difference in the operation of ColoEDR for mandatory EDR and voluntary EDR is in the form
of the supply function used. In particular, we allow heterogeneity in the supply function for tenants in terms of their capacity
Dn. Recall, that in the case of mandatory EDR the desired reduction capacity δ was used. This difference stems from the fact
that the reduction target is ﬂexible for voluntary demand response and creates signiﬁcant challenges – both in terms of efﬁciency,
since it allows the chance of market power to emerge because of capacity differences, and for analysis, since it adds considerable
complexity.
B. Efﬁciency Analysis of ColoEDR for Voluntary EDR
Given the adaptation of ColoEDR to the voluntary EDR setting, it is natural to ask how the efﬁciency of the mechanism
changes when the operator has ﬂexibility in the amount of response to provide to an EDR signal. Intuitively, the increased
ﬂexibility leads to the possibility of more inefﬁciency, but how large is this effect?

---

## Page 14

14
We again quantify efﬁciency through a comparison with the (socially) optimal outcome. Assuming that each tenant has a cost
ci(·) associated with energy reduction that is convex, increasing, and ci(x) = 0, ∀x ≤0 (Assumption 1). Then the allocation that
maximizes social utility (the sum of operator’s and tenants’ utility) solves the following problem
max
d,s
ud −
n
X
i=1
ci(si)
(28a)
subject to
n
X
i=1
si = d
(28b)
0 ≤si ≤Di.
(28c)
Finally, note that our analysis makes the following natural assumptions on the unit price u and the marginal cost of each
tenants. Note that they are analogous to Assumption 2 and Assumption 3.
Assumption 4. The market clearing price p is lower than the price offered by the utility for any d > 0, i.e., u ≥
Pn
i=1 bi
Pn
i=1 Di .
Assumption 5. The marginal cost of each tenants satisﬁes ∂+cn(z)
∂z

z=0 ≥γnu
2 , ∀n.
Before moving to the main results, let us ﬁrst deﬁne some notation. Let γn =
Dn
Pn
i=1 Di , we have P
n γn = 1. Here γn
behaves like “market share” of tenant n in the voluntary DR market. In the EDR case, γn = 1/N for all n. Furthermore, deﬁne
γ = maxn γn, as the “dominant share” in load reduction among the tenants, and D = maxn Dn.
C. Market Equilibrium Characterization
As in the case of mandatory EDR, we consider both the cases price-taking and and price-anticipating tenants.
1) Price-taking Tenants: Given other tenants, each price-taking tenant n optimizes the following cost over bidding value
bn,
Pn(bn, b−n) = pSn(bn, p) −cn(Sn(bn, p)) = pDn −bn −cn(Dn −bn
p )
So, in a price-taking equilibrium (b, d, p), we must have Pn(bn; b−n) ≥Pn(¯bn; b−n) hold for each tenant n over all ¯bn ≥0.
Also, the market clearing price must satisfy (24) and the total reduction must satisfy (25). Using techniques similar to the proof
of Theorem 3, we can completely characterize the the price-taking equilibrium of ColoEDR in voluntary EDR as follows:
Theorem 14. There exists a unique equilibrium of the game deﬁned by (P1, . . . , PN) for ColoEDR. For such an equilibrium,
the vector st deﬁned by st
n = S(p(bt), bt
n) is the unique optimal solution to the following optimization:
max
ud −
ud2
2 P
n Dn −
X
n
cn(sn)
(29a)
s.t.
X
n
sn = d
(29b)
d ≥0, 0 ≤sn ≤Dn,
n = 1, . . . , N,
(29c)
2) Price-anticipating Tenants: Given other tenants, each price-anticipating tenant n optimizes the following cost over
bidding value bn,
Qn(bn, b−n) = p(b)Sn(bn, p) −cn(Sn(bn, p)) = γn
√
Σmbm
v
u
u
tu
n
X
i=1
Di −bn −cn(Dn −
bn
Σmbm
rPn
i=1 Di
u
),
So, in a price-anticipating equilibrium (b, d, p), we must have Qn(bn; b−n) ≥Qn(¯bn; b−n) for all n over all ¯bn. Also, the
market clearing price must satisfy (24) and the total reduction d must satisfy (25).

---

## Page 15

15
Using techniques similar to the proof of Theorem 7, we can completely characterize the the price-anticipating equilibrium of
ColoEDR in voluntary EDR as follows.
Theorem 15. There exists a unique equilibrium of the game deﬁned by (Q1, . . . , QN) for ColoEDR. For such an equilibrium,
the vector sa deﬁned by sa
n = S(p(ba), ba
n) is the unique optimal solution to the following optimization:
max
ud −
ud2
2 P
n Dn −
X
n
ˆcn(sn)
(30a)
s.t.
X
n
sn = d
(30b)
d ≥0, 0 ≤sn ≤Dn,
n = 1, . . . , N,
(30c)
where, for sn ≥0,
ˆcn(sn) =1
2

sn γnu
2
+ cn(sn)

+ 1
2
Z sn
0
sγnu
2
−∂+cn(z)
∂z
2
+ 2∂+cn(z)
∂z
zu
ΣiDi dz,
(31)
and for sn < 0,
ˆcn(sn) = 0.
Like in the case of mandatory EDR, the above characterization can be approximated using a modiﬁed cost function when γn
is small, i.e., when there are a large number of ﬁrms and all ﬁrms have similar market shares.
Lemma 16. For 0 ≤sn ≤Dn, the modiﬁed cost in (31) can be upper and lower bounded by,
cn(sn) ≤ˆcn(sn) ≤cn(sn) + sn γnu
2 ,
Furthermore, where the left or right derivatives are deﬁned, we have
∂−cn(sn)
∂sn
≤∂−ˆcn(sn)
∂sn
≤∂+ˆcn(sn)
∂sn
≤∂+cn(sn)
∂sn
+ γnu
2 .
(32a)
D. Bounding Efﬁciency Loss
We now use the characterization results of Theorem 14 and Theorem 15 to analyze the social efﬁciency of ColoEDR in the
voluntary EDR setting for both price-taking and price-anticipating tenants.
Theorem 17. For price taking tenants, the welfare loss of ColoEDR is bounded by udt −P
n cn(st
n) ≥ud∗−P
n cn(s∗
n) −
ud∗2
2 P
n Dn . Moreover, the bound is tight.
Theorem 18. For price anticipating tenants, the welfare loss of ColoEDR is bounded by uda−P
n cn(sa
n) ≥ud∗−P
n cn(s∗
n)−
u
2

ΣnDnγn +
d∗2
ΣnDn

.
Theorem 17 highlights that the price-taking market equilibrium is efﬁcient when the optimal energy reduction d∗is small. This
is due to the proﬁt maximizing behavior of the operator: when the social optimal d∗is large, the operator has greater opportunity
to raise his proﬁt by lowering the market price.
Comparing Theorem 18 with Theorem 17, we can see that when tenants are price-anticipating, the additional welfare loss due
to the price-anticipating behavior of tenants is a function of γn, the market share of the tenants. It is easy to see the additional
loss of social utility is minimized when γn = 1/N for all n, i.e., when the reduction capacity of each tenant is equal.
Additionally, we can obtain tight bounds on the market clearing price, energy reduction quantity, and operator’s proﬁt in a
similar fashion as our analysis done for the mandatory EDR case using Theorem 14 and Theorem 15. The results are summarized
in Table II and Table III.

---

## Page 16

16
Tenants
Price Ratio
Colo Extra Proﬁt
Welfare Loss
Price-taking
[1 −
d∗
ΣnDn , 1]
[0, ud∗2/ΣnDn]
[0, ud∗2/2ΣnDn]
Price-anticipating
[1 −
d∗
ΣnDn , 1]
[0, ud∗2/ΣnDn]
[0, u(ΣnDnγn + d∗2/ΣnDn)/2]
TABLE II
PERFORMANCE GUARANTEE OF ColoEDR COMPARED TO THE SOCIAL OPTIMAL ALLOCATION.
Price Markup
Load Reduction
Operator’s cost
[0, uγ/2]
[−D/2, 0]
[0, uD]
TABLE III
PERFORMANCE GUARANTEE OF ColoEDR WHEN TENANTS ARE PRICE-ANTICIPATING COMPARED TO THEM BEING PRICE-TAKING.
E. Market Clearing Price
Proposition 19. When tenants are price-taking, the operator running ColoEDR uses more on-site generation and pays a lower
price for power reduction to its tenants than the social optimal. Speciﬁcally, dt ≤d∗and (1 −
d∗
P
n Dn )p∗≤pt ≤p∗.
By Lemma 16, we can characterize the the price markup under the supply function bidding mechanism:
Theorem 20. Let (pt, dt) be the equilibrium price and total tenant energy reduction when tenants are price-taking, and (pa, da)
be those when tenants are price-anticipating, then let γ = maxn γn, D = maxn Dn, we have, dt ≥da ≥dt −D/2 and pt ≤
pa ≤min(p∗, pt + uγ/2).
F. Operator’s proﬁt
Let Uo(p, d) = (u −p)d be the operator’s when the market clearing price is p and the total demand response from tenants
are d. From the price and vdr-quantity bounds provided in the previous sections, we can give bound on the utility of ColoEDR.
Theorem 21. Suppose that Assumptions 1, 4, 5 hold. The net utility for the colo operator of ColoEDR can be characterized by
0 = Uo(p∗, d∗) ≤Uo(pa, da) ≤Uo(pt, dt) ≤
ud∗2
ΣnDn , and furthermore, Uo(pt, dt) ≤Uo(pa, da) + uD.
Table II shows that as the optimal reduction d∗increases, there is more opportunity for the operator to proﬁtably reduce
market price and increase his own proﬁt. Table III shows further that, when tenants are price-anticipating, they will drive the
market clearing price up, provide less energy reduction and reduce the operator’s proﬁt. However, all these additional losses can
be bounded by linear functions of γ, the dominant share of the energy reduction capacity. Hence the loss due to price-anticipating
behavior of tenants are minimized D1 = D2 = · · · = DN.
VI. CASE STUDY
Our goal in this section is to investigate ColoEDR in a realistic scenario. Given the theoretical results in the prior sections,
we know that ColoEDR is efﬁcient for both the operator and tenants when the number of tenants is large, but that it may use
excessive on-site generation (in the worst case). Thus, two important issues to address in the case study are: How efﬁcient is the
pricing mechanism in small markets, i.e., when N is small? What is the impact of the pricing mechanism on on-site generation
in realistic scenarios? Additionally, the case study allows us to better understand when it is feasible to obtain load shedding from
tenants, i.e., how ﬂexible must tenants be in order to actively participate in a load shedding program?
We discuss only on mandatory EDR in this section. The results in the case of voluntary EDR are parallel.
A. Simulation Settings
We use trace-based simulations in our case study. Our simulator takes the tenants’ workload trace and a trace of mandatory
EDR signals from PJM as its inputs. It then executes ColoEDR (by emulating the bidding process and tenants’ energy reduction
for EDR), and outputs the resulting equilibrium. The settings we use for modeling the colocation data center and the tenant costs
follow.

---

## Page 17

17
0
4
8
12
16
20
24
0
0.2
0.4
0.6
Hour
Workload
 
 
MSN
Wiki
University
S
MSR
(a)
4
5
6
7
8
9
10 11 12
0
500
1000
1500
2000
2500
Hour
EDR (kWh)
(b)
Fig. 1. (a) Workload traces. (b) Energy reduction for PJM’s EDR on January 7, 2014 [32].
Colocation data center setup. We consider a colocation data center located in Ashburn, VA, which is a major data center
market served by PJM Interconnection [32]. By default, there are three participating tenants interested in EDR, though we vary
the number of participating tenants during the experiments.
Each participating tenant has 2,000 servers, and each server has an idle and peak power of 150W and 250W, respectively. The
default PUE of the colo is set to 1.5 (typical for colo), and hence, whenever a tenant reduces 1kWh energy, the corresponding
energy reduction at the colo level amounts to 1.5kWh. Thus, the maximum possible power reduction is 2.25MW (i.e., 1.5MW
IT plus 0.75 non-IT). We assume that the colo operator counts the extra energy reduction at the colo level as part of the tenants’
contributions, and rewards the tenants accordingly.
The colo has an on-site diesel generator, which has cost 0.3$/kWh estimated based on typical fuel efﬁciency [44].
For setting the energy reduction target received by the colo, we follow the EDR signals issued by PJM Interconnection
on January 7, 2014, when many states in eastern U.S. experienced an extremely cold weather and faced electricity production
shortage [32]. Fig. 1(b) shows the total energy reduction requirement by PJM, which we further normalize and scale down such
that maximum energy reduction target for our considered colo is 900kWh.
Tenant workloads characteristics. We choose three representative types of workloads for participating tenants: tenant 1 is
running delay-sensitive workloads (e.g., user-facing web service), tenant 2 is running delay-moderate workloads (e.g., enterprise’s
internal services), and tenant 3 is running delay-tolerant workload (e.g., back-end processing).
The workload traces for the three participating tenants were collected from logs of MSR [35], Wiki [36], and a public
university (anonymous for review), respectively. Fig. 1(a) illustrates a snapshot of the traces, where the workloads are normalized
with respect to each tenant’s maximum service capacity.
The illustrated results us an average utilization for each tenant of 30%, consistent with reported values from real systems [6].
Our results are not particularly sensitive to this choice.
There are various power management techniques, e.g., load migration/scheduling, that can be used for reducing tenants’ server
energy consumption. Here, as a concrete example, we consider that tenants dynamically turn on/off servers according to workloads
for energy saving subject to SLA [23]. This power-saving technique has been widely studied [13], [23] and also recently applied
in real systems (e.g., Facebook’s AutoScale [45]).
When tenants save energy for EDR by turning off some unused servers, their application performance might be affected. We
adopt a simple model based on an M/G/1/Processor-Sharing queueing model, as follows. For a tenant with M servers each with
a service rate of µ, denote the workload arrival rate by λ. When m servers are shut down, we model the total delay cost as
¯c(m) = λ · β · T · delay(m) =
βT
1
uM −
1
M−m , where u =
λ
µM denotes the normalized workload arrival (i.e., utilization without
turning off servers), T is the duration of an EDR event, and β is a cost parameter ($/time unit/job). In our simulations, we set the
cost parameter for tenant 1, tenant 2 and tenant 3 as 0.1, 0.03, 0.006, respectively, which are already higher than those considered
in the prior context of turning off servers for energy saving [23]. Note that we have experimented with a variety of other models
as well and the results do not qualitatively change.
We use a standard model for energy usage [6] and take the energy reduction s as linear in the number of servers shut down,

---

## Page 18

18
4
 
6
 
8
 
10
 
12
0
100
200
300
Social cost ($)
Hour 
(a) Social cost
4
 
6
 
8
 
10
 
12
0
500
1000
Hour 
Energy reduction (kWh)
 
 
T1
T2
T3
Diesel
(b) Energy reduction
4
 
6
 
8
 
10
 
12
0
50
100
150
200
Hour
Net utility ($)
 
 
T1
T2
T3
(c) Tenants’ net proﬁts
4
 
6
 
8
 
10
 
12
0
100
200
300
Hour
Cost ($)
 
 
Tenants
Diesel
(d) Operator’s total cost
4
 
6
 
8
 
10
 
12
0
0.1
0.2
0.3
0.4
Price ($/kWh)
Hour
 
 
Diesel price
(e) Market clearing price
4
 
6
 
8
 
10
 
12
0
50
100
Utilization (%)
Hour
 
 
Utilization bound
(f) Tenant 1’s utilization
4
 
6
 
8
 
10
 
12
0
50
100
Utilization (%)
Hour 
 
 
Utilization bound
(g) Tenant 2’s utilization
4
 
6
 
8
 
10
 
12
0
50
100
Utilization (%)
Hour
 
 
Utilization bound
(h) Tenant 3’s utilization
Fig. 2. Performance comparison under default settings. Throughout this and later plots, the bars in each cluster are the price-taking, price-anticipating, socially
optimal, and diesel only (if applicable) outcomes.
i.e., s = θ·m, where θ is a constant decided by server’s idle power and T . Then, it yields the following cost function for tenants’s
energy reduction c(s) = ¯c( s
θ ) −¯c(0), where ¯c( · ) is deﬁned in the above paragraph. Note that we have experimented with a
variety of other forms, and our results are not sensitive to the details of this cost function.
Finally, note that tenants typically have delay performance requirement which, based on the above queueing model, is translated
as an utilization upper bound. Such translation is also common in real systems (e.g., default policy for auto-scaling virtual machines
[26]). In our simulation, we capture the performance constraint by setting utilization upper bounds for tenant 1, tenant 2, and
tenant 3 as 0.5, 0.6, and 0.8, respectively.
Efﬁciency benchmarks. Throughout our experiments, we consider the price-taking, price-anticipating, and social optimal
outcomes. Additionally, we consider one other benchmark, diesel only, which is meant to capture common practice today. Under
diesel only, the full EDR response is provided by the on-site diesel generator. Throughout, our results are presented in grouped
bar plots with the bars representing (from left to right) the price-taking, price-anticipating, social optimal, and diesel only (if
applicable) outcomes.
While other mechanisms (e.g., direct pricing [24], auction [46]) have been introduced in recent papers, we do not compare
ColoEDR with them here because ColoEDR is already typically indistinguishable from the social optimal cost.
B. Performance Evaluation
We now discuss our main results, shown in Fig. 2.
Social cost. We ﬁrst compare in Fig. 2(a) the social costs incurred by different algorithms. Note that ColoEDR is close to
the social cost optimal under both price-taking and price-anticipating cases even though there are only three participating tenants.
Further, the resulting social costs in both the price-taking and price-anticipating scenarios are signiﬁcantly lower than that of the
diesel only outcome. This shows a great potential of tenants’ IT power reduction for EDR, which is consistent with the prior
literature on owner-operated data center demand response [1], [24], [43].
Energy reduction contributions. Fig. 2(b) plots EDR energy reduction contributions from tenants and the diesel generator.
As expected from analytic results, both price-taking and price-anticipating tenants tend to contribute less to EDR (compared
to the social optimal) because of their self-interested decisions. In other words, given self-interested tenants, the colo operator
needs more diesel generation than the social optimal. Nonetheless, the difference is fairly small, much smaller than predicted
by the worst-case analytic results. This highlights that worst-case results were too pessimistic in this case. Of course, one must

---

## Page 19

19
3
6
9
12
15
18
0
100
200
300
Social cost ($)
# of tenants
(a) Social cost
3
6
9
12
15
18
0
0.1
0.2
0.3
0.4
Price ($/kWh)
# of tenants
 
 
Diesel price
(b) Market price
3
6
9
12
15
18
0
50
100
150
200
250
# of tenants
Net utility ($)
 
 
T1
T2
T3
(c) Tenants’ net proﬁts
3
6
9
12
15
18
0
200
400
# of tenants
Cost ($)
 
 
Tenants
Diesel
(d) Operator’s total cost
Fig. 3. Impact of number of tenants.
remember that all tenant reduction extracted is in-place of diesel generation, and so serves to make the demand response more
environmentally friendly.
Beneﬁts for tenants and colocation operator. We show in Fig. 2(c) and Fig. 2(d) that both the tenants and the colo operator
can beneﬁt from ColoEDR. Speciﬁcally, Fig. 2(c) presents net proﬁt (i.e., payment made by colo operator minus performance
cost) received by tenants, showing that all participating tenants receive positive net rewards. While price-anticipating tenants can
receive higher net rewards than when they are price-taking, the extra reward gained is quite small. Similarly, Fig. 2(d) shows cost
saving for the colo operator, compared to the “diesel only” case .
Market clearing price. Fig. 2(e) shows the market clearing price. Naturally, when using ColoEDR to incentivize tenants for
EDR while minimizing the total cost, the colo operator will not pay the tenants at price higher than its diesel price (shown via the
red horizontal line). We also note that the price under the price-anticipating case is higher than that under the price-taking case,
because the price-anticipating tenants are more strategic. However, the price difference between price-anticipating and price-taking
cases is quite small, which again conﬁrms our analytic results.
Tenant’ server utilization. Tenants’ server utilizations are shown in Figs. 2(f), 2(g) and 2(h), respectively. These illustrate that,
while tenants reduce energy for EDR, their server utilizations still stay within their respective limits (shown via the red horizontal
lines), satisfying performance constraints. This is because tenants typically provision their servers based on the maximum possible
workloads (plus a certain margin), while in practice their workloads are usually quite low, resulting in a “slackness” that allows
for saving energy while still meeting their performance requirements.
C. Sensitivity Analysis
To complete our case study, we investigate the sensitivity of the conclusions discussed above to the settings used. For each
study, we only show results that are signiﬁcantly different than those in Fig. 2.
Impact of the number of tenants. First, we vary the number of participating tenants and show the results in Fig. 3. To make
results comparable, we ﬁx the EDR energy reduction requirement as well as total number of servers: tenant 1, tenant 2 and tenant
3 are each equally split into multiple smaller tenants, each having fewer servers. We then aggregate replicas of the same tenant
together for an easy viewing in the ﬁgures, e.g., “tenant 1” in the ﬁgures represent the whole group of tenants that are obtained
by splitting the original tenant 1. One interesting observation is that as more tenants participate in EDR, the market becomes
more “competitive”. Hence, each individual tenant can only gain less net reward, but both the price and the aggregate net reward
become higher (see Figs. 3(b) and 3(c)). Motivated by this, one might suggest a possible trick: a tenant may gain more utility by
splitting its servers and pretending as multiple tenants. In practice, however, each tenant has only one account (for billing, etc.)
which requires contracts and base fees, and thus pretending as multiple tenants is not possible in a colo.
Impact of the price of diesel. Fig. 4 illustrates how our result changes as the diesel price varies. Intuitively, as shown in
Fig. 4(a), the social cost (which includes diesel cost as a key component) increases with the diesel price. We see from Figs. 4(b)
and 4(c) that, when diesel price is very low (e.g., 0.1$/kWh), the colo operator is willing to use more diesel and offers a lower
price to tenants. As a result, tenants contribute less to EDR. As the diesel price increases (e.g., from 0.2$/kWh to 0.3$/kWh),

---

## Page 20

20
0.1 0.2 0.3 0.4 0.5 0.6
0
200
400
600
Social cost ($)
Diesel price ($/kWh)
(a) Social cost
0.1
0.2
0.3
0.4
0.5
0.6
0
500
1000
Diesel price ($/kWh)
Energy reduction (kWh)
 
 
T1
T2
T3
Diesel
(b) Energy reduction
0.1 0.2 0.3 0.4 0.5 0.6
0
0.2
0.4
0.6
Price ($/kWh)
Diesel price ($/kWh)
 
 
Diesel price
(c) Market price
0.1
0.2
0.3
0.4
0.5
0.6
0
100
200
300
400
Diesel price ($/kWh)
Net utility ($)
 
 
T1
T2
T3
(d) Tenants’ net proﬁts
Fig. 4. Impact of diesel price.
20
40
60
80 100 120
0
500
1000
1500
2000
EDR requirement (%)
Energy reduction (kWh)
 
 
T1
T2
T3
Diesel
(a) Energy reduction
20
40
60
80
100 120
0
0.1
0.2
0.3
0.4
Price ($/kWh)
EDR requirement (%)
 
 
Diesel price
(b) Market price
Fig. 5. Impact of EDR energy reduction target.
the colo operator increases the market price (but still below the diesel price) to encourage tenants to cut more energy for EDR.
Nonetheless, tenants’ energy reduction contribution cannot increase arbitrarily due to their performance constraints. Speciﬁcally,
after the diesel price exceeds 0.4$/kWh, tenants will not contribute more to EDR (i.e., almost all their IT energy reduction
capabilities have been exploited), even though the colo operator increases the reward. In this case, tenants simply receive higher
net rewards without further contributing to EDR, as shown in Fig. 4(d).
Impact of EDR requirement. Fig. 5 varies the EDR energy reduction target, with the maximum reduction ranging from
20% to 120% of the colo’s peak IT power consumption. As the EDR energy reduction target increases, tenants’ energy reduction
for EDR also increases; after a certain threshold, diesel generation becomes the main approach to EDR, while the increase in
tenant’s contribution is diminishing (even though the colo operator increases the market price), because of tenants’ performance
requirements that limit their energy reduction capabilities.
Impact of tenants’ workloads. In Fig. 6(a)-6(b), we vary the tenants’ workload intensity (measured in terms of the average
server utilization when all servers are active) from 10% to 50%, while still keeping the maximum utilization bounds to 50%,
60% and 80% as the performance requirements for the three tenants, respectively. While it is straightforward that when tenants
have more workloads, they tend to contribute less to EDR, because they need to keep more servers active to deliver a good
performance. Nonetheless, even when their average utilization without turning off servers is as high as 50% (which is quite high
in real systems, considering that the average utilization is only around 10-30% [6]), tenants can still contribute more than 20%
of EDR energy reduction under ColoEDR, showing again the potential of IT power management for EDR.
Impact of workload prediction error. In practice, tenants may not perfectly estimate their own workload arrival rates. To
cope with possible trafﬁc spikes, tenants can either keep more servers active as a backup or deliberately overestimate the workload
arrival rate by a certain overestimation factor. We choose the later approach in our simulation. Fig. 6(c)-6(d) shows the result
under workload prediction errors. We see that both the social cost and market price are fairly robust against tenants’ workload
over-predictions. For example, the social cost increases by less than 10%, even when tenants overestimate their workloads by 20%
(which is already sufﬁciently high in practice, as shown in [13]). Other results (e.g., tenants’ net reward, colo operator’s total cost)
are also only minimally affected, thereby demonstrating the robustness of ColoEDR against tenants’ workload over-predictions.

---

## Page 21

21
10
20
30
40
50
0
100
200
300
Social cost ($)
Utilization (%)
(a) Social cost
10
20
30
40
50
0
500
1000
Utilization (%)
Energy reduction (kWh)
 
 
T1
T2
T3
Diesel
(b) Energy reduction
0
5
10
15
20
0
100
200
300
Social cost ($)
Over−prediction rate (%)
(c) Social cost
0
5
10
15
20
0
0.1
0.2
0.3
0.4
Price ($/kWh)
Over−prediction rate (%)
 
 
Diesel price
(d) Market price
Fig. 6. Impact of tenants’ workloads and the workload prediction errors.
VII. RELATED WORK
Our work contributes both to the growing literature on data center demand response, and to the literature studying supply
function equilibria. We discuss each in turn below.
Recently, data center demand response has received a growing amount of attention. A variety of approaches have been
considered, such as optimizing grid operator’s pricing strategies for data centers [24] and tuning computing (e.g., server control
and scheduling) and/or non-computing knobs (e.g., cooling system) in data centers for various types of demand response programs
[1], [2], [7], [21], [40]. Field tests by LBNL also verify the practical feasibility of data center demand response using a combination
of existing power management techniques (e.g., load migration) [15]. These studies, however, have all focused on large owner-
operated data centers.
In contrast, to our best knowledge, colocation demand response has been investigated by only a few previous works. The
ﬁrst is [33], which proposes a simple mechanism, called iCODE, to incentivize tenants’ load reduction. But, iCODE is purely
based on “best effort” and does not include any energy reduction target (needed for EDR). More importantly, iCODE is designed
without considering strategic behavior by tenants, and can be compromised by price-anticipating tenants [33]. More relevant to
the current work is [46], which proposes a VCG-type auction mechanism where colocation participation in EDR programs. While
the mechanism is approximately truthful, it asks participating tenants to reveal their private cost information through complex
bidding functions. Further, the colocation operator may be forced to make arbitrarily high payments to tenants. In contrast, our
proposed solution provides a simple bidding space, protects tenants’ private valuation, and ensures that the colocation operator
does not incur a higher cost for EDR than the case tenant contributions. Thus, unlike [46], ColoEDR beneﬁts both colocation
operator and tenants, giving both parties incentives to cooperate for EDR.
Finally, it is important to note that our approach builds on, and adds to, the supply function mechanism literature. Supply
function bidding (c.f. the seminal work by [19]) is frequently used in electricity markets due to its simple bidding language
and the avoidance of the unbounded payments typical in VCG-like mechanisms. Supply function bidding mechanisms have been
extensively studied, e.g., [3], [5], [10], [16], [17], [38]. The literature primarily focuses on existence and computation of supply
function equilibrium, sometimes additionally proving bounds on efﬁciency loss. Our work is most related to [18], which considers
an inelastic demand δ that must be satisﬁed via extracting load shedding from consumers and proves efﬁcient bounds on supply
function equilibrium. In contrast, our work assumes that the operator has an outside option (diesel) that can be used to satisfy the
inelastic demand. This leads to a multistage game between the tenants and the proﬁt-maximizing operator, a dynamic which has
not been studied previously in the supply function literature.
VIII. CONCLUSION
In this paper, we focused on “greening” colocation demand response by designing a pricing mechanism that can extract load
reductions from tenants during EDR events. Our mechanism, ColoEDR, can be used in both mandatory and voluntary EDR
programs and is easy put in place given systems available in colos today. The main technical contribution of the work is the

---

## Page 22

22
analysis of the ColoEDR mechanism, which is a supply function mechanism for an elastic setting, a setting for which efﬁciency
results have not previously been attained in the supply function literature. Our results highlight that ColoEDR provides provably
near-optimal efﬁciency guarantees, both when tenants are price-taking and when they are price-anticipating. We also evaluate
ColoEDR using trace-based simulation studies and validate that ColoEDR is both beneﬁcial to the colo operator (by reducing
costs), to the environment (by reducing diesel usage), and to the tenants (by providing payments for reductions).
IX. REFERENCES
[1] D. Aikema, R. Simmonds, and H. Zareipour. Data centres in the ancillary services market. In IGCC, 2012.
[2] B. Aksanli and T. S. Rosing. Providing regulation services and managing data center peak power budgets. In DATE, 2014.
[3] E. J. Anderson and X. Hu. Finding supply function equilibria with asymmetric ﬁrms. Oper. Res., 56(3):697–711, 2008.
[4] L. L. Andrew, M. Lin, and A. Wierman. Optimality, fairness, and robustness in speed scaling designs. In ACM SIGMETRICS Performance Evaluation Review,
volume 38, pages 37–48. ACM, 2010.
[5] R. Baldick, R. Grant, and E. Kahn. Theory and application of linear supply function equilibrium in electricity markets. Journal of Regulatory Economics,
25(2):143–167, 2004.
[6] L. A. Barroso, J. Clidaras, and U. Hoelzle. The Datacenter as a Computer: An Introduction to the Design of Warehouse-Scale Machines. Morgan & Claypool,
2013.
[7] H. Chen, A. K. Coskun, and M. C. Caramanis. Real-time power control of data centers for providing regulation service. In CDC, 2013.
[8] Data Center Knowledge. Inside SuperNAP 8: Switch’s Tier IV data fortress. Feb. 11, 2014,
http://www.datacenterknowledge.com/archives/2014/02/11/inside-supernap-8-switchs-tier-iv-data-fortress/.
[9] DatacenterMap. Colocation USA, http://www.datacentermap.com/usa/.
[10] C. J. Day, B. F. Hobbs, and J.-S. Pang. Oligopolistic competition in power networks: a conjectured supply function approach. Power Systems, IEEE
Transactions on, 17(3):597–607, 2002.
[11] EnerNOC. Ensuring U.S. grid security and reliability: U.S. EPA’s proposed emergency backup generator rule, 2013,
http://www.whitehouse.gov/sites/default/ﬁles/omb/assets/oira 2060/2060 12102012-2.pdf.
[12] X. Fan, W.-D. Weber, and L. A. Barroso. Power provisioning for a warehouse-sized computer. In ACM SIGARCH Computer Architecture News, volume 35,
pages 13–23. ACM, 2007.
[13] A. Gandhi, M. Harchol-Balter, R. Raghunathan, and M. A. Kozuch. Autoscale: Dynamic, robust capacity management for multi-tier data centers. ACM Trans.
Comput. Syst., 30(4):14:1–14:26, Nov. 2012.
[14] M. Ghamkhari and H. Mohsenian-Rad. Data centers to offer ancillary services. In SmartGridCom, 2012.
[15] G. Ghatikar, V. Ganti, N. E. Matson, and M. A. Piette. Demand response opportunities and enabling technologies for data centers: Findings from ﬁeld studies,
2012.
[16] R. Green. Increasing competition in the british electricity spot market. J. of Industrial Economics, pages 205–216, 1996.
[17] R. J. Green and D. M. Newbery. Competition in the british electricity spot market. J. of Political Economy, pages 929–953, 1992.
[18] R. Johari and J. N. Tsitsiklis. Parameterized supply function bidding: Equilibrium and efﬁciency. Operations research, 59(5):1079–1089, 2011.
[19] P. D. Klemperer and M. A. Meyer. Supply function equilibria in oligopoly under uncertainty. Econometrica: Journal of the Econometric Society, pages
1243–1277, 1989.
[20] S. Li, M. Brocanelli, W. Zhang, and X. Wang. Data center power control for frequency regulation. In PES, 2013.
[21] Y. Li, D. Chiu, C. Liu, L. T. Phan, T. Gill, S. Aggarwal, Z. Zhang, B. T. Loo, D. Maier, and B. McManus. Towards dynamic pricing-based collaborative
optimizations for green data centers. In ICDEW, 2013.
[22] H. Lim, A. Kansal, and J. Liu. Power budgeting for virtualized data centers. In USENIX ATC, 2011.
[23] M. Lin, A. Wierman, L. L. H. Andrew, and E. Thereska. Dynamic right-sizing for power-proportional data centers. In IEEE Infocom, 2011.
[24] Z. Liu, I. Liu, S. Low, and A. Wierman. Pricing data center demand response. In SIGMETRICS, 2014.
[25] K. Managan. Demand repsonse: A market overview, 2014, http://enaxisconsulting.com.
[26] Microsoft Azure. How to use the autoscaling application block,
http://azure.microsoft.com/en-us/documentation/articles/cloud-services-dotnet-autoscaling-application-block/.
[27] A. Misra. Responding before electric emergencies, http://www.afcom.com/digital-library/pub-type/communique/responding-before-electric-emergencies/.
[28] A.-H. Mohsenian-Rad and A. Leon-Garcia. Optimal residential load control with price prediction in real-time electricity pricing environments. Smart Grid,
IEEE Transactions on, 1(2):120–133, 2010.
[29] NRDC. Scaling up energy efﬁciency across the data center industry: Evaluating key drivers and barriers. Issue Paper, Aug. 2014.

---

## Page 23

23
[30] S. Ong, P. Denholm, and E. Doris. The impacts of commercial electric utility rate structure elements on the economics of photovoltaic systems. National
Renewable Energy Laboratory, 2010.
[31] PJM. Emergency demand response (load management) performance report – 2012/2013. Dec. 2012.
[32] PJM RTO. http://www.pjm.com/.
[33] S. Ren and M. A. Islam. Colocation demand response: Why do I turn off my servers? In ICAC, 2014.
[34] Santa Babara County. Air Pollution Control District, http://www.ourair.org/do-you-really-need-a-diesel-generator/.
[35] E. Thereska, A. Donnelly, and D. Narayanan. Sierra: a power-proportional, distributed storage system. Tech. Rep. MSR-TR-2009-153, 2009.
[36] G. Urdaneta, G. Pierre, and M. Van Steen. Wikipedia workload analysis for decentralized hosting. Computer Networks, 2009.
[37] J. Verge. Symantec Signs Multi-Megawatt Lease at Santa Clara Data Center, 2015, http://www.datacenterknowledge.com/.
[38] X. Vives. Strategic supply function competition with private information. Econometrica, 79(6):1919–1966, 2011.
[39] D. Wang, S. Govindan, A. Sivasubramaniam, A. Kansal, J. Liu, and B. Khessib. Underprovisioning backup power infrastructure for datacenters. In ASPLOS,
2014.
[40] H. Wang, J. Huang, X. Lin, and H. Mohsenian-Rad. Exploring smart grid and data center interactions for electric power load balancing. SIGMETRICS
Perform. Eval. Rev., 41(3):89–94, Jan. 2014.
[41] R. Wang, N. Kandasamy, and C. Nwankpa. Data centers as demand response resources in the electricity market: Some preliminary results. In
FeedbackComputing, 2012.
[42] A. Wierman, L. L. Andrew, and A. Tang. Power-aware speed scaling in processor sharing systems. In INFOCOM 2009, IEEE, pages 2007–2015. IEEE, 2009.
[43] A. Wierman, Z. Liu, I. Liu, and H. Mohsenian-Rad. Opportunities and challenges for data center demand response. In IGCC, 2014.
[44] Wikipedia, http://en.wikipedia.org/wiki/Diesel generator.
[45] Q. Wu. Making facebook’s software infrastructure more energy efﬁcient with autoscale, 2014.
[46] L. Zhang, S. Ren, C. Wu, and Z. Li. A truthful incentive mechanism for emergency demand response in colocation data centers. In INFOCOM, 2015.

---

## Page 24

24
APPENDIX
A. Proof of Proposition 1
When tenants are price takers, they maximize the payout Pn(bn, p) = pSn(bn, p) −cn(sn) over the bid bn. Note that
bn ∈[0, pδ] as no tenant will bid beyond pδ otherwise the payout Pn < 0. Hence b = (b1, . . . , bn) is an equilibrium if and only
if the following condition is satisﬁed
∂−cn(sn)
∂sn
≤p,
0 ≤bn < pδ,
(A.33a)
∂+cn(sn)
∂sn
≥p,
0 < bn ≤pδ.
(A.33b)
At least one feasible solution to (9) exists because it is minimizing a continuous function over a compact set. Furthermore, (9b)
- (9c) satisfy standard constraint qualiﬁcation, hence for the Lagrangian
L(s, µ) =
X
n
cn(sn) + µ((δ −y) −
X
n
sn),
there exists optimal primal dual pair (s, µ), such that (9b) and (9c) are satisﬁed, and
∂−cn(sn)
∂sn
≤µ,
sn > 0,
(A.34a)
∂+cn(sn)
∂sn
≥µ,
sn ≥0.
(A.34b)
Given the optimal (s, µ), let p = µ, and bn = p(δ −sn), then (9b) implies p satisﬁes (2), and (A.34a)-(A.34b) implies (A.33a)
- (A.33b), hence an equilibrium exists.
Conversely, if (b, p) is an equilibrium and p satisﬁes (2), the resulting allocation s is optimal to (9). To see this, if 0 ≤sn <
δ −y for all n, (A.33a)-(A.33b) is equivalent to (A.34a)-(A.34b) if we set µ = p, hence (s, µ) is primal dual optimal pair for
(9). If sn = (δ −y), then sm = 0, ∀m̸ = n. In this case, we set ¯µ = min{p, ∂+cn(sn)/∂sn}, and we can check that (s, ¯µ) is
the primal dual optimal solution for (9).
B. Proof of Theorem 3
By Proposition 1, when tenants are price-taking, for any y, the there is always an equilibrium, and the resulting s is always
the optimal allocation to provide (δ −y) energy reduction.
Hence we only need to verify that the on-site generation level y is the solution to (14a)-(14c). Similar to the proof of Proposition
1, by Assumption 2, the ﬁrst order optimality condition for the y in (14a)-(14c) is
α
Nδ (y + (N −1)δ) = p. By Proposition 1,
p satisﬁes the relation (2), substitute the left-hand-side into (2) and solve for y, we have y =
q
ΣnbnNδ
α
−(N −1)δ. This is
exactly the on-site generation y that minimizes costo(b, y) given in (12). Hence the datacenter will always pick y that is optimal
for (14a)-(14c), together with Proposition 1, an equilibrium exists, and the resulting allocation (s, y) is optimal for (14a)-(14c).
C. Proof of Proposition 4
Since y ≥0, it sufﬁces to prove that whenever the optimal on-site generation is non-zero, y∗> 0, yt ≥y∗. From (4), the
Lagrangian of SCM is
L(s, y, µ∗, λ∗) =
X
n
cn(sn) + αy + µ∗((δ −y) −
X
n
sn) −λ∗y.
By constraint qualiﬁcation and the KKT conditions, assuming y∗> 0, then λ = 0, µ∗= α, hence the market clearing price in
the optimal allocation should be p∗= α.

---

## Page 25

25
Next, consider the market price for price taking tenants. From (13),
pt =
P
i∈N bt
i
(N −1)δ + yt =
r
(Σi∈N bt
i)α
Nδ
.
(A.35)
The second equality yields P
i∈N bt
i = ((N−1)δ+yt)2
Nδ
α. Substitute this back to (A.35),
pt =
P
i∈N bt
i
(N −1)δ + yt = (N −1)δ + yt
Nδ
α.
(A.36)
And note that yt ∈[0, δ] and p∗= α, thus (A.36) yields N−1
N p∗≤pt ≤p∗.
Finally, from (14), the Lagrangian of the price-taking characterization optimization is,
L(s, y, µt, λt) =
X
n
cn(sn) +
α
2Nδ (y + (N −1)δ)2 + µt((δ −y) −
X
n
sn) −λty.
By examining the KKT condition and using a similar argument to the proof of Proposition 1, we have pt = µt, also,
∂−cn(st
n)
∂stn
≤
pt ≤p∗≤
∂+cn(s∗
n)
∂s∗n
. Thus, ∀n, st
n ≤s∗
n. Since y = δ −P sn, yt ≥y∗.
D. Proof of Proposition 2
From the proof of Proposition 4, we see that when y∗> 0, λ∗= 0, and µ∗= α. Furthermore, we have P
n sn < δ, but
sn = δ −bn
µ∗. Hence (Nδ −Σnbn
α
) < δ. Conversely, if (10) holds, then α(N −1)δ < P
n bn. But by Proposition 1 and (2), we
have P
n bn = (p∗(N −1)δ + y). By combining the two equations above: α(N −1)δ < p∗((N −1)δ + y∗). However, from the
proof in Proposition 1, we have p∗≤α, hence we must have y∗> 0.
On the other hand, when the data center operator is proﬁt maximizing, the cost to the operator costo(b, y) = (Σnbn)(δ−y)
(N−1)δ+y +αy
is a convex function in y over the domain y ≥0. By ﬁrst order condition, the cost is minimized when
y′ =
r
N δΣnbn
α
−(N −1)δ,
(A.37)
then y = y′ if and only if y′ ∈[0, δ]. However, Σnbn = Σnp(δ −sn) = p((N −1)δ + y) ≤α(Nδ), where the last inequality
is because y ≤δ, and p ≤α, since operator always has the option to use on-site generation to get unit cost of energy reduction
at α. Hence we always have y′ ≤δ. So, if y > 0, by (A.37), (11) must hold, conversely, if (11) holds, then by (A.37), y′ > 0,
so operator will use y = y′.
E. Proof of Theorem 5
Note that (s∗, y∗) is a feasible solution to (14). By Theorem 3, we have P
n cn(st
n)+
α
2Nδ (yt +(N −1)δ)2 ≤P
n cn(s∗
n)+
α
2Nδ (y∗+ (N −1)δ)2. Rearranging, we have
X
n
cn(st
n) + αyt −
 X
n
cn(s∗) + αy∗
!
≤
α
2Nδ (yt −y∗)
 2δ −(yt + y∗)

= α
2Nδ [−(yt −y∗)2 + 2(δ −y∗)(yt −y∗)] ≤
α
2Nδ [−(yt −y∗−(δ −y∗))2 + (δ −y∗)2]
= α
2Nδ (δ −y∗)2 ≤αδ
2N .
F. Proof of Theorem 6
From Proposition 4, we have N−1
N α ≤pt ≤p∗= α, and 0 ≤yt ≤δ, which yields
cost∗
o(p∗, y∗) −costo(pt, yt) = p∗(δ −y∗) + αy∗−
 pt(δ −yt) + αyt
= (α −pt)(δ −yt)

---

## Page 26

26
Substituting the above bounds for pt and yt gives 0 ≤cost∗
o(p∗, y∗) −costo(pt, yt) ≤αδ
N .
G. Proof of Theorem 7
The proof proceeds in a number of steps. We ﬁrst show that the payoff function Qn is a concave and continuous function
for each ﬁrm n. We then establish necessary and sufﬁcient conditions for b to be an equilibrium; these conditions look similar
to the optimality conditions (A.33a)-(A.33b) in the proof of Proposition 1, but for a “modiﬁed” cost function deﬁned according
to (21). We then show the correspondence between these conditions and the optimality conditions for the problem (20a)-(20c).
This correspondence establishes existence of an equilibrium, and uniqueness of the resulting allocation.
Step 1: If b is an equilibrium, and Assumption 2 is satisﬁed, at least one coordinate of b is positive.
By Assumption 2, 0 < α <
Σnbn
(N−1)δ , hence at least one coordinate of b must be positive.
Step 2: The function Qn(¯bn; b−n) is concave and continuous in ¯bn, for ¯bn ≥0. From (16) and by plugging p(b) into sn in
(1), we have
Qn(¯bn; b−n) =
r
(Σm̸=nbm + ¯bn)αδ
N
−¯bn −cn
 
δ −
¯bn
p
Σm̸=nbm + ¯bn
r
Nδ
α
!
.
When Σm̸=nbm + ¯bn > 0, the function ¯bn/
p
Σm̸=nbm + ¯bn is a strictly concave function of ¯bn (for ¯bn ≥0). Since cn is
assumed to be convex and nondecreasing (and hence continuous), it follows that Qn(¯bn, b−n) is concave and continuous in ¯bn,
for ¯bn ≥0.
It is easy to show that for sn to be positive, we need bn ≤bn where bn = 1
2

αδ
N +
q
αδ
N ( αδ
N + 4Σm̸=nbm)

.
Step 3:In an equilibrium, 0 ≤bn ≤bn, ∀n.
Tenant n would never bid more than ¯bn given b−n. If bn > bn, then S(p(b), bn) = δ −
bn
√
bn+Σm̸=nbm
Nδ
α < 0. so the payoff
Qn(bn; b−n) becomes negative; on the other hand, Qn(bn; b−n) = 0.
We specify the following condition when marginal cost of production is not less than the price:
∀n,
∂−cn(sn)
∂sn
≤p(b),
sn > 0.
(A.38)
This condition is satisﬁed when tenants are price-taking, in the next step, we show that (A.38) also holds in an equilibrium
outcome when tenants are price-anticipating.
Step 4: The vector b is an equilibrium if and only if (A.38) is satisﬁed, at least one component of b is positive, and for each n,
bn ∈[0, bn], and the following conditions hold:
if 0 < bn ≤bn,
1
2
∂+cn(sn)
∂sn
+ α
2N

+ 1
2
s∂+cn(sn)
∂sn
−α
2N
2
+ ∂+cn(sn)
∂sn
2snα
Nδ
≥p(b),
(A.39a)
if 0 ≤bn < bn,
1
2
∂−cn(sn)
∂sn
+ α
2N

+ 1
2
s∂−cn(sn)
∂sn
−α
2N
2
+ ∂−cn(sn)
∂sn
2snα
Nδ
≤p(b).
(A.39b)
By Step 2, Qn(bn; b−n) is concave and continuous for bn ≥0. By Step 3, bn ∈[0, bn]. bn must maximize Qn(bn; b−n) over
0 ≤bn ≤bn, and satisfy the following ﬁrst order optimality conditions:
∂+Qn(bn; b−n)
∂bn
≤0,
if 0 < bn ≤bn;
∂−Qn(bn; b−n)
∂bn
≥0,
if 0 ≤bn < bn;

---

## Page 27

27
Recalling the expression for p(b) given in (13), we have
1
2√Σmbm
r
αδ
N −1 + ∂−cn(sn)
∂sn
1
p(b)(1 −
bn
2Σmbm ) ≤0,
if 0 ≤bn < bn;
1
2
√
Σmbm
r
αδ
N −1 + ∂+cn(sn)
∂sn
1
p(b)(1 −
bn
2Σmbm ) ≥0,
if 0 < bn ≤bn.
We now note that by (13) and (1), we have :
1
√Σmbm =
1
p(b)
p α
Nδ , and
bn
√Σmbm = (δ −sn)p α
Nδ .
Substituting these two equations into the above, we have
1
2p(b)
α
N −1 + ∂−cn(sn)
∂sn
1
p(b)

1 −
1
2p(b)
α
N
δ −sn
δ

≤0.
(A.40a)
1
2p(b)
α
N −1 + ∂+cn(sn)
∂sn
1
p(b)

1 −
1
2p(b)
α
N
δ −sn
δ

≥0.
(A.40b)
To show (A.38) holds, we divide into two cases, when N ≥2, by rearranging (A.40a), we have
∂−cn(sn)
∂sn
1
p(b) ≤
2Np(b) −α
2Np(b) −α δ−sn
δ
≤1.
This is because by Assumption 2, 2Np(b) −α > 0 when N ≥2. Also, we have 2Np(b) −α δ−sn
δ
≥2Np(b) −α. Hence
(A.38) holds for N ≥2.
When N = 1, we can simplify (A.40a) further to
1
2p(b)α −1 + ∂−cn(sn)
∂sn
1
2p(b) ≤0, ⇒p(b) ≥1
2

α + ∂−cn(sn)
∂sn

≥∂−cn(sn)
∂sn
.
The last inequality is because α ≥∂−cn(sn)
∂sn
, otherwise p(b) > α, but proﬁt maximizing operator will not pay for price more
than α, contradiction. Hence (A.38) must hold for all N. After multiplying through (A.40a)-(A.40b) by p(b) and rearranging,
we have two quadratic inequalities in terms of p(b). Solving the inequalities lead to two sets of conditions of p(b) that satisfy
the ﬁrst order optimality conditions, they are:
if 0 ≤bn < bn,
1
2
∂−cn(sn)
∂sn
+ α
2N

± 1
2
s∂−cn(sn)
∂sn
−α
2N
2
+ 4∂−cn(sn)
∂sn
snα
2Nδ
≤p(b)
(A.41a)
if 0 < bn ≤bn,
1
2
∂+cn(sn)
∂sn
+ α
2N

± 1
2
s∂+cn(sn)
∂sn
−α
2N
2
+ 4∂+cn(sn)
∂sn
snα
2Nδ
≥p(b)
(A.41b)
However, only the conditions with plus sign satisﬁes (A.38), the conditions with minus sign violates (A.38) because since
∀sn > 0,
p(b) ≤
α
2N ≤∂+cn(0)
∂sn
< ∂−cn(sn)
∂sn
.
Hence we discard the conditions with minus sign and note that (A.41b)-(A.41a) corresponds to (A.39a)-(A.39b).
Conversely, suppose that b has at least one strictly positive component, that 0 ≤bn ≤bn, and that b satisﬁes (A.38) and
(A.39a)-(A.39b). Then we may simply reverse the argument: by Step 2, Qn(bn; b−n) is concave and continuous in bn ≥0, and
in this case the conditions (A.39a)-(A.39b) imply that bn maximizes Qn(bn; b−n) over 0 ≤bn ≤bn. Since we have already
shown that choosing bn > bn is never optimal for ﬁrm n, we conclude that b is an equilibrium, and it is easy to check that in
this case condition (A.38) is satisﬁed.
Step 5: If Assumption 2 holds, then the function ˆcn(sn) deﬁned in (21) is continuous, and strictly convex and strictly increasing
over sn ≥0, with ˆc(sn) = 0 for sn ≤0.
ˆcn(sn) is continuous on sn > 0 by continuity of cn and on sn < 0 by deﬁnition. We only need to show that ˆcn(0) = 0, this is

---

## Page 28

28
because when sn = 0, cn(sn) = 0, sn α
2N = 0, and integrating from 0 to sn is 0. Hence ˆcn(sn) = 0 for sn ≤0.
For sn ≥0, we simply compute the directional derivatives of ˆcn:
∂+ˆcn(sn)
∂sn
= 1
2
 α
2N + ∂+cn(sn)
∂sn

+ 1
2
s α
2N −∂+cn(sn)
∂sn
2
+ 2∂+cn(sn)
∂sn
snα
Nδ ,
∂−ˆcn(sn)
∂sn
= 1
2
 α
2N + ∂−cn(sn)
∂sn

+ 1
2
s α
2N −∂+cn(sn)
∂sn
2
+ 2∂+cn(sn)
∂sn
snα
Nδ .
Since cn is strictly increasing and convex, for 0 ≤sn < ¯sn, we will have
0 ≤∂+ˆc(sn)
∂sn
< ∂−ˆc(¯sn)
∂sn
≤∂+ˆc(¯sn)
∂sn
.
This guarantees that ˆcn is strictly increasing and strictly convex over sn ≥0.
Step 6: There exists a unique vector s ≥0, y ≥0 and at least one scalar ρ > 0 such that:
1
2
∂+cn(sn)
∂sn
+ α
2N

+ 1
2
s∂+cn(sn)
∂sn
−α
2N
2
+ ∂+cn(sn)
∂sn
2snα
Nδ
≥ρ,
if sn ≥0;
(A.42a)
1
2
∂−cn(sn)
∂sn
+ α
2N

+ 1
2
s∂+cn(sn)
∂sn
−α
2N
2
+ ∂+cn(sn)
∂sn
2snα
Nδ
≤ρ,
if sn > 0;
(A.42b)
α
Nδ (y + (N −1)δ) = ρ;
(A.42c)
X
n
sn = (δ −y).
(A.42d)
The vector s and y is then the unique optimal solution to (20a)-(20c).
By Step 5, since ˆcn is continuous and strictly over the convex, compact feasible region for each n, we know that (20a)-(20c)
have a unique optimal solution s, y. As in the proof of Proposition 1, form the Lagrangian
L(s, y; ρ) =
X
n
ˆcn(sn) +
α
2Nδ (y + (N −1)δ)2 + ρ((δ −y) −
X
n
sn).
By assumption 2, y > 0, and by the fact that ˆcn(sn) = 0 for sn ≤0, sn ≥0. there exists a Lagrange multiplier ρ such
that (s, y, ρ) satisfy the stationarity conditions which corresponds to (A.42a)-(A.42c) when we expand the deﬁnition of ˆcn(sn),
together with the constraint (A.42d). The fact that ρ > 0 follows by (A.42c) as y > 0.
Step 7: If s ≥0, y ≥0 and ρ > 0 satisfy (A.42a)-(A.42d), then the triple (b, ρ, y) deﬁned by bn = (δ −sn)ρ is an equilibrium
as deﬁned in (17) and (18).
First observe that with this deﬁnition, together with (A.42d) and the fact that sn ≥0, we have bn ≥0 for all n. Furthermore, we
can show bn ≤bn, since sn ≥0, bn ≤ρδ, but by (A.42c)-(A.42d), we have
ρ =
α
Nδ (y + (N −1)δ) =
α
Nδ (Nδ −
X
n
sn)
(A.43)
Substitute the deﬁnition sn = δ −bn
ρ into (A.43), we have
ρ =
α
Nδ
Σnbn
ρ
⇒ρ =
r
Σnbnα
Nδ
.
(A.44)
Substituting (A.44) into bn ≤ρδ, we have bn ≤
q
(Σm̸=nbm+bn)αδ
N
, Solving this inequality we have bn ≤bn.
Finally, at least one component of b is strictly positive, since otherwise we have sn1 = sn2 = δ for some n1̸ = n2, in which
case Σnsn > δ, which contradicts (A.42d). (or sn = δ, y = 0, contradicting our assumption that y > 0.)
By Step 4, to check that b is an equilibrium, we must only check the stationarity conditions (A.39a)-(A.39b). We simply note

---

## Page 29

29
that under the identiﬁcation bn = ρ(δ −sn), using (A.44) and (A.42c), we have
y =
r
ΣnbnNδ
α
−(N −1)δ;
ρ =
Σnbn
(N −1)δ + y = p(b).
Substitute p(b) into (A.42a) will correspond to (A.39a), and (A.42b) implies (A.39b) and (A.38) because ∂−cn(sn)
∂sn
≤∂+cn(sn)
∂sn
.
Thus (b, ρ, y) is an equilibrium.
Step 8: If (b, p(b), y) is an equilibrium, then there exists a scalar ρ ≥0 such that the vector b deﬁned by sn = S(p(b), bn)
satisﬁes (A.42a)-(A.42d).
We simply reverse the argument of Step 7. Since b is an equilibrium bids, by (18) and sn = S(p(b), bn), we have P
n sn = (δ−y),
i.e., (A.42d) is satisﬁed. By Step 4, b satisﬁes (A.39a)-(A.39b). Since y > 0 by Assumption 2, 0 ≤sn < δ for all n, let
ρ = max
n
p(b),1
2
∂−cn(sn)
∂sn
+ α
2N

+ 1
2
r
(∂+cn(sn)
∂sn
−α
2N )2 + ∂+cn(sn)
∂sn
2snα
Nδ
o
.
In this case ρ > 0 and 0 ≤bn ≤bn for all n, so (A.39b) implies (A.42b) by deﬁnition of ρ, and (A.42a) holds by (A.39a) and
the fact that ∂−cn(sn) ≤∂+cn(sn) (by convexity).
Step 9: There exists an equilibrium b, and for any equilibrium that price is greater than marginal cost, the vector s deﬁned by
sn = S(p(b), bn) is the unique optimal solution of (A.42a)-(A.42d).
The conclusion is now straightforward. Existence follows from Steps 6 and 7. Uniqueness of the resulting production vector s,
and the fact that s is an optimal solution to (20a)-(20c), follows by Steps 6 and 8.
H. Proof of Lemma 8
We exploit the structure of the modiﬁed cost ˆcn to prove the result. Note that, for all n, sn ≥0, if we deﬁne Gn(sn) =
R sn
0
q
( ∂+cn(z)
∂z
−
α
2N )2 + ∂+cn(z)
∂z
2zα
Nδ dz, then
Gn(sn) ≥
Z sn
0
s∂+cn(z)
∂z
−α
2N
2
dz = cn(sn) −sn α
2N .
First inequality is because z ≥0, last equality is because by convexity and Assumption 3, we have ∂+cn(z)
∂z
≥∂+cn(0)
∂sn
≥
α
2N .
Hence we have ˆcn(sn) = 1
2
 cn(sn) + sn α
2N

+ 1
2Gn(sn) ≥cn(sn).
On the other hand, notice that sn ≤δ, we have:
Gn(sn) ≤
Z sn
0
s∂+cn(z)
∂z
−α
2N
2
+ ∂+cn(z)
∂z
2δα
Nδ dz
=
Z sn
0
s∂+cn(z)
∂z
+ α
2N
2
dz = cn(sn) + sn α
2N .
Hence we have ˆcn(sn) = 1
2
 cn(sn) + sn α
2N

+ 1
2Gn(sn) ≤cn(sn) + sn α
2N . The bounds for the left and right derivatives can
be obtained from taking the left (or right) derivatives at the bounds of Gn(sn).
I. Proof of Theorem 9
Firstly we will prove one side of the inequality pt ≤pa, yt ≤ya. Recall that by the examinging the Lagrangians of the
optimizations in Proposition 4 in and Theorem 7, we have pt ≥∂−cn(st
n)/∂sn, pt ≤∂+cn(st
n)/∂sn, pa ≥∂−ˆcn(sa
n)/∂sn, pa ≤
∂+ˆcn(sa
n)/∂sn, at the domain where the left or right derivative is deﬁned, and pt =
α
Nδ (yt+(N −1)δ), pa =
α
Nδ (ya+(N −1)δ).
If yt > ya, then pt > pa. Also, because the total energy reduction δ is constant, we have P
n st
n < P
n sa
n.

---

## Page 30

30
Hence there exist sr > 0 such that sa
r > st
r for some r ∈{1, . . . , N}. Therefore, by strict convexity of cn (Assumption 1):
pt ≤∂+cr(st
r)
∂sr
< ∂−cr(sa
r)
∂sr
.
(A.45)
However, by Lemma 8 we have ∂−ˆcr(sr)
∂sr
≥∂−cr(sr)
∂sr
. Hence, we have
pa ≥∂−ˆcr(sa
r)
∂sr
≥∂−cr(sa
r)
∂sr
.
(A.46)
Combining (A.45) and (A.46), we have pt < pa, contradiction. Hence we have yt ≤ya, and pt ≤pa.
Next we show the other side of the inequality pa ≤pt +
α
2N , ya ≤yt + δ
2, by the previous part, we have P
n sa
n ≤P
n st
n.
Let n = arg maxm(st
m −sa
m), clearly st
n ≥sa
n, otherwise P
n st
n < P
n sa
n, contradiction.
If st
n = sa
n, then ∀m, st
m = sa
m, and yt = ya, then pt = pa.
If st
n > sa
n, then by strict convexity of cn (assumption 1), and the fact that sa
n ≥0, st
n > 0, we have
∂+ˆcn(sa
n)
sn
< ∂−cn(st
n)
sn
≤pa.
(A.47)
Also, by Lemma 8, we have ∂+ˆcn(sn)
∂sn
≤∂+cn(sn)
∂sn
+
α
2N , this gives us
pa ≤∂+ˆcn(sa
n)
∂sn
≤∂+cn(sa
n)
∂sn
+ α
2N .
(A.48)
Combining (A.58) and (A.59), we have pa < pt +
α
2N . Hence we have
α
Nδ (ya + (N −1)δ) < α
Nδ (yt + (N −1)δ) + α
2N , ⇒ya < yt + δ
2.
J. Proof of Theorem 13
Given any ε > 0, let ε′ = 1
2ε. Consider the following set of cost function:
c1(s1) =













α
2N s1,
if s1 < ε′;
α(1 −
3ε′
2Nδ )s1 + C1,
ε′ ≤s1 ≤δ −ε′;
2αs1 + C2,
s1 > δ −ε′
where C1, C2 are constants that make c1 continuous6, then c1 is piece-wise linear and convex. Also, ∀m̸ = 1, cm(sm) = 2αsm.
It is easy to see that s∗
1 = δ −ε′ and y∗= ε′ is the optimal allocation.
Let sa
1 = ε′, ya = δ −ε′, and ∀m̸ = 1, sa
m = 0, we claim that (sa, ya) is the unique optimal solution to (20a)-(20c). To see
this, let ρ = α(1 −ε/(Nδ)), then,
α
Nδ (ya + (N −1)δ) = ρ;
X
n
sa
n = δ −ya;
(A.49a)
∂−ˆc1(sa
1)
∂s1
≤ρ;
∂+ˆc1(sa
1)
∂s1
≥ρ;
∂+ˆcm(0)
∂sm
≥ρ,
∀m̸ = 1.
(A.49b)
where the second inequality is because if we let Hn be the term under square root for ∂+ˆcn(sn)
∂sn
, then
Hn =
s∂+cn(sn)
∂sn
−( α
2N −α
N
sn
δ )
2
+ ( α2
N 2
(δ + sn)(δ −sn)
δ2
)
≥∂+cn(sn)
∂sn
−( α
2N −α
N
sn
δ ).
6C1 = −αε′( (2N−1)δ−3ε′
2Nδ
), and C2 = −α
Nδ (Nδ2 + δε′ −3ε′)

---

## Page 31

31
Note that ∂+ˆcn(sn)
∂sn
= 1
2( ∂+cn(sn)
∂sn
+
α
2N )+ 1
2Hn. Hence we have
∂+ˆc1(sa
1 )
∂s1
≥
∂+c1(sa
1 )
∂s1
+ αs1
2Nδ = ρ. These conditions correspond
to (A.42a)-(A.42d), so we conclude that (sa, ya) is the unique optimal solution to (20a)-(20c). Hence ya −y∗= δ −2ε′ = δ −ε.
K. Proof of Theorem 11
As (s∗, y∗) is a feasible solution to (20), by Theorem 7, we have
X
n
ˆcn(sa
n) +
α
2Nδ (ya + (N −1)δ)2 ≤
X
n
ˆcn(s∗
n) +
α
2Nδ (y∗+ (N −1)δ)2.
(A.50)
Rearranging, we have P
n ˆcn(sa
n) + αya −
 P
n ˆcn(s∗
n) + αy∗
≤
α
N

(ya −y∗)(1 −ya+y∗
2δ
)

. By Corollary 10 and the fact
that y∗≤δ, ya ≤δ, both terms in the brackets are positive, hence right-hand-side expression is maximized when y∗→0+ and
ya = δ, hence
 X
n
ˆcn(sa
n) + αya
!
−
 X
n
ˆcn(s∗
n) + αy∗
!
≤αδ
2N .
(A.51)
However, by Lemma 8, we have P
n ˆcn(s∗
n) ≤P
n cn(s∗
n) +
α
2N (P
n sn) ≤P
n cn(s∗
n) + αδ
2N ; and P
n ˆcn(sa
n) ≥P
n cn(sa
n).
Substituting the above relations into (A.51) and rearranging, we have the desired result.
L. Proof of Theorem 12
First, we compare the cost by operator between the price-taking and price anticipating cases, by deﬁnition (15) and rearranging,
we have costo(pa, ya) −costo(pt, yt) = (pa −pt)
 δ −yt
+ (α −pa) (ya −yt). By the fact that pa =
α
Nδ (ya + (N −1)δ)
(shown in Theorem 9) and the fact that 0 ≤ya ≤δ, we have
α
N −1
N

≤pa ≤α.
(A.52)
By the upper bound of pa in (A.52) and the upper bounds of pt, yt in Theorem 9, we have
costo(pa, ya) −costo(pt, yt) ≥0.
(A.53)
Similarly, using the lower bound of pa in (A.52) and the upper bounds of pa, ya in Theorem 9, we have
costo(pa, ya) −costo(pt, yt) ≤
 α
2N

· (δ) +

α · 1
N
 δ
2

= αδ
N .
Second, we compare the cost by the operator to the social optimal. Since the energy reduction goal δ is the same, by Proposition
4 and Corollary 10, we have pt ≤p∗and pa ≤p∗. Hence we have costo(pt, yt) ≤costo(pa, ya) ≤costo(p∗, y∗). Furthermore,
costo(p∗, y∗) −costo(pt, yt) = αδ −(pt(δ −yt) + αyt)
=(α −pt)(δ −yt) = α
δ −yt
Nδ

(δ −yt) ≤αδ
N .
(A.54)
Lastly by (A.53) and (A.54), we have cost(p∗, y∗) −cost(pa, ya) ≤cost(p∗, y∗) −cost(pt, yt) ≤αδ
N .
M. Proof Sketch of Theorem 14
Theo proof is similar to that of Theorem 3, which uses Proposition 1, note that in the VDR case, we can change Nδ in the
proof of Theorem 3 to ΣnDn, and interpret the variable y as ΣnDn −d, α as u and γn as 1/N in the proof of Theorem 3.

---

## Page 32

32
N. Proof Sketch of Theorem 15
Theo proof is similar to that of Theorem 7. note that in the VDR case, we can change Nδ in the proof of Theorem 3 to
ΣnDn, and interpret the variable y as ΣnDn −d, α as u and γn as 1/N in the proof of Theorem 7.
O. Proof of Lemma 16
For the bound on the magnitude of the modiﬁed cost, we exploit the structure of the modiﬁed cost ˆcn to prove the result.
Note that, for all n, sn ≥0, if we deﬁne Gn(sn) =
R sn
0
r
∂+cn(z)
∂z
−γnu
2
2
+ 2 ∂+cn(z)
∂z
zu
ΣiDi , then
Gn(sn) ≥
Z sn
0
s∂+cn(z)
∂z
−γnu
2
2
dz = cn(sn) −sn uγn
2 .
First inequality is because z ≥0, last equality is because by convexity and Assumption 5, we have ∂+cn(z)
∂z
≥∂+cn(0)
∂sn
≥uγn
2 .
Hence we have ˆcn(sn) = 1
2
 cn(sn) + sn
uγ
2

+ 1
2Gn(sn) ≥cn(sn).
On the other hand, notice that sn ≤Dn, we have:
Gn(sn) ≤
Z sn
0
s∂+cr(sn)
∂sn
−uγn
2
2
+ 2∂+cn(sn)
∂sn
γnudz = cn(sn) + sn α
2N .
Hence we have ˆcn(sn) = 1
2
 cn(sn) + sn α
2N

+ 1
2Gn(sn) ≤cn(sn) + sn
uγn
2 . The bounds for the left and right derivatives can
be obtained from taking the left (or right) derivatives at the bounds of Gn(sn).
P. Proof of Theorem 17
We can combine (26) with (27) to eliminate the
pPn
i=1 bi term to get a relation between market price and the vdr-quantity
decided by the proﬁt maximizing operator:
p =
u
Pn
i=1 Di (
n
X
i=1
Di −d)
(A.55)
By the characterization theorem, we have ud∗−
ud∗2
2 P
n Dn −P
n cn(s∗
n) ≤udt −
udt2
2 P
n Dn −P
n cn(st
n). Rearranging, we
have
ud∗−
X
n
cn(s∗
n) ≤udt −
X
n
cn(st
n) + u(d∗2 −dt2)
2 P
n Dn
≤udt −
X
n
cn(st
n) + u P
n d∗2
2 P
n Dn
where the last inequality is due to the fact that dt ≥0.
Q. Proof of Theorem 18
By Theorem 15, we have uda −uda2
2
−P
n ˆcn(sa
n) ≥uda −ud∗2
2
−P
n ˆcn(s∗
n) Using Lemma 16, and rearranging, we have
uda −
X
n
cn(sa
n)
≥ud∗−
X
n
cn(s∗
n) −u(d∗2 −da2)
2 P
n Dn
−
X
n
s∗
n
γnu
2
≥ud∗−
X
n
cn(s∗
n) −u P
n Dn
2
−
X
n
Dn γnu
2
=ud∗−
X
n
cn(s∗
n) −u
2
X
n
Dn(1 + γn).

---

## Page 33

33
where the ﬁrst inequality is because cn(sa
n) ≤ˆcn(sa
n), and ˆcn(s∗
n) ≤cn(s∗
n) + s∗
n
γnu
2 , and the second inequality is becuase
s∗
n ≤Dn.
R. Proof of Proposition 19
The Lagrangian of the welfare maximization problem (28) is
L(s, d; µ, ¯λ, λ) = ud −
n
X
i=1
ci(si) + µ(
n
X
i=1
si −d) +
n
X
i=1
λisi +
n
X
i=1
¯λi(Di −si).
By constraint qualiﬁcation, the optimal primal dual solutions (s, y; µ) satisﬁes the KKT conditions
µ∗= u,
∂−cn(sn)
∂sn
≤µ∗, if 0 < sn ≤Dn
∂+cn(sn)
∂sn
≥µ∗, if 0 ≤sn < Dn.
Hence the market clearing price in the optimal allocation should be p∗= u. Now consider the market clearing price for price
taking tenants, from (A.55), we know that pt = u −
udt
P
n Dn ≤u = p∗. Similarly, by Theorem 14 and looking at the Lagrangian
of (29), we have
∂−cn(st
n)
∂sn
≤pt for all 0 < st
n ≤Dn, hence for all n, such that st
n > 0 and s∗
n < Dn, we have
∂−cn(st
n)
∂sn
≤pt ≤p∗≤∂+cn(s∗
n)
∂sn
,
hence st
n ≤s∗
n for all such n, on the other hand, if st
n = 0 or s∗
n = Dn, we also have st
n ≤s∗
n, hence dt = P
n st
n ≤P
n s∗
n = d∗.
Finally, by the fact that dt ≤d∗and (A.55), we have
pt = u −
udt
P
n Dn ≥u −
ud∗
P
n Dn =

1 −
d∗
P
n Dn

p∗.
S. Proof of Theorem 20
Firstly we will prove one side of the inequality pt ≤pa, dt ≥da. We can prove this by contradiction. Suppose dt < da, then
by (A.55), pt > pa. Also, P
n st
n < P
n sa
n.
Hence there exist sa
r > 0 such that sa
r > st
r for some r ∈{1, . . . , N}. Therefore, by the stationarity of the Lagrangian of
(29) and strict convexity of cn (Assumption 1):
pt ≤∂+cr(st
r)
∂sr
< ∂−cr(sa
r)
∂sr
(A.56)
However, by the stationarity of the Lagrangian of (30) and Lemma 16, we have
pa ≥∂−ˆcr(sa
r)
∂sr
≥∂−cr(sa
r)
∂sr
.
(A.57)
Combining (A.45) and (A.46), we have pt < pa, contradiction. Hence we have yt ≤ya, and pt ≤pa.
Next we show the other side of the inequality pa ≤pt + uγ
2 , da ≤dt −D
2 , by the previous part, we have P
n sa
n ≤P
n st
n.
Let n = arg maxm(st
m −sa
m), clearly st
n ≥sa
n, otherwise P
n st
n < P
n sa
n, contradiction.
If st
n = sa
n, then ∀m, st
m = sa
m, and dt = da. By (A.55), pt = pa.
If st
n > sa
n, then by stationary condition of the Lagrangian of (29) and strict convexity of cn (assumption 1), and the fact
that sa
n ≥0, st
n > 0, we have
∂+cn(sa
n)
∂sn
< ∂−cn(st
n)
sn
≤pt.
(A.58)

---

## Page 34

34
Also, by Lemma 16 and stationary condition of Lagrangian of (30), we have deﬁnition of
pa ≤∂+ˆcn(sa
n)
∂sn
≤∂+ˆcn(sa
n)
∂sn
+ γnu
2 .
(A.59)
Combining (A.58) and (A.59), we have pa < pt + γnu
2
≤pt + uγ
2 . Substitute the above relation into (A.55), we have
u −
uda
P
n Dn < u −
udt
P
n Dn + uγ
2 ,
da > dt −D
2 ,
the last inequality is because D = maxn Dn = (P
n Dn)γ.
T. Proof of Theorem 21
Firstly, by theorem 20, da ≤dt, and pa ≥pt, hence Uo(pa, da) ≤Uo(pt, dt). Furthermore,
Uo(pt, dt) −Uo(pa, da) = (u −pt)dt −(u −pa)da
=(u −pt)(dt −da) + da(pa −pt).
(A.60)
By theorem 20, we have dt ≤da + D/2, pa ≤pt + uγ/2, and by the fact that da ≤P
n Dn, we have
Uo(pt, dt) −Uo(pa, da) ≤u · D
2 + (
X
n
Dn)uγ
2 = uD.
(A.61)