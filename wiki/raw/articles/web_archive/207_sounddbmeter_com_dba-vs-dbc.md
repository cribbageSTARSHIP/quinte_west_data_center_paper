---
title: "dBA vs dBC: Difference Between A and C Weighting (With Chart)"
subtitle: "Category: Acoustics (dBA vs dBC) & Health Impacts | Evidence ID: #207"
date: "Archived: 2026-10-04 20:20"
---

* **Original URL:** <https://sounddbmeter.com/dba-vs-dbc/>
* **Research Category:** Acoustics (dBA vs dBC) & Health Impacts
* **Archival File:** `207_sounddbmeter_com_dba-vs-dbc.pdf`
* **Extraction Status:** Full Web Transcript PDF

---

# Source Content

Short answer: dBA (A-weighting) turns down low and very high frequencies to match how human ears hear everyday sounds, so it is used for hearing-risk and environmental limits. dBC (C-weighting) is almost flat and keeps the bass, so it is used for peaks, loud music and low-frequency noise. For bass-heavy sounds, dBC reads much higher than dBA.
Both are frequency weightings defined in the sound level meter standard IEC 61672-1. They don’t measure different things: they measure the same sound pressure level, filtered differently before it is averaged. This guide shows the two curves, the exact corrections at each frequency, when to use which, and what the gap between dBC and dBA tells you.
dBA vs dBC vs dBZ at a Glance
|  | dBA (A-weighting) | dBC (C-weighting) | dBZ (Z-weighting) | 
|---|---|---|---|
| Frequency response | Strongly reduces bass below about 500 Hz and the very highest frequencies | Almost flat from about 31.5 Hz to 8 kHz; small roll-off at the extremes | Flat (“zero”) from 10 Hz to 20 kHz | 
| Based on | Human hearing at moderate levels (the 40-phon equal-loudness curve) | Hearing at high levels (around 100 phon), when bass sounds relatively louder | No hearing model: the raw pressure | 
| Typical use | Workplace noise (OSHA, NIOSH, EU), traffic and neighbour noise, product ratings | Peak and impulse noise, concerts and clubs, subwoofers, home cinema calibration | Analysis, research, frequency spectra | 
| Example (diesel engine idling) | 80 dBA | About 90 dBC | About 91 dBZ | 
A and C Weighting Values by Frequency
These are the corrections a sound level meter applies at each octave-band centre frequency (IEC 61672-1). A negative number means the meter turns that frequency down before adding everything up.
| Frequency | A-weighting (dB) | C-weighting (dB) | Z-weighting (dB) | 
|---|---|---|---|
| 20 Hz | −50.5 | −6.2 | 0 | 
| 31.5 Hz | −39.4 | −3.0 | 0 | 
| 63 Hz | −26.2 | −0.8 | 0 | 
| 125 Hz | −16.1 | −0.2 | 0 | 
| 250 Hz | −8.6 | 0.0 | 0 | 
| 500 Hz | −3.2 | 0.0 | 0 | 
| 1,000 Hz | 0.0 | 0.0 | 0 | 
| 2,000 Hz | +1.2 | −0.2 | 0 | 
| 4,000 Hz | +1.0 | −0.8 | 0 | 
| 8,000 Hz | −1.1 | −3.0 | 0 | 
| 16,000 Hz | −6.6 | −8.5 | 0 | 
| 20,000 Hz | −9.3 | −11.2 | 0 | 
Between 500 Hz and 4 kHz, the three weightings agree within about 3 dB, so speech and most everyday sounds read almost the same in dBA and dBC. The difference appears with bass: at 63 Hz a tone reads 26 dB lower in dBA than in dBC. (Frequency and level are separate properties of a sound; see dB vs Hz.)
Why Hearing and Noise Limits Use dBA
At normal levels your ears are far less sensitive to low frequencies, and low frequencies are also less damaging to the inner ear for the same pressure. A-weighting mirrors that, so a single dBA number tracks both how loud a sound seems and its risk to hearing. That is why the 8-hour limits of OSHA and NIOSH (90 and 85 dB(A)), the EU action values (80 and 85 dB(A)) and most environmental and appliance ratings are in dBA. Check a working day with the noise exposure calculator.
When to Use dBC
- Peaks and impulses: gunshots, hammer blows and fireworks are limited by their C-weighted peak. The EU sets peak action values of 135 and 137 dB(C) and a limit of 140 dB(C); see is 130 dB loud?
- Concerts and clubs: most of the energy is in the bass, which dBA mostly ignores, so many venues and festivals monitor dB(C) alongside dB(A).
- Home cinema and studios: speaker levels are traditionally calibrated with pink noise to 85 dB C-weighted (slow) per channel for film reference level.
- Low-frequency noise complaints: humming from heat pumps, transformers, ventilation or a neighbour’s subwoofer may read quietly in dBA but loud in dBC; see apartment noise complaint levels.
What the Gap Between dBC and dBA Tells You
Measure the same sound in both weightings and subtract. A small gap (0–5 dB) means the sound is mostly in the mid and high frequencies, like speech or a vacuum cleaner. A large gap means strong bass. The WHO Guidelines for Community Noise note that when dB(C) exceeds dB(A) by more than 10 dB, low-frequency content is significant and a frequency analysis should be considered, because dBA alone underestimates the annoyance.
| Sound | Typical dBC − dBA | What it means | 
|---|---|---|
| Speech, TV dialogue | 0–3 dB | Mid-frequency sound: dBA is a fair summary | 
| Vacuum cleaner, hair dryer | 1–4 dB | Mostly mid and high frequencies | 
| Road traffic at a distance | 5–10 dB | Tyre noise plus engine rumble | 
| Diesel engine, ventilation plant | 8–15 dB | Strong low-frequency content | 
| Club music, subwoofer, bass through a wall | 15–25 dB or more | Bass dominates; dBA underestimates how intrusive it is | 
To see exactly which frequencies are responsible, use the frequency analyzer. To hear the effect, play a 63 Hz tone with the tone generator and compare the meter in dB(A) and dB(C). For a worked example at one level, see 90 dBA vs 90 dBC.
Frequency Weighting vs Time Weighting
The letter after dB is the frequency weighting. Separately, meters apply a time weighting: Fast (125 ms), Slow (1 s) or Impulse. Standard notation combines both: LAF is A-weighted Fast, LAeq is the A-weighted energy average, LCpeak is the C-weighted peak. Music loudness uses yet another curve, K-weighting, which gives LUFS values; measure them with the audio loudness meter.
Which Weighting Does Our Meter Use?
The free sound decibel meter on our homepage shows dB(A), dB(C) and dB(Z), using A and C filters built to the IEC 61672 formulas, with Fast or Slow time weighting. Use dB(A) for “how loud is it and is it safe”, and dB(C) or dB(Z) when bass matters. Our guide on how to measure decibels covers placement and averaging. Phone microphones roll off at low frequencies, so dB(C) and dB(Z) readings of deep bass are less reliable than dB(A); online decibel meter accuracy explains why, and you can improve readings if you calibrate your microphone.
Frequently Asked Questions
Is dBC louder than dBA?
For the same sound, dBC is equal to or higher than dBA, because it removes less bass. The difference ranges from almost 0 dB for speech to 20 dB or more for bass-heavy music.
Can I convert dBA to dBC?
Not with a fixed number. The difference depends on how much low-frequency energy the sound has, so you need to measure both or analyse the spectrum.
Which is more accurate, dBA or dBC?
Both are equally accurate; they answer different questions. dBA estimates perceived loudness and hearing risk; dBC captures the full energy, including bass.
What is dBZ?
Z-weighting (zero) is flat from 10 Hz to 20 kHz. It replaced the older “linear” or “flat” settings and shows the unweighted sound pressure level.
What is the difference between dB and dBA?
Plain dB is an unweighted level (or a ratio); dBA is the A-weighted level. See dB vs dBA for that comparison, and the decibel units guide for every dB unit.
