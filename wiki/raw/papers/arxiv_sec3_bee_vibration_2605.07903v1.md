# BeeVe: Unsupervised Acoustic State Discovery in Honey Bee Buzzing
**arXiv ID:** 2605.07903v1
**Source File:** arxiv_sec3_bee_vibration_2605.07903v1.pdf

## Page 1

BEEVE: UNSUPERVISED DISCOVERY OF NON-SEMANTIC ACOUSTIC
STATES, TOWARDS A NON-INVASIVE ASSESSMENT OF HONEY BEE
COLONY HEALTH
HAMZE HAMMAMI AND NIDHAL ABDULAZIZ
Abstract. Discovering structure in biological signals without supervision is a fundamental
problem in computational intelligence, yet existing bioacoustic methods assume vocal pro-
duction models or predefined semantic units, leaving non-vocal species poorly served. Honey
bees are a compelling instance of this gap: their collective buzzing arises from mechanical
muscle vibrations rather than any communicative vocal apparatus, and while evidence sug-
gests these vibrations reflect colony physiological state, no existing vocal framework applies.
This work introduces BeeVe, an unsupervised framework for acoustic state discovery in
collective honey bee buzzing. BeeVe uses the self-supervised Patchout Spectrogram Trans-
former (PaSST) as a frozen feature extractor to produce general acoustic embeddings, then
trains a Vector-Quantized Variational Autoencoder (VQ-VAE) entirely without labels on
those embeddings, learning a finite discrete codebook of acoustic tokens directly from un-
labelled hive audio. All learning applied to bee audio is unsupervised: no labels, pretext
tasks, or contrastive objectives are used at any stage. Each token represents a recurring
acoustic pattern, and the full codebook forms a reusable vocabulary of colony-level acoustic
states discovered entirely without annotation.
Post-hoc evaluation against known queen
status reveals that the learned tokens separate queenright and queenless conditions with
Jensen-Shannon Divergence values between 0.609 and 0.688, and that the queenless condi-
tion further decomposes into three internally coherent sub-states stable across experiments
with different codebook sizes and random seeds. Token transition analysis further confirms
non-random sequential structure in the learned vocabulary (p ≪0.001), consistent across all
three experiments. Generalisation to unseen recordings preserves both token overlap (Jac-
card = 0.947) and global manifold topology. These results demonstrate that unsupervised
discrete codebook learning can recover repeatable acoustic structure from a non-vocal bio-
logical signal without annotation, opening a path toward non-invasive acoustic hive health
monitoring.
Keywords: bioacoustics, PaSST, representation learning, state discovery, unsupervised learn-
ing, VQ-VAE.
1. Introduction
Honey bees are essential pollinators whose global decline poses serious risks to ecosystems
dependent on their pollination. While bee communication is primarily understood through
pheromonal signals and the waggle dance [14], evidence suggests that collective buzzing re-
flects deeper physiological and behavioural states of the colony. Acoustic correlates have been
identified for queen presence and loss [12, 11], swarming preparation [5], and modulatory vibra-
tional signals such as the dorso-ventral abdominal vibration [16], indicating that the acoustic
Date: May 11, 2026.
MSC2020: Primary 68T07 (Machine learning), Secondary 92B05 (General biology).
1
arXiv:2605.07903v1  [cs.SD]  8 May 2026

---

## Page 2

2
H. HAMMAMI AND N. ABDULAZIZ
output of a hive is not random noise but structured emergent behaviour linked to internal
colony state. This makes acoustic monitoring a promising non-invasive alternative to physi-
cal hive inspection, with early detection of conditions such as queen loss or swarming offering
practical benefits for colony health management [1].
Building on the acoustic monitoring direction, Hammami and Abdulaziz [9] proposed a
supervised classifier for queen status detection from hive audio, demonstrating that acoustic
signals are sufficiently structured for machine learning-based state detection. The present work
extends this by removing the supervision requirement entirely, asking whether that structure
can be discovered without any labels.
Early attempts to record animal sounds date to the late 19th century [4]. A significant
landmark demonstration specific to bees came from Karl von Frisch [7], whose decoding of
the waggle dance showed that bee behaviour encodes structured spatial information, earning
the Nobel Prize in 1973 and establishing that signals produced by bees carry meaning beyond
simple reflex.
Modern non-human communication research has advanced significantly through machine
learning and representation learning, with large-scale models increasingly explored as tools for
analysing animal acoustic systems. These advances have enabled self-supervised approaches to
pattern discovery in animal vocalisations, learning meaningful representations directly from un-
labelled audio without manual annotation, particularly valuable where the underlying structure
and semantics remain unknown.
NatureLM-Audio [17] presents an audio-language foundation model that learns general
acoustic features from unlabelled animal sound data through self-supervised representation
learning. This addresses a key limitation of earlier studies, namely the reliance on narrowly
curated datasets and task-dependent feature engineering, and produces representations trans-
ferable across species and tasks.
Building on this idea, AVES [8] introduced a self-supervised transformer encoder for animal
vocalizations, demonstrating that meaningful acoustic representations can be learned without
manual annotation and transferred effectively across species and tasks, showing that latent rep-
resentations learned from animal sounds exhibit structure that is useful for downstream tasks.
A direct investigation of this transferability was provided by [18], who systematically compared
SSL models pre-trained on animal vocalizations, specifically AVES, against models pre-trained
on human speech, across three bioacoustic datasets. Their results showed that pre-training
on bioacoustic data yields marginal improvements over speech-pretrained models in most set-
tings, and that further fine-tuning on automatic speech recognition tasks produces inconsistent
gains. A significant finding suggests that the general-purpose representations capture structure
sufficiently transferable to non-human vocalizations.
The WhaleLM framework [20] applies neural sequence models to sperm whale vocalizations
and demonstrates that whale codas exhibit long-range dependencies and structure. The study
shows that these vocal sequences encode information about both current and future behavior,
providing evidence that animal communication systems may contain higher-order structure.
Importantly, this work operates on coda unit types already identified and segmented by ma-
rine biologists, meaning the discrete units are externally defined rather than learned from raw
audio. Complementing this line of work, Paradise et al. introduced WhAM [15], which mod-
els sperm whale vocalizations using translation neural architectures. Their approach frames
animal communication as a representation learning problem, where latent embeddings capture
communicative structure without explicit human-defined labels.

