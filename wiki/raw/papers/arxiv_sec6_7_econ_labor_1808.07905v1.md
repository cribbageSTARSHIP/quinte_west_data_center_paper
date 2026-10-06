# Optimal Energy-Efficient Policies for Data Centers through Sensitivity-Based Optimization
**arXiv ID:** 1808.07905v1
**Source File:** arxiv_sec6_7_econ_labor_1808.07905v1.pdf

## Page 1

arXiv:1808.07905v1  [math.OC]  23 Aug 2018
Optimal Energy-Eﬃcient Policies for Data Centers through
Sensitivity-Based Optimization
Jing-Yu Ma∗, Li Xia†, Quan-Lin Li
Abstract
In this paper, we propose a novel dynamic decision method by applying the
sensitivity-based optimization theory to ﬁnd the optimal energy-eﬃcient policy of
a data center with two groups of heterogeneous servers. Servers in Group 1 always
work at high energy consumption, while servers in Group 2 may either work at high
energy consumption or sleep at low energy consumption. An energy-eﬃcient control
policy determines the switch between work and sleep states of servers in Group 2 in a
dynamic way. Since servers in Group 1 are always working with high priority to jobs,
a transfer rule is proposed to migrate the jobs in Group 2 to idle servers in Group
1. To ﬁnd the optimal energy-eﬃcient policy, we set up a policy-based Poisson equa-
tion, and provide explicit expressions for its unique solution of performance potentials
by means of the RG-factorization. Based on this, we characterize monotonicity and
optimality of the long-run average proﬁt with respect to the policies under diﬀerent
service prices. We prove that the bang-bang control is always optimal for this opti-
mization problem, i.e., we should either keep all servers sleep or turn on the servers
such that the number of working servers equals that of waiting jobs in Group 2. As an
easy adoption of policy forms, we further study the threshold-type policy and obtain
a necessary condition of the optimal threshold policy. We hope the methodology and
results derived in this paper can shed light to the study of more general energy-eﬃcient
data centers.
Keywords: Queueing; Data center; Energy-eﬃcient policies; Sensitivity-based
optimization; Markov decision process.
∗Jing-Yu Ma and Quan-Lin Li are both with the School of Economics and Management Sciences,
Yanshan University, Qinhuangdao 066004, China (e-mail: mjy0501@126.com, liquanlin@tsinghua.edu.cn).
†Li Xia is with the Center for Intelligent and Networked Systems (CFINS), Department of Automation,
TNList, Tsinghua University, Beijing 100084, China (e-mail: xial@tsinghua.edu.cn).
1

---

## Page 2

1
Introduction
Data centers have become a core part of the IT infrastructure for Internet service.
Typically, hundreds of thousands of servers are deployed in a data center to provide ubiq-
uitous computing environments. Tremendous energy consumption becomes a signiﬁcant
operation expense of data centers. In 2014, the electricity consumption of data centers in
the USA estimated 70 billion KWh, accounted for 2% of the national electricity consump-
tion [43]. The data centers in the USA are expected to consume energy 140 TWh and
spend $13 billion energy bills by 2020 [37], while these ﬁgures in Europe will reach 104
TWh and $9.6 billion [7]. The energy consumption of data centers consists of three main
parts: servers, networks and cooling, while servers are the major one. It is estimated that
servers consume around 70% of the total energy consumption in a data center with tiered
architectures [26]. On the other hand, reducing the energy consumption of servers also can
help reduce the energy consumption of networking and cooling. Therefore, energy-eﬃcient
scheduling of servers is of signiﬁcance for the energy management of data centers.
During the last two decades, considerable attention has been paid to studying the
energy eﬃciency of data centers. An early interesting observation by Barroso and H¨olzle [1]
demonstrated that a lot of data centers were designed to be able to handle the peak loads
eﬀectively, but it directly caused that a signiﬁcant number of servers (about 20%) are
often idle in the oﬀ-peak period. Although the idle servers do not provide any service,
they still consume a notable amount of energy. Therefore, it is necessary to design an
energy-eﬃcient mechanism for eﬀectively saving energy of idle servers. Previous studies
demonstrate that a potential power cutting could be as remarkable as 40% [4]. For this
purpose, a key technique, called an energy-eﬃcient state ‘sleep’ or ‘oﬀ’, was introduced to
save energy for idle servers. See Gandhi et al. [14] and Kuehn and Mashaly [28] for more
interpretations.
In this case, some queueing models either with server energy-eﬃcient
states (e.g., work, idle, sleep, and oﬀ) or with server control policies (e.g., vacation, setup,
and N-policy) were developed in the study of energy-eﬃcient data centers.
Queueing
theory and Markov (reward or decision) processes become two useful mathematical tools
in analyzing energy-eﬃcient data centers. See Gandhi [9] and Li et al. [31] for more details.
Few available studies have applied queueing theory and Markov processes to perfor-
mance analysis and optimization of energy-eﬃcient data centers. Important examples in
the recent literature are remarked as follows. Gandhi et al. [11] considered a data cen-
2

---

## Page 3

ter with multiple identical servers, the states of which include work, idle, sleep and oﬀ,
and their energy consumption have a decreasing order. One crucial technique given in
Gandhi et al. [11,13] was to develop some interesting queueing models, for example, the
M/M/k queue with setup times. Since then, some multi-server queues have received at-
tention (for example, queues with server vacations, queues with either local setup times
or N-policy), and they were successfully applied to energy-eﬃcient management of data
centers. Readers may refer to recent publications for more details, among which are Maz-
zucco et al. [34], Schwartz et al. [42], Gandhi and Harchol-Balter [12], Gandhi et al. [10],
Maccio and Down [33], Phung-Duc [38], Chen et al. [6], and Li et al. [31].
In the study of energy-eﬃcient data centers, it is a key to develop eﬀective optimal
methods and dynamic control techniques in data centers. So far, there have been two
classes of optimal methods applied to the analysis of energy-eﬃcient data centers. The
ﬁrst class is regarded as ‘static optimization’ with two basic steps. Step one is to set up
performance cost (i.e., a suitable performance-energy tradeoﬀ) of a data center, where the
performance cost can be expressed by means of queueing indexes of the data center. Step
two is to optimize the performance cost with respect to some key parameters of the data
center by using, such as, linear programming, nonlinear programming, integer program-
ming, and bilevel programming. The second class is viewed as ‘dynamic optimization’ in
which Markov decision processes or stochastic network optimization are applied to energy-
eﬃcient management of data centers, e.g., see Benini et al. [2] and Yao et al. [57] for more
details.
For the static optimization, some available works have been successfully conducted ac-
cording to two key points: The ﬁrst key point is to emphasize how to construct a suitable
utility function for the performance-energy tradeoﬀ, which needs to synchronously opti-
mize several diﬀerent performance measures, for example, reducing energy consumption,
reducing system response time, and improving quality of service. The second key point is
to minimize performance cost with respect to some crucial parameters of data centers by
means of, such as linear programming and nonlinear programming. On such a research
line, Gandhi et al. [11] recalled two classes of performance-energy tradeoﬀs: (a) ERWS,
the weighted sum β1[R] + β2[E] of the mean response time [R] and the mean power cost
[E], where β1, β2 ≥0 are weighted coeﬃcients; and (b) ERP, the product [R][E] of
the mean response time and the mean power cost. For the ERP, Gandhi et al. [11] ﬁrst
described the data center as a queue to compute the two mean values [R] and [E], and
3

---

## Page 4

then provided an optimization method to minimize the ERP. Also, they further analyzed
optimality or near-optimality of several diﬀerent energy-eﬃcient policies.
In addition,
Gandhi [9] gave some extended results and a systematical summarization with respect to
minimizing the ERP. Maccio and Down [33] generalized the ERP by Gandhi [11] to a
more general performance cost function as follows.
f (β, w) =
M
X
i=1
βi ([R])wR,i ([E])wE,i ([C])wC,i ,
where [C] is the expected cycle rate, and βi, wR,i, wE,i and wC,i for 1 ≤i ≤M are nonneg-
ative weighted coeﬃcients, β = (βi : 1 ≤i ≤M) and w = (wR,i, wE,i, wC,i : 1 ≤i ≤M).
They used the queueing models to compute the three mean values [R], [E] and [C], and
then provided some discussion on the optimality of cost function f (β, w). Gebrehiwot et
al. [15] made another interesting generalization of the ERP and ERWS by Gandhi [11]
through introducing the multiple intermediate sleep states. Under more general assump-
tions with general service and setup times, they computed the two mean values [R] and
[E] by means of some queueing insensitivity, and then discussed the optimality of the ERP
and ERWS. Further, Gebrehiwot et al. [16, 17] generalized the FCFS queueing results of
the data center with multiple intermediate sleep states to the processor-sharing discipline
and the shortest remaining processing time (SRPT) discipline, respectively. Diﬀerent from
the ERP and ERWS, Mitrani [35,36] considered a data center of N identical servers whose
ﬁrst part contains m servers. The idle or work state of servers is controlled by two diﬀerent
thresholds: an up threshold U and a down threshold D. He designed a simple three-layer
queue to describe the energy-eﬃcient data center in terms of a new performance cost:
C = c1L + c2S, where L and S are the average numbers of jobs present and of energy
consumption, respectively. He provided expressions for computing the average numbers
L and S such that the performance cost C can be optimized with respect to the three
parameters m, U and D.
However, for the dynamic optimization, little work has been done on applying Markov
decision processes to set up optimal dynamic control policies for energy-eﬃcient data cen-
ters. In general, such a study is more interesting, diﬃcult and challenging due to the fact
that a complicated queueing model with synchronously multiple control objectives (e.g.,
reducing energy consumption, reducing system response time and guaranteeing quality of
service) needs to be synthetically established in a Markov decision process. For a data
center with multiple identical servers, Kamitsos et al. [23–25] constructed a discrete-time
4

---

## Page 5

Markov decision process by uniformization and proved that the optimal sleep energy-
eﬃcient policy is simply hysteretic. Hence, this problem has a double threshold structure
by means of the optimal hysteretic policy given in Hipp and Holzbaur [19] and Lu and
Serfozo [32]. On the other hand, as some close research to energy-eﬃcient data centers,
it is worthwhile to note that the policy optimization and dynamic power management
for electronic systems or equipments were developed well by means of Markov decision
processes and stochastic network optimization. Important examples include: (a) Discrete-
time Markov decision processes by Benini et al. [2] and Yang et al. [56]; (b) Continuous-
time Markov decision processes by Qiu and Pedram [40] and Qiu et al. [41]; (c) Stochastic
network optimization by Yao et al. [57] and Huang and Neely [20]; (d) It has become in-
creasingly important to simplify the method of Markov decision processes such that more
complicated stochastic networks can be analyzed eﬀectively. On this research line, event-
driven techniques of Markov decision processes have received high attention for the past
one decade. Important examples include the event-driven power management by ˇSimuni´c
et al. [44], and the event-driven optimization techniques by Becker et al. [3], Cao [5],
Koole [27], Engel and Etzion [8], and Xia et al. [52].
The purpose of this paper is to apply the Markov decision processes to set up an
optimal dynamic control policy for energy-eﬃcient data centers. To do this, we ﬁrst ap-
ply the sensitivity-based optimization theory in the study of data centers.
Note that
the sensitivity-based optimization is greatly reﬁned from the Markov decision processes
through re-expressing the Poisson equation (corresponding to the Bellman optimality
equation) by means of several novel tools, for instance, performance potential and perfor-
mance diﬀerence (see Cao’s book [5]). Also, the sensitivity-based optimization theory can
be eﬀectively related to the Markov reward processes (e.g., see Li [29] and Li and Cao [30])
so that it is an eﬀective dynamic decision method for performance optimization of many
practical Markov systems. The key idea in the sensitivity-based optimization theory is a
performance diﬀerence equation that can quantify the performance diﬀerence of a Markov
system under any two diﬀerent policies. The diﬀerence equation gives a clear relation that
explains how the system performance is varying with respect to policies. See an excellent
book by Cao [5] for more details. So far, the sensitivity-based optimization theory has
been applied to performance optimization of queueing systems (or networks). Important
examples include an early invited overview by Xia and Cao [48]; the MAP/M/1 queue
by Xia et al. [50]; the closed queueing networks by Xia and Shihada [54], Xia [46] and
5

---

## Page 6

