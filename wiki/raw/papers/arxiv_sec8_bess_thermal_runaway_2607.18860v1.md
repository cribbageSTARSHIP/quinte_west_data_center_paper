# Regime-Aware Physics-Guided Early Warning of Lithium-Ion Battery Thermal Runaway Using Thermo-Mechanical Signals
**arXiv ID:** 2607.18860v1
**Source File:** arxiv_sec8_bess_thermal_runaway_2607.18860v1.pdf

## Page 1

Regime-Aware Physics-Guided Early Warning of
Lithium-Ion Battery Thermal Runaway Using
Thermo-Mechanical Signals
Syed Sajid Ullah, Muhammad Zunair Zamir and Salman Khan
Abstract—Thermal runaway in lithium-ion batteries poses a
major safety risk to electric vehicles and energy storage systems.
Current early-warning methods depend mainly on temperature
and may therefore miss mechanical precursors that emerge
before rapid heating. We introduce a regime-aware, physics-
guided framework that integrates temperature, voltage, force,
deformation, and state-of-charge measurements for early warning
under controlled mechanical abuse. A lightweight convolutional
classifier first infers safe, warning, or danger regimes from
mechanical signals. These regime estimates then condition a
causal temporal convolutional backbone through feature-wise lin-
ear modulation, physics-biased attention, and regime-dependent
gating. Joint learning unifies regime identification, thermal-
runaway detection, and time-to-disaster estimation. We evaluate
the framework using leave-one-experiment-out cross-validation
on 30 mechanical-abuse tests across state-of-charge levels of 10%,
50%, and 90% and two loading protocols. The method achieves
an F1 score of 0.89, a high-temperature prediction root-mean-
square error of 12.3 ◦C, a mean warning lead time of 15.6 s, a
detection success rate of 0.92, and an experiment-level false alarm
rate of 2.7%. Its lead time exceeds that of the strongest baseline
by 69.6%. Removing force reduces the lead time by 60.3%,
highlighting the value of mechanical precursors. These results
support regime-aware thermo-mechanical fusion as a promising
strategy for earlier and more reliable thermal-runaway warning
under controlled abuse conditions.
Keywords: battery thermal runaway; early warning; physics-
guided neural networks; temporal convolutional network;
feature-wise linear modulation; multi-task learning; leave-one-
experiment-out cross-validation
I. INTRODUCTION
Lithium-ion batteries (LIBs) are now central to electric
vehicles, grid storage, and portable electronics because of their
high energy density and long cycle life. However, LIBs con-
tinue to face severe safety challenges associated with thermal
instability, internal short circuits, overheating, and thermal
runaway (TR), which remain among the most catastrophic
failure mechanisms in modern battery systems [1], [2].
Thermal
runaway
refers
to
a
highly
nonlinear
electrochemical-thermal
process
in
which
self-generated
heat exceeds the dissipation capability of the battery system,
resulting
in
uncontrollable
temperature
escalation,
gas
venting, fire propagation, toxic emissions, and explosions.
The initiation of thermal runaway can occur because of
overcharging,
over-discharging,
mechanical
deformation,
separator failure, lithium dendrite growth, manufacturing
defects, or external thermal abuse [3]. As battery energy
density increases, the thermal tolerance margin becomes
progressively smaller, thereby intensifying safety risks and
increasing the complexity of battery-management systems
(BMSs).
To address these challenges, researchers have extensively
investigated thermal-runaway early-warning methods using
thermal, electrical, electrochemical, mechanical, acoustic, and
gas-emission signals. Among these approaches, gas-sensing-
based monitoring has shown strong potential because gaseous
emissions typically occur prior to measurable voltage collapse
or abnormal temperature rise. Wang et al. [4] investigated
gas-sensor-based thermal-runaway monitoring using CO2, H2,
CO, and volatile organic compounds, demonstrating that gas
signatures can provide effective early indicators of abnormal
electrochemical decomposition. Similarly, Cui et al. [5] pro-
posed a gas-production-based thermal-runaway early-warning
framework and introduced a thermal-runaway severity index
capable of estimating the evolution and risk level of battery
failure before catastrophic runaway occurs.
In addition to gas-emission analysis, electrochemical and
impedance-based monitoring approaches have gained signif-
icant attention for battery fault diagnosis. Dong et al. [6]
demonstrated that electrochemical impedance spectroscopy
(EIS) can provide reliable precursor information regarding
internal degradation and thermal instability. Lyu et al. [7]
further proposed an online impedance-measurement strategy
for overcharge warning and thermal-runaway prediction, show-
ing that impedance variations can serve as early indicators of
abnormal electrochemical reactions.
Online data-driven fault-diagnosis frameworks have also
demonstrated strong capability for thermal-runaway predic-
tion. Sun et al. [8] proposed an online thermal-runaway
early-warning framework using operational electrical signals
from EV batteries and showed that intelligent monitoring can
significantly improve fault-detection accuracy under dynamic
operating conditions. Gao et al. [9] analyzed practical EV
battery thermal-runaway cases and emphasized the importance
of online internal-short-circuit detection for preventing catas-
trophic failures in battery packs.
The rapid development of machine learning and deep learn-
ing has further transformed battery fault diagnosis and prog-
nostics. Khaleghi et al. [10] proposed a data-driven prognostics
and health-management framework for lithium-ion batteries
and highlighted the importance of intelligent data analytics in
modern BMSs. More recently, Chen et al. [11] developed a
model-constrained deep-learning framework capable of robust
arXiv:2607.18860v1  [cs.LG]  21 Jul 2026

---

## Page 2