---

## Page 3

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
3
Table 1. Comparison of Bioacoustic Approaches
Method
Signal
Supervision
Learned Codebook
NatureLM [17]
Vocal
Self-sup.
–
AVES [8]
Vocal
Self-sup.
–
WhaleLM [20]
Vocal
Self-sup.
–
WhAM [15]
Vocal
Self-sup.
–
Sarkar & Doss [19]
Vocal
Self-sup.
✓
James et al. [10]
Vocal
Unsup.
✓
Abdollahi et al. [1]
Non-vocal
Supervised
–
Kanelis et al. [11]
Non-vocal
Supervised
–
Carvalho Jr. et al. [3]
Non-vocal
Unsup.
–
BeeVe
Non-vocal
Unsup.
✓
A particularly relevant line of work concerns the discretization of animal vocalizations into
sequences of learned acoustic tokens, a concept very much aligned with this study. [19] investi-
gated if discrete token sequences through vector quantization of SSL embeddings can capture
and leverage the temporal structure of animal calls, applying this framework to four datasets
covering marmosets and dogs.
Their distance analysis demonstrated that vector-quantized
token sequences generated from HuBERT embeddings exhibit meaningful separability by call-
type and caller identity, and that a k-nearest neighbour classifier operating on Levenshtein
distances between token sequences achieves reasonable classification performance. This rep-
resents the first application of discrete audio tokenization to bioacoustics, establishing that
learned codebooks can capture relevant variation in animal vocalizations, a finding directly
motivating the approach taken in the present work.
Further supporting the view that non-human communication can be studied using modern
ML algorithms, a very recent study by James et al. [10] extended a discrete acoustic tokeniza-
tion to a real-time interactive setting, developing an audio-LLM that engages in naturalistic
vocal exchanges with live zebra finches. Their system represents individual calls as discrete to-
kens learned through vector quantization, demonstrating that compact learned codebooks can
capture meaningful acoustic variation in animal vocalizations and enable downstream sequence
modeling.
Carvalho Jr. et al. [3] apply a convolutional autoencoder with HDBSCAN clustering to
bee audio for unsupervised queenless detection, demonstrating that unsupervised methods can
match or exceed supervised baselines on this task.
However, the approach targets binary
classification and produces no reusable discrete vocabulary of acoustic states.
These advances share a common principle, structure in animal acoustics can be recovered
from data without a predefined semantic assumptions. However, all prior work targets vocal
species, those producing sound through a dedicated phonatory apparatus [6], and mostly relies
on predefined discrete units, as in WhaleLM and WhAM. Honey bee buzzing is non-vocal,
arising from muscle vibrations reflecting the collective state rather than communicative intent.
Table 1 positions key works across signal type, supervision, and discretization.

---

## Page 4

4
H. HAMMAMI AND N. ABDULAZIZ
BeeVe frames the signal as non-vocal and applies unsupervised discrete codebook learning
directly to bee audio, where PaSST serves as a frozen feature extractor pretrained on AudioSet
[13] and queen status is used only for post-hoc evaluation.
Accordingly, this work does not model honey-bee buzzing as a language, nor does it aim
to decode explicit communicative messages. Instead, a state-discovery perspective is adopted
where semantic units, communicative intent, and generative structure are not assumed. Rep-
resentations emerge through unsupervised learning, and the resulting structure is evaluated
against known states and examined for finer sub-state organisation. The central question is
whether non-random, compositional structure is inherent in collective honey-bee buzzing as an
emergent property of colony behaviour. This work frames that question as a computational in-
telligence problem, applying unsupervised representation learning and discrete codebook learn-
ing to recover structure from a biological signal without annotation.
The main contributions of this work are:
• Proposes a framework for unsupervised discrete acoustic pattern discovery applied to
a non-vocal species, making no semantic assumptions about the signal.
• Experimental demonstration that VQ-VAE tokens separate queenright and queenless
state conditions (JSD 0.609-0.688) without any label supervision.
• Characterisation of three internally stable queenless sub-states consistent across differ-
ent codebook sizes and random seeds, suggesting the possibility of distinct behavioural
modes within the queenless condition.
• Statistical evidence of non-random temporal structure in the learned token sequences.
2. Methodology
The block diagram in Figure 1 summarises the general methodology.
Figure 1. Method summary.
2.1. UrBAN Dataset. Acoustic data equivalent to approximately five hours of hive record-
ings was sampled from the UrBAN dataset [2]. The UrBAN dataset contains well over 1000
hours of honey-bee hive audio collected under real-world conditions. For the purposes of a con-
trolled and interpretable experiment, the amount of data used is limited while preserving data
diversity through annotations. These annotations are used only to ensure that recordings from
multiple conditions are represented in the experiment and are not used as labels for training.

---