Xia and Jia [51]; and the open queueing networks by Xia [47] and Xia and Chen [49].
In addition, the sensitivity-based optimization theory was also applied to network energy
management, for example, the multi-hop wireless networks by Xia and Shihada [55] and
the tandem queues with power constraints by Xia et al. [53].
The main contributions of this paper are twofold.
The ﬁrst one is to apply the
sensitivity-based optimization theory to study the optimal energy-eﬃcient policies of data
centers for the ﬁrst time, in which we propose a job transfer rule among the server groups
such that the sleep energy-eﬃcient mechanism becomes more eﬀective. Diﬀerent from pre-
vious works in the literature for applying an ordinary Markov decision process to dynamic
control of data centers, we propose and develop an easier and more convenient dynamic
decision method: sensitivity-based optimization, in the study of energy-eﬃcient data cen-
ters. Crucially, this sensitivity-based optimization method may open a new avenue to the
optimal energy-eﬃcient policy of more complicated data centers. The second contribution
is to characterize the optimal energy-eﬃcient policy of data centers. We set up a policy-
based Poisson equation and provide explicit expression for its unique solution by means of
the RG-factorization. Based on this, we analyze the monotonicity and optimality of the
long-run average proﬁt with respect to the energy-eﬃcient policies under some restrained
service prices. We obtain the structure of optimal energy-eﬃcient policy. Speciﬁcally, we
prove that the bang-bang control is optimal for this problem, which signiﬁcantly reduces
the large search space. We also provide an eﬀective way to design and verify the threshold-
type mechanism in practice, which is of great signiﬁcance to solve the mechanism design
problem of energy-eﬃcient data centers. Therefore, the results of this paper give new
insights on understanding not only mechanism design of energy-eﬃcient data centers, but
also applying the sensitivity-based optimization to dynamic control of data centers. We
hope that the methodology and results given in this paper can shed light to the study of
more general energy-eﬃcient data centers.
The remainder of this paper is organized as follows. In Section 2, we describe the
problem of an energy-eﬃcient data center with two groups of diﬀerent servers. In Section
3, for the energy-eﬃcient data center, we ﬁrst establish a policy-based continuous-time
birth-death process with ﬁnite states. Then we deﬁne a suitable reward function with
respect to states and policies of the birth-death process. Based on this, we formulate a
dynamic optimization problem to ﬁnd the optimal energy-eﬃcient policy of the data center.
In Section 4, we set up a policy-based Poisson equation and provide explicit expression for
6

---

## Page 7

its unique solution by means of the RG-factorization. In Section 5, we deﬁne a perturbation
realization factor of the policy-based control process of the data center, and analyze how
the service price impacts on the perturbation realization factor. In Section 6, we use the
Poisson equation to derive a useful performance diﬀerence equation. Based on this, we
discuss the monotonicity and optimality of the long-run average proﬁt with respect to the
energy-eﬃcient policies, and prove the optimality of the bang-bang control. In Section 7,
we use the Poisson equation to further study a class of threshold energy-eﬃcient policies,
and obtain the necessary condition of the optimal threshold policy. Finally, we give some
discussions and conclude this paper in Section 8.
2
Problem Description
In this section, we give a problem description of the energy-eﬃcient problem in data
centers. As the large variation of working loads in data centers, it is widely adopted to
organize and operate the data center in a multiple-tier architecture such that the on/oﬀ
scheduling can be performed in diﬀerent tiers to save energy [26]. In this paper, we study
a data center with two groups of heterogeneous servers. There is no waiting room for
jobs in the data center, which can be viewed as a loss queue. The assumption of loss
queue model is reasonable for data centers and it is also widely used in telephone systems,
computer networks, cloud computing, and so on [18,21,45]. In what follows we provide a
detailed problem description for the data center.
Server groups: The data center contains two server groups: Groups 1 and 2, each of
which is also one of the interactive subsystems of the data center. Groups 1 and 2 contain
n and m servers, respectively. Hence the data center contains n+m servers. Servers in the
same group are homogeneous and in diﬀerent groups are heterogeneous. Note that Group
1 is viewed as a base-line group whose servers are always at the work state to guarantee a
necessary service capacity in the data center. Each server in Group 1 consumes an amount
of energy per unit of time. By contrast, Group 2 is regarded as a reserved group whose
servers may either work or sleep so that each of the m servers can switch its state between
work and sleep. If one server in Group 2 is at the sleep state, then it consumes a smaller
amount of energy to maintain the sleep state.
Power consumption: The power consumption rates (i.e., power consumption per
unit of time) for the two groups of servers are described as: P1,W and P2,W for the work
7

---

## Page 8

state in Groups 1 and 2, respectively; and P2,S only for the sleep state in Group 2. We
assume that 0 < P2,S < P2,W .
Arrival processes: The arrivals of jobs at the data center are a Poisson process with
arrival rate λ. Each arriving job is assigned to a server of the two groups according to the
following allocation rules:
(a) Each server in Group 1 must be fully utilized so that Group 1 provides a priority
service over Group 2. If Group 1 has some idle servers, then the arriving job immediately
enters the idle server in Group 1 and receives service there. Furthermore, if all the servers
of Group 1 are busy but Group 2 has some idle servers, then the arriving job immediately
enters an idle server in Group 2 and receives service there.
(b) No waiting room. A job can be served at an idle server or wait at a sleeping server
in Group 2. If all the servers of Groups 1 and 2 are occupied, then any arriving job must
be lost immediately. Note that each server may contain only one job, hence the total
number of jobs in the data center cannot exceed the number n + m.
(c) Opportunity cost. Once the data center contains n + m jobs, then any arriving job
has to be lost immediately due to no waiting room. This leads to an opportunity cost
with respect to the job loss.
Service processes: In Groups 1 and 2, the service times provided by each server are
independent and exponential with the service rate µ1 and µ2, respectively. We assume
that µ1 ≥µ2 as a fast condition, which makes the prior use of servers in Group 1.
Once a job enters the data center to receive or wait for service, it has to pay a holding
cost in Group 1 or Group 2. We assume a so-called cheap condition that the holding cost
in Group 1 is always cheaper than that in Group 2. The fast and cheap conditions are
intuitive to guarantee the prior use of servers in Group 1. That is, the servers in Group 1
are not only faster but also cheaper than those in Group 2.
If a job ﬁnishes its service at a server and leaves the system, then the data center can
obtain a ﬁxed service revenue from each served job. The service discipline of each server
in the data center is First Come First Serve (FCFS).
Transfer rule: Based on prior use of servers in Group 1, whenever a server in Group
1 becomes idle, an incomplete-service job (if exists) in Group 2 should be transferred to
the idle server in Group 1 to save processing time. When a job is transferred from Group
2 to Group 1, the data center needs to pay a transfer cost.
Independence: We assume that all the random variables deﬁned above in the data
8

---

## Page 9

center are independent.
Finally, the data center, together with its operational mode and mathematical nota-
tions, are simply depicted in Figure 1.
Figure 1: Energy-eﬃcient management of data centers.
Remark 1 A further interpretation for the transfer rule: When a job is being served
at a server of Group 2, it can be transferred to one idle server of Group 1 and restart
its service when an idle server in Group 1 is available. Note that each server in Group
1 is not only faster but also cheaper than that in Group 2, that is, the fast and cheap
conditions guarantee that servers in Group 1 have priority than those in Group 2. From
the memoryless property of exponential distributions, the restarting service in Group 1 is
still faster and cheaper than its original service in Group 2. Therefore, this transfer rule
eﬀectively supports energy-eﬃcient management of the data center due to the fact that the
servers of Group 1 are fully utilized while servers of Group 2 are kept in sleep state as
many as possible.
9

---

## Page 10

Remark 2 Although some authors (e.g., see Gandhi et al. [11], Mitrani [35, 36] and
Maccio and Down [33]) analyzed the energy-eﬃcient data center with two groups of servers,
where one is the base-line group and the other is the reserved or subsidiary group, all the
servers in the two groups given in their papers are assumed to be identical. From such
a point of view, it is easy to understand that those queueing models given in their works
are the same as only Group 2 of our paper. On the other hand, it is noted that for our
queueing model, Group 1 has a large inﬂuence on analysis of Group 2 due to introducing
new transfer rules. In fact, our queueing model here has been discussed in Li et al. [31]
with a more general setting.
3
Optimization Model Formulation
In this section, for the energy-eﬃcient data center, we ﬁrst establish a policy-based
continuous-time Markov process, and show that its inﬁnitesimal generator has the simple
structure of a birth-death process with ﬁnite states. Then, we deﬁne a suitable reward
function with respect to both states and policies of the birth-death process. Based on this,
we set up a dynamic optimization model to deal with the optimal energy-eﬃcient policy
of the data center.
In the data center with Group 1 of n servers and Group 2 of m servers, we need to
introduce both ‘states’ and ‘policies’ to express stochastic dynamics of this data center. Let
I (t) and J (t) be the number of jobs in Groups 1 and 2, respectively. Then, (I (t) , J (t))
is regarded as the state of the data center at time t. Let all the cases of state (I (t) , J (t))
form a state space as follows.
Ω= {(0, 0) , (1, 0) , . . . , (n, 0) , (n, 1) , . . . , (n, m)} .
Note that such a state (n −i, j) for 1 ≤i ≤n and 1 ≤j ≤m does not exist according
to the transfer rule. However, the policies are deﬁned with a little bit more complication.
Let di,j be the number of servers turned on in Group 2 at the state (I (t) , J (t)) = (i, j),
for i = 0, 1, . . . , n and j = 0, 1, . . . , m. From the problem description in Section 2, it is
easy to see that
di,j =







0,
i = 0, 1, . . . , n −1, j = 0,
0,
i = n, j = 0,
0, 1, . . . , m,
i = n, j = 1, 2, . . . , m.
(1)
10

---

## Page 11

Now, we provide an interpretation for the above expression: If I (t) = 0, 1, . . . , n −1, then
J (t) = 0 due to the transfer rule. In this case with i = 0, 1, . . . , n, di,0 is taken as zero
due to the energy-eﬃcient cause. While once I (t) = n, J (t) may be any element in the
set {0, 1, . . . , m}. In this case with i = n and j̸ = 0, dn,j may be taken as any element in
the set {0, 1, . . . , m}.
Corresponding to each case of state (I (t) , J (t)) at time t, we deﬁne a time-homogeneous
policy as
d = (d0,0, d1,0, . . . , dn,0; dn,1, dn,2, . . . , dn,m) .
It follows from (1) that
d = (0, 0, . . . , 0; dn,1, dn,2, . . . , dn,m) .
(2)
Let all the possible policies d given in (2) compose a policy space as follows.
D = {d : d = (0, 0, . . . , 0; dn,1, dn,2, . . . , dn,m) , di,j ∈{0, 1, . . . , m} , (i, j) ∈Ω} .
Let X(d)(t) = (I (t) , J (t))(d) be the system state at time t under any given policy d ∈D.
Then, {X(d)(t) : t ≥0} is a policy-based continuous-time birth-death process on the state
space Ωwhose inﬁnitesimal generator is given by
B(d) =



















−λ
λ
µ1
−(λ + µ1)
λ
...
...
...
nµ1
−(λ + nµ1)
λ
ν (dn,1)
−[λ + ν (dn,1)]
λ
...
...
...
ν (dn,m−1)
−[λ + ν (dn,m−1)]
λ
ν (dn,m)
−ν (dn,m)



















,
(3)
where ν (dn,j) = nµ1 + (dn,j ∧j) µ2 for j = 1, 2, . . . , m, and a ∧b denotes the minimal one
between two real numbers a and b. Note that dn,j ≥0, it is clear that ν (dn,j) ≥nµ1 > 0.
Thus, the birth-death process B(d) must be irreducible, aperiodic and positive recurrent
for any given policy d ∈D. In this case, we write the stationary probability vector of the
Markov process

X(d)(t) : t ≥0
	
under a policy d ∈D.
π(d) =

π(d) (0, 0) , π(d) (1, 0) , . . . , π(d) (n, 0) , π(d) (n, 1) , . . . , π(d) (n, m)

.
(4)
11

---

## Page 12

Obviously, the stationary probability vector π(d) is the unique solution to the system
of linear equations: π(d)B(d) = 0 and π(d)e = 1, where e is a column vector of ones with
proper dimension. We write
ξi,0 = λi
i!µi
1
,
i = 0, 1, . . . , n,
(5)
and
ξ(d)
n,j =
λn
n!µn
1
λj
j
Π
i=1ν (dn,i)
,
j = 1, 2, . . . , m,
(6)
b(d) =
n
X
i=0
ξi,0 +
m
X
j=1
ξ(d)
n,j.
(7)
It follows from Subsection 1.1.4 of Chapter 1 in Li [29] that
π(d) (i, 0) =
1
b(d) ξi,0,
i = 0, 1, . . . , n;
(8)
π(d) (n, j) =
1
b(d) ξ(d)
n,j,
j = 1, 2, . . . , m.
(9)
For any two vectors a = (a1, a2, . . . , aK) and b = (b1, b2, . . . , bK), we say that a ≥b if
ai ≥bi for any 1 ≤i ≤K. The following proposition provides an interesting observation
on how a policy d ∈D inﬂuences the stationary probability vector π(d).
Proposition 1 For any two given policies d1, d2 ∈D with d1 ≥d2, then
π(d1) (i, 0) ≥π(d2) (i, 0) ,
i = 0, 1, . . . , n.
Proof: For any two given policies d1, d2 ∈D with d1 ≥d2, then it follows from (5)
that
ξ(d1)
i,0
= ξ(d2)
i,0
= λi
i!µi
1
,
i = 0, 1, . . . , n.
If d1 ≥d2, then for each j = 1, 2, . . . , m, it is clear that d1
n,j ≥d2
n,j, this gives
ν
 d1
n,j

= nµ1 +
 d1
n,j ∧j