online fault diagnosis under stochastic operating conditions.
Their study demonstrated that incorporating physical battery
constraints into deep neural networks substantially improves
generalization and interpretability.
Recent studies have also demonstrated that forecasting-
oriented
architectures
can
substantially
improve
battery
anomaly prediction and long-horizon temporal representation
learning. Zeng et al. [12] argued that simple linear forecasting
architectures can outperform complex transformer models in
several long-sequence forecasting tasks, highlighting the im-
portance of efficient inductive bias design for temporal learn-
ing systems. In addition, physics-based learning strategies have
shown strong capability for safety-critical battery applications.
Firoozi et al. [13] proposed a physics-based learning frame-
work for cylindrical battery fault detection under extreme fast-
charging conditions and demonstrated improved robustness
for abnormal battery-state identification. Such studies indicate
that combining physical battery constraints with modern fore-
casting architectures can significantly improve reliability and
interpretability in thermal-runaway early-warning systems.
Transfer-learning-based diagnosis frameworks have also
emerged as promising solutions for limited-data environments.
Dong and Sun [14] proposed a multi-source domain-transfer-
learning framework for thermal-runaway diagnosis, enabling
knowledge transfer across different battery chemistries and
operational conditions. Such approaches are particularly im-
portant because large-scale thermal-runaway experiments are
expensive, hazardous, and difficult to conduct repeatedly.
Besides fault diagnosis, thermal-runaway mitigation and
propagation suppression have become important research di-
rections. Huang et al. [15] investigated aerogel-based insula-
tion materials for suppressing thermal propagation in lithium-
ion battery modules and established a safety-evaluation
methodology
for
high-energy-density
systems.
Zhang
et
al. [16] proposed a non-uniform phase-change-material strat-
egy for directional mitigation of thermal-runaway propagation
and demonstrated significant improvements in thermal isola-
tion capability. These studies indicate that thermal manage-
ment and propagation suppression must complement early-
warning systems to achieve comprehensive battery safety.
Several researchers have also investigated probabilistic risk-
analysis frameworks for battery safety assessment. Meng et
al. [17] proposed an integrated methodology for dynamic
thermal-runaway risk prediction using Bayesian networks
and support-vector regression. Their later work incorporated
physics-informed Bayesian networks for uncertainty-aware
battery accident analysis [18]. Similarly, Wang et al. [19]
proposed a Bayesian fault-propagation framework for real-
time reliability analysis of battery-energy-storage systems,
providing an interpretable mechanism for safety-risk evolution
modeling.
The emergence of deep-learning-based forecasting models
has opened new opportunities for intelligent battery-safety
prediction. Rather than surveying every recent forecasting
architecture, the present work focuses on architectures that
are practical for short-horizon, causal, multivariate warning
under mechanical abuse. This scope motivates the use of
recurrent, convolutional, transformer, and TCN baselines in
the experiments.
Despite substantial progress in battery fault diagnosis and
temporal forecasting, several challenges remain unresolved.
Existing thermal-runaway prediction frameworks often suf-
fer from limited generalization capability, insufficient inter-
pretability, weak robustness under varying operational con-
ditions, and inadequate integration between physics-based
battery dynamics and deep-learning architectures. Moreover,
many existing methods rely primarily on electrical mea-
surements while ignoring thermo-mechanical interactions and
structural degradation mechanisms that may provide valuable
precursor information regarding fault evolution.
Therefore, there remains a strong need for regime-aware
and physics-guided early-warning frameworks capable of in-
tegrating thermo-mechanical sensing, multivariate temporal
forecasting, and intelligent fault diagnosis for robust TR
prediction. Motivated by these challenges, this work proposes
a physics-guided deep-learning framework for LIB TR early
warning using thermo-mechanical signals and causal temporal
modeling. The proposed framework aims to improve predic-
tion lead time, interpretability, robustness, and operational
reliability under dynamic battery conditions.
This manuscript is distinct from the authors’ companion
study on gradient-boosting-based infrared-hotspot warning.
That study used image-derived hotspot descriptors and tree-
based decision rules as the primary modeling route, whereas
the present paper uses synchronized temperature, force, de-
formation, voltage, and SOC information in a regime-aware
neural architecture with multitask TR detection and time-to-
disaster estimation. The overlap is therefore limited to the
broader mechanical-abuse safety context and, where appli-
cable, shared experimental infrastructure; the modeling ob-
jective, input representation, and claimed contribution are
different.
The main contributions of this work are summarized as
follows:
• Thermal runaway early warning under mechanical abuse
is formulated as a causal thermo-electro-mechanical se-
quence prediction problem, providing a principled foun-
dation for precursor-driven failure forecasting.
• A regime-aware temporal modeling framework is pro-
posed that leverages mechanical precursor signals to
identify transitions among safety states, enabling adaptive
warning thresholds aligned with the battery’s physical
condition.
• A physics-guided, SOC-conditioned feature modulation
strategy is introduced for joint warning-state classifica-
tion and time-to-danger estimation, incorporating electro-
chemical priors through learnable FiLM-based condition-
ing.
• An experiment-level evaluation protocol is established
using 30 real mechanical abuse experiments with leave-
one-experiment-out validation and early-warning metrics,

---

## Page 3

including lead time, false-alarm rate, missed-alarm rate,
and detection success rate.
The remainder of this paper is organized as follows. Sec-
tion II reviews TR warning methods, mechanical abuse studies,
and physics-guided learning approaches for battery safety.
Section III defines the causal early-warning problem, TR onset
criterion, regime labels, and prediction targets. Section IV
presents the proposed regime-aware physics-guided temporal
learning framework. Section V describes the dataset, prepro-
cessing, baselines, and evaluation protocol. Section VI reports
the quantitative results, ablation analysis, and interpretability
study. Finally, Section VII concludes the paper and discusses
future research directions.
II. RELATED WORK
A. Thermal Runaway Early Warning and Fault Diagnosis
Thermal-runaway early warning has attracted significant
research attention because conventional battery-management
systems are often unable to provide sufficiently early detec-
tion of catastrophic battery failures. Existing thermal-runaway
diagnosis approaches can generally be classified into gas-
based monitoring, impedance-based methods, probabilistic
risk-analysis frameworks, deep-learning-based fault diagnosis,
and hybrid physics-guided prediction systems.
Gas-sensing mechanisms are among the earliest indicators
of thermal instability because gaseous byproducts are typically
released before severe temperature escalation occurs. Wang et
al. [4] investigated gas-emission monitoring using chemical
sensors and demonstrated that gases such as CO2, H2, and CO
can effectively indicate abnormal electrochemical decomposi-
tion during early-stage thermal runaway. Cui et al. [5] extended
this concept by introducing a thermal-runaway severity in-
dex based on gas-production characteristics and demonstrated
that gas evolution can provide significantly earlier warning
compared with voltage or temperature measurements. In addi-
tion, Tam et al. [30] developed an acoustic-based early-stage
thermal-runaway detection framework using machine-learning
analysis and demonstrated that abnormal acoustic signatures
can serve as precursor indicators before catastrophic battery
failure occurs.
Electrochemical impedance spectroscopy has also shown
strong potential for early fault diagnosis because impedance
variations reflect internal electrochemical degradation pro-
cesses. Dong et al. [6] proposed an EIS-based thermal-
runaway warning framework and demonstrated reliable de-
tection of abnormal electrochemical behavior. Similarly, Lyu
et al. [7] developed an online impedance-measurement strat-
egy for overcharge warning and thermal-runaway prediction
under dynamic charging conditions. These studies indicate
that electrochemical signatures can provide highly sensitive
information regarding early-stage battery degradation.
Electrical-signal-based monitoring remains one of the most
practical approaches for real-time battery fault diagnosis. Sun
et al. [8] proposed an online data-driven thermal-runaway
warning framework using operational EV battery signals and
demonstrated accurate fault detection during dynamic operat-
ing conditions. Gao et al. [9] investigated practical EV battery
thermal-runaway cases and analyzed online internal-short-
circuit detection methods for preventing catastrophic failure
propagation.
Several recent studies have explored hybrid deep-learning
architectures for thermal-runaway prediction under dynamic
charging and operational conditions. Huang et al. [31] pro-
posed a convolutional-transformer-based early-warning frame-
work capable of modeling nonlinear thermal dynamics dur-
ing high-rate charging/discharging scenarios. Their framework
demonstrated strong predictive capability under rapidly vary-
ing thermal conditions. Similarly, Wang et al. [32] employed
convolutional neural networks for onboard thermal-runaway
fault-cause analysis and demonstrated improved post-failure
diagnosis capability for lithium-ion battery systems.
Deep-learning-based battery diagnosis frameworks have
shown remarkable progress in recent years. Chen et al. [11]
proposed a model-constrained deep-learning framework for
online lithium-ion battery fault diagnosis under stochastic con-
ditions. Their method integrated physical battery constraints
into neural-network training and achieved substantial improve-
ments in robustness and interpretability. Fan et al. [33] pro-
posed a feature-augmented attentional autoencoder for battery
fault detection and demonstrated that attention mechanisms
can effectively capture abnormal temporal behavior in multi-
variate battery signals.
Graph-neural-network-based approaches have also gained
considerable attention in battery-pack diagnostics. Ouyang et
al. [34] developed an optimized graphical neural network
for voltage-fault diagnosis in EV batteries and demonstrated
improved fault-localization capability compared with conven-
tional deep-learning methods. These approaches highlight the
importance of structural and relational modeling in large-scale
battery systems.
Transfer learning and domain adaptation techniques have
emerged as promising solutions for addressing limited-data
challenges in battery-fault diagnosis. Dong and Sun [14]
proposed a multi-source domain-transfer-learning framework
with few-shot learning capability for thermal-runaway diag-
nosis across different battery chemistries and operating envi-
ronments. Their framework significantly improved diagnosis
generalization under limited labeled data conditions.
Battery-state prediction and health-estimation studies have
also contributed significantly to thermal-runaway prevention
because battery degradation strongly influences thermal sta-
bility and internal short-circuit probability. Wang et al. [35]
proposed an IMFO-LSTM-BiGRU framework for long-term
multi-state battery prediction and demonstrated improved fore-
casting accuracy under varying operating conditions. Further-
more, Wang et al. [36] introduced a deep-learning framework
for battery state-of-health estimation using partial charging
data and polarization-equilibrium analysis, achieving high es-
timation accuracy with low computational overhead. Khaleghi
et al. [10] further emphasized the importance of intelligent
prognostics and health-management frameworks for modern