## Page 5

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
5
2.2. Feature Extraction and Model Architecture. Audio data is transformed into acous-
tic representations using the Patchout Spectrogram Transformer (PaSST), audio is loaded at
22,050 Hz before feature extraction. The model variant passt s swa p16 128 ap476 is used,
loaded from the hear21passt library [13] with pretrained weights and no fine-tuning. Times-
tamp embeddings are extracted at approximately 23 ms intervals (hop length 512 at 22,050 Hz),
yielding one 1295-dimensional feature vector per frame.
The feature vector embeddings are passed as the input to a Vector-Quantized Variational
Autoencoder (VQ-VAE) the exact architecture can be seen in Figure 2, consisting of three
components:
• Encoder: Compresses PaSST embeddings into a 128-dimensional continuous latent
representation ze ∈R128 through five fully connected blocks (1295 →1024 →512 →
512 →128)with LayerNorm, GELU activation, dropout, and a residual connection at
the 512 →512 stage.
• Vector Quantizer: Maps the latent representation ze to the nearest entry in a learned
codebook C = {e1, e2, . . . , eK}, where K ∈{32, 64} depending on the experiment,
K = 64 is the primary baseline at this data scale (five hours), K = 32 is tested with
the smaller three-hour subset for a more compact vocabulary. Encoder outputs and
codebook entries are L2-normalized before distance (Equation 1).
(1)
k∗= arg min
k ∥norm(ze) −norm(ek)∥2
The continuous representation is replaced with this entry (Equation 2).
(2)
zq = ek∗
Gradients bypass the non-differentiable quantization step via straight-through esti-
mation, and the codebook is updated by EMA with decay α = 0.99 (Equation 3).
(3)
ek ←αek + (1 −α)¯z(k)
e
where ¯z(k)
e
is the running mean of encoder outputs assigned to entry k.
• Decoder: Reconstructs the original 1295-dimensional space from zq through four
stages (128 →512 →512 →1024 →1295) with LayerNorm, GELU, dropout, a
residual connection at the first stage, and a final linear projection without activation.
The decoder output ˆx ∈R1295 approximates the original PaSST embedding.
2.3. Training Objective. The VQ-VAE is trained using a composite loss function consisting
of a reconstruction term and a combined quantization term (Equation 4):
(4)
Ltotal = Lrecon + λLvq
where: λ = 0.1
The outer weight λ = 0.1 ensures that the reconstruction term Lrecon remains the dominant
training signal, quantization is kept as a regulariser to prevent the codebook from collapsing
in early training. The quantization loss Lvq is a combination of three terms (Equation 5):

---

## Page 6

6
H. HAMMAMI AND N. ABDULAZIZ
Figure 2. VQ-VAE architecture.
(5)
Lvq = Lcodebook + βLcommit + γLdiversity
where: β = 0.25,
γ = 0.1
Each term serves a distinct objective:
• Reconstruction Loss measures the mean squared error between the original PaSST
embedding and the decoder output (Equation 6):
(6)
Lrecon = ∥x −ˆx∥2
where: x ∈R1295 is the original input,
ˆx ∈R1295 is the reconstructed output
• Codebook Loss pulls codebook entries toward the encoder outputs assigned to them,
ensuring the vocabulary remains relevant to what the encoder is producing (Equa-
tion 7):
(7)
Lcodebook = ∥zq −sg[ze]∥2
where: sg[·] is the stop-gradient operator,
zq is the quantized representation
• Commitment Loss encourages the encoder to commit to a codebook entry rather
than fluctuating between multiple entries (Equation 8):
(8)
Lcommit = ∥sg[zq] −ze∥2
where: ze ∈R128 is the continuous encoder output

---

## Page 7

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
7
• Diversity Loss encourages uniform utilization of the codebook through entropy reg-
ularization, preventing codebook collapse (Equation 9):
(9)
Ldiversity = −
K
X
k=1
pk log pk
where: pk is the usage frequency of codebook entry k,
K ∈{32, 64}
Training proceeds in two phases: for the first 10 epochs only Lrecon is active, allowing the
encoder and decoder to establish a meaningful representation before quantization is introduced
and preventing early codebook collapse. After epoch 10 the full Ltotal is applied. Early stopping
halts training when validation loss does not improve by more than 0.0005 over 15 epochs, subject
to a minimum active token threshold of ⌊K/6⌋, ensuring training is not terminated while the
codebook is still forming. Following training, a post-processing step merges tokens with cosine
similarity exceeding 0.92 and removes tokens with usage below 2%, reassigning their frames to
the nearest active entry and renumbering sequentially.
3. Experimental Setup
3.1. Model Quality Evaluation. The following metrics assess the quality of the VQ-VAE
and its learned codebook across experiments.
Reconstruction Quality: The primary quantitative measure of model performance is the
mean squared error between PaSST embeddings and decoder reconstructions, assessed through
Equation 6.
Codebook Utilization: Codebook perplexity measures how uniformly the model uses its
vocabulary, (Equation 10):
(10)
Perplexity = exp
 
−
K
X
k=1
pk log pk
!
where: pk is the usage frequency of codebook entry k
Higher perplexity indicates more uniform codebook usage, meaning the model is using a
larger portion of its vocabulary to represent the data.
3.2. Validation Against Known Conditions. A core objective of this work is to determine
whether the learned representations capture meaningful acoustic states without supervision.
Token usage distributions and latent embeddings are examined post-hoc against known hive
conditions. queen status (queenright vs. queenless) is used as the evaluation label, matched
to recordings via the nearest preceding inspection date from inspections 2021.csv. These
labels are never exposed during training.
Token Distribution Between States: The Jensen-Shannon Divergence (JSD) between
queenright and queenless token usage distributions quantifies how distinctly the two conditions
use the learned codebook.
2D Latent Projection: Latent embeddings are projected to 2D using UMAP and t-SNE
for visual inspection of cluster structure and separation between conditions.

---

## Page 8