µ2 ≥nµ1 +
 d2
n,j ∧j

µ2 = ν
 d2
n,j

,
hence it follows from (6) that
ξ(d1)
n,j
=
λn
n!µn
1
λj
j
Π
i=1ν

d1
n,i
 ≤
λn
n!µn
1
λj
j
Π
i=1ν

d2
n,i
 = ξ(d2)
n,j .
12

---

## Page 13

It is easy to see from (7) that
b(d1) =
n
X
i=0
ξi,0 +
m
X
j=1
ξ(d1)
n,j
≤
n
X
i=0
ξi,0 +
m
X
j=1
ξ(d2)
n,j
= b(d2).
Thus, it follows (8) that for each i = 0, 1, . . . , n,
π(d1) (i, 0) =
1
b(d1)ξi,0 ≥
1
b(d2) ξi,0 = π(d2) (i, 0) .
This completes the proof.
The following theorem provides a useful observation that some special policies d ∈D
have no eﬀect on both the inﬁnitesimal generator B(d) and the stationary probability
vector π(d). Note that this theorem will be necessary and useful for the analysis of policy
monotonicity and optimality in our later study, for example, the proof of Theorem 3.
Theorem 1 Suppose that two policies d1, d2 ∈D satisfy the following two conditions:
For each j = 1, 2, . . . , m, (a) if d1
n,j ∈{1, 2, . . . , j −1}, then we take d2
n,j = d1
n,j; and (b) if
d1
n,j ∈{j, j + 1, . . . , m}, we take d2
n,j as any element of the set {j, j + 1, . . . , m}. We have
B(d1) = B(d2),
π(d1) = π(d2).
Proof: It is easy to see from (3) that the ﬁrst n + 1 rows of the matrix B(d1) is the
same as those of the matrix B(d2).
In what follows we compare the latter m rows of the matrix B(d1) with those of the
matrix B(d2). For the two policies d1, d2 ∈D satisfying the two conditions (a) and (b),
by using ν (dn,j) = nµ1 + (dn,j ∧j) µ2, it is clear that for j = 1, 2, . . . , m,
ν
 d1
n,j

= nµ1 + jµ2 = ν
 d2
n,j

.
Thus, it follows from (3) that B(d1) = B(d2), this also gives that π(d1) = π(d2). This
completes the proof.
Based on the problem description in Section 2, we deﬁne a suitable reward function for
the energy-eﬃcient data center. For convenience of readers, here we explain both energy
consumption cost and system operational cost with respect to some key factors of the data
center. We summarize ﬁve classes of costs in the data center as follows.
(a) Energy consumption cost. It is seen from Section 2 that P1,W and P2,W are the
energy consumption rates for the work state in Group 1 and Group 2, respectively; while
13

---

## Page 14

P2,S is the energy consumption rate for the sleep state only in Group 2. In addition, C1
is the energy consumption price.
(b) Holding cost. Each job in the data center has to pay a holding cost C(1)
2
(resp. C(2)
2 )
per unit of sojourn time in Group 1 (resp. Group 2). Moreover, we have two assumed
conditions: A fast condition µ1 ≥µ2, and a cheap condition C(1)
2
≤C(2)
2 .
(c) Transfer cost. If there are some idle servers in Group 1, then the jobs in the servers
in Group 2 must be transferred to the idle servers in Group 1 as many as possible. In this
case, such each transfer needs to pay a transfer cost C3 for each job.
(d) Opportunity cost. Once the data center has contained n+m jobs, then any arriving
job has to be lost immediately. This leads to an opportunity cost due to the job loss, hence
C4 is an opportunity cost for each lost job.
(e) Service price. If a job ﬁnishes its service at a server and leaves this system, then
the data center gains a ﬁxed service revenue (or earnings) R for each served job, that is,
R is the service price.
Based on the above cost and price deﬁnition, a reward function with respect to both
states and policies is deﬁned as a proﬁt rate (i.e. the total revenues minus the total costs
per unit of time). Therefore, the reward function at state (I (t) , J (t))(d) under policy d
is deﬁned as
f (d) (i, j) =R [iµ1 + (j ∧di,j) µ2] −[nP1,W + di,jP2,W + (m −di,j) P2,S] C1
−
h
iC(1)
2
+ jC(2)
2
i
−iµ11{j>0}C3 −λ1{i=n,j=m}C4,
(10)
where 1{·} is an indicator function whose value is 1 when the event in {·} happens, other-
wise its value is 0. Furthermore, the job transfer rate from Group 2 to Group 1 is given
by iµ11{j>0}. If 0 ≤i ≤n −1, then j = 0 and iµ11{j>0}C3 = 0. If i = n and j = 0, then
iµ11{j>0}C3 = 0. If i = n and 1 ≤j ≤m, then iµ11{j>0}C3 = nµ1C3.
For convenience of readers, it is necessary to explain the reward function from four
diﬀerent cases as follows.
Case (a): For i = 0 and j = 0,
f (0, 0) = −(nP1,W + mP2,S) C1.
(11)
Case (b): For i = 1, 2, . . . , n and j = 0,
f (i, 0) = Riµ1 −(nP1,W + mP2,S) C1 −iC(1)
2 .
(12)
14

---

## Page 15

Note that in Cases (a) and (b), there is no job in Group 2, thus each server of Group
2 is at the sleep state. However, in the following two cases (c) and (d), there are some
jobs in Group 2, hence the policy d will play a key role in opening or closing some servers
of Group 2 in order to eﬀectively save energy.
Case (c): For i = n, j = 1, 2, . . . , m −1; and dn,j = 0, 1, . . . , m,
f (d) (n, j) = R [nµ1 + (j ∧dn,j) µ2] −[nP1,W + dn,jP2,W + (m −dn,j) P2,S] C1
−
h
nC(1)
2
+ jC(2)
2
i
−nµ1C3.
(13)
To further simplify or compute (13), we need to especially deal with j ∧dn,j. To this end,
if dn,j = 1, 2, . . . , j, then j ∧dn,j = dn,j, hence we have
f (d) (n, j) = Rnµ1 + [Rµ2 −(P2,W −P2,S) C1] dn,j
−(nP1,W + mP2,S) C1 −
h
nC(1)
2
+ jC(2)
2
i
−nµ1C3;
(14)
while if dn,j = j + 1, j + 2, . . . , m, then j ∧dn,j = j, hence we have
f (d) (n, j) = R (nµ1 + jµ2) −(P2,W −P2,S) C1dn,j
−(nP1,W + mP2,S) C1 −
h
nC(1)
2
+ jC(2)
2
i
−nµ1C3.
(15)
Case (d): For i = n and j = m; and dn,m = 0, 1, . . . , m, we obtain that m ∧dn,m =
dn,m, and we have
f (d) (n, m) = R (nµ1 + dn,mµ2) −[nP1,W + dn,mP2,W + (m −dn,m) P2,S] C1
−
h
nC(1)
2
+ mC(2)
2
i
−nµ1C3 −λC4
= Rnµ1 + [Rµ2 −(P2,W −P2,S) C1] dn,m
−(nP1,W + mP2,S) C1 −
h
nC(1)
2
+ mC(2)
2
i
−nµ1C3 −λC4.
(16)
We deﬁne an (n + m + 1)-dimensional column vector composed of the elements f (i, j)
and f (d) (i, j) as
f (d) =

f (0, 0) , f (1, 0) , . . . , f (n, 0) , f (d) (n, 1) , . . . , f (d) (n, m)
T
,
(17)
where aT denotes transpose of vector or matrix a.
In the remainder of this section, the long-run average proﬁt of the data center (or
the policy-based continuous-time birth-death process

X(d)(t) : t ≥0
	
) under an energy-
15

---

## Page 16

eﬃcient policy d is deﬁned as
ηd =
lim
T→+∞E
 1
T
Z T
0
f (d) 
(I (t) , J (t))(d)
dt

=
lim
T→+∞E
 1
T
Z T
0
f (d) 
X(d)(t)

dt

= π(d)f (d),
(18)
where π(d) and f (d) are given by (4) and (17), respectively.
We observe that as the number of working servers in Group 2 decreases, the total
revenues and the total costs in the data center will decrease synchronously, vice versa.
Thus, there is a tradeoﬀbetween the total revenues and the total costs. This motivates us
to study an optimal mechanism design for the energy-eﬃcient data center. The objective
is to ﬁnd an optimal energy-eﬃcient policy d∗such that the long-run average proﬁt ηd is
maximize, that is,
d∗= arg max
d∈D
n
ηdo
.
(19)
In fact, it is diﬃcult and challenging to analyze the properties of the optimal energy-
eﬃcient policy d∗, and to provide an eﬀective algorithm for computing the optimal policy
d∗. In the next section, we will introduce the sensitivity-based optimization theory to
study this energy-eﬃcient optimization problem.
4
The Poisson Equation and Its Explicit Solution
In this section, for the energy-eﬃcient data center, we set up a Poisson equation which
is derived by means of the law of total probability focusing on some stop times. It is
worth noting that the Poisson equation provides a useful relation between the sensitivity-
based optimization and the Markov decision processes (MDPs). Also, we use the RG-
factorization, given in Li and Cao [30] or Li [29], to solve the Poisson equation and provide
the explicit expression for its unique solution.
For d ∈D, it follows from Chapter 2 in Cao [5] that for the policy-based continuous-
time Markov process

X(d)(t) : t ≥0
	
, we deﬁne the performance potential as
g(d) (i, j) = E
Z +∞
0
h
f (d) 
(I (t) , J (t))(d)
−ηdi
dt
 (I (0) , J (0))(d) = (i, j)

= E
Z +∞
0
h
f (d) 
X(d)(t)

−ηdi
dt
 X(d) (0) = (i, j)

,
(20)
16

---

## Page 17

where ηd is deﬁned in (18). It is seen from Cao [5] that for any policy d ∈D, g(d) (i, j)
quantiﬁes the contribution of the initial state (i, j) to the long-run average proﬁt of the
data center. Here g(d) (i, j) is also called the relative value function or the bias in the
traditional MDP theory, see, e.g. Puterman [39]. We further deﬁne a column vector g(d)
with elements g(d) (i, j) for (i, j) ∈Ωas
g(d) =

g(d) (0, 0) , g(d) (1, 0) , . . . , g(d) (n, 0) , g(d) (n, 1) , . . . , g(d) (n, m)
T
.
(21)
We deﬁne the ﬁrst departure time from state (i, j) as
τ = inf
n
t ≥0 : (I (t) , J (t))(d)̸ = (i, j)
o
,
where (I (0) , J (0))(d) = (i, j). Clearly, τ is a stop time of the Markov process

X(d)(t) : t ≥0
	
.
Based on this, if (i, j) = (0, 0), then it is seen from (3) that state (0, 0) is the upper bound-
ary state of the birth-death process B(d), hence (I (τ) , J (τ))(d) = (1, 0). Similarly, we get
a basic relation for the stop time τ as follows.
(I (τ) , J (τ))(d) =




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




(1, 0) ,
(i, j) = (0, 0) ,
(i −1, 0) , (i + 1, 0) ,
(i, j) = (i, 0) , i = 1, 2, . . . , n −1,
(n −1, 0) , (n, 1) ,
(i, j) = (n, 0) ,
(n, j −1) , (n, j + 1) ,
(i, j) = (n, j) , j = 1, 2, . . . , m −1,
(n, m −1) ,
(i, j) = (n, m) .
(22)
Now, we derive a Poisson equation to compute the column vector g(d) in terms of
the stop time τ and the basic relation (22). By a similar computation to that in Li and
Cao [30] or Xia et al. [50], our analysis is decomposed into ﬁve parts as follows.
17

---

## Page 18

For i = 1, 2, . . . , n −1 and j = 0, we have
g(d) (i, 0) =E
Z +∞
0
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (0) , J (0))(d) = (i, 0)

=E {τ| I (t) = i, J (t) = 0}
h
f (i, 0) −ηdi
+ E
Z +∞
τ
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (τ) , J (τ))(d)

=
1
λ + iµ1
h
f (i, 0) −ηdi
+
λ
λ + iµ1
E
Z +∞
0
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (0) , J (0))(d) = (i + 1, 0)

+
iµ1
λ + iµ1
E
Z +∞
0
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (0) , J (0))(d) = (i −1, 0)

=
1
λ + iµ1
h
f (i, 0) −ηdi
+
λ
λ + iµ1
g(d) (i + 1, 0) +
iµ1
λ + iµ1
g(d) (i −1, 0) ,
(23)
where for the birth-death process

X(d)(t) : t ≥0
	
, it is easy to see that
Z τ
0
h
f (d) 
(I (t) , J (t))(d)
−ηdi
dt = τ
h
f (i, 0) −ηdi
,
E {τ| I (t) = i, J (t) = 0} =
1
λ + iµ1
.
Thus, we obtain
iµ1g(d) (i −1, 0) −(λ + iµ1) g(d) (i, 0) + λg(d) (i + 1, 0) = ηd −f (i, 0) .
(24)
Base on (23), with a boundary consideration, for i = 0 and j = 0, we have
−λg(d) (0, 0) + λg(d) (1, 0) = ηd −f (0, 0) .
(25)
For i = n and j = 0, we have
nµ1g(d) (n −1, 0) −(λ + nµ1) g(d) (n, 0) + λg(d) (n, 1) = ηd −f (n, 0) .
(26)
18