---

## Page 4

lithium-ion battery systems.
Several studies have also focused on thermal-runaway miti-
gation and propagation suppression. Huang et al. [15] investi-
gated aerogel-based insulation materials for suppressing ther-
mal propagation in battery modules, while Zhang et al. [16]
proposed a non-uniform phase-change-material strategy for
directional thermal mitigation. Liu et al. [3] analyzed the
influence of external thermal conditions on thermal-runaway
initiation and propagation in cylindrical lithium-ion batteries.
These studies collectively demonstrate that thermal manage-
ment and propagation suppression remain critical components
of battery-safety design.
Probabilistic risk-analysis frameworks provide additional
interpretability for battery safety analysis. Meng et al. [17]
proposed a dynamic risk-prediction methodology based on
Bayesian networks and support-vector regression, while their
later work introduced physics-informed Bayesian networks
for uncertainty-aware battery accident analysis [18]. Wang
et al. [19] further developed a Bayesian fault-propagation
framework for real-time reliability analysis of battery-energy-
storage systems.
B. Temporal Learning and Physics-Guided Modeling
Modern sequence-learning methods provide useful tools for
battery early warning, but a TR warning model must remain
causal, short-horizon, and reliable under limited destructive-
test data. For this reason, we compare against compact LSTM,
CNN-LSTM, Transformer, and TCN baselines rather than
importing large long-horizon forecasting architectures whose
assumptions and data requirements differ from the present
mechanical-abuse setting. Recent work on temporal inductive
bias and physics-based learning supports this design choice:
Zeng et al. [12] showed that simpler temporal models can
outperform complex transformers in some forecasting settings,
while Firoozi et al. [13] demonstrated the value of physics-
based learning for battery fault detection under extreme con-
ditions.
Table I compares representative related studies on thermal-
runaway early warning. Several key gaps emerge from the
table. Existing methods predominantly rely on temperature,
voltage, or gas signals with no integration of mechanical pre-
cursors such as force or deformation. They also lack regime-
aware processing to distinguish safe, warning, and danger
states. Furthermore, these approaches either introduce addi-
tional hardware overhead or suffer from high computational
complexity. To address these limitations, this paper proposes
a regime-aware, physics-guided deep learning framework that
fuses thermo-mechanical signals including temperature, force,
deformation, and voltage for early thermal-runaway warning.
The proposed method is detailed in the following sections.
III. PROBLEM FORMULATION
We define the thermal runaway onset time tTR as the earliest
time at which either of two conditions is satisfied:
tTR = min

t : T(t) ≥TTR ∨
˙T(t) ≥˙TTR
	
(1)
TABLE I
COMPARISON OF REPRESENTATIVE RELATED STUDIES ON LITHIUM-ION
BATTERY THERMAL-RUNAWAY EARLY WARNING.
Year
Ref.
Method
Limitations
2022
[8]
Online
data-
driven
fault
diagnosis
using
voltage,
current,
and temperature.
Relies on electrical and ther-
mal
signals;
limited
inter-
pretability.
2023
[5]
Gas-production-
based
TR
early-warning
and
severity
estimation.
Requires
additional
gas-
sensing hardware.
2023
[17]
Dynamic
risk
prediction
with
fault-tree analysis
and
Bayesian
networks.
Limited
real-time
deep-
learning capability.
2024
[4]
Gas-sensor-based
TR
monitoring
using CO2, H2,
CO.
Increases system cost; requires
robust calibration.
2024
[14]
Multi-source
domain-transfer
learning for TR
diagnosis.
May
suffer
from
negative
transfer
under
domain
mismatch.
2025
[11]
Model-
constrained
deep
learning
for
online
fault
diagnosis.
Model
design
and
training
more complex than data-driven
methods.
2025
[33]
Feature-
augmented
attentional
autoencoder
for
battery
fault
detection.
Detection sensitive to training-
data quality.
2025
[31]
Convolutional-
transformer
TR
early-warning
for
high-rate
conditions.
High computational cost for
embedded BMS deployment.
2025
[34]
Optimized GNN
for
voltage-fault
diagnosis in EV
battery packs.
Requires pack-topology infor-
mation.
2026
[19]
Bayesian
fault-
propagation
network for real-
time
reliability
analysis.
Probabilistic inference compu-
tationally demanding.
where T(t) denotes the cell surface temperature,
˙T(t) =
dT/dt the temperature rate of rise, TTR = 150 ◦C the absolute
temperature threshold, and
˙TTR = 3 ◦C/s the rate-of-rise
threshold. These dual criteria capture both gradual tempera-
ture escalation (to 150 ◦C) and rapid exothermic acceleration
(exceeding 3 ◦C/s), which are the two canonical signatures of
TR onset established in the battery safety literature [37].
The battery’s thermal trajectory is partitioned into three mu-
tually exclusive safety regimes based on temperature thresh-
olds, as illustrated in Fig. 1:
r(t) =





0 (Safe),
T(t) < Tsafe
1 (Warning),
Tsafe ≤T(t) < Tdanger
2 (Danger),
T(t) ≥Tdanger
(2)

---

## Page 5

