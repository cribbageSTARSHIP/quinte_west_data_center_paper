# Infrared Hotspot-Guided Early Warning of Lithium-Ion Battery Thermal Runaway Under Mechanical Abuse
**arXiv ID:** 2608.20383v1
**Source File:** arxiv_sec8_bess_thermal_runaway_2608.20383v1.pdf

## Page 1

Infrared Hotspot-Guided Early Warning of
Lithium-Ion Battery Thermal Runaway Under
Mechanical Abuse
Syed Sajid Ullah*
School of Energy and Electrical Engineering
Chang’an University
Xi’an, 710064, China
sajid@chd.edu.cn
Salman Khan
School of Energy and Electrical Engineering
Chang’an University
Xi’an, China
Muhammad Zunair Zamir
School of Information Engineering
Chang’an University
Xi’an, 710064, China
Abstract—Mechanical abuse can trigger thermal runaway (TR)
in lithium-ion batteries through localized heat generation before
sensor signals become decisive. This paper proposes a two-
stage early-warning approach that estimates localized thermal
instability from infrared hotspot dynamics and then fuses this
instability score with mechanical, electrical, thermal, and image-
intensity features for a 20-frame warning horizon. Evaluation
uses repeated experiment-wise three-fold validation, with out-of-
fold Stage-I scores during Stage-II training to prevent stacked-
model optimism. Hotspot dynamics alone achieve Stage-I ROC-
AUC 0.945, and the two-stage classifier reaches Stage-II ROC-
AUC 0.908, exceeding direct multimodal fusion while preserving
an interpretable intermediate instability signal. Thermal gradient
rise precedes voltage-based detection by 40 frames (4 seconds)
on average, enabling earlier battery management system inter-
vention. Lead-time analysis at a fixed 0.5 threshold yields a 14.8-
frame mean lead time.
Index Terms—Lithium-ion battery, thermal runaway, me-
chanical abuse, thermal imaging, hotspot dynamics, multimodal
learning, early warning, explainable AI.
I. INTRODUCTION
Lithium-ion batteries power electric vehicles, portable elec-
tronics, and grid-scale storage because of their high energy
density and long cycle life. Safety failures remain a critical
concern, especially when a cell undergoes thermal runaway
(TR): rapid heat release, gas venting, fire, and propagation to
adjacent cells [1].
Mechanical abuse constitutes a major failure trigger [2].
Indentation, compression, penetration, and crash-induced de-
formation damage internal layers, cause separator failure, and
initiate internal short circuits. The resulting localized Joule
heating can evolve into TR if undetected [3].
Conventional warning strategies depend on voltage drop,
scalar surface temperature, force, or deformation thresh-
olds [4]. These signals describe abuse progression, but they
may not capture the spatially localized thermal response that
precedes runaway. Infrared thermal imaging provides this
spatial information through hotspot formation, growth, thermal
gradient, entropy, and centroid motion [5]. Existing work
still leaves three practical gaps for compact early-warning
pipelines: single-stage fusion can submerge thermal patterns
among other features, temporal splits can leak frame-level
correlations into test sets, and diagnostic reporting is often
not separated cleanly from the prediction pipeline.
*Corresponding author: Syed Sajid Ullah (sajid@chd.edu.cn).
We present a two-stage early-warning strategy that decou-
ples localized thermal instability detection from final warning
prediction. Stage I estimates an annotated thermal-instability
state from hotspot features alone. Stage II then combines this
instability signal with mechanical, electrical, scalar thermal,
and four global IR intensity statistics. Hotspot dynamics are
therefore distilled into a physically interpretable instability
score rather than being submerged directly among many
multimodal inputs. Surface temperature can rise by over 150◦C
during the stable stage, well before voltage collapse becomes
detectable. This temporal gap creates an early window for in-
tervention that conventional voltage-threshold methods cannot
exploit. At the 10 Hz IR frame rate, the observed 40-frame
thermal gradient lead corresponds to 4 seconds of advance
warning before voltage-based detection, sufficient for a battery
management system to trigger mitigation.
The core contributions are:
• A leakage-controlled two-stage architecture that distills
thermal-image features into an intermediate instability
score before multimodal fusion.
• A compact hotspot-dynamics representation for Stage-I
instability estimation, achieving ROC-AUC 0.945 under
experiment-wise validation.
• Structured diagnostic reporting that exposes classifier
evidence while preserving the intermediate instability
score as an interpretable monitoring variable.
The two-stage design targets interpretability and leakage-
controlled evaluation while improving operating-threshold per-
formance over direct multimodal fusion.
II. RELATED WORK
Mechanically induced TR has been studied under inden-
tation, compression, nail penetration, and impact [6]. These
events induce internal short circuits and localized Joule heat-
ing, making early diagnosis challenging because the critical
precursor can be spatially localized before global cell temper-
ature rises [7], [8].
Sensor-based warning methods commonly use voltage, tem-
perature, force, strain, gas, pressure, or ultrasonic measure-
ments [9]–[11]. These are practical and compatible with
battery management systems, but scalar measurements may
provide delayed or spatially incomplete information. Data-
driven classifiers improve on fixed thresholds by learning
nonlinear relationships among sensor signals, yet they can still
underuse spatial thermal patterns [12].
arXiv:2608.20383v1  [eess.SY]  29 Jun 2026