---

## Page 19

For i = n and j = 1, 2, . . . , m −1, we have
g(d) (n, j) =E
Z +∞
0
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (0) , J (0))(d) = (n, j)

=E {τ| I (t) = n, J (t) = j}
h
f (d) (n, j) −ηdi
+ E
Z +∞
τ
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (τ) , J (τ))(d)

=
1
λ + ν (dn,j)
h
f (d) (n, j) −ηdi
+
λ
λ + ν (dn,j)E
Z +∞
0
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (0) , J (0))(d) = (n, j + 1)

+
ν (dn,j)
λ + ν (dn,j)E
Z +∞
0
h
f (d) 
X(d)(t)

−ηdi
dt
 (I (0) , J (0))(d) = (n, j −1)

=
1
λ + ν (dn,j)
h
f (d) (n, j) −ηdi
+
λ
λ + ν (dn,j)g(d) (n, j + 1)
+
ν (dn,j)
λ + ν (dn,j)g(d) (n, j −1) ,
(27)
where
E {τ| I (t) = n, J (t) = j} =
1
λ + ν (dn,j).
(28)
It follows from (27) that
ν (dn,j) g(d) (n, j −1) −[λ + ν (dn,j)] g(d) (n, j) + λg(d) (n, j + 1) = ηd −f (d) (n, j) . (29)
For i = n and j = m, with a boundary consideration, a similar analysis to (29) gives
ν (dn,m) g(d) (n, m −1) −ν (dn,m) g(d) (n, m) = ηd −f (d) (n, m) .
(30)
Note that ν (dn,m) = nµ1 + (dn,m ∧m) µ2 = nµ1 + dn,mµ2 due to the fact that dn,m ∈
{0, 1, . . . , m}.
It follows from (24), (25), (26), (29) and (30) that
B(d)g(d) = ηde −f (d)
or
−B(d)g(d) = f (d) −ηde,
(31)
where f (d) is given in (17) and B(d) is given in (3).
To solve the system of linear equations (31), we note that rank
 B(d)
= n + m and
det
 B(d)
= 0 due to that the size of the matrix B(d) is n + m + 1. Hence, this system of
19

---

## Page 20

linear equations (31) exists inﬁnitely-many solutions with a free constant of an additive
term. Let B be a matrix obtained through omitting the ﬁrst row and the ﬁrst column
vectors of the matrix B(d). Then,
B =



















−(λ + µ1)
λ
2µ1
−(λ + 2µ1)
λ
...
...
...
nµ1
−(λ + nµ1)
λ
ν (dn,1)
−[λ + ν (dn,1)]
λ
...
...
...
ν (dn,m−1)
−[λ + ν (dn,m−1)]
λ
ν (dn,m)
−ν (dn,m)



















.
Obviously, rank(B) = n + m and the size of the matrix B is n + m. Hence, the matrix B
is invertible.
Let h(d) and ϕ(d) be two column vectors of size n + m obtained through omitting the
ﬁrst element of the two column vectors f (d)−ηde and g(d) with size n+m+1, respectively.
Then,
h(d) =














f (1, 0) −ηd
...
f (n, 0) −ηd
f (d) (n, 1) −ηd
...
f (d) (n, m) −ηd














def
=














h(d)
1
...
h(d)
n
h(d)
n+1
...
h(d)
n+m














,
ϕ(d) =














g(d) (1, 0)
...
g(d) (n, 0)
g(d) (n, 1)
...
g(d) (n, m)














.
Therefore, it follows from (31) that
−Bϕ(d) = h(d) + µ1e1g(d) (0, 0) ,
(32)
where e1 is a column vector with the ﬁrst element be one and all the others be zero. Note
that the matrix −B is invertible and (−B)−1 > 0, thus, the system of linear equations
(32) always exists one unique solution
ϕ(d) = (−B)−1 h(d) + µ1 (−B)−1 e1 · ℑ,
(33)
where g(d) (0, 0) = ℑis any given constant.
For convenience of computation, we take
g(d) (0, 0) = ℑ= 1. In this case, we have
ϕ(d) = (−B)−1 h(d) + µ1 (−B)−1 e1.
(34)
20

---

## Page 21

To provide an explicit expression for the unique solution to the system of linear equa-
tions (32), it is easy to see from (34) that we need to ﬁrst establish an explicit expression
for the invertible matrix (−B)−1. While the explicit expression of the invertible matrix
(−B)−1 can be obtained by means of the RG-factorization, which is given in Li and Cao [30]
for QBD processes, and more generally, Li [29] for general Markov processes.
To express the invertible matrix (−B)−1, we write the UL-type U-measure as
Un+m = −ν (dn,m) ,
Un+m−1 = −[λ + ν (dn,m−1)] + λ (−Un+m)−1 ν (dn,m) ,
Uk = A(k)
1
+ λ (−Uk+1)−1 A(k+1)
2
,
k = n + m −2, n + m −3, . . . , 1,
and the UL-type R- and G-measures as
Rk
=
λ (−Uk+1)−1 ,
k = 1, 2, . . . , n + m −1,
Gk
=
(−Uk)−1 A(k)
2 ,
k = 2, 3, . . . , n + m,
where
A(k)
1
=



−(λ + kµ1) ,
k = 1, 2, . . . , n,
−[λ + ν (dn,k−n)] ,
k = n + 1, n + 2, . . . , n + m −1,
A(k)
2
=



kµ1,
k = 2, 3, . . . , n,
ν (dn,k−n) ,
k = n + 1, n + 2, . . . , n + m.
Thus, the UL-type RG-factorization of the birth-death process B is given by
B = (I −RU) UD (I −GL) ,
where
RU =











0
R1
0
R2
...
...
0
Rn+m−1
0











,
GL =











0
G2
0
G3
0
...
...
Gn+m
0











,
and
UD = diag (U1, U2, . . . , Un+m) .
Therefore, we obtain
(−B)−1 = (I −GL)−1 (−UD)−1 (I −RU)−1 .
21

---

## Page 22

Let
X(l)
k
= RlRl+1 · · · Rl+k−2, 1 ≤l ≤n + m −1, 2 ≤k ≤n + m,
Y (l)
k
= GlGl−1 · · · Gl−k+2, 2 ≤k ≤l ≤n + m.
Then,
(I −GL)−1 =











1
Y (2)
2
1
Y (3)
3
Y (3)
2
1
...
...
...
...
Y (n+m)
n+m
Y (n+m)
n+m−1
· · ·
Y (n+m)
2
1











,
(I −RU)−1 =











1
X(1)
2
X(1)
3
· · ·
X(1)
n+m
1
X(2)
2
· · ·
X(2)
n+m−1
1
· · ·
X(3)
n+m−2
...
...
1











,
and
(−UD)−1 = diag

(−U1)−1 , (−U2)−1 , . . . , (−Un+m)−1
.
Thus, we obtain the explicit expression
(−B)−1 =











1
Y (2)
2
1
Y (3)
3
Y (3)
2
1
...
...
...
...
Y (n+m)
n+m
Y (n+m)
n+m−1
· · ·
Y (n+m)
2
1











diag

(−U1)−1 , (−U2)−1 , . . . , (−Un+m)−1
·











1
X(1)
2
X(1)
3
· · ·
X(1)
n+m
1
X(2)
2
· · ·
X(2)
n+m−1
1
· · ·
X(3)
n+m−2
...
...
1











.
(35)
It is worthwhile to note that for the U-, R- and G-measures discussed above, each
of them depends on the policy d ∈D. For simpliﬁcation of descriptions, we omit such
superscript d in their formulae or equations.
22

---

## Page 23

Remark 3 In general, it is diﬃcult to solve the high-dimensional system of linear equa-
tions (32) for a general Markov process. However, the RG-factorization method is usually
very eﬀective for solving such problem for a level-dependent QBD process, in which the
expression of the invertible matrix (−B)−1 is similar to that in (35) with elements changed
from scalar to block matrices. In addition, it is also a key that the vector ϕ(d) can be nu-
merically computed from (33) and (35) by using the RG-factorization. See Li and Cao [30]
for more details.
The following theorem provides an explicit expression for the vector ϕ(d) under a
constraint condition g(d) (0, 0) = 1. Note that this expression is very useful for applications
of the sensitivity-based optimization theory in our later study.
Theorem 2 If g(d) (0, 0) = 1, then for k = 1,
g(d) (1, 0) = (−U1)−1

h(d)
1
+
m+n
X
j=2
X(1)
j h(d)
j

+ G1;
For 2 ≤k ≤n,
g(d) (k, 0) = (−Uk)−1

h(d)
k
+
m+n−k+1
X
j=2
X(k)
j
h(d)
j+k−1


+
k−1
X
i=1
Y (k)
k−i+1 (−Ui)−1

h(d)
i
+
m+n−i+1
X
j=2
X(i)
j h(d)
j+i−1

+
k
Y
j=1
Gj;
For n + 1 ≤k ≤n + m −1,
g(d) (n, k −n) = (−Uk)−1

h(d)
k
+
m+n−k+1
X
j=2
X(k)
j
h(d)
j+k−1


+
k−1
X
i=1
Y (k)
k−i+1 (−Ui)−1

h(d)
i
+
m+n−i+1
X
j=2
X(i)
j h(d)
j+i−1

+
k
Y
j=1
Gj;
For k = n + m,
g(d) (n, m) = (−Un+m)−1 h(d)
n+m +
n+m−1
X
i=1
Y (n+m)
n+m−i+1 (−Ui)−1
×

h(d)
i
+
m+n−i+1
X
j=2
X(i)
j h(d)
j+i−1

+
n+m
Y
j=1
Gj.
23

---

## Page 24

Proof: It is seen from (34) that we need to compute two parts: µ1 (−B)−1 e1 and
(−B)−1 h(d). For the ﬁrst part, we obtain
µ1 (−B)−1 e1 = µ1 (−U1)−1 
1, Y (2)
2
, Y (3)
3
, . . . , Y (n+m)
n+m
T
.
Since G1 = (−U1)−1 µ1 and Y (k)
k
= Qk
j=2 Gj, we obtain
µ1 (−B)−1 e1 =

G1, G2G1, G3G2G1, . . . ,
m+n
Y
j=1
Gj


T
.
For the second part, we have
(−B)−1 h(d) =

















(−U1)−1 h
h(d)
1
+ Pm+n
j=2 X(1)
j
h(d)
j
i
...
(−Uk)−1 h
h(d)
k
+ Pm+n−k+1
j=2
X(k)
j
h(d)
j+k−1
i
+ Pk−1
i=1 Y (k)
k−i+1 (−Ui)−1 h
h(d)
i
+ Pm+n−i+1
j=2
X(i)
j h(d)
j+i−1
i
...
(−Un+m)−1 h(d)
n+m + Pn+m−1
i=1
Y (n+m)
n+m−i+1 (−Ui)−1
×
h
h(d)
i
+ Pm+n−i+1
j=2
X(i)
j h(d)
j+i−1
i

















.
Therefore, a simple computation for the vector ϕ(d) = (−B)−1 h(d) + µ1 (−B)−1 e1 can
derive our desired results. This completes the proof.
Remark 4 (1) Theorem 2 provides an eﬀective method of solving the continuous-time
Poisson equation −B(d)g(d) = f (d) −ηde, through an equation transformation



g(d) (0, 0) = ℑ,
ϕ(d) = (−B)−1 h(d) + µ1 (−B)−1 e1 · ℑ,
(36)
where ℑis any given constant, and (−B)−1 can be eﬀectively computed by means of the
RG-factorization given in Li [29].
It is necessary to set up a general solution to the system of linear equations (36). Let
ϕ(d)
0
be the unique solution to the system of linear equations −Bϕ(d)
0
= h(d). Then, the
general solution is given by ϕ(d) = ϕ(d)
0
+ µ1 (−B)−1 e1 · ℑ.
(2) To deal with the Poisson equation, some authors (e.g., see Chapter 2 of Cao [5]
and Hunter [22]) provided a fundamental matrix method to give a special solution under
a constraint condition π(d)g(d) = ηd, by which the Poisson equation is well related to the
24

---

## Page 25

well-known fundamental matrix (e.g., (I −P + eπ) g = f or (−Q + eπ) g = f). From
the fundamental matrix method, our undetermined constant ℑcan be determined by
ℑ=
ηd −̟
(d) (−B)−1 h(d)
π(d) (0, 0) + µ1̟
(d) (−B)−1 e1
,
where̟
(d) is a row vector obtained through omitting the ﬁrst element of the stationary
probability vector π(d), that is,̟
(d) =

π(d) (1, 0) , . . . , π(d) (n, 0) , π(d) (n, 1) , . . . , π(d) (n, m)