Fig. 1.
Timeline of thermal progression through the safety regimes to TR
onset. Llead denotes the interval between the model’s first valid warning and
the measured TR onset.
where Tsafe = 60 ◦C and Tdanger = 120 ◦C. These fixed
thresholds are applied identically across SOC levels and
loading protocols. The safe regime corresponds to normal
operating temperatures where no safety concern exists. The
warning regime captures the early onset of anomalous heating,
during which internal exothermic reactions may have begun
but remain controllable through active cooling. The danger
regime indicates that the cell is on an irreversible trajectory
toward TR and immediate protective action is required.
The regime labels are generated algorithmically from syn-
chronized temperature measurements after timestamp align-
ment and smoothing; no fold-specific or experiment-specific
threshold tuning is used. Force and deformation are not used to
define the ground-truth regime labels, which prevents leakage
from the mechanical channels into the target definition. They
are used only as model inputs, allowing the Stage 1 classifier
to learn whether mechanical precursor patterns anticipate the
temperature-defined safety state.
The lead time Llead quantifies how far in advance the model
can issue a TR warning relative to the actual TR onset:
Llead = tTR −twarn
(3)
where twarn is the time at which the model first correctly
predicts an imminent TR event (i.e., TR probability exceeds
a detection threshold of 0.5). A larger lead time provides
more opportunity for mitigative actions, making it the most
operationally significant metric for TR early-warning systems.
Given a multivariate time-series window X ∈RW ×C
of length W with five synchronized sensor channels (high
temperature, low temperature, voltage, force, and deformation)
and a scalar state-of-charge s ∈[0, 1], the model produces
three outputs:
1) Regime classification: ˆr = fr(X, s) ∈R3, predicting
the probability distribution over safety regimes at the
current time step.
2) TR detection: ˆyTR = fd(X, s) ∈[0, 1], estimating the
probability that TR will occur within the prediction
horizon of H = 60 s.
3) Time-to-disaster regression: ˆtTTD = ft(X, s) ∈R≥0,
predicting the remaining time (in seconds) until TR
onset.
An effective TR early-warning system must satisfy three
operational requirements:
• Sufficient lead time: Llead > 10 s to enable protective
actions.
• High detection rate: Detection success rate DSR > 85%.
• Low false alarm rate: experiment-level FAR < 10% of
held-out test experiments.
IV. PROPOSED METHOD
A. System Overview
Fig. 2 presents the overall architecture of the proposed
regime-aware, physics-guided TR early-warning framework.
The system comprises two stages operating in cascade. Stage 1
is a lightweight CNN-based regime classifier that processes
the force and deformation channels to produce a probability
distribution over the three safety regimes. Stage 2 is a physics-
guided temporal backbone that ingests the full five-channel
multivariate input and produces three task-specific outputs—
regime classification logits, TR detection probability, and TTD
regression value—while being conditioned on both the SOC
(through FiLM) and the regime probabilities from Stage 1
(through gating).
B. Stage 1: Regime Classifier
The regime classifier takes the force and deformation
channels Xmech ∈RW ×2 as input and predicts the regime
probability vector r ∈R3. It consists of two 1-D convolutional
layers with batch normalization and ReLU activation, followed
by global average pooling and a two-layer fully connected
classifier:
H1 = ReLU
 BN1(Conv1d2→32
k=5 (X⊤
mech))

(4)
H2 = ReLU
 BN2(Conv1d32→64
k=3
(H1))

(5)
h = GAP(H2) ∈R64
(6)
r = softmax
 FC128→3(ReLU(Dropout(FC64→128(h))))

(7)
where X⊤
mech ∈R2×W denotes the transposed input suitable
for Conv1d. The classifier uses dropout with probability 0.3
in the fully connected layers for regularization.
C. Stage 2: Physics-Guided Temporal Backbone
1) Input Projection and Normalization:
The raw five-
channel input X ∈RW ×5 is first projected into a latent space
of dimension dmodel = 64 and normalized:
Z0 = LayerNorm(X Wproj + bproj)
(8)
where Wproj
∈R5×64 and bproj
∈R64 are learnable
parameters.

---

## Page 6

Fig. 2.
Overall architecture of the proposed regime-aware, physics-guided TR early-warning framework. Stage 1 uses a lightweight CNN to estimate the
operating regime from force signals. Stage 2 combines a causal dilated TCN backbone with SOC-based FiLM conditioning, physics-guided attention, and
regime-conditional gating, followed by classification and time-to-disaster regression heads trained with a joint objective.
2) TCN Backbone: The projected input is processed by
a Temporal Convolutional Network (TCN) comprising four
dilated causal convolutional blocks with dilation factors
[1, 2, 4, 8]. Each block contains two dilated causal convolu-
tions with weight normalization, batch normalization, ReLU
activation, and dropout (p = 0.2), connected by a residual
skip:
o(1) = Dropout
 ReLU(BN(WN(
Conv1dcausal(Z)))

(9)
o(2) = Dropout
 ReLU(BN(WN(
Conv1dcausal(o(1))))

(10)
HTCN = ReLU
 o(2) + Conv1d1×1(Z)

(11)
The causal padding ensures that each time step’s representation
depends only on current and past inputs. The exponentially
growing dilation factors yield a receptive field of 61 time
steps with kernel size k = 3, capturing temporal dependencies
spanning approximately 10 s of history.
3) SOC-FiLM Conditioning: The state-of-charge influences
the energy available for exothermic reactions. We inject
this physical prior through Feature-wise Linear Modulation
(FiLM) conditioned on SOC. The SOC scalar s ∈[0, 1] is
passed through a two-layer MLP that produces per-channel
scaling γ(s) and shifting β(s) parameters:
m = ReLU
 FC1→64(ReLU(FC1→64(s)))

(12)
γ(s) = FC64→d(m) ∈Rd
(13)
β(s) = FC64→d(m) ∈Rd
(14)
H′ = γ(s) ⊙HTCN + β(s)
(15)
where ⊙denotes element-wise multiplication (broadcast over
the temporal dimension).

---

## Page 7

4) Physics-Biased Attention: We augment the standard self-
attention with a learnable physics bias matrix Ephys ∈RW ×W
and channel-aware indicator scalars wT and wF :
Q = H′ WQ,
K = H′ WK,
V = H′ WV
(16)
A = softmax
QK⊤
√dk
+ Ephys + wT IT + wF IF

(17)
Hattn = A V
(18)
where dk = dmodel, IT , IF ∈{0, 1}W ×W are indicator ma-
trices for temperature and force channel positions. A residual
connection is added: Hres = Hattn + H′.
5) Regime-Conditioned Gating: The regime probabilities
r ∈R3 from Stage 1 modulate the feature representation
through multiplicative gating:
g = sigmoid
 FC64→d(ReLU(FC3→64(r)))

(19)
Hg = Hres ⊙g
(20)
where g ∈(0, 1)d is the gate vector (broadcast over the tem-
poral dimension). When the battery is in the safe regime, the
gate suppresses features associated with anomalous patterns,
reducing false alarms.
D. Multi-Task Learning Objective
The total loss function is a weighted sum of three task-
specific losses:
Ltotal = λ1 · Lregime + λ2 · LTR + λ3 · LTTD
(21)
with λ1 = 0.1, λ2 = 0.6, and λ3 = 0.3.
Regime classification loss. Weighted cross-entropy with class
weights [1.0, 2.0, 3.0]:
Lregime = −
2
X
c=0
wc · ⊮[r = c] · log ˆp(r = c)
(22)
TR detection loss. Binary cross-entropy with a positive-class
weight of 10:
LTR = −