8
H. HAMMAMI AND N. ABDULAZIZ
Spatial Separation: Separation in the latent space is assessed using the silhouette score
and a nearest-neighbour outlier analysis, measuring the fraction of queenless embeddings spa-
tially closer to the queenright cluster than to their own condition.
Sub-state Analysis: Internal structure within the queenless condition is investigated by
applying k-means clustering (k = 3) to queenless embeddings in the full 128-dimensional space.
Sub-states are characterised by their dominant token and token purity, and examined through
a PCA projection computed exclusively on queenless embeddings to remove distortion from
the queenright mass.
3.3. Temporal Analysis. Token sequences are treated as a discrete time series to evaluate
token transition, using three metrics.
Token Transition Matrix: A first-order transition count matrix C ∈ZK×K is accu-
mulated from all consecutive token pairs (ti, ti+1), then row-normalised to give conditional
probabilities P(ti+1 | ti).
Transition Entropy: Shannon entropy of each token’s outgoing distribution measures how
predictable its successor is:
(11)
Hi = −
X
j
P(ti+1=j | ti=i) log2 P(ti+1=j | ti=i)
The ratio Hi/Hmax, where Hmax = log2 Kactive, normalises for codebook size.
Statistical Tests: Two chi-squared tests assess if temporal structure is statistically signifi-
cant. A goodness-of-fit test against a uniform baseline. A second chi-squared independence test
applied to the full transition sub-matrix of active tokens observes if joint distribution P(ti+1, ti)
departs from the product of marginals, i.e. whether knowledge of the current token provides
information about the next.
3.4. Generalization to Unseen Data. Token distribution shift between training and unseen
recordings is quantified by JSD, where values below 0.2 indicate stable generalization and values
above 0.3 indicate significant distribution shift. Jaccard overlap measures the proportion of
active training tokens that remain active on the test recording. Manifold consistency is assessed
by projecting unseen embeddings through the UMAP fitted on training data (Equations 12-13),
placing each test point relative to its nearest neighbours in the training set so that topology
can be compared directly across seen and unseen recordings.
(12)
pj|i = exp

−max(0, d(xi, xj) −ρi)
σi

(13)
qij =
1
1 + a∥yi −yj∥2b
where ρi is the distance to the nearest neighbour of xi, σi normalises local density, yi ∈R3
is the low-dimensional position of xi, and a, b are fitted constants.
4. Experimental Results
4.1. Experiment Configuration. Three full-scale experiments were conducted. The base-
line (E1 baseline) uses 5 hours of training data, random seed 0, and a codebook of size 64.
E2 small codebook uses 3 hours of data with a codebook of 32 to assess the effect of vocab-
ulary size. E1 baseline seed1 repeats the baseline with a different random seed to evaluate
robustness. Prior to full-scale training, small-scale experiments on 1 minute and 30 minutes

---

## Page 9

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
9
Table 2. Model Evaluation Metrics
Experiment
Training Data
Codebook
Seed
Epochs
Recon Loss
Perplexity
Active Tokens
E1 baseline
350k frames (5h)
64
0
25
0.91
15.82
19/64
E1 baseline seed1
350k frames (5h)
64
1
22
0.93
14.54
17/64
E2 small codebook
210k frames (3h)
32
0
22
1.30
16.64
18/32
of audio confirmed that the VQ-VAE learns structured representations even under severely
limited data.
4.2. Model Evaluation. Given the unsupervised nature of this work, codebook distribu-
tion and reconstruction error are the primary quality indicators. All figures in the following
subsections refer to E1 baseline evaluated on an unseen recording. Table 2 summarises the
configuration and key metrics for each experiment.
4.2.1. Reconstruction. Figure 3 shows the total loss and validation reconstruction loss for the
baseline experiment. The warmup period is identifiable as the green shaded area in the plot.
During epochs 1-10, only the reconstruction loss drives backpropagation, and the model con-
verges to a stable reconstruction loss. At epoch 11, the full quantization loss is introduced,
which causes a sharp spike in total loss as the vector quantizer begins pulling outputs towards
codebook entries. This spike is expected behaviour at this stage of training, arising from the
discontinuity introduced by activating the quantization term. The reconstruction loss itself
also spikes but recovers much more quickly. Overall loss remains at a higher plateau, but the
model recovers and reconstruction continues to improve.
Figure 3. Loss and reconstruction curves for the baseline experiment.
Figure 4 shows the reconstruction quality for the test recording. The decoder output is
compared against the original PaSST features. Large error margins concentrate in the upper
band of dimensions, which is the high-activation region of the PaSST embedding space, while
the lower dimensions (approximately 700 to 1295) are reconstructed with near-zero error. This
pattern is a consequence of the discrete bottleneck and reflects correct model behaviour rather
than failure. PaSST processes audio as mel spectrogram patches; the high-activation dimen-
sions (0-500) encode the mid-frequency range where bee buzzing patterns exist. The other
dimensions (700-1295) correspond to frequency content above where bees produce meaningful
sound, which is why this region shows near-zero reconstruction error. The codebook learns one
representative embedding per token, capturing the dominant pattern across frames assigned

---

## Page 10

10
H. HAMMAMI AND N. ABDULAZIZ
to that token. Within-state variation is largest in the high-activation dimensions precisely be-
cause that is where the bee signal is richest and most variable. The concentration of error in
dimensions 0-500 indicates that is where the model spends its representational capacity, which
is exactly where it should. The goal is not perfect reconstruction. A codebook that recon-
structed everything perfectly would not be performing any meaningful compression. Fidelity
loss is unavoidable when collapsing continuous embeddings into one of a fixed set of discrete
codes, particularly given the high dimensionality of the data.
Figure 4. Reconstruction quality on the test recording.
The codebook represents the colony-level acoustic state rather than preserving individual
frame variation. The remaining error reflects the deviation of each frame from the average
pattern of its assigned token, which is the expected cost of discrete compression.
4.2.2. Codebook. Figure 5 shows the validation perplexity and active token count across epochs.
Perplexity rises steadily from 7.5 to approximately 9.25, reflecting that token usage grows more
evenly across the codebook. Active tokens grow from 11 at the start of training to 18 by the
final epochs, showing no codebook collapse.
Figure 5. Codebook perplexity and active token count across training epochs.
Figure 6 shows the learned codebook structure. The PCA projection shows tokens are well
separated and spread out across the space.
A similarity matrix confirms that token pairs
have low cosine similarity, with only some pairs showing moderate similarity. The usage bar
chart shows that most tokens are used at comparable frequencies, though token 19 is used
substantially more than the rest.