.
It is worth noting that in solving the Poisson equation, our RG-factorization method is
superior to the fundamental matrix method because the RG-factorization given in Li [29]
can easily deal with the inverse of a high-dimensional transition matrix; while computing
the inverse (I −P + eπ)−1 or (−Q + eπ)−1, however, is very diﬃcult for a matrix P or
Q with large size, and it also needs to ﬁrst compute the stationary probability vector π.
5
Impact of Service Price
In this section, we deﬁne a perturbation realization factor of the policy-based birth-
death process, and analyze how the service price impacts on the perturbation realization
factor.
Note that the results given in this section will be utilized for establishing the
optimal policy of the energy-eﬃcient data center in the later section.
For the performance potential vector ϕ(d) under a constraint condition g(d) (0, 0) = 1,
we deﬁne a perturbation realization factor as
G(d) (n, j) def
= g(d) (n, j −1) −g(d) (n, j) , j = 1, 2, . . . , m.
It follows from Theorem 2 that
g(d) (n, j −1) = (−Un+j−1)−1
"
h(d)
n+j−1 +
m−j+2
X
k=2
X(n+j−1)
k
h(d)
n+j+k−2
#
+
n+j−2
X
i=1
Y (n+j−1)
n+j−i
(−Ui)−1
"
h(d)
i
+
m+n−i+1
X
k=2
X(i)
k h(d)
k+i−1
#
+
n+j−1
Y
k=1
Gk
and
g(d) (n, j) = (−Un+j)−1
"
h(d)
n+j +
m−j+1
X
k=2
X(n+j)
k
h(d)
n+j+k−1
#
+
n+j−1
X
i=1
Y (n+j)
n+j−i+1 (−Ui)−1
"
h(d)
i
+
m+n−i+1
X
k=2
X(i)
k h(d)
k+i−1
#
+
n+j
Y
k=1
Gk.
25

---

## Page 26

To express the perturbation realization factor G(d) (n, j) by means of the service price R,
we write
A0,0 = 0,
B0,0 = (nP1,W + mP2,S) C1 > 0;
For i = 1, 2, . . . , n,
Ai,0 = iµ1 > 0,
Bi,0 = (nP1,W + mP2,S) C1 + iC(1)
2
> 0;
For j = 1, 2, . . . , m and dn,j = 0, 1, . . . , m,
A(d)
n,j = nµ1 + (j ∧dn,j) µ2 > 0,
B(d)
n,j = [nP1,W + dn,jP2,W + (m −dn,j) P2,S] C1 + nC(1)
2
+ jC(2)
2
+ nµ1C3 + λ1{i=n,j=m}C4 > 0.
Then, for i = 0, 1, . . . , n and j = 0,
f (i, 0) = RAi,0 −Bi,0;
For j = 1, 2, . . . , m,
f (d) (n, j) = RA(d)
n,j −B(d)
n,j .
Thus, we obtain
ηd = π(d)f (d)
=
n
X
i=0
π (i, 0) f (i, 0) +
m
X
j=1
π (n, j) f (d) (n, j)
= RD(d) −F (d),
where
D(d) =
n
X
i=0
π (i, 0) Ai,0 +
m
X
j=1
π (n, j) A(d)
n,j > 0,
and
F (d) =
n
X
i=0
π (i, 0) Bi,0 +
m
X
j=1
π (n, j) B(d)
n,j > 0.
26

---

## Page 27

Then,
h(d) =














h(d)
1
...
h(d)
n
h(d)
n+1
...
h(d)
n+m














=














f (1, 0) −ηd
...
f (n, 0) −ηd
f (d) (n, 1) −ηd
...
f (d) (n, m) −ηd














=














R

A1,0 −D(d)
−

B1,0 −F (d)
...
R

An,0 −D(d)
−

Bn,0 −F (d)
R
h
A(d)
n,1 −D(d)i
−
h
B(d)
n,1 −F (d)i
...
R
h
A(d)
n,m −D(d)i
−
h
B(d)
n,m −F (d)i














.
If a job ﬁnishes its service at a server and leaves this system immediately, then the
data center can obtain a ﬁxed revenue R from each job. Obviously, R is the service price
provided by the data center. Now, we study the inﬂuence of the service price R on the
perturbation realization factor G(d) (n, j). Note that all the numbers (−Uk)−1, X(k)
j
, Y (k)
j
and Gj are positive and are independent of the service price R, while all the numbers h(d)
j
are the linear functions of R.
We write
W (d)
n,j = (−Un+j)−1
(h
A(d)
n,j −D(d)i
+
m−j+1
X
k=2
X(n+j)
k
h
A(d)
n,j+k−1 −D(d)i)
+
n
X
i=1
Y (n+j)
n+j−i+1 (−Ui)−1 h
Ai,0 −D(d)i
+
n+j−1
X
i=n+1
Y (n+j)
n+j−i+1 (−Ui)−1 h
A(d)
n,i−n −D(d)i
+
X
3≤k+i≤n+1
n+j−1
X
i=1
Y (n+j)
n+j−i+1 (−Ui)−1
m+n−i+1
X
k=2
X(i)
k
h
Ak+i−1,0 −D(d)i
+
X
n+2≤k+i≤n+m+1
n+j−1
X
i=1
Y (n+j)
n+j−i+1 (−Ui)−1
m+n−i+1
X
k=2
X(i)
k
h
A(d)
n,k+i−1−n −D(d)i
and
V (d)
n,j = (−Un+j)−1
(h
B(d)
n,j −F (d)i
+
m−j+1
X
k=2
X(n+j)
k
h
B(d)
n,j+k−1 −F (d)i)
+
n
X
i=1
Y (n+j)
n+j−i+1 (−Ui)−1 h
Bi,0 −F (d)i
+
n+j−1
X
i=n+1
Y (n+j)
n+j−i+1 (−Ui)−1 h
B(d)
n,i−n −F (d)i
+
X
3≤k+i≤n+1
n+j−1
X
i=1
Y (n+j)
n+j−i+1 (−Ui)−1
m+n−i+1
X
k=2
X(i)
k
h
Bk+i−1,0 −F (d)i
+
X
n+2≤k+i≤n+m+1
n+j−1
X
i=1
Y (n+j)
n+j−i+1 (−Ui)−1
m+n−i+1
X
k=2
X(i)
k
h
B(d)
n,k+i−1−n −F (d)i
,
27

---

## Page 28

then, we obtain that for j = 1, 2, . . . , m,
G(d) (n, j) = g(d) (n, j −1) −g(d) (n, j)
= R
h
W (d)
n,j−1 −W (d)
n,j
i
−
h
V (d)
n,j−1 −V (d)
n,j
i
+ (1 −Gn+j)
n+j−1
Y
k=1
Gk.
(37)
We can see that G(d) (n, j) quantiﬁes the diﬀerence among two adjacent performance
potentials g(d) (n, j) and g(d) (n, j −1). It measures the long-run eﬀect on the average
proﬁt of the data center when the system state is changed from (n, j −1) to (n, j), which
indicates the occurrence of a service completion event. From later discussion in Section
6, we will see that G(d) (n, j) plays a fundamental role in the performance optimization
of data centers and the sign of G(d) (n, j) + c directly determines the selection of decision
actions, as shown in (49) later, where c is deﬁned as
c = R −(P2,W −P2,S) C1
µ2
.
(38)
To this end, we analyze how the service price impacts on G(d) (n, j) + c as follows.
Substituting (37) into the linear equation G(d) (n, j) + c = 0, we obtain
R
h
W (d)
n,j−1 −W (d)
n,j
i
−
h
V (d)
n,j−1 −V (d)
n,j
i
+ (1 −Gn+j)
n+j−1
Y
k=1
Gk + c = 0.
(39)
Substituting (38) into the above equation, we obtain that the unique solution of the price
R in (39) is given by
ℜ(d)
n,j =
h
V (d)
n,j−1 −V (d)
n,j
i
−(1 −Gn+j) Qn+j−1
k=1
Gk + (P2,W −P2,S)C1
µ2
1 +
h
W (d)
n,j−1 −W (d)
n,j
i
.
(40)
It is easy to see that (a) if R ≥ℜ(d)
n,j, then G(d) (n, j) + c ≥0; and (b) if R ≤ℜ(d)
n,j, then
G(d) (n, j) + c ≤0.
In the energy-eﬃcient data center, we deﬁne two critical values, related to the service
price, as
RH = max
d∈D
n
0, ℜ(d)
n,1, ℜ(d)
n,2, . . . , ℜ(d)
n,m
o
(41)
and
RL = min
d∈D
n
ℜ(d)
n,1, ℜ(d)
n,2, . . . , ℜ(d)
n,m
o
.
(42)
The following proposition uses the two critical values related to the service price to
provide a key condition whose purpose is to establish a sensitivity-based optimization
28

---

## Page 29

framework of the energy-eﬃcient data center in our later study. Also, this proposition will
be useful in the next section for studying the monotonicity of the energy-eﬃcient policies.
Proposition 2 (1) If R ≥RH, then for any d ∈D and for each j = 1, 2, . . . , m, we have
G(d) (n, j) + c ≥0.
(43)
(2) If 0 ≤R ≤RL, then for any d ∈D and for each j = 1, 2, . . . , m, we have
G(d) (n, j) + c ≤0.
(44)
Proof: (1) For any d ∈D and for each j = 1, 2, . . . , m, since R ≥RH and RH =
maxd∈D
n
0, ℜ(d)
n,1, ℜ(d)
n,2, . . . , ℜ(d)
n,m
o
, we have
R ≥ℜ(d)
n,j,
which clearly makes that G(d) (n, j) + c ≥0.
(2) For any d ∈D and for each j = 1, 2, . . . , m, if 0 ≤R ≤RL, we have
R ≤ℜ(d)
n,j,
this gives that G(d) (n, j) + c ≤0. This completes the proof.
6
Monotonicity and Optimality
In this section, we use the Poisson equation to derive a useful performance diﬀerence
equation, and discuss the monotonicity and optimality of the long-run average proﬁt of
the energy-eﬃcient data center with respect to the policies. Based on this, we give the
optimal energy-eﬃcient policy under some restrained service prices.
For any given policy d ∈D, the policy-based continuous-time birth-death process
{X(d)(t) : t ≥0} with inﬁnitesimal generator B(d) given in (3) is irreducible, aperiodic
and positive recurrent, hence the long-run average proﬁt of the data center is given by
ηd = π(d)f (d),
and the Poisson equation is written as
B(d)g(d) = ηde −f (d).
29

---

## Page 30

With a similar role played by state (i, j), it is seen from (3) that the policy d directly aﬀects
not only the elements of the inﬁnitesimal generator B(d) but also the reward function
f (d).
That is, if the policy d changes, then the inﬁnitesimal generator B(d) and the
reward function f (d) will have their corresponding changes. To express such a change
mathematically, we take two diﬀerent policies d and d′, both of which correspond to their
inﬁnitesimal generators B(d) and B(d′), and to their reward functions f (d) and f (d′).
The following lemma provides a useful equation for the diﬀerence ηd′ −ηd of the long-
run average performances ηd and ηd′ for any two policies d, d′ ∈D. The performance
diﬀerence equation plays a key role in the sensitivity-based optimization theory. Note
that the performance diﬀerence equation was given in Cao [5], while here we restate it
with some simple discussion, for convenience of readers.
Lemma 1 For any two policies d, d′ ∈D, we have
ηd′ −ηd = π(d′) h
B(d′) −B(d)
g(d)+

f (d′) −f (d)i
.
(45)
Proof: Note that π(d′)B(d′) = 0, B(d)g(d) = ηde −f (d), π(d′)e = 1, we compute
π(d′) h
B(d′) −B(d)
g(d)+

f (d′) −f (d)i
= −π(d′) · B(d)g(d) + π(d′)f (d′) −π(d′)f (d)
= −π(d′) h
ηde −f (d)i
+ ηd′ −π(d′)f (d)
= ηd′ −ηd.
This completes the proof.
Now, we describe the ﬁrst role played by the performance diﬀerence, in which we set
up a partial order relation in the policy set D so that the optimal policy in D can be found
numerically. Based on the performance diﬀerence ηd′ −ηd for any two policies d, d′ ∈D,
we can set up a partial order in the policy set D as follows. We write d′ ≻d if ηd′ > ηd;
d′ ≈d if ηd′ = ηd; d′ ≺d if ηd′ < ηd. Also, we write d′ ⪰d if ηd′ ≥ηd; d′ ⪯d if ηd′ ≤ηd.
By using this partial order, our research target is to ﬁnd an optimal policy d∗∈D such
that d∗⪰d for any policy d ∈D, or
d∗= arg max
d∈D
n
ηdo
.
Note that the policy set D and the state space Ωare both ﬁnite, thus an enumeration
method is feasible for ﬁnding the optimal energy-eﬃcient policy d∗in the policy set D.
30

---

## Page 31