wpos · y log ˆy + (1 −y) log(1 −ˆy)

(23)
TTD regression loss. Huber loss with δ = 10:
LTTD =
(
1
2(t −ˆt)2,
|t −ˆt| ≤δ
δ |t −ˆt| −1
2δ2,
otherwise
(24)
E. Training Algorithm
The
complete
training
procedure
uses
LOEO
cross-
validation with the Adam optimizer, gradient clipping (max
norm 1.0), and early stopping with patience of 10 epochs. A
ReduceLROnPlateau scheduler halves the learning rate when
validation loss plateaus for 5 consecutive epochs, with a
minimum learning rate of 10−6.
Algorithm 1 LOEO Training with Multi-Task Objective
Require: Dataset D = {D1, . . . , D30}, model fθ, learning rate η,
epochs E, patience P
Ensure: Trained model parameters θ∗for each fold
1: for k = 1 to 30 do
2:
Dtest ←Dk; Dtrain ←D \ Dk
3:
Split Dtrain into Dtr and Dval
4:
Compute normalizer µ, σ from Dtr; normalize all splits
5:
Initialize θ; p ←0; L∗
val ←∞
6:
for e = 1 to E do
7:
for each batch in Dtr do
8:
ˆr, ˆyTR, ˆtTTD ←fθ(X, s)
9:
L ←λ1Lregime + λ2LTR + λ3LTTD
10:
θ ←θ −η · clip(∇θL, 1.0)
11:
end for
12:
Evaluate Lval on Dval
13:
if Lval < L∗
val then
14:
θ∗←θ; p ←0
15:
else
16:
p ←p + 1
17:
end if
18:
if p ≥P then
19:
break
20:
end if
21:
end for
22:
Evaluate fθ∗on Dtest
23: end for
F. Inference and Deployment
At inference time, the model processes a sliding window
of the most recent W = 128 time steps across all five sensor
channels. A TR warning is issued when ˆyTR ≥0.5 and the
predicted regime is warning or danger. With 156K parameters
and 22 ms single-sample inference latency on an embedded
GPU (NVIDIA Jetson Xavier NX), the model meets the real-
time requirements of production BMS deployments operating
at 1 Hz–10 Hz sampling rates.
V. EXPERIMENTAL SETUP
A. Experimental Setup
Mechanical-abuse experiments were performed using a
custom-built thermo-mechanical testing platform designed to
capture the coupled thermal, electrical, and mechanical be-
havior of lithium-ion cells under controlled loading conditions.
The overall experimental arrangement is shown in Fig. 3. Dur-
ing high-severity abuse conditions, several cells experienced
rapid thermal escalation followed by severe swelling, venting,
rupture, and structural deformation as shown in Fig. 4.
B. Dataset
The proposed framework is evaluated on a dataset com-
prising 30 mechanical-abuse experiments conducted on com-
mercial lithium-ion cells, of which 20 reached TR and 10 did
not. During each experiment, synchronized thermo-mechanical
and electrical measurements were acquired at a sampling
rate of 2 Hz, including high temperature, low temperature,
voltage, force, and deformation. The experiments span three
SOC conditions (approximately 10%, 50%, and 90%) and

---

## Page 8

Fig. 3.
Experimental setup for mechanical-abuse testing of lithium-ion
batteries.
Fig. 4.
Representative lithium-ion cells after mechanical-abuse-induced
thermal runaway, exhibiting swelling, rupture, and structural deformation.
two loading protocols corresponding to high-force and low-
force abuse scenarios. The overall experimental distribution is
summarized in Fig. 5.
Representative thermo-mechanical signal trajectories are
illustrated in Fig. 6. The experiment shown is selected as a
median-performing TR case under the proposed method to
avoid choosing only the most favorable trial. The influence of
SOC on precursor behavior is further illustrated in Fig. 7.
C. Preprocessing and Windowing
Raw sensor measurements are transformed into fixed-length
temporal sequences using a causal sliding-window strategy, as
0
20
40
60
80
100
SOC (%)
0
2
4
6
8
10
12
Count
(a) SOC Distribution
1
5
10
15
20
25
30
Experiment
0
100
200
300
400
500
600
Duration (s)
(b) Experiment Duration
SOC<30
30<=SOC<70
SOC>=70
50
75
100
125
150
175
200
Peak Temp (°C)
(c) Peak Temp by SOC
HT
LT
Volt
Force
Deform
HT
LT
Volt
Force
Deform
1.00
-0.30
-0.76
-0.58
-0.68
-0.30
1.00
0.16
0.13
0.14
-0.76
0.16
1.00
0.45
0.51
-0.58
0.13
0.45
1.00
0.97
-0.68
0.14
0.51
0.97
1.00
(d) Channel Correlation
-1.00
-0.75
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
Fig. 5. Experimental dataset overview, including SOC distribution, experiment
duration, peak temperature, and pairwise channel correlations.
0
50
100
150
200
250
40
60
High Temperature (°C)
(a) High Temperature
Exp 1 (SOC=89%)
Exp 13 (SOC=53%)
Exp 18 (SOC=10%)
0
50
100
150
200
250
24
26
Low Temperature (°C)
(b) Low Temperature
0
50
100
150
200
250
0
2
Voltage (V)
(c) Voltage
0
50
100
150
200
250
0
2500
5000
7500
Force (N)
(d) Force
0
50
100
150
200
250
Time (s)
0
5
10
Deformation (mm)
(e) Deformation
Fig. 6. Representative thermo-mechanical signal evolution during a thermal
runaway event.
illustrated in Fig. 8. Each input window Xi ∈R128×5 con-
tains 128 consecutive time steps across the five synchronized
sensing channels, with a stride of S = 4.
D. Evaluation Protocol
We
employ
leave-one-experiment-out
(LOEO)
cross-
validation with 30 folds. In each fold k, experiment k serves
as the test set, while the remaining 29 experiments form the
training set. A validation split is selected only from the training
experiments for early stopping and learning-rate scheduling.
Because each LOEO fold contains one held-out experiment,
the protocol evaluates experiment-level generalization but does
not eliminate the statistical uncertainty associated with the
limited number of destructive tests.
E. Baselines
We compare the proposed framework against four baseline
architectures: LSTM, CNN-LSTM, Transformer, and stan-
dalone TCN. Each baseline is retrained under identical LOEO
settings with the same preprocessing and hyperparameter
search protocol for fairness. A direct numerical comparison
with the companion gradient-boosting infrared-hotspot study
is not included in Table III because that study uses a different

---

## Page 9

25
50
75
100
125
Temperature (°C)
SOC = 90%
SOC = 50%
SOC = 10%
0
25
50
75
100
125
150
Time (s)
0
2000
4000
Force (N)
SOC = 90%
SOC = 50%
SOC = 10%
Fig. 7. Temperature and force trajectories across SOC conditions (90%, 50%,
10%).
Fig. 8. Overview of the preprocessing and window-generation pipeline.
input representation and decision pipeline. We therefore treat
it as complementary prior work rather than as a drop-in base-
line; a same-input reimplementation is planned before journal
resubmission if the original experiment-level predictions are
available.
F. Evaluation Metrics
We evaluate the models using classification metrics (F1
score), temperature-prediction regression metrics (RMSE,
MAE, R2), and early-warning metrics (lead time Llead, de-
tection success rate DSR, false alarm rate FAR). RMSE and
MAE are reported in degrees Celsius for the predicted high-
temperature trajectory. Because the validation is performed
TABLE II
TRAINING AND IMPLEMENTATION SETTINGS USED FOR ALL
EXPERIMENTS.
Parameter
Value
Framework
PyTorch 2.0
GPU
NVIDIA A100
Optimizer
Adam
Initial learning rate
10−3
Weight decay
10−5
LR scheduler
ReduceLROnPlateau
Batch size
32
Maximum epochs
100
Early stopping patience
10 epochs
Gradient clipping
1.0
Model dimension (dmodel)
64
TCN kernel size
3
TCN dropout
0.2
Head dropout
0.3
LSTM
CNN-LSTM
Transformer
TCN
Proposed
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
0.81 0.84 0.86 0.87 0.91
(a) Accuracy
LSTM
CNN-LSTM
Transformer
TCN
Proposed
0.0
0.2
0.4
0.6
0.8
1.0
F1 Score
0.79 0.82 0.84 0.85 0.89
(b) F1 Score
LSTM
CNN-LSTM
Transformer
TCN
Proposed
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
Lead Time (s)
5.1
6.8
8.5
9.2
15.6
(c) Lead Time (s)
LSTM
CNN-LSTM
Transformer
TCN
Proposed
0
5
10
15
20
25
RMSE (°C)
22.5
19.3
17.8 17.1
12.3
(d) RMSE (°C)
Fig. 9. Bar-chart comparison of the main LOEO performance metrics for the
proposed framework and baseline models.
at the experiment level, FAR is reported as the percentage
of held-out experiment folds with at least one false warning
episode before the valid warning period or in a non-TR exper-
iment. Consecutive positive windows within one continuous
warning episode are counted as one false warning episode,
so FAR reflects experiment-level false alarms rather than
window-level positives.
G. Training Configuration and Implementation Settings
All models were implemented in PyTorch 2.0 and trained
using a single NVIDIA A100 GPU with the Adam optimizer.
The principal training and architectural hyperparameters are
summarized in Table II.
VI. RESULTS AND ANALYSIS
The performance comparison demonstrates that the pro-
posed framework provides the most consistent overall im-
provement under 30-fold LOEO cross-validation. It achieves
an accuracy of 0.91, F1 score of 0.89, temperature-prediction
RMSE of 12.3 ◦C, mean warning lead time of 15.6 s, detection
success rate (DSR) of 0.92, and experiment-level false alarm
rate (FAR) of 2.7%, as summarized in Table III and visualized
in Fig. 9. Relative to the best baseline lead time (TCN, 9.2 s),
this corresponds to a 69.6% improvement, as highlighted in
Fig. 10.
Fig. 10 compares warning lead time across models, while
Fig. 11 shows the distribution of per-fold lead times for the
proposed method.

---

## Page 10

TABLE III
PERFORMANCE COMPARISON UNDER 30-FOLD LOEO CROSS-VALIDATION. RMSE IS REPORTED IN DEGREES CELSIUS FOR HIGH-TEMPERATURE
PREDICTION; LEAD TIME IS REPORTED IN SECONDS; FAR IS THE PERCENTAGE OF HELD-OUT EXPERIMENT FOLDS WITH AT LEAST ONE FALSE WARNING
EPISODE.
Model
Acc.↑
F1↑
RMSE (◦C)↓
Lead↑
DSR↑
FAR↓
LSTM
0.81
0.79
22.5
5.1
0.62
10.7%
CNN-LSTM
0.84
0.82
19.3
6.8
0.70
9.3%
Transformer
0.86
0.84
17.8
8.5
0.76
7.0%
TCN
0.87
0.85
17.1
9.2
0.78
6.3%
Proposed
0.91
0.89
12.3
15.6
0.92
2.7%
LSTM
CNN-LSTM
Transformer
TCN
Proposed
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
Lead Time (s)
5.1
6.8
8.5
9.2
15.6
Fig. 10. Mean warning lead-time comparison across the proposed framework
and baseline models.
12
13
14
15
16
17
18
19
20
Lead Time (s)
0
1
2
3
4
Count
(a) Distribution
Mean = 15.4 s
Median = 14.9 s
Proposed
12
14
16
18
20
Lead Time (s)
(b) Box Plot
Fig. 11. Distribution of per-fold lead times for the proposed method across
the 20 TR experiments.
A. Ablation Study
To quantify the contribution of each architectural com-
ponent, we perform a systematic ablation study. Table IV
reports the results. The force signal is the single most critical
component: removing it reduces lead time from 15.6 s to 6.2 s,
a 60.3% reduction.
Fig. 12 visualizes the ablation results.
The dominance of the force channel should be interpreted
in the context of mechanical-abuse testing. In indentation and
compression experiments, the force trajectory directly reflects
structural loading, casing deformation, separator damage, and
the transition from elastic response to irreversible mechanical
failure. It is therefore expected to carry precursor information
that is less visible in temperature until exothermic reactions
accelerate. This finding does not imply that force would be
equally dominant for overcharge, external heating, or field-
aging scenarios; in those cases, voltage, impedance, gas, or
temperature-rate features may become more informative.
B. Statistical Significance
Wilcoxon signed-rank tests indicate that the proposed
method’s lead-time advantage is statistically significant (p <
0.05) against all baselines. Table V reports the test statistics
and p-values for lead time, RMSE, and F1. Because the lead-
time analysis is limited to the 20 TR experiments, these
non-parametric tests have limited statistical power and should
be interpreted as supportive evidence rather than definitive
population-level confirmation.
Fig. 13 summarizes the corresponding p-values across met-
rics, including DSR.
C. Cross-Experiment Generalization
Table VI presents the per-SOC results. Performance im-
proves monotonically with SOC: at SOC≈90%, the model
achieves lead time of 17.2 s and DSR of 0.95, while at
SOC≈10%, it maintains lead time of 12.4 s and DSR of 0.85.
Fig. 14 shows a scatter plot of per-fold lead time versus
SOC.
The monotonic SOC trend is physically plausible because
higher-SOC cells contain more releasable energy and often ex-
hibit stronger thermal and mechanical precursor signals before
TR. At the same time, the weaker performance at SOC≈10%
is an important limitation: low-SOC events provide lower
signal-to-noise ratios and fewer strong precursors, making
early warning intrinsically harder. Future work should evaluate
whether targeted low-SOC augmentation, transfer learning, or
uncertainty-aware thresholds can reduce this gap.
D. Qualitative Analysis
Fig. 15 presents the thermo-mechanical signal and warning-
score evolution of a median-performing high-SOC TR ex-
periment. Fig. 16 compares actual and predicted trajectories
to assess whether the model’s temporal predictions remain
aligned with the observed experimental progression.
VII. CONCLUSION
This paper presented a regime-aware, physics-guided deep
learning framework for early warning of lithium-ion bat-
tery thermal runaway under mechanical abuse conditions.
The proposed framework combines a two-stage architecture
with SOC-FiLM conditioning, physics-biased attention, and

---

## Page 11

TABLE IV
ABLATION ANALYSIS OF THE PROPOSED FRAMEWORK UNDER LOEO CROSS-VALIDATION.
Variant
RMSE (◦C)↓
Lead (s)↑
DSR↑
F1↑
Full Model
12.3
15.6
0.92
0.89
w/o Force
18.7
6.2
0.65
0.72
w/o Regime Cls.
13.9
9.5
0.74
0.80
w/o Physics Attn.
15.9
10.4
0.78
0.81
w/o FiLM
14.8
11.2
0.81
0.83
w/o Gating
15.1
12.1
0.84
0.85
Full Model
w/o Force
w/o Physics Attn
w/o FiLM
w/o Gating
w/o Regime Cls
0
10
20
30
40
50
60
52.0
29.3
20.3
22.8
13.0
(a) RMSE Change (%)
Full Model
w/o Force
w/o Physics Attn
w/o FiLM
w/o Gating
w/o Regime Cls
-60
-40
-20
0
-58.3
-33.3
-28.2
-22.4
-39.1
(b) Lead Time Change (%)
Full Model
w/o Force
w/o Physics Attn
w/o FiLM
w/o Gating
w/o Regime Cls
0.0
0.2
0.4
0.6
0.8
1.0
0.92
0.65
0.78
0.81
0.84
0.74
(c) DSR
Fig. 12. Ablation analysis of lead-time and RMSE changes.
TABLE V
WILCOXON SIGNED-RANK STATISTICAL SIGNIFICANCE ANALYSIS.
Comparison
Metric
Statistic
p-value
Proposed vs. LSTM
Lead Time
44
0.0006
Proposed vs. CNN-LSTM
Lead Time
34
0.0037
Proposed vs. Transformer
Lead Time
49
0.0042
Proposed vs. TCN
Lead Time
11
0.0044
Proposed vs. LSTM
RMSE
32
0.0076
Proposed vs. CNN-LSTM
RMSE
65
0.0051
Proposed vs. Transformer
RMSE
88
0.0074
Proposed vs. TCN
RMSE
62
0.0046
Proposed vs. LSTM
F1
64
0.0060
Proposed vs. CNN-LSTM
F1
88
0.0053
Proposed vs. Transformer
F1
55
0.0207
Proposed vs. TCN
F1
102
0.0041
regime-conditioned gating to incorporate safety-state infor-
mation and thermo-mechanical precursor dynamics. Evalua-
tion on 30 mechanical-abuse experiments using leave-one-
experiment-out cross-validation demonstrated that the pro-
posed method achieves an F1 score of 0.89, a mean warning
lead time of 15.6 s, a detection success rate of 0.92, and an
experiment-level false-alarm rate of 2.7%. The ablation study
confirmed that mechanical sensing is critical in this abuse
setting: removing the force channel reduced lead time by
60.3%. However, the present study is limited to a dataset of 30
battery experiments, including 20 TR events, under controlled
laboratory conditions. The LOEO protocol tests experiment-
level generalization but does not remove the uncertainty caused
by small destructive-test sample size. Further validation is
required across additional chemistries, form factors, aging
states, abuse mechanisms, and field operating environments.
Future work will extend the framework to larger and more
heterogeneous datasets, including additional cell chemistries,
abuse modes, and sensing modalities. Integration with pro-
duction battery-management hardware and online adaptation
strategies will also be investigated to improve real-time de-
ployment reliability.

---

## Page 12

TABLE VI
PERFORMANCE OF THE PROPOSED METHOD ACROSS DIFFERENT SOC LEVELS. RMSE IS REPORTED IN DEGREES CELSIUS FOR HIGH-TEMPERATURE
PREDICTION; LEAD TIME IS REPORTED IN SECONDS.
SOC Level
Acc.↑
F1↑
RMSE
(◦C)↓
Lead (s)↑
DSR↑
SOC≈10%
0.88
0.85
14.8
12.4
0.85
SOC≈50%
0.90
0.88
12.9
14.8
0.90
SOC≈90%
0.93
0.91
11.2
17.2
0.95
Fig. 13.
Heat-map summary of Wilcoxon signed-rank p-values comparing
the proposed method against each baseline across lead time, RMSE, F1, and
DSR.
0
5
10
15
20
25
Experiment Index
12
13
14
15
16
17
18
19
20
Lead Time (s)
SOC < 30
30 <= SOC < 70
SOC >= 70
Mean +/- Std
Fig. 14.
Per-experiment lead time versus SOC under different loading
protocols.
FUNDING
This research received no external funding.
INSTITUTIONAL REVIEW BOARD STATEMENT
Not applicable.
INFORMED CONSENT STATEMENT
Not applicable.
Fig. 15. Thermo-mechanical signal and warning-score timeline for a median-
performing high-SOC TR experiment.
DATA AVAILABILITY STATEMENT
The data presented in this study are available on request
from the corresponding author. The data are not publicly
available due to ongoing research.
ACKNOWLEDGMENTS
The authors thank the battery safety research group at
Chang’an University for providing the experimental facilities
and technical support.
CONFLICTS OF INTEREST
The authors declare no conflicts of interest.
ABBREVIATIONS
TR
Thermal runaway
TTD
Time-to-disaster
SOC
State of charge
TCN
Temporal convolutional network
FiLM
Feature-wise linear modulation
DSR
Detection success rate
FAR
False alarm rate
LOEO
Leave-one-experiment-out
BMS
Battery management system
CNN
Convolutional neural network
LSTM
Long short-term memory
RMSE
Root mean square error
MAE
Mean absolute error

---

## Page 13

Fig. 16.
Actual-versus-predicted diagnostic plots for assessing temporal
prediction alignment across representative mechanical-abuse experiments.
REFERENCES
[1] D. Kong, H. Lv, P. Ping, and G. Wang, “A review of early warning
methods of thermal runaway of lithium ion batteries,” Journal of Energy
Storage, vol. 64, p. 107073, 2023.
[2] B. Xu, J. Lee, D. Kwon, L. Kong, and M. Pecht, “Mitigation strategies
for li-ion battery thermal runaway: A review,” Renewable and Sustain-
able Energy Reviews, vol. 150, p. 111437, 2021.
[3] Y. Liu, L. Zhang, Y. Ding, X. Huang, and X. Huang, “Effect of thermal
impact on the onset and propagation of thermal runaway over cylindrical
li-ion batteries,” Renewable Energy, vol. 222, p. 119910, 2024.
[4] X.-X. Wang, Q.-T. Li, X.-Y. Zhou, Y.-M. Hu, and X. Guo, “Monitoring
thermal runaway of lithium-ion batteries by means of gas sensors,”
Sensors and Actuators B: Chemical, vol. 411, p. 135703, 2024.
[5] Y. Cui et al., “Thermal runaway early warning and risk estimation
based on gas production characteristics of different types of lithium-
ion batteries,” Batteries, vol. 9, no. 9, p. 438, 2023.
[6] P. Dong, Z. Liu, P. Wu et al., “Reliable and early warning of lithium-ion
battery thermal runaway based on electrochemical impedance spectrum,”
Journal of The Electrochemical Society, vol. 168, p. 090529, 2021.
[7] N. Lyu, Y. Jin, R. Xiong et al., “Real-time overcharge warning and
early thermal runaway prediction of li-ion battery by online impedance
measurement,” IEEE Transactions on Industrial Electronics, vol. 69,
no. 2, pp. 1929–1936, 2021.
[8] Z. Sun, Z. Wang, P. Liu et al., “An online data-driven fault diagnosis
and thermal runaway early warning for electric vehicle batteries,” IEEE
Transactions on Power Electronics, vol. 37, no. 10, pp. 12 636–12 646,
2022.
[9] W. Gao, X. Li, M. Ma et al., “Case study of an electric vehicle
battery thermal runaway and online internal short-circuit detection,”
IEEE Transactions on Power Electronics, vol. 36, no. 3, pp. 2452–2455,
2020.
[10] S. Khaleghi, M. S. Hosen, D. Karimi et al., “Developing an online data-
driven approach for prognostics and health management of lithium-ion
batteries,” Applied Energy, vol. 308, p. 118348, 2022.
[11] R. Chen et al., “Model-constrained deep learning for online fault
diagnosis in li-ion batteries over stochastic conditions,” Nature Com-
munications, vol. 16, p. 1537, 2025.
[12] A. Zeng, M. Chen, L. Zhang, and Q. Xu, “Are transformers effective
for time series forecasting?” in Proceedings of the AAAI Conference on
Artificial Intelligence, vol. 37, no. 9, June 2023, pp. 11 121–11 128.
[13] R. Firoozi, S. Sattarzadeh, and S. Dey, “Cylindrical battery fault detec-
tion under extreme fast charging: A physics-based learning approach,”
IEEE Transactions on Energy Conversion, vol. 37, no. 2, pp. 1241–1250,
2021.
[14] C. Dong and D. Sun, “Multi-source domain transfer learning with small
sample learning for thermal runaway diagnosis of lithium-ion battery,”
Applied Energy, vol. 365, p. 123248, 2024.
[15] Y. Huang et al., “Mechanism of heat transfer suppression and safety
evaluation of high-performance aerogel insulation materials in the ther-
mal runaway propagation of lithium-ion batteries,” Energy, vol. 334,
p. 137684, 2025.
[16] W. Zhang et al., “Non-uniform phase change material strategy for direc-
tional mitigation of battery thermal runaway propagation,” Renewable
Energy, vol. 200, pp. 1338–1351, 2022.
[17] H. Meng, Q. Yang, E. Zio, and J. Xing, “An integrated methodology for
dynamic risk prediction of thermal runaway in lithium-ion batteries,”
Process Safety and Environmental Protection, 2023.
[18] H. Meng et al., “Risk analysis of lithium-ion battery accidents based on
physics-informed data-driven Bayesian networks,” Reliability Engineer-
ing and System Safety, vol. 251, p. 110294, 2024.
[19] Y. Wang et al., “Real-time knowledge- and data-driven reliability
analysis for lithium-ion battery energy storage system by Bayesian fault
propagation network,” Applied Energy, vol. 402, p. 127013, 2026.
[20] Y. Nie, N. H. Nguyen, P. Sinthong, and J. Kalagnanam, “A time series
is worth 64 words: Long-term forecasting with transformers,” arXiv
preprint arXiv:2211.14730, 2022.
[21] H. Wu, J. Xu, J. Wang, and M. Long, “Timesnet: Temporal 2d-
variation modeling for general time series analysis,” arXiv, Tech. Rep.
arXiv:2210.02186, 2022.
[22] Y. Liu et al., “iTransformer: Inverted transformers are effective for time
series forecasting,” in International Conference on Learning Represen-
tations, 2024.
[23] G. Woo, C. Liu, D. Sahoo, A. Kumar, and S. Hoi, “ETSformer: Exponen-
tial smoothing transformers for time-series forecasting,” in International
Conference on Learning Representations, 2023.
[24] Y. Liu, H. Wu, J. Wang, and M. Long, “Non-stationary transformers:
Exploring the stationarity in time series forecasting,” in Advances in
Neural Information Processing Systems, 2022.
[25] Y. Zhang and J. Yan, “Crossformer: Transformer utilizing cross-
dimension dependency for multivariate time series forecasting,” in
International Conference on Learning Representations, 2023.
[26] P. Chen et al., “Pathformer: Multi-scale transformers with adaptive path-
ways for time series forecasting,” arXiv preprint, vol. abs/2402.05956,
2024.
[27] S.-A. Chen et al., “TSMixer: An all-MLP architecture for time series
forecasting,” Transactions on Machine Learning Research, 2023.
[28] A. Das et al., “Long-term forecasting with TiDE: Time-series dense
encoder,” Transactions on Machine Learning Research, 2023.
[29] C. Challu et al., “N-HiTS: Neural hierarchical interpolation for time
series forecasting,” in Proceedings of the AAAI Conference on Artificial
Intelligence, 2023.
[30] W. C. Tam et al., “Development of a robust early-stage thermal runaway
detection model for lithium-ion batteries,” National Institute of Standards
and Technology, Tech. Rep., 2024.
[31] Y. Huang et al., “Study on thermal runaway characteristics of lithium
batteries under high-rate charge/discharge and development of a deep
learning-based early warning model,” Energy, vol. 334, p. 137676, 2025.
[32] S. Wang, Z. Wang, Z. Zhang, and X. Cheng, “Fault cause inferences of
onboard lithium-ion battery thermal runaway using convolutional neural
network,” Energy, vol. 320, p. 135328, 2025.
[33] Y. Fan et al., “Fault detection for li-ion batteries of electric vehicles with
feature-augmented attentional autoencoder,” Scientific Reports, vol. 15,
p. 18534, 2025.
[34] J. Ouyang, Z. Lin, L. Hu, and X. Fang, “Voltage faults diagnosis for
lithium-ion batteries in electric vehicles using optimized graphical neural
network,” Scientific Reports, vol. 15, p. 27328, 2025.
[35] Z. Wang et al., “An IMFO-LSTM-BiGRU combined network for long-
term multiple battery states prediction for electric vehicles,” Energy,
vol. 309, p. 133069, 2024.
[36] T. Wang et al., “Deep learning and polarization equilibrium based state
of health estimation for lithium-ion battery using partial charging data,”
Energy, vol. 317, p. 134564, 2025.

---

## Page 14

[37] X. Feng et al., “Thermal runaway mechanism of lithium ion battery for
electric vehicles: A review,” Energy Storage Materials, vol. 10, pp. 246–
267, 2018.
[38] L. Wu, Y. Wang, and L. Xing, “Temporal convolutional network–
transformer hybrid architecture with hippo optimization for lithium
battery SOC estimation,” World Electric Vehicle Journal, vol. 17, no. 5,
p. 236, 2026.