---

## Page 11

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
11
Figure 6. similarity matrix, and usage distribution.
4.3. State Validation. To determine whether the concentration of error in the high-activation
dimensions reflects meaningful learning, and whether the encoder captures genuine state vari-
ation, the learned representations were evaluated against known hive conditions. Token usage
patterns were analyzed across different states, and embeddings were projected to 2D using
UMAP to observe whether spatial separation occurred between conditions.
4.3.1. Validation Data and Labeling. Inference was performed on all recordings, producing
token assignments for each audio frame. queen status labels were derived from hive inspection
records using the inspections 2021.csv annotation file.
Each recording was matched to
the nearest preceding inspection entry for its hive, assigning either a queenright (QR) label,
denoting a colony with a functioning queen, or a queenless (QNL) label, denoting a colony
from which the queen had been removed. Of the 326 recordings, all were successfully matched,
yielding 262 queenright files (4.59M frames) and 64 queenless files (1.12M frames), a class ratio
of approximately 4:1. These labels were not used during training and are employed solely for
post-hoc validation purposes.
4.3.2. Validation Results. Table 3 summarises the metrics for state validation across all ex-
periments.
Token usage separation between the two known conditions is substantial, with
Jensen-Shannon Divergence values ranging from 0.609 to 0.688. This separation was achieved
without any label supervision during training. queenright colonies consistently utilized a vo-
cabulary of 13-16 active tokens with Shannon entropy of 2.04-2.40 bits, reflecting diverse and
distributed token usage. queenless colonies, by contrast, collapsed to only 5-6 active tokens
with entropy of 1.13-1.25 bits, with a single dominant token accounting for 56-58% of all frames
across all experiments; however, this could be due to the limitation of queenless data compared
to queenright. Most importantly, the proportion of QNL outliers falling within the QR cluster
remains below 2% across all experiments, indicating that the model can generally differentiate
between the QNL and QR states.
Further analysis of the metrics in Table 3 identifies how the model learned these patterns
in an unsupervised manner; the metrics each capture a distinct aspect of the learned repre-
sentations. The Jensen-Shannon Divergence (JSD) operates on the token usage distributions
and measures how different the two conditions are in terms of which codebook entries they use
and how frequently. A JSD of 0 indicates identical distributions (no pattern differences across
states) while a value of 1 indicates completely non-overlapping distributions; the 0.609-0.688
range observed here shows that there are clearly distinct patterns between the two states. JSD

---

## Page 12

12
H. HAMMAMI AND N. ABDULAZIZ
Table 3. State validation metrics across all experiments.
Experiment
Condition
JSD
Active Tokens
Entropy (bits)
Top Token (%)
Silhouette
QNL Outliers
E1 baseline
queenright
0.609
13/64
2.042
39.04
0.046
1.57%
queenless
5/64
1.134
58.00
E1 baseline seed1
queenright
0.688
13/64
2.210
27.68
0.016
1.57%
queenless
6/64
1.187
56.30
E2 small codebook
queenright
0.663
16/32
2.398
19.94
0.188
1.70%
queenless
6/32
1.247
56.45
is computed over the entire condition rather than individual frames, so it reflects a global
acoustic signature rather than the behaviour of a single recording.
The Shannon entropy of a condition’s token distribution measures the diversity of acoustic
patterns produced: a high entropy indicates that many tokens are used with roughly equal
frequency, while a low entropy reflects concentration on a small number of tokens. The token
usage in Figure 7 shows that queenright colonies exhibit more diverse token usage with one
dominant token while the remainder are used at a more stable frequency; queenless colonies,
in contrast, show limited token usage with only three tokens being dominant. This further
supports the lower entropy observed in queenless colonies compared to the higher entropy of
queenright colonies.
Figure 7. Baseline queen status token usage heatmap.
The silhouette score operates in the 128-dimensional latent space rather than on token
distributions, measuring whether individual frame embeddings cluster more tightly with frames
of their own condition than with frames of the opposite condition. Positive values indicate that
points are closer to their own group than to the other; the moderate scores observed here (0.016-
0.188) reflect that while the two conditions are tokenwise very distinct, their latent embeddings
partially overlap in the continuous space prior to quantization.
Finally, the QNL outlier percentage measures the fraction of queenless frame embeddings
that are spatially closer to the queenright cluster centroid than to their own; the consistently
low values across all experiments confirm that queenless representations form a coherent and
self-contained region in the latent space, despite the class imbalance in the dataset. The embed-
dings are clustered in their 128-dimensional latent space and projected into more interpretable
forms using dimensionality reduction methods. UMAP and t-SNE projections are shown for
two different experiments in Figure 8. It can be observed that in these projections, queenright

---