Since d = (0, 0, . . . , 0; dn,1, dn,2, . . . , dn,m) and dn,j ∈{0, 1, . . . , m}, it is seen that the policy
set D contains (m + 1)m elements so that the enumeration method will require a huge
computation workload. However, our following work can greatly reduce the optimization
complexity by means of the sensitivity-based optimization theory.
Now, we discuss the monotonicity of the long-run average proﬁt ηd with respect to a
decision element dn,j of any policy d ∈D, for dn,j = 0, 1, . . . , m. This result is derived
by the following two theorems, in which we show that for any policy d ∈D and for each
j = 1, 2, . . . , m, the long-run average proﬁt ηd is unimodal with respect to each decision
element dn,j ∈{0, 1, . . . , m}.
Theorem 3 For any policy d ∈D and for each j = 1, 2, . . . , m, the long-run average
proﬁt ηd is linearly decreasing with respect to each decision element dn,j, where dn,j ∈
{j, j + 1, . . . , m}.
Proof: For each j = 1, 2, . . . , m, we consider two interrelated policies d, d′ ∈D as
follows.
d =

0, 0, . . . , 0; dn,1, dn,2, . . . , dn,j−1, dn,j,dn,j+1, . . . , dn,m

,
d′ =
 0, 0, . . . , 0; dn,1, dn,2, . . . , dn,j−1, j,dn,j+1, . . . , dn,m

,
where dn,j > j. It is seen that the two policies d, d′ have one diﬀerence only between their
corresponding decision elements dn,j and j. In this case, it is seen from Theorem 1 that
B(d) = B(d′) and π(d) = π(d′). Also, it is easy to check from (13) to (17) that
f (d) −f (d′) =

0, 0, . . . , 0; 0, 0, . . . , 0, −(dn,j −j) (P2,W −P2,S) C1,0, . . . , 0
T
.
Thus, it follows from Lemma 1 that
ηd −ηd′ = π(d) h
B(d) −B(d′)
g(d′)+

f (d) −f (d′)i
= −π(d) (n, j) (dn,j −j) (P2,W −P2,S) C1
or
ηd = ηd′ −π(d) (n, j) (dn,j −j) (P2,W −P2,S) C1.
(46)
Since π(d) = π(d′) by Theorem 1, it is easy to see that π(d) (n, j) = π(d′) (n, j) can be
determined by d′
n,j = j. This indicates that π(d) (n, j) is irrelevant to the decision element
dn,j. Again, note that ηd′ is irrelevant to the decision element dn,j, and P2,W −P2,S and C1
31

---

## Page 32

are two positive constants. Thus, it is easy to see from (46) that the long-run average proﬁt
ηd is linearly decreasing with respect to each decision element dn,j ∈{j, j + 1, . . . , m}.
This completes the proof.
In what follows we discuss the left half part of the unimodal structure of the long-run
average proﬁt ηd with respect to each decision element dn,j ∈{0, 1, . . . , j}. Compared to
the analysis of its right half part in Theorem 3, our discussion for the left half part is a
little bit complicated.
Let the optimal energy-eﬃcient policy d∗= arg max
d∈D

ηd	
be
d∗=
 0, 0, . . . , 0; d∗
n,1, d∗
n,2, . . . , d∗
n,m

.
Then, it is seen from Theorem 3 that
d∗
n,1 ∈{0, 1} ;
...
d∗
n,j ∈{0, 1, . . . , j} ;
...
d∗
n,m ∈{0, 1, . . . , m} .
Thus, Theorem 3 makes the area of ﬁnding the optimal energy-eﬃcient policy d∗from a
large set {0, 1, . . . , m}m to a shrunken area {0, 1} × {0, 1, 2} × · · · × {0, 1, . . . , m}.
To ﬁnd the optimal energy-eﬃcient policy d∗, we consider two energy-eﬃcient policies
with an interrelated structure as follows.
d =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, dn,j,dn,j+1, . . . , dn,m

,
d′ =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, d′
n,j,dn,j+1, . . . , dn,m

,
where d′
n,j > dn,j, and dn,j, d′
n,j ∈{1, 2, . . . , j}. It is easy to check from (3) that
B(d′) −B(d)=

















0
0
...
...
0

d′
n,j −dn,j

µ2
−

d′
n,j −dn,j

µ2
0
0
...
...
0
0

















.
(47)
32

---

## Page 33

On the other hand, from the reward functions given in (13) to (15), it is seen that for
j = 1, 2, . . . , m, and dn,j = 0, 1, . . . , m,
f (d) (n, j) = [Rµ2 −(P2,W −P2,S) C1] dn,j
+ Rnµ1 −(nP1,W −mP2,S) C1 −
h
nC(1)
2
+ jC(2)
2
i
−nµ11{j>0}C3 −λ1{i=n,j=m}C4
and
f (d′) (n, j) = [Rµ2 −(P2,W −P2,S) C1] d′
n,j
+ Rnµ1 −(nP1,W −mP2,S) C1 −
h
nC(1)
2
+ jC(2)
2
i
−nµ11{j>0}C3 −λ1{i=n,j=m}C4.
Hence, we have
f (d′) −f (d) =
 0, 0, . . . , 0, µ2c
 d′
n,j −dn,j

, 0, . . . , 0
T .
(48)
We write
ηd|dn,j=k = π(d)|dn,j=k · f (d)|dn,j=k.
The following theorem discusses the left half part of the unimodal structure of the long-run
average proﬁt ηd with respect to each decision element dn,j ∈{0, 1, . . . , m}.
Theorem 4 If R ≥RH, then for any policy d ∈D and for each j = 1, 2, . . . , m, the
long-run average proﬁt ηd is strictly monotone increasing with respect to each decision
element dn,j, where dn,j ∈{0, 1, . . . , j}.
Proof: For each j = 1, 2, . . . , m, we consider two energy-eﬃcient policies with an
interrelated structure as follows.
d =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, dn,j,dn,j+1, . . . , dn,m

,
d′ =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, d′
n,j,dn,j+1, . . . , dn,m

,
where d′
n,j > dn,j, and dn,j, d′
n,j ∈{0, 1, . . . , j}.
Applying Lemma 1, it follows from
(47) and (48) that
ηd′ −ηd = π(d′) h
B(d′) −B(d)
g(d)+

f (d′) −f (d)i
= µ2π(d′) (n, j)
 d′
n,j −dn,j
 h
g(d) (n, j −1) −g(d) (n, j) + c
i
= µ2π(d′) (n, j)
 d′
n,j −dn,j
 h
G(d) (n, j) + c
i
,
(49)
33

---

## Page 34

where G(d) (n, j) = g(d) (n, j −1)−g(d) (n, j). If R ≥RH, then it is seen from Proposition
2 that G(d) (n, j) + c ≥0.
Thus, we obtain that for the two policies d, d′ ∈D with
d′
n,j > dn,j and dn,j, d′
n,j ∈{0, 1, . . . , j},
ηd′ > ηd.
This shows that
ηd|dn,j=1 < ηd|dn,j=2 < · · · < ηd|dn,j=m−1 < ηd|dn,j=m.
This completes the proof.
When R ≥RH, we use Figure 2 to provide an intuitive summary for the main results
given in Theorems 3 and 4. In the right half part of Figure 2,
ηd = ηd′ −π(d) (n, j) (dn,j −j) (P2,W −P2,S) C1
shows that ηd is a linear function of the decision element dn,j. By contrast, in the right
half part of Figure 2, we need to ﬁrst introduce a restrictive condition: R ≥RH, under
which
ηd′ −ηd = µ2π(d′) (n, j)
 d′
n,j −dn,j
 h
G(d) (n, j) + c
i
.
Let d′
n,j = j. Then,
ηd = ηd′ −µ2π(d′) (n, j) (j −dn,j)
h
G(d) (n, j) + c
i
.
Since G(d) (n, j) depends on the decision element dn,j, it is clear that ηd is a nonlinear
function of the decision element dn,j.
Theorem 5 If 0 ≤R ≤RL, then for any d ∈D and for each j = 1, 2, . . . , m, the long-
run average proﬁt ηd is strictly monotone decreasing with respect to each decision element
dn,j, where dn,j ∈{0, 1, . . . , j}.
Proof: This proof is similar to the proof of Theorem 4. For each j = 1, 2, . . . , m, we
consider two energy-eﬃcient policies with an interrelated structure as follows.
d =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, dn,j,dn,j+1, . . . , dn,m

,
d′ =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, d′
n,j,dn,j+1, . . . , dn,m

,
34

---

## Page 35

1     2      3      4    ĂĂ    j-1    j     j+1   ĂĂm-3 m-2  m-1  m 
h d
,n j
d
R ≥ RH  
It is needed in the left half part 
Figure 2: The unimodal structure of the long-run average proﬁt.
where d′
n,j > dn,j, and dn,j, d′
n,j ∈{0, 1, . . . , j}. It is clear that
ηd′ −ηd = µ2π(d′) (n, j)
 d′
n,j −dn,j
 h
G(d) (n, j) + c
i
.
If 0 ≤R ≤RL, then it is seen from Proposition 2 that for any d ∈D and for each
j = 1, 2, . . . , m, G(d) (n, j) + c ≤0. Thus, we obtain that for the two policies d, d′ ∈D
with d′
n,j > dn,j and dn,j, d′
n,j ∈{0, 1, . . . , j},
ηd′ < ηd.
This shows that
ηd|dn,j=1 > ηd|dn,j=2 > · · · > ηd|dn,j=m−1 > ηd|dn,j=m.
This completes the proof.
When 0 ≤R ≤RL, we use Figure 3 to provide an intuitive summary for the main
results given in Theorems 3 and 5.
The following theorem establishes the optimal energy-eﬃcient policy d∗in the data
center, and also computes the maximal long-run average proﬁt.
Theorem 6 The optimal energy-eﬃcient policy d∗and the maximal long-run average
proﬁt ηd∗can be determined in the following two diﬀerent cases:
35

---

## Page 36

1     2      3      4    ĂĂ    j-1    j     j+1   ĂĂm-3 m-2  m-1  m 
h d
,n j
d
It is needed in the left half part 
R ≤ RL  
Figure 3: The decreasing structure of the long-run average proﬁt.
(a) If R ≥RH, then
d∗= (0, 0, . . . , 0; 1, 2, . . . , m)
and
ηd∗=
n
X
i=0
λi
i!µi
1
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
m
P
j=1
λj
j
Π
i=1 (nµ1 + iµ2)
h
Riµ1 −(nP1,W + mP2,S) C1 −iC(1)
2
i
+
m
X
j=1
λn
n!µn
1
λj
j
Π
i=1 (nµ1 + iµ2)
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
m
P
j=1
λj
j
Π
i=1 (nµ1 + iµ2)
n
R (nµ1 + jµ2) −
h
nC(1)
2
+ jC(2)
2
i
−[nP1,W + jP2,W + (m −j) P2,S] C1 −nµ11{j>0}C3 −λ1{i=n,j=m}C4
o
.
(b) If 0 ≤R ≤RL, then
d∗= (0, 0, . . . , 0; 0, 0, . . . , 0)
36

---

## Page 37

and
ηd∗=
n
X
i=0
λi
i!µi
1
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
m
P
j=1
λj
(nµ1)j
h
Riµ1 −(nP1,W + mP2,S) C1 −iC(1)
2
i
+
m
X
j=1
λn
n!µn
1
λj
(nµ1)j
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
m
P
j=1
λj
(nµ1)j
n
Rnµ1 −[nP1,W + mP2,S] C1
−
h
nC(1)
2
+ jC(2)
2
i
−nµ11{j>0}C3 −λ1{i=n,j=m}C4
o
.
Proof: (a) For the optimal energy-eﬃcient policy d∗= (0, 0, . . . , 0; 1, 2, . . . , m), it is
clear that d∗
n,j = j and d∗
n,j ∧j = j. Thus, it follows from (5), (6) and (7) that
ξi,0 = λi
i!µi
1
,
i = 0, 1, . . . , n,
and
ξ(d∗)
n,j
=
λn
n!µn
1
λj
j
Π
i=1 (nµ1 + iµ2)
,
j = 1, 2, . . . , m,
b(d∗) =
n
X
i=0
λi
i!µi
1
+ λn
n!µn
1
m
X
j=1
λj
j
Π
i=1 (nµ1 + iµ2)
.
It follows from (8) and (9) that for i = 0, 1, . . . , n,
π(d∗) (i, 0) =
λi
i!µi
1
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
m
P
j=1
λj
j
Π
i=1 (nµ1 + iµ2)
,
and for j = 1, 2, . . . , m,
π(d∗) (n, j) =
λn
n!µn
1
λj
j
Π
i=1 (nµ1 + iµ2)
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
m
P
j=1
λj
j
Π
i=1 (nµ1 + iµ2)
.
At the same time, from (11) to (16) we obtain that for i = 0, 1, . . . , n,
f (i, 0) = Riµ1 −(nP1,W + mP2,S) C1 −iC(1)
2 ,
37

---

## Page 38