---

## Page 2

Thermal imaging captures hotspot formation, spatial thermal
gradients, and propagation behavior [13]. Recent multimodal
studies have combined thermal images with sensor streams
and interpretable machine-learning tools for thermal-runaway
prediction [14], [15]. Image and sensor fusion is a promising
direction, but these studies do not always separate localized
thermal-instability estimation from the final warning decision.
Language-model-assisted safety reporting relates to this
goal but is not treated here as an independent predictor. Prior
work on self-decoupled or multimodal sensing emphasizes
the value of physically separated evidence channels for early
warning [16]. Our diagnostic layer follows this spirit, restrict-
ing itself to structured reporting from classifier outputs rather
than free-form language classification.
Across these directions, prior studies have explored ther-
mal imaging, multimodal fusion, and diagnostic interpretation
separately. This work combines hotspot-derived instability
scoring, experiment-wise leakage control, and structured di-
agnostic reporting within one compact early-warning pipeline.
Table I positions this work against representative studies in
each direction.
III. METHODOLOGY
A. Experimental Setup and Dataset
Cylindrical lithium-ion cells under indentation loading yield
synchronized frame-level records [18] with mechanical, elec-
trical, scalar thermal, and infrared thermal-image metadata
at 10 Hz. Hotspot blobs extracted from IR images provide
spatial dynamics (area, gradient, entropy, centroid coordi-
nates, growth, and velocity). Runaway-propagation frames are
excluded to concentrate on pre-runaway prediction, leaving
12,425 training rows from 194 experiments; five propagation-
only experiments are retained only for threshold-based signal
comparisons. Fig. 1 shows representative IR frames together
with the proposed two-stage model’s predicted warning prob-
ability ˆpt at key frames. Table II summarizes the dataset.
frame 0̂
pt=0.02
Exp 149
Stable (start)
frame 53̂
pt=0.50
Decision frame
frame 64 (TR onset)
TR onset
frame 0̂
pt=0.04
Exp 151
frame 52̂
pt=0.54
frame 80 (TR onset)
frame 0̂
pt=0.04
Exp 152
frame 58̂
pt=0.56
frame 71 (TR onset)
Fig. 1. Representative thermal IR frames for Experiments 149, 151, and 152 at
the stable starting frame, the model’s decision frame (with predicted warning
probability ˆpt), and the thermal-runaway (TR) onset frame, illustrating how
the proposed two-stage model’s warning signal tracks the visible thermal
progression.
Feature groups (Table III) organize inputs by physical role:
mechanical, electrical, scalar thermal, image intensity, and
hotspot dynamics.
The Stage-I target merges precursor and localized-instability
frames into one positive instability class against stable frames;
Stage II uses a binary label marking whether TR occurs within
the next 20 frames. Event-derived variables are excluded to
prevent leakage.
B. Problem Formulation
For each frame t, the multimodal feature vector is
xt = [xm
t , xe
t, xth
t , xint
t
, xhot
t
],
(1)
where xm
t , xe
t, xth
t , xint
t
, and xhot
t
denote mechanical, elec-
trical, scalar thermal, image-intensity, and hotspot-dynamics
features.
In Stage I, the localized thermal-instability state is estimated
from hotspot-dynamics features only:
ˆst = P(zt = 1 | xhot
t
),
(2)
where zt is the annotated thermal-instability label and ˆst ∈
[0, 1] is the estimated instability score. Restricting Stage I
to hotspot dynamics ensures ˆst depends purely on observed
thermal spatial patterns.
In Stage II, the instability score augments compact sensor
and image-intensity features:
˜xt = [xm
t , xe
t, xth
t , xint
t
, ˆst],
(3)
and the early-warning probability is estimated as
ˆpt = P(yt = 1 | ˜xt),
(4)
where yt indicates whether TR occurs within the next 20
frames.
C. Baseline Classifiers
• Sensor-only: Mechanical, electrical, and scalar-thermal
measurements.
• Image-all: Raw intensity statistics plus hotspot-dynamics
features.
• Hotspot-only: Area, centroid, gradient, entropy, growth-
rate, and velocity features.
• Direct multimodal: All feature groups fused in one stage.
• Proposed two-stage: Stage I produces ˆst, and Stage II
combines it with sensor features and four raw intensity
statistics.
Stage I compares Sensor-only, Image-all, Hotspot-only, and
Multimodal; Stage II compares Sensor-only, Image-all, Direct
multimodal, and the proposed two-stage design under the same
grouped folds. Deep-learning baselines (LSTM, CNN-LSTM,
MLP) use 10-frame input sequences, Adam at 10−3, batch
size 128, up to 30 epochs, and patience 6. Ablations remove
the Stage-I score, raw intensity statistics, or time from the
proposed configuration.