## Page 13

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
13
Table 4. Sub-state statistics across all experiments.
Sub-state A
Sub-state B
Sub-state C
Experiment
Size (%)
Dom. Token
Purity (%)
Size (%)
Dom. Token
Purity (%)
Size (%)
Dom. Token
Purity (%)
E1 baseline
57.6
T0
97.5
22.0
T10
53.6
20.4
T19
90.8
E1 baseline seed1
57.4
T1
97.9
23.0
T8
88.7
19.5
T5
73.1
E2 small codebook
57.1
T12
97.7
21.6
T3
89.3
21.3
T11
41.9
embeddings form a single connected region while queenless frames do not form a single con-
tiguous region but instead appear as two to three isolated clusters separated from the main
queenright mass.
Figure 8. 2D latent projections coloured by queen status.
4.3.3. Sub-states. An interesting observation from the state validation projections is that UMAP
and t-SNE form distinct clusters that are not fully connected. In t-SNE, two clusters are clearly
dominant while a third is either barely formed or sparsely populated. To investigate this, QNL
embeddings were isolated in the 128-dimensional latent space and K-means clustering (k = 3)
was applied. Three distinct sub-states were identified across all three experiments.
Figure 9 shows the PCA projection of the queenless embeddings colored by sub-state for the
baseline experiment. Because the projection is solely from queenless frames, the resulting axes
show the principal modes of variation within the queenless condition. In other words, possible
sub-states within a known state can be discovered, which may reflect additional conditions
beyond the original queenless status.
This setup removes the dense bias of the queenright
mass; by removing the healthy state and discovering sub-states in the queenless condition,
three spatial regions emerge, confirming that the sub-state structure is present in the learned
representations themselves.

---

## Page 14

14
H. HAMMAMI AND N. ABDULAZIZ
Figure 9. PCA projection of queenless embeddings coloured by sub-state.
Figure 10 shows the token composition of each sub-state. Sub-state A accounts for 57.6%
of queenless frames and is entirely dominated by a single token (T0 at 97.5%), with the most
acoustic concentration and repetition in tokens of the three modes. Sub-state C comprises
20.4% of queenless frames and is also dominated by a single token (T19 at 90.8%). Sub-state
B accounts for the remaining 22.0% and exhibits a more distributed pattern, with T10 at
53.2% and T16 at 24.7%, suggesting a mixture rather than a single dominant token.
The
grey remainder in each bar shows the contribution of all other tokens, which is negligible in
Sub-states A and C but reaches 13.4% in Sub-state B.
In Figure 11, all embeddings including queenright frames are projected through UMAP, the
same baseline projection from Figure 8, with queenright frames shown in grey and queenless
frames coloured by their sub-state assignment. The UMAP projection achieves a reasonable
separation of the three sub-states, with each forming a visually distinct region. A small number
of outlier points appear in neighbouring sub-state regions and within the queenright cluster;
these are likely frames assigned to non-dominant tokens within their sub-state, which sit closer
to the queenright manifold in the full 128-dimensional space and therefore project into adjacent
regions under UMAP’s non-linear compression.
The outcome of three internally coherent sub-states within the queenless condition suggests
that queen absence does not produce a single response but a possible set of distinct behavioural
modes which the model discovered entirely without supervision. Table 4 further supports this
through the size, dominant token, and purity of each sub-state across all three experiments.

---

## Page 15

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
15
Figure 10. Token composition of queenless sub-states for the baseline experiment.
Figure 11. UMAP projection QNL sub-state.
Based on the metrics, Sub-state A is the most consistent finding across all experiments. Its
size remains fixed at approximately 57% of all queenless frames, regardless of codebook size or
random seed, and its purity is consistently above 97%, meaning that in every model trained,

---

## Page 16

16
H. HAMMAMI AND N. ABDULAZIZ
more than half of all queenless audio frames collapse into a single dominant token with near-
complete uniformity. The token ID changes between experiments because IDs are arbitrary
labels assigned during training and carry no semantic meaning.
Sub-state C shows similarly high purity in E1 baseline (90.8%) but drops to 73.1% in
E1 baseline seed1 and 41.9% in E2 small codebook. The E1 at 73% is still acceptable; how-
ever, the drop in E2 is likely a consequence of the smaller codebook forcing variation within
fewer tokens, which dilutes the purity of clusters. Despite this variation in purity, the size of
this state remains stable at 20-21% across all experiments, suggesting the grouping itself is
consistent even if the token assignment is less concentrated.
Sub-state B is the least uniform of the three. Not only is there a mixture of tokens, but
the purity of the dominant token varies across models, ranging from 53.6% in E1 baseline to
89.3% in E2 small codebook. Its dominant token accounts for only roughly half of its frames
in two experiments, consistent with the 13.4% grey remainder seen in Figure 10, supporting
the interpretation of Sub-state B as a mixed mode rather than a single well-defined state.
However, its size also remains stable at approximately 22-23% of queenless frames, suggesting
it still consistently captures a distinct region of the queenless space even if more heterogeneous
than the other two sub-states.
Figure 12 shows deviation of each sub-state’s mean PaSST feature profile from the overall
queenless mean. Sub-state A consistently activates above the queenless mean, Sub-state C
is broadly suppressed below the queenless mean in the same region, suggesting lower overall
energy. Sub-state B shows a mixed pattern, consistent with its interpretation as a heterogeneous
behavior rather than a single well-defined state.
Figure 12. PaSST feature deviation.
4.4. Token Temporal Structure. Table 5 summarises temporal statistics across all experi-
ments.
The chi-squared independence test rejects the null hypothesis of token independence at
p ≪0.001 across all experiments (χ2 > 16M, df ≤196), confirming that the token sequence

---