and j = 1, 2, . . . , m,
f (d∗) (n, j) = R (nµ1 + jµ2) −[nP1,W + jP2,W + (m −j) P2,S] C1
−
h
nC(1)
2
+ jC(2)
2
i
−nµ11{j>0}C3 −λ1{i=n,j=m}C4.
Thus, we obtain
ηd∗=
n
X
i=0
π(d∗) (i, 0) f (i, 0) +
m
X
j=1
π(d∗) (n, j) f (d∗) (n, j) .
A simple computation directly derives our desired result.
(b) For the optimal policy d∗= (0, 0, . . . , 0; 0, 0, . . . , 0), it is clear that d∗
n,j = 0 so that
d∗
n,j ∧j = 0. A similar analysis to that in (a) can lead to our desired result. This completes
the proof.
Remark 5 The results of Theorem 6 are intuitive due to the fact that when the service
price is suitably high, the number of working servers is equal to the number of waiting jobs
in Group 2; while when the service price is lower, each server opened at the work state
will pay a high energy consumption cost but receive a low revenue, thus the proﬁt cannot
increase and all the servers in Group 2 would like to be at the sleep state.
When the price RL < R < RH, we can further derive the following theorem about the
monotonicity of ηd with respect to the decision element dn,j.
Theorem 7 If RL < R < RH, then the long-run average proﬁt ηd is monotone (either
increasing or decreasing) with respect to the decision element dn,j, where j = 1, 2, . . . , m
and dn,j ∈{0, 1, . . . , j}.
Proof:
Similar to the ﬁrst part of the proof for Theorem 4, we consider any two
energy-eﬃcient policies with an interrelated structure as follows.
d =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, dn,j,dn,j+1, . . . , dn,m

,
d′ =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, d′
n,j,dn,j+1, . . . , dn,m

,
where dn,j, d′
n,j ∈{0, 1, . . . , j}. Applying Lemma 1, we obtain
ηd′ −ηd = µ2π(d′) (n, j)
 d′
n,j −dn,j
 h
G(d) (n, j) + c
i
.
(50)
38

---

## Page 39

On the other hand, we can similarly obtain the following diﬀerence equation
ηd −ηd′ = µ2π(d) (n, j)
 dn,j −d′
n,j
 h
G(d′) (n, j) + c
i
.
(51)
By summing (50) and (51), we have
µ2π(d′) (n, j)
 d′
n,j −dn,j
 h
G(d) (n, j) + c
i
+µ2π(d) (n, j)
 dn,j −d′
n,j
 h
G(d′) (n, j) + c
i
= 0.
We can directly derive
π(d′) (n, j)
h
G(d) (n, j) + c
i
= π(d) (n, j)
h
G(d′) (n, j) + c
i
.
Therefore, we have the sign conservation equation
G(d) (n, j) + c
G(d′) (n, j) + c = π(d) (n, j)
π(d′) (n, j) > 0.
(52)
The above equation means that the sign of G(d) (n, j) + c and G(d′) (n, j) + c are always
identical when a particular decision element dn,j is changed to any d′
n,j. With the sign
conservation equation (52) and the performance diﬀerence equation (51), we can directly
derive that the long-run average proﬁt ηd is monotone with respect to dn,j. This completes
the proof.
Based on Theorems 4, 5, and 7, we can directly derive that the optimal decision element
d∗
n,j has the bang-bang control form, no matter what the value of R will be.
Corollary 1 The optimal decision element d∗
n,j is either 0 or j, i.e., the bang-bang control
is optimal.
With Corollary 1, we should either keep all servers sleep or turn on the servers such
that the number of working servers equals the number of waiting jobs in Group 2. We can
see that the search space of dn,j can be reduced from {0, 1, . . . , j} to a 2-element set {0, j},
which is a signiﬁcant reduction of optimization complexity. The form of the bang-bang
control is also very simple and it is easy to adopt in practice, while the optimality of the
bang-bang control guarantees the performance conﬁdence of such simple forms of control.
7
Threshold Energy-Eﬃcient Policy
We have proved the optimality of the bang-bang control, no matter what the value
of R will be.
In practice, threshold-type policy is another category of policies which
39

---

## Page 40

also have a very simple form and are widely adopted in many practical systems. In this
section, we focus our study on the threshold-type policy, although its optimality is not
yet proved rigorously in our problem.
We use the Poisson equation to study a class
of threshold energy-eﬃcient policies, and obtain the necessary condition of the optimal
threshold energy-eﬃcient policy.
Now, we introduce an interesting subset of the policy set D as follows. To this end,
for θ = 1, 2, . . . , m + 1, we write dθ as an energy-eﬃcient policy d with dn,j = 0 if
1 ≤j ≤θ −1 and dn,j = j if θ ≤j ≤m, i.e.,
dθ
def
=

0, 0, . . . , 0; 0, 0, . . . , 0
|
{z
},
θ−1 zeros
θ, θ + 1, . . . , m

.
Let
D∆def
= {dθ : θ = 1, 2, . . . , m + 1} .
Then,
D∆=




0, 0, . . . , 0; 0, 0, . . . , 0
|
{z
},
θ−1 zeros
θ, θ + 1, . . . , m

: θ = 1, 2, . . . , m + 1


.
It is easy to see that D∆⊂D.
For a policy dθ, it is clear that if 1 ≤j ≤θ −1, then dn,j = 0 and dn,j ∧j = 0; and if
θ ≤j ≤m, then dn,j = j and dn,j ∧j = j. Thus, it follows from (5), (6) and (7) that
ξi,0 = λi
i!µi
1
,
i = 0, 1, . . . , n,
and
ξ(dθ)
n,j
=
λn
n!µn
1
λj
(nµ1)j ,
j = 1, 2, . . . , θ −1,
ξ(dθ)
n,j
=
λn
n!µn
1
λθ−1
(nµ1)θ−1
λj−θ+1
j
Π
i=θ (nµ1 + iµ2)
,
j = θ, θ + 1, . . . , m,
b(dθ) =
n
X
i=0
λi
i!µi
1
+ λn
n!µn
1
θ−1
X
j=1
λj
(nµ1)j + λn
n!µn
1
λθ−1
(nµ1)θ−1
m
X
j=θ
λj−θ+1
j
Π
i=θ (nµ1 + iµ2)
.
It follows from (8) and (9) that for i = 0, 1, . . . , n,
π(dθ) (i, 0) =
λi
i!µi
1
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
θ−1
P
j=1
λj
(nµ1)j + λn
n!µn
1
λθ−1
(nµ1)θ−1
m
P
j=θ
λj−θ+1
j
Π
i=θ (nµ1 + iµ2)
;
40

---

## Page 41

for j = 1, 2, . . . , θ −1,
π(dθ) (n, j) =
λn
n!µn
1
λj
(nµ1)j
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
θ−1
P
j=1
λj
(nµ1)j + λn
n!µn
1
λθ−1
(nµ1)θ−1
m
P
j=θ
λj−θ+1
j
Π
i=θ (nµ1 + iµ2)
;
and for j = θ, θ + 1, . . . , m,
π(dθ) (n, j) =
λn
n!µn
1
λθ−1
(nµ1)θ−1
λj−θ+1
j
Π
i=θ (nµ1 + iµ2)
nP
i=0
λi
i!µi
1
+ λn
n!µn
1
θ−1
P
j=1
λj
(nµ1)j + λn
n!µn
1
λθ−1
(nµ1)θ−1
m
P
j=θ
λj−θ+1
j
Π
i=θ (nµ1 + iµ2)
.
It follows from (11) to (16) that for i = 0, 1, . . . , n,
f (i, 0) = Riµ1 −(nP1,W + mP2,S) C1 −iC(1)
2 ;
for j = 1, 2, . . . , θ −1,
f (dθ) (n, j) = Rnµ1 −(nP1,W + mP2,S) C1 −
h
nC(1)
2
+ jC(2)
2
i
−nµ1C3;
and for j = θ, θ + 1, . . . , m,
f (dθ) (n, j) = R (nµ1 + jµ2) −[nP1,W + jP2,W + (m −j) P2,S] C1
−
h
nC(1)
2
+ jC(2)
2
i
−nµ1C3 −λ1{i=n,j=m}C4.
Note that
ηdθ =
n
X
i=0
π(dθ) (i, 0) f (i, 0) +
m
X
j=1
π(dθ) (n, j) f (dθ) (n, j) .
We obtain the explicit expression of the long-run average proﬁt under policy dθ as follows.
ηdθ =
n
X
i=0
π(dθ) (i, 0) f (i, 0)
h
Riµ1 −(nP1,W + mP2,S) C1 −iC(1)
2
i
+
θ−1
X
j=1
π(dθ) (n, j)
n
Rnµ1 −(nP1,W + mP2,S) C1 −
h
nC(1)
2
+ jC(2)
2
i
−nµ1C3
o
+
m
X
j=θ
π(dθ) (n, j)
n
R (nµ1 + jµ2) −[nP1,W + jP2,W + (m −j) P2,S] C1
−
h
nC(1)
2
+ jC(2)
2
i
−nµ1C3 −λ1{i=n,j=m}C4
o
.
41

---

## Page 42

Let
θ∗=
arg max
θ∈{1,2,...,m+1}
n
ηdθ
o
.
Then, we call dθ∗the optimal threshold energy-eﬃcient policy in the policy set D∆. Since
D∆⊂D, the partially ordered set D shows that D∆is also a partially ordered set. Based
on this, it is easy to see from the two partially ordered sets D and D∆that
ηdθ∗≤ηd∗.
If ηdθ∗= ηd∗, then we call dθ∗the optimal threshold energy-eﬃcient policy in the original
policy set D; If ηdθ∗< ηd∗, then we call dθ∗the suboptimal threshold energy-eﬃcient
policy in the original policy set D.
We take a minimal positive integer θ∗∈{1, 2, . . . , m + 1} such that
dθ∗=

0, 0, . . . , 0; 0, 0, . . . , 0
|
{z
},
θ∗−1 zeros
θ∗, θ∗+ 1, . . . , m

.
For the optimal threshold energy-eﬃcient policy dθ∗, the following theorem determines
the positive or negative property of the function G(dθ) (n, θ) + c for θ = θ∗−1, θ∗, θ∗+ 1,
although the explicit expression of the perturbation realization factor G(dθ) (n, θ) is not
given yet. This may be useful for us to understand the role played by Proposition 2 in
analyzing the monotonicity and optimality of the energy-eﬃcient policies. Furthermore,
we also derive the necessary condition of the optimal threshold energy-eﬃcient policy.
Theorem 8 For the threshold energy-eﬃcient policies of the data center, the optimal
threshold policy d∗
θ satisﬁes the following condition
G(dθ∗−1) (n, θ∗−1) + c ≤0,
G(dθ∗) (n, θ∗) + c ≥0,
G(dθ∗+1) (n, θ∗+ 1) + c ≥0.
Proof: We consider three threshold energy-eﬃcient policies with an interrelated struc-
ture as follows.
dθ∗=

0, 0, . . . , 0; 0, 0, . . . , 0
|
{z
},
θ∗−1 zeros
θ∗, θ∗+ 1, . . . , m

,
dθ∗+1 =

0, 0, . . . , 0; 0, 0, . . . , 0
|
{z
},
θ∗−1 zeros
0, θ∗+ 1, . . . , m

,
dθ∗−1 =

0, 0, . . . , 0; 0, 0, . . . , 0
|
{z
},
θ∗−2 zeros
θ∗−1, θ∗, . . . , m

.
42

---

## Page 43

It follows from Lemma 1 that for two energy-eﬃcient policies with an interrelated structure
d =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, dn,j,dn,j+1, . . . , dn,m

,
d′ =

0, 0, . . . , 0; dn,1, . . . , dn,j−1, d′
n,j,dn,j+1, . . . , dn,m

,
it is clear that
ηd′ −ηd = µ2π(d′)  d′
n,j −dn,j
 h
G(d) (n, j) + c
i
.
Thus, we obtain
ηdθ∗+1 −ηdθ∗= −θ∗µ2π(dθ∗+1) h
G(dθ∗) (n, θ∗) + c
i
,
which, together with ηdθ∗+1 −ηdθ∗≤0, leads to
G(dθ∗) (n, θ∗) + c ≥0.
Similarly, we have
ηdθ∗−ηdθ∗+1 = θ∗µ2π(dθ∗) h
G(dθ∗+1) (n, θ∗+ 1) + c
i
,
which indicates
G(dθ∗+1) (n, θ∗+ 1) + c ≥0.
Also, we have
ηdθ∗−ηdθ∗−1 = −(θ∗−1) µ2π(dθ∗) h
G(dθ∗−1) (n, θ∗−1) + c
i
,
which indicates
G(dθ∗−1) (n, θ∗−1) + c ≤0.
This completes the proof.
8
Conclusion
In this paper, we propose a novel dynamic decision method by applying the sensitivity-
based optimization theory to study the optimal energy-eﬃcient policy of a data center with
two groups of heterogeneous servers. We propose a job transfer rule among the group-
servers such that the sleep energy-eﬃcient mechanism of Group 2 becomes more eﬀective.
To ﬁnd the optimal energy-eﬃcient policy of the data center, we set up a policy-based
43

---

## Page 44