---

## Page 3

TABLE I
POSITIONING AGAINST REPRESENTATIVE PRIOR WORK.
Reference
Mech. abuse
Hotspot dyn.
Fusion
Exp. split
Diag. reporting
[4]
Partial
No
No
N/A
No
[9], [10], [12]
Yes
No
Partial
Partial
No
[13]
Partial
Partial
Partial
Partial
No
[14], [15]
Partial
Partial
Yes
Partial
No
[17]
Partial
No
Partial
N/A
Yes
This work
Yes
Yes
Yes
Yes
Yes
TABLE II
DATASET SUMMARY USED FOR PRELIMINARY EXPERIMENTS.
Item
Value
Frame-level observations
40,730
Number of experiments
199
Number of columns
38
Pre-runaway rows
12,425
Experiments used for training
194
Stage-I target
Stable vs. precursor/localized
Stage-II target
TR within next 20 frames
TABLE III
FEATURE GROUPS AND THEIR PHYSICAL INTERPRETATION.
Group
Example features
Physical meaning
Mechanical
force, deformation, dF/dt
Abuse severity
Electrical
voltage
Electrical response
Scalar thermal
high temp, low temp, temp range
Global surface heating
Thermal image
mean, std, max, min intensity
Image-level thermal state
Hotspot dynamics
area, centroid, gradient, entropy, growth, velocity
Localized thermal instability
D. Two-Stage Architecture
Fig. 2 illustrates the architecture, with two sequential stages
and a constrained diagnostic reporting layer. Stage I receives
hotspot dynamics only and outputs an instability probability.
Stage II does not re-feed those hotspot descriptors directly;
instead, it fuses the out-of-fold instability score with sensor
variables and four global image-intensity statistics, creating
an interpretable bottleneck between localized thermal evidence
and the final warning decision. The diagnostic layer then
reports structured evidence from the trained classifier without
changing the prediction itself.
A LightGBM gradient-boosting classifier is used for both
stages because the task is low-dimensional tabular fusion with
nonlinear cross-modality interactions and occasional missing
hotspot coordinates, for which tree boosting is stronger and
easier to audit than a larger end-to-end network. All Light-
GBM variants share the same hyperparameters and grouped
folds for a fair comparison. During training, Stage II receives
out-of-fold Stage-I scores for training rows; the Stage-I clas-
sifier is then refitted on the outer training fold to score the
outer test fold, preventing overfitted in-sample predictions.
SHapley Additive exPlanations (SHAP) are then computed on
the trained models to inspect which variables dominate each
stage.
E. Evaluation Metrics
All
classifiers
use
experiment-wise
three-fold
cross-
validation repeated over three random seeds [19]. Table IV
summarizes the evaluation metrics.
TABLE IV
EVALUATION METRICS.
Metric
Stage
Description
ROC-AUC
I, II
Area under ROC curve
AP
I, II
Average precision
Lead time
II
Frames from first warning to TR onset
Mean ROC-AUC with min-max range across folds is re-
ported for both stages. Tables also report AP, F1, and balanced
accuracy (BAcc) at the default threshold of 0.5. Lead time is
evaluated at the same threshold; a valid warning must cross
the threshold before TR and within the 20-frame horizon.
IV. RESULTS AND DISCUSSION
This section reports model performance for both stages
of the two-stage framework, ablation results, and diagnostic
feature analysis. Fig. 3 summarizes the Stage-I hotspot-feature
contributions and the Stage-II single-modality contributions.
Area
Cen-
troid
Gra-
dient
Entro-
py
Growth
rate
Velo-
city
0.5
0.6
0.7
0.8
0.9
1.0
1.1
ROC-AUC
0.942
0.923
0.832
0.788
0.862
0.794
Stage-I image-feature contribution
Mechanical Electrical
Scalar
thermal
Thermal
image
Proposed
two-stage
0.5
0.6
0.7
0.8
0.9
1.0
1.1
ROC-AUC
0.871
0.706
0.657
0.655
0.908
Stage-II modality contribution
Fig. 3.
(a) Stage-I hotspot-feature contribution to instability detection. (b)
Stage-II single-modality contribution to early warning, with the proposed two-
stage model shown for comparison.
A. Stage I: Thermal Instability Detection
Fig. 4 shows why thermal imaging provides earlier diagnos-
tic information than conventional signals. In Experiment 84,
surface temperature rises from 31◦C to 230◦C during the
stable stage while voltage remains at 4.0 V and hotspot area
shows no appreciable growth. Voltage collapses to 0 V only in