## Page 17

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
17
Table 5. Temporal token sequence statistics.
Experiment
Active Tokens
Self-transitions
Transition Entropy H (bits)
H/Hmax
Chi-squared Independence Test
E1 baseline
15/64
51%
2.35 ± 0.86
0.60
p ≪0.001
E1 baseline seed1
13/64
54%
2.08 ± 0.74
0.56
p ≪0.001
E2 small codebook
13/32
58%
2.42 ± 0.58
0.65
p ≪0.001
carries temporal structure and is not memoryless. Every active token exhibits non-uniform
outgoing transitions (p < 0.05, goodness-of-fit against uniform baseline). Outgoing transition
entropy averages 2.08-2.42 bits against a maximum possible 3.70-3.91 bits (H/Hmax = 0.56-
0.65), indicating structured but non-deterministic transitions. Two tokens exhibit markedly
lower entropy: T0 (H = 0.10 bits) and T10 (H = 0.59 bits). The transition matrix in Figure 13
confirms this directly, T0 transitions to itself with probability 0.99 and T10 with 0.93, while
all other active tokens distribute probability across multiple successors.
These two tokens
correspond to the dominant queenless sub-states identified in Section 4.3, suggesting their
persistence is a property of colony behavior rather than a quantization artifact.
Approximately half of all frame-to-frame transitions are self-transitions (51-58%), which is
expected given the 23 ms frame resolution relative to colony-level acoustic phenomena that
operate on timescales of seconds to minutes. The remaining 42-49% of non-self transitions are
not claimed to reflect meaningful state changes; at this resolution they are likely dominated by
quantization boundary effects and noise. The more informative finding is that self-transition
rates vary substantially across tokens (0.28-0.99), and that when transitions do occur they follow
structured pathways rather than distributing randomly across the codebook, both properties
confirmed by the chi-squared independence test (p ≪0.001) and consistent across all three
experiments.
Figure 13. Token transition probability matrix
4.5. Unseen Data. Token Distribution. Of the 19 active training tokens, 18 are also active
in the test file, giving a Jaccard overlap of 0.947 and a JSD of 0.2065. The test file uses the same

---

## Page 18

18
H. HAMMAMI AND N. ABDULAZIZ
tokens at broadly similar relative frequencies, with lower absolute counts due to the smaller
file size.
Manifold Projection. Figure 14 shows the UMAP manifolds for training, test, and over-
lay. The test manifold recovers a similar global shape to the training manifold despite being
computed from approximately 10% of the data (17,531 test samples vs. 175,336 training sam-
ples). When overlaid, test embeddings fall primarily within one region of the training manifold,
consistent with the dominant token observed in the token distribution, confirming that global
manifold topology is preserved under unseen input.
Figure 14. UMAP manifold projections for training, test, and overlay.
5. Discussion and Limitations
The central question of this work is whether collective honey bee buzzing contains structured,
repeatable acoustic states that can be recovered without supervision. The results across three
independent experiments consistently support that it does, with token separation, stable sub-
state structure, and preserved manifold topology on unseen recordings all emerging without
any imposed supervision.
One question is why models such as HuBERT, wav2vec, or AVES were not used as compari-
son baselines. These models carry inductive biases toward vocal production systems: HuBERT
and wav2vec target speech, AVES targets animal vocalizations. Honey bee buzzing does not
arise from such a system; it is mechanically generated through muscle activity. Applying a
vocally biased encoder to a mechanically generated signal would be methodologically unsound
rather than informative. PaSST was selected instead as a domain-agnostic audio encoder that
carries no vocal production assumptions. Continuous embeddings from PaSST alone capture
variation but do not produce a countable, reusable vocabulary; the vector quantization step
forces the model to commit to recurring patterns. The discretization is neither assumed to
be correct nor optimal; it is validated post-hoc by consistency, reuse, and separability. The
codebook matters here more than reconstruction; unlike work on vocal species, generating or
reconstructing similar sounds carries limited benefit when the signal is not a direct communi-
cation means.
Whether the evaluation is sufficient is also a fair challenge. JSD, entropy, clustering purity,
and token overlap are not ground truth validation, and this work does not claim they are. They
evaluate necessary conditions for meaningful structure rather than ground truth. Queen status
is used solely as a post-hoc analysis signal and is never exposed to the model during training,

---

## Page 19