Poisson equation and provide explicit expression for its unique solution by means of the
RG-factorization. Based on this, we derive the monotonicity and optimality of the long-run
average proﬁt with respect to the energy-eﬃcient policies under some restrained service
prices. We prove the optimality of the bang-bang control, which signiﬁcantly reduces the
action search space. We also study the threshold energy-eﬃcient policy and derive the
necessary condition of the optimal threshold policy. Diﬀerent from previous works in the
literature on applying the traditional MDP theory to the dynamic control of data centers,
the sensitivity-based optimization method used in this paper is easier and more convenient
in the study of energy-eﬃcient data centers. This sensitivity-based optimization method
may open a new avenue to study the optimal energy-eﬃcient policy for more complicated
data centers.
Along such a research line of applying the sensitivity-based optimization and the RG-
factorization to the energy-eﬃcient data centers, the extension to multiple groups of het-
erogeneous servers deserves further investigations. The control policy will become more
complicated when multiple groups of servers are considered. Another interesting research
topic is to consider diﬀerent cost structures, waiting capacities, service disciplines, or job
migration rules. Especially, when the job migration is not allowed in data centers, the com-
plexity of the dynamic control problem will dramatically increase and it deserves further
more investigations.
Acknowledgements
Li Xia was supported by the National Key Research and Development Program of
China (2016YFB0901900, 2017YFC0704100), the National Natural Science Foundation
of China under grant No. 61573206 and No. U1301254, the National 111 International
Collaboration Project (B06002), and the Suzhou-Tsinghua Innovation Leading Action
Project.
Quan-Lin Li was supported by the National Natural Science Foundation of China
under grant No. 71671158 and No. 71471160, and by the Natural Science Foundation of
Hebei province under grant No. G2017203277.
44

---

## Page 45

References
[1] Barroso, L. A., H¨olzle, U. (2007). The case for energy-proportional computing. Com-
puter, Vol. 40, No. 12, 33–37.
[2] Benini, L., Bogliolo, A., De Micheli, G. (2000). A survey of design techniques for
system-level dynamic power management. IEEE Transactions on Very Large Scale
Integration (VLSI) Systems, Vol. 8, No. 3, 299–316.
[3] Becker, R., Zilberstein, S., Lesser, V. (2004). Decentralized Markov decision processes
with event-driven interactions. In: Proceedings of the Third International Joint Con-
ference on Autonomous Agents and Multiagent Systems, Vol. 1, 302–309.
[4] Bodenstein, C., Schryen, G., Neumann, D. (2012). Energy-aware workload manage-
ment models for operation cost reduction in data centers. European Journal of Oper-
ational Research, Vol. 222, No. 1, 157–167.
[5] Cao, X. R. (2007). Stochastic learning and optimization—A sensitivity-based approach.
New York: Springer.
[6] Chen, X., Wardi, Y., Yalamanchili, S. (2018). Instruction-throughput regulation in
computer processors with data-center applications. Discrete Event Dynamic Systems:
Theory and Applications, Vol. 28, No. 1, 127–158.
[7] De Napoli, C., Forestiero, A., Lagana, D., Lupi, G., Mastroianni, C., Spataro, L.
(2016). Business Scenarios for Geographically Distributed Data Centers. RT-ICAR-
CS-16-03.
[8] Engel, Y., Etzion, O. (2011). Towards proactive event-driven computing. In: Proceed-
ings of the 5th ACM International Conference on Distributed Event-Based System, pp.
125–136.
[9] Gandhi, A. (2013). Dynamic Server Provisioning for Data Center Power Management.
Ph.D. Thesis, School of Computer Science, Carnegie Mellon University, Pittsburgh,
USA.
[10] Gandhi, A., Doroudi, S., Harchol-Balter, M., Scheller-Wolf, A. (2014). Exact analysis
of the M/M/k/setup class of Markov chains via recursive renewal reward. Queueing
Systems, Vol. 77, No, 2, 177–209.
45

---

## Page 46

[11] Gandhi, A., Gupta, V., Harchol-Balter, M., Kozuch, M. A. (2010). Optimality anal-
ysis of energy-performance trade-oﬀfor server farm management. Performance Eval-
uation, Vol. 67, No, 11, 1155–1171.
[12] Gandhi, A., Harchol-Balter, M. (2013). M/G/k with staggered setup. Operations
Research Letters, Vol. 41, No. 4, 317–320.
[13] Gandhi, A., Harchol-Balter, M., Adan, I. (2010). Server farms with setup costs. Per-
formance Evaluation, Vol. 67, No. 11, 1123–1138.
[14] Gandhi, A., Harchol-Balter, M., Kozuch, M. A. (2012). Are sleep states eﬀective in
data centers? In: 2012 International Green Computing Conference (IGCC), pp. 1–10.
[15] Gebrehiwot, M. E., Aalto, S., Lassila, P. (2016). Optimal energy-aware control policies
for FIFO servers. Performance Evaluation, Vol. 103, 41–59.
[16] Gebrehiwot, M. E., Aalto, S., Lassila, P. (2016). Energy-performance trade-oﬀfor
processor sharing queues with setup delay. Operations Research Letters, Vol. 44, No.
1, 101–106.
[17] Gebrehiwot, M. E., Aalto, S., Lassila, P. (2017). Energy-aware SRPT server with
batch arrivals: Analysis and optimization. Performance Evaluation, Vol. 115, 92–107.
[18] Hassin, R., Shaki, Y. Y., Yovel, U. (2015). Optimal service-capacity allocation in a
loss system. Naval Research Logistics, Vol. 62, No. 2, 81–97.
[19] Hipp, S. K., Holzbaur, U. D. (1988). Decision processes with monotone hysteretic
policies. Operations Research, Vol. 36, No. 4, 585–588.
[20] Huang, L., Neely, M. J. (2013). Utility optimal scheduling in energy-harvesting net-
works. IEEE/ACM Transactions on Networking, Vol. 21, No. 4, 1117–1130.
[21] Hong, K. S., Lee, C. (2013). Integrated pricing and capacity decision for a telecommu-
nication service provider. Multimedia Tools and Applications, Vol. 64, No. 2, 389–406.
[22] Hunter, J. J. (1982). Generalized inverses and their application to applied probability
problems. Linear Algebra and its Applications, Vol. 45, 157–198.
46

---

## Page 47

[23] Kamitsos, I., Andrew, L., Kim, H., Chiang, M. (2010). Optimal sleep patterns for
serving delay-tolerant jobs. In: Poceedings of the 1st International Conference on
Energy-Eﬃcient Computing and Networking, pp. 31–40.
[24] Kamitsos, I., Andrew, L., Kim, H., Ha, S. (2012). Better energy-delay tradeoﬀvia
server resource pooling. In: The 2012 International Conference on Computing, Net-
working and Communications, pp. 611–616.
[25] Kamitsos, I., Ha, S., Andrew, L., Bawa, J., Butnariu, D., Kim, H., Chiang, M. (2017).
Optimal sleeping: models and experiments for energy-delay tradeoﬀ. International
Journal of Systems Science: Operations & Logistics, Vol. 4, No. 4, 356–371.
[26] Kliazovich, D., Bouvry, P., Khan, S. U. (2012). GreenCloud: a packet-level simulator
of energy-aware cloud computing data centers. The Journal of Supercomputing, Vol.
62, No. 3, 1263–1283.
[27] Koole, G. (1998). Structural results for the control of queueing systems using event-
based dynamic programming. Queueing Systems, Vol. 30, No. 3–4, 323–339.
[28] Kuehn, P. J., Mashaly, M. E. (2015). Automatic energy eﬃciency management of
data center resources by load-dependent server activation and sleep modes. Ad Hoc
Networks, Vol. 25, Part B, 497–504.
[29] Li, Q. L. (2010). Constructive computation in stochastic models with applications: the
RG-factorizations. Springer.
[30] Li, Q. L., Cao, J. (2004). Two types of RG-factorizations of quasi-birth-and-death
processes and their applications to stochastic integral functionals. Stochastic Models,
Vol. 20, No. 3, 299–340.
[31] Li, Q. L., Ma, J. Y., Xie, M. Z., Xia, L. (2017). Group-server queues. In: International
Conference on Queueing Theory and Network Applications, pp. 49–72.
[32] Lu, F. V., Serfozo, R. F. (1984). M/M/1 queueing decision processes with monotone
hysteretic optimal policies. Operations Research, Vol. 32, No. 5, 1116–1132.
[33] Maccio, V. J., Down, D. G. (2015). On optimal policies for energy-aware servers.
Performance Evaluation, Vol. 90, 36–52.
47

---

## Page 48

[34] Mazzucco, M., Dyachuk, D., Deters, R. (2010). Maximizing cloud providers revenues
via energy aware allocation policies. In: IEEE International Conference on Cloud
Computing, pp. 131–138.
[35] Mitrani, I. (2011). Service center trade-oﬀs between customer impatience and power
consumption. Performance Evaluation, Vol. 68, No. 11, 1222–1231.
[36] Mitrani, I. (2013). Managing performance and power consumption in a server farm.
Annals of Operations Research, Vol. 202, No. 1, 121–134.
[37] Natural Resources Defense Council. (2016). Environmental Issues [Online]. Avail-
able: https://www.nrdc.org/resources/americas-data-centers-consuming-and-wasting-
growing-amounts-energy.
[38] Phung-Duc, T. (2017). Exact solutions for M/M/c/setup queues. Telecommunication
Systems, Vol. 64, No. 2, 309–324.
[39] Puterman, M. L. (2014). Markov decision processes: discrete stochastic dynamic pro-
gramming. John Wiley & Sons.
[40] Qiu, Q., Pedram, M. (1999). Dynamic power management based on continuous-time
Markov decision processes. In: Proceedings of the 36th Annual ACM/IEEE Design
Automation Conference, pp. 555–561.
[41] Qiu, Q., Qu, Q., Pedram, M. (2001). Stochastic modeling of a power-managed system-
construction and optimization. IEEE Transactions on Computer-Aided Design of In-
tegrated Circuits and Systems, Vol. 20, No. 10, 1200–1217.
[42] Schwartz, C., Pries, R., Tran-Gia, P. (2012). A queuing analysis of an energy-saving
mechanism in data centers. In: The International Conference on Information Network
(ICOIN), pp. 70–75.
[43] Shehabi, A., Smith, S., Sartor, D., et al. (2016). United States Data Center Energy
Usage Report. Lawrence Berkely Lab.
[44] ˇSimuni´c, T., Benini, L., Glynn, P., De Micheli, G. (2001). Event-driven power man-
agement. IEEE Transactions on Computer-Aided Design of Integrated Circuits and
Systems, Vol. 20, No. 7, 840–857.
48

---

## Page 49

[45] Tan, Y., Lu, Y., Xia, C. H. (2012). Provisioning for large scale loss network sys-
tems with applications in cloud computing. ACM Sigmetrics Performance Evaluation
Review, Vol. 40, No. 3, 83–85.
[46] Xia, L. (2014). Service rate control of closed Jackson networks from game theoretic
perspective. European Journal of Operational Research, Vol. 237, No. 2, 546–554.
[47] Xia, L. (2014). Event-based optimization of admission control in open queueing net-
works. Discrete Event Dynamic Systems: Theory and Applications, Vol. 24, No. 2,
133–151.
[48] Xia, L., Cao, X. R. (2012). Performance optimization of queueing systems with per-
turbation realization. European Journal of Operational Research, Vol. 218, No. 2, 293–
304.
[49] Xia, L., Chen, S. (2018). Dynamic pricing control for open queueing networks. IEEE
Transactions on Automatic Control, Online Publication, Pages 1–11.
[50] Xia, L., He, Q. M., Alfa, A. S. (2017). Optimal control of state-dependent service
rates in a MAP/M/1 queue. IEEE Transactions on Automatic Control, Vol. 62, No.
10, 4965–4979.
[51] Xia, L., Jia, Q. S. (2015). Parameterized Markov decision process and its application
to service rate control. Automatica, Vol. 54, 29–35.
[52] Xia, L., Jia, Q. S., Cao, X. R. (2014). A tutorial on event-based optimization——A
new optimization framework. Discrete Event Dynamic Systems: Theory and Applica-
tions, Vol. 24, No. 2, 103–132.
[53] Xia, L., Miller, D., Zhou, Z., Bambos, N. (2017). Service rate control of tandem
queues with power constraints. IEEE Transactions on Automatic Control, Vol. 62, No.
10, 5111–5123.
[54] Xia, L., Shihada, B. (2013). Max-min optimality of service rate control in closed
queueing networks. IEEE Transactions on Automatic Control, Vol. 58, No. 4, 1051–
1056.
49

---

## Page 50

[55] Xia, L., Shihada, B. (2015). A Jackson network model and threshold policy for joint
optimization of energy and delay in multi-hop wireless networks. European Journal of
Operational Research, Vol. 242, No. 3, 778–787.
[56] Yang, J., Zhang, S., Wu, X., Ran, Y., Xi, H. (2017). Online learning-based server
provisioning for electricity cost reduction in data center. IEEE Transactions on Control
Systems Technology, Vol. 25, No. 3, 1044–1051.
[57] Yao, Y., Huang, L., Sharma, A. B., Golubchik, L., Neely, M. J. (2014). Power cost
reduction in distributed data centers: A two-time-scale approach for delay tolerant
workloads. IEEE Transactions on Parallel and Distributed Systems, Vol. 25, No. 1,
200–211.
50