---

## Page 4

Fig. 2. Two-stage early-warning architecture. Stage I maps hotspot dynamics to an instability score, Stage II fuses that score with sensor and image-intensity
features for 20-frame-ahead TR warning, and the diagnostic layer reports structured evidence without altering the classifier output.
the precursor stage, by which point temperature has already
exceeded 256◦C. In Experiment 22, a more gradual failure
mode appears: voltage declines from 4.0 V to 1.8 V while
hotspot area grows consistently. In both cases, thermal signals
reveal anomaly progression before voltage reaches a decisively
abnormal reading, motivating a pipeline that converts hotspot
dynamics into an explicit instability score before final fusion.
Table V quantifies this temporal advantage across all 199
experiments using threshold-based detection. Thermal gradient
rise provides the earliest warning with a mean lead of 40.3
frames before runaway, compared to 21.0 frames for voltage
drop below 3.5 V. It detects pre-runaway anomaly in 143
of 199 experiments (71.9%) versus only 74 for the voltage
threshold, confirming broader but not universal coverage.
TABLE V
FRAME-LEVEL LEAD TIME BEFORE THERMAL RUNAWAY FOR
THRESHOLD-BASED DETECTION.
Signal
Mean lead
(frames)
Median
lead
Min
lead
Max
lead
Exp.
detected
Voltage < 3.5 V
21.0
13
1
125
74
Surface temp. > 50◦C
21.1
13
1
115
76
Hotspot area > 1.5× baseline
21.9
13
1
96
44
Thermal gradient rise
40.3
42
1
171
143
Stage-I results appear in Table VI, while Fig. 3a disag-
gregates the hotspot branch into six feature families. Area-
based cues are strongest (ROC-AUC 0.942), followed by
centroid features (0.923); growth rate (0.862) and gradient
(0.832) remain useful but weaker, while entropy (0.788)
and velocity (0.794) are the least discriminative on their
own. Sensor-only achieves ROC-AUC 0.881, reflecting limited
early-warning information from scalar measurements alone.
Hotspot-only achieves 0.945, confirming that the combined
hotspot descriptor set closely matches annotated precursor
and localized-instability states. Image-all performs similarly
(0.946), while Multimodal achieves the highest ROC-AUC of
0.949, indicating complementary information between hotspot
and sensor features.
TABLE VI
STAGE-I THERMAL INSTABILITY DETECTION RESULTS ACROSS REPEATED
EXPERIMENT-WISE FOLDS.
Model
ROC-AUC mean
ROC-AUC min
ROC-AUC max
AP mean
F1 mean
BAcc mean
Sensor-only
0.881
0.833
0.934
0.747
0.688
0.840
Sensor-no-time
0.880
0.828
0.934
0.752
0.688
0.840
Image-all
0.946
0.930
0.966
0.753
0.726
0.864
Hotspot-only
0.945
0.931
0.958
0.732
0.726
0.866
Multimodal
0.949
0.929
0.974
0.783
0.725
0.855
B. Stage II: Early-Warning Prediction
Table VII summarizes Stage-II performance together with
the deep-learning baselines, and Fig. 3b isolates the predictive
strength of each physical modality when used alone. Mechan-
ical variables are strongest (ROC-AUC 0.871), ahead of elec-
trical (0.706), scalar thermal (0.657), and the thermal-image
pathway (0.655) – all well below the proposed two-stage
model’s 0.908, also plotted in Fig. 3b for direct comparison.
The full two-stage classifier reaches ROC-AUC 0.908 versus
0.903 for Direct multimodal fusion, with stronger threshold-
level gains (F1 0.752 vs. 0.738; BAcc 0.836 vs. 0.824).
LightGBM with the two-stage design also outperforms all
three deep-learning baselines by 5 to 7 ROC-AUC points.