BEEVE: UNSUPERVISED ACOUSTIC STATE DISCOVERY IN HONEY BEE BUZZING
19
not even as semi-supervision.
It serves to validate that real state discovery has occurred.
Whether these states reflect genuine biological structure or model artefacts cannot be fully
resolved without biological annotation. However, Sub-state A accounting for 57% of queenless
frames at over 97% purity is robust enough that consistent recurrence cannot plausibly be
attributed to noise.
The most significant limitation is scalability. The experiments use five hours of audio from
a controlled subset of the UrBAN dataset, chosen to study representation behaviour under
interpretable conditions rather than to maximise performance. The codebook result, while
stable, may not represent the full diversity of acoustic states across all hives, seasons, and
conditions in the full 1000 hours. The learning itself does not guarantee quality at scale; what
is demonstrated is the stability of learning under controlled conditions.
6. Conclusion
This work demonstrates that unsupervised discrete representation learning, using a Vector-
Quantized Variational Autoencoder trained on PaSST embeddings, can recover a discrete vo-
cabulary of acoustic states without any label supervision. The learned tokens are separated
from queenright and queenless states, and the queenless condition decomposes into coher-
ent sub-states, token transition analysis reveals distinct non-random sequential patterns, with
statistically significant dependencies between successive tokens confirmed across all three ex-
periments.
The broader contribution is conceptual as much as technical. This work does not claim to
identify new biological behaviours; rather, it demonstrates the capability to recover structured
acoustic patterns from a non-vocal species without any prior assumptions or annotations, in
a domain where most computational approaches assume predefined labels, known behaviour
categories, or vocal production structure. Honey bees are treated on their own terms, with
their signals modeled as emergent colony state rather than as communicative output borrowed
from vocal species frameworks. Extending this approach to the full dataset and grounding the
discovered sub-states through biological annotation remain the most immediate directions for
future work.
Non-invasive acoustic monitoring of this kind carries practical implications beyond the im-
mediate technical results. While queen loss and swarming detection are already established
targets in hive monitoring, the unsupervised nature of BeeVe opens the possibility of identify-
ing states beyond those currently labelled, capturing colony behaviour that inspection schedules
and predefined classifiers may miss entirely. Early detection of any such state without physical
inspection reduces colony disturbance and lowers the barrier to timely intervention, particularly
for small-scale beekeepers. More broadly, a tool that requires no annotated data to deploy con-
tributes to the movement toward species-sensitive, low-cost monitoring, supporting pollinator
conservation at a time of accelerating colony collapse.
References
1. Mahsa Abdollahi, Pierre Giovenazzo, and Tiago H Falk, Automated beehive acoustics monitoring: A com-
prehensive review of the literature and recommendations for future work, Applied Sciences 12 (2022), no. 8,
3920.
2. Mahsa Abdollahi, Yi Zhu, Heitor R Guimar˜aes, Nico Coallier, S´egol`ene Maucourt, Pierre Giovenazzo, and
Tiago H Falk, Urban: Urban beehive acoustics and phenotyping dataset, Scientific Data 12 (2025), no. 1,
536.

---

## Page 20

20
H. HAMMAMI AND N. ABDULAZIZ
3. Cleiton M Carvalho Jr, ´Icaro de Lima Rodrigues, and Danielo G Gomes, Unsupervised acoustic detection of
queenless hives in honeybees (apis mellifera ligustica), Brazilian e-Science Workshop (BreSci), SBC, 2025,
pp. 49–56.
4. Christine Erbe and Jeanette A Thomas, Exploring animal behavior through sound: Volume 1: Methods,
Springer Nature, 2022.
5. Sara Ferrari, Mitchell Silva, Marcella Guarino, and Daniel Berckmans, Monitoring of swarming sounds in
bee hives for early detection of the swarming period, Computers and electronics in agriculture 64 (2008),
no. 1, 72–77.
6. W Tecumseh Fitch, The evolution of speech: a comparative review, Trends in cognitive sciences 4 (2000),
no. 7, 258–267.
7. Karl von Frisch, The dance language and orientation of bees, Harvard University Press, 1993.
8. Masato Hagiwara, Aves: Animal vocalization encoder based on self-supervision, ICASSP 2023-2023 IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP), IEEE, 2023, pp. 1–5.
9. Hamze Hammami and Nidhal Abdulaziz, Beebetter: A multi-modal beehive system for honeybee health
monitoring and hazard detection, 2024 7th International Conference on Signal Processing and Information
Security (ICSPIS), IEEE, 2024, pp. 1–5.
10. Logan S James, Benjamin Hoffman, Jen-Yu Liu, Marius Miron, Milad Alizadeh, Emmanuel Fernandez,
Matthieu Geist, Diane Kim, Aza Raskin, Jon T Sakata, et al., Zebra finch females flexibly communicate
with each other and with ai-driven acoustic interaction models, bioRxiv (2026), 2026–02.
11. Dimitrios Kanelis, Vasilios Liolios, Fotini Papadopoulou, Maria-Anna Rodopoulou, Dimitrios Kampelopou-
los, Kostas Siozios, and Chrysoula Tananaki, Decoding the behavior of a queenless colony using sound
signals, Biology 12 (2023), no. 11, 1392.
12. WH Kirchner, Acoustical communication in honeybees, Apidologie 24 (1993), no. 3, 297–307.
13. Khaled Koutini, Jan Schl¨uter, Hamid Eghbal-Zadeh, and Gerhard Widmer, Efficient training of audio
transformers with patchout, arXiv preprint arXiv:2110.05069 (2021).
14. Axel Michelsen, Wolfgang H Kirchner, and Martin Lindauer, Sound and vibrational signals in the dance
language of the honeybee, apis mellifera, Behavioral ecology and sociobiology 18 (1986), no. 3, 207–212.
15. Orr Paradise, Pranav Muralikrishnan, Liangyuan Chen, Hugo Flores Garc´ıa, Bryan Pardo, Roee Diamant,
David F Gruber, Shane Gero, and Shafi Goldwasser, Wham: Towards a translative model of sperm whale
vocalization, arXiv preprint arXiv:2512.02206 (2025).
16. Michael Ramsey, M Bencsik, and MI Newton, Extensive vibrational characterisation and long-term moni-
toring of honeybee dorso-ventral abdominal vibration signals, Scientific Reports 8 (2018), no. 1, 14571.
17. David Robinson, Marius Miron, Masato Hagiwara, Benno Weck, Sara Keen, Milad Alizadeh, Gagan Narula,
Matthieu Geist, and Olivier Pietquin, Naturelm-audio: an audio-language foundation model for bioacous-
tics, arXiv preprint arXiv:2411.07186 (2024).
18. Eklavya Sarkar and Mathew Magimai Doss, Comparing self-supervised learning models pre-trained on hu-
man speech and animal vocalizations for bioacoustics processing, ICASSP 2025-2025 IEEE International
Conference on Acoustics, Speech and Signal Processing (ICASSP), IEEE, 2025, pp. 1–5.
19. Eklavya Sarkar and Mathew Magimai Doss, Towards leveraging sequential structure in animal vocalizations,
arXiv preprint arXiv:2511.10190 (2025).
20. Pratyusha Sharma, Shane Gero, Daniela Rus, Antonio Torralba, and Jacob Andreas, Whalelm: Finding
structure and information in sperm whale vocalizations and behavior with machine learning, bioRxiv (2024),
2024–10.
School of Engineering and Physical Sciences, Heriot-Watt University Dubai
Email address: hh2095@hw.ac.uk
School of Engineering and Physical Sciences, Heriot-Watt University Dubai
Email address: Nidhal.Abdulaziz@hw.ac.uk