---

## Page 5

0
50
100
150
Frame
0
2
4
Voltage (V)
Exp. 84
0
50
100
150
200
Frame
0
2
4
Voltage (V)
Exp. 22
0
50
100
150
Frame
0
200
400
Temp. (°C)
0
50
100
150
200
Frame
0
200
400
Temp. (°C)
0
50
100
150
Frame
0
2500
5000
Force (N)
0
50
100
150
200
Frame
0
2500
5000
Force (N)
0
50
100
150
Frame
0.00
0.05
0.10
Hotspot area
0
50
100
150
200
Frame
0.00
0.05
0.10
Hotspot area
Stable
Precursor
Runaway
TR onset
Fig. 4.
Multimodal sensor trajectories for Experiments 84 and 22. Stage
backgrounds combine color with light gray hatch patterns for black-and-
white readability: green (stable), yellow (precursor), orange (localized), red
(runaway). Dashed line: TR onset. Thermal signals become abnormal before
voltage reaches a critical reading.
TABLE VII
STAGE-II EARLY-WARNING COMPARISON: LIGHTGBM AND
DEEP-LEARNING BASELINES.
Model
ROC-AUC
mean
ROC-AUC
min
ROC-AUC
max
AP
F1
BAcc
LightGBM variants
Sensor-only
0.896
0.881
0.916
0.781
0.733
0.821
Image-all
0.683
0.666
0.706
0.572
0.498
0.637
Direct multimodal
0.903
0.884
0.923
0.795
0.738
0.824
Proposed two-stage
0.908
0.894
0.924
0.796
0.752
0.836
Deep-learning baselines (sequence length 10)
LSTM
0.850
0.838
0.860
0.731
0.691
0.764
CNN-LSTM
0.843
0.825
0.857
0.719
0.687
0.760
MLP
0.839
0.827
0.861
0.684
0.694
0.767
Full ROC and precision-recall curves for both stages appear
in Fig. 5.
C. Ablation Study and Diagnostic Reporting
Ablation results appear in Table VIII. Removing the Stage-I
score reduces ROC-AUC from 0.908 to 0.905, while removing
the raw intensity statistics reduces it further to 0.896. The
strongest Stage-II behavior therefore comes from combining
the explicit instability score with a small amount of global
image context rather than feeding hotspot dynamics directly
into the warning model.
SHAP analysis (Fig. 6) provides feature-attribution insight
beyond raw importance scores. In Stage I, the top hotspot
0.00
0.25
0.50
0.75
1.00
FPR
0.0
0.2
0.4
0.6
0.8
1.0
TPR
Stage I: ROC
Sensor-only (0.906)
Image-all (0.961)
Hotspot-only (0.966)
0.00
0.25
0.50
0.75
1.00
Recall
0.2
0.4
0.6
0.8
1.0
Precision
Stage I: PR
Sensor-only (0.820)
Image-all (0.863)
Hotspot-only (0.849)
0.00
0.25
0.50
0.75
1.00
FPR
0.0
0.2
0.4
0.6
0.8
1.0
TPR
Stage II: ROC
Sensor-only (0.916)
Image-all (0.679)
Direct multi (0.924)
Proposed (0.921)
0.00
0.25
0.50
0.75
1.00
Recall
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Precision
Stage II: PR
Sensor-only (0.808)
Image-all (0.559)
Direct multi (0.839)
Proposed (0.826)
Fig. 5.
ROC and precision-recall curves for Stage I and Stage II classifier
comparisons. AUC and AP values appear in the legend.
TABLE VIII
ABLATION STUDY FOR THE STAGE-II EARLY-WARNING MODEL.
Model
ROC-AUC mean
AP mean
F1 mean
BAcc mean
Direct multimodal
0.903
0.795
0.738
0.824
Proposed two-stage
0.908
0.796
0.752
0.836
Ablation: no Stage-I score
0.905
0.794
0.751
0.835
Ablation: no intensity stats
0.896
0.781
0.733
0.821
Ablation: no time
0.902
0.791
0.743
0.828
features (growth rate, thermal gradient, area) show asymmetric
SHAP distributions: positive values increase the instability
score, confirming that growing, spatially non-uniform heating
drives the classifier toward instability detection. In Stage II, the
injected instability score is the dominant feature, followed by
compact image-intensity and voltage-related cues, indicating
that the final warning combines localized hotspot evidence
with coarse global heating and electrical response. An aggre-
gated “Other” row preserves the remaining lower-magnitude
SHAP contributions.
At threshold 0.5, the model produces 183 valid in-horizon
warnings with a mean lead time of 14.8 frames, and the
remaining detections occur beyond the 20-frame horizon,
indicating early risk awareness. The best mean F1 occurs at
0.55, but its gain over 0.5 is below 0.001, so we keep 0.5
as the default and leave stricter precision-recall trade-offs to
deployment-specific tuning.
These results remain dataset-specific: the learning-based
evaluation uses 194 experiments with pre-runaway frames,
and the earliest handcrafted cue appears in 143 of 199 ex-
periments rather than all cases. Transfer to other cell formats,
abuse modes, chemistries, or pack-level propagation scenarios

---

## Page 6

−2.5
0.0
2.5
SHAP value
other (agg.)
hotspot velocity
hotspot cx
strong hotspot area
thermal entropy
thermal gradient
early hotspot area
Stage I: Hotspot SHAP
Positive
Negative
−2
0
2
SHAP value
other (agg.)
thermal instability score
temp range
std intensity
deformation
soc
time
Stage II: Multimodal SHAP
Fig. 6. SHAP summary plots for Stage I (hotspot-only) and Stage II (two-
stage). Red: positive impact toward instability or warning; blue: negative
impact. Each panel shows the top 6 features plus an aggregated “Other” row
for the remaining contributions.
5
10
15
20
Lead time (frames)
0
10
20
30
40
50
Experiments
Warning lead time
Mean 14.8
0.2
0.4
0.6
0.8
Threshold
0.2
0.4
0.6
0.8
1.0
Score
Threshold calibration
Precision
Recall
F1
Default
Fig. 7. (left) Warning lead-time distribution. (right) Precision, recall, and F1
as functions of decision threshold for Stage II. The default 0.5 threshold is
near-optimal for F1.
remains unvalidated. The diagnostic reporting module only
verbalizes structured evidence from the trained warning model
and does not alter the classifier decision [17].
V. CONCLUSION
We presented a two-stage thermal hotspot-aware framework
for early warning of mechanically induced lithium-ion battery
TR. Thermal signatures (temperature, gradient, hotspot area)
precede voltage collapse by up to 40 frames on average, mo-
tivating a decoupled design that first distills hotspot dynamics
into a localized instability score (Stage I ROC-AUC 0.945)
before compact multimodal fusion (Stage II ROC-AUC 0.908).
SHAP analysis confirms that this instability score remains the
dominant Stage-II driver.
Future work should validate the model across additional
abuse modes, cell chemistries, and pack-level propagation set-
tings while studying deployment-specific threshold calibration
and end-to-end thermal-video alternatives.
REFERENCES
[1] X. Feng, M. Ouyang, X. Liu, L. Lu, Y. Xia, and X. He, “Thermal
runaway mechanism of lithium ion battery for electric vehicles: A
review,” Energy Storage Materials, vol. 10, pp. 246–267, 2018.
[2] H. Li, D. Zhou, M. Zhang, B. Liu, and C. Zhang, “Multi-field interpreta-
tion of internal short circuit and thermal runaway behavior for lithium-
ion batteries under mechanical abuse,” Energy, vol. 263, p. 126027,
2023.
[3] B. Liu, Y. Jia, C. Yuan et al., “Safety issues and mechanisms of lithium-
ion battery cell upon mechanical abusive loading: A review,” Energy
Storage Materials, vol. 24, pp. 85–112, 2020.
[4] C. Liu et al., “Review—understanding thermal runaway in lithium-ion
batteries: Trigger, mechanism, and early warning strategies,” Journal of
The Electrochemical Society, vol. 171, p. 120527, 2024.
[5] T. Shan, P. Zhang, Z. Wang et al., “Insights into extreme thermal
runaway scenarios of lithium-ion batteries fire and explosion: A critical
review,” Journal of Energy Storage, vol. 88, p. 111532, 2024.
[6] J. Hu, X. Zhang, Y. Wang et al., “A mechanistic modeling method for
limited overcharge abuse of lithium-ion batteries,” Energy, vol. 334, p.
137645, 2025.
[7] J. E, H. Xiao, S. Tian, and Y. Huang, “A comprehensive review on
thermal runaway model of a lithium-ion battery: Mechanism, thermal,
mechanical, propagation, gas venting and combustion,” Renewable En-
ergy, vol. 229, p. 120762, 2024.
[8] Y. Xiao, F. Yang, Z. Gao et al., “Review of mechanical abuse related
thermal runaway models of lithium-ion batteries at different scales,”
Journal of Energy Storage, vol. 64, p. 107145, 2023.
[9] X. X. Wang, Q. T. Li, X. Y. Zhou, Y. M. Hu, and X. Guo, “Monitoring
thermal runaway of lithium-ion batteries by means of gas sensors,”
Sensors and Actuators B: Chemical, vol. 411, p. 135703, 2024.
[10] W. C. Tam, J. Chen, H. Fang, W. Tang, J. Deng, and A. Putorti,
“Development of an early-stage thermal runaway detection model for
lithium-ion batteries,” Journal of Power Sources, vol. 641, p. 236714,
2025.
[11] H. Lee, Y. H. Seo, and P. S. Ma, “Advanced ultrasonic detection of
lithium-ion battery thermal runaway under various heating powers,”
Applied Energy, vol. 396, p. 126328, 2025.
[12] Z. Liu and Y. Li, “Lithium battery thermal-runaway monitoring based on
whole-feature neural networks,” Journal of The Electrochemical Society,
vol. 171, p. 080517, 2024.
[13] L. Lin, K. Hartono, Y. Ko, R. Mallela, Y. Samantaray, H. Bouteiller,
M. Z. Bazant, and H. Wang, “Mechanically induced thermal runaway
severity analysis of li-ion batteries and continuous energy release mon-
itoring,” Journal of Energy Storage, vol. 133, p. 118078, 2025.
[14] S. S. Gajghate, M. M. Noor, S. Kumar, P. J. Bansod, S. D. Shelare,
K. C. Nikam, L. D. Jathar, and M. S. Dennison, “A transformer-guided
multi-modal learning framework for predictive and causal assessment of
thermal runaway in high-energy batteries,” Scientific Reports, vol. 15,
p. 37054, 2025.
[15] A. El Abed, G. Nassreddine, O. Al-Khatib, M. Nassereddine, and
A. Hellany, “Explainable and optuna-optimized machine learning for
battery thermal runaway prediction under class imbalance conditions,”
Thermo, vol. 5, no. 3, p. 23, 2025.
[16] Z. Li, M. Jiao, K. Chen, Y. Gao, Y. Gao, C. Lian, J. Zhang, and F. Xuan,
“A self-decoupling multimodal sensor for enhanced early warning of
lithium-ion battery thermal runaway,” Research, vol. 9, p. research.1120,
2026.
[17] C. X. He, Y. H. Liu, X. Y. Huang et al., “A reduced-order thermal
runaway network model for predicting thermal propagation of lithium-
ion batteries in large-scale power systems,” Applied Energy, vol. 373,
p. 123955, 2024.
[18] J. Li, Q. Li, Z. Qin, and X. Huang, “Multimodal Neural Network-
Based Temperature Prediction Method for Lithium-Ion Batteries Under
Mechanical Abuse Scenarios,” Journal of Xi’an Jiaotong University,
vol. 60, no. 2, pp. 38–48, 2026, article number: 0253-987X(2026)02-
0038-11.
[19] J. Jeong, E. Kwak, J. H. Kim, and K. Y. Oh, “Prediction of thermal run-
away for a lithium-ion battery through multiphysics-informed deeponet
with virtual data,” eTransportation, vol. 21, p. 100337, 2024.