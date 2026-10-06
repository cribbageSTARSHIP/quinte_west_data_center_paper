---
title: "dBA vs dBC: Which One Should You Use?"
subtitle: "Category: Acoustics (dBA vs dBC) & Health Impacts | Evidence ID: #206"
date: "Archived: 2026-10-04 20:20"
---

* **Original URL:** <https://realtimesoundmeter.org/blog/dba-vs-dbc>
* **Research Category:** Acoustics (dBA vs dBC) & Health Impacts
* **Archival File:** `206_realtimesoundmeter_org_blog_dba-vs-dbc.pdf`
* **Extraction Status:** Full Web Transcript PDF

---

# Source Content

dBA vs dBC: Which One Should You Use?
Updated Mar 30, 2026 • 7 min read
If you've ever looked at the technical specifications of a sound level meter, or even just browsed the settings of a noise measurement app, you've likely encountered two mysterious acronyms: dBA and dBC.
Both measure sound pressure levels in decibels (dB), but they can give you two completely different numbers for the exact same noise source. For example, a diesel generator might measure 85 dBA but 100 dBC.
Why the difference? And more importantly, if you are trying to determine if a noise is dangerous or illegal, which one should you use? This guide will demystify frequency weighting networks and help you choose the right setting for the job.
The Problem: Your Ears Aren't Microphones
To understand dBA and dBC, you first need to understand human hearing. Our ears are not "flat" frequency receivers. We are extremely sensitive to mid-range frequencies (where human speech lies, roughly 500 Hz to 4,000 Hz) but quite insensitive to very low frequencies (bass) and very high frequencies (treble).
If you play a 100 Hz tone (low bass) and a 1,000 Hz tone (mid-range whistle) at the exact same physical intensity, the 1,000 Hz tone will sound much louder to you.
Standard microphones, however, don't discriminate. They measure raw sound pressure regardless of pitch. To make a sound meter match what humans actually hear, engineers created electronic filters known as Frequency Weightings.
dBA: The "Human Ear" Standard
A-Weighting (dBA) is the most common filter. It drastically cuts (attenuates) low-frequency sounds to mimic the human ear's response at low-to-moderate volume levels.
- What it does: It treats low bass sounds as "less important," just like your brain does.
- When to use it: Almost always. It is the international standard for assessing hearing damage risk, environmental noise pollution, and OSHA/NIOSH compliance.
- The Logic: Since your ears are less sensitive to bass, low-frequency noise is less likely to cause hearing damage unless it is extremely loud. Therefore, dBA is the best predictor of potential hearing loss.
Most simple noise apps and our own Online Sound Meter primarily reflect A-weighted or "speech-band" measurements because that's what matters for general health and safety.
dBC: The "Bass Heavy" Standard
C-Weighting (dBC) is a much flatter filter. It includes much more of the low-frequency energy in the measurement. It doesn't cut the bass nearly as much as dBA.
- What it does: It provides a reading that is closer to the "true" physical sound pressure level across all frequencies.
- When to use it: When measuring machinery with heavy vibration, engines, compressors, or entertainment systems with subwoofers.
- The Logic: Sometimes, you need to know about the bass. For example, low-frequency noise can travel through walls and cause structural vibration, even if it doesn't "sound" loud to the human ear.
The Comparison: When Numbers Don't Match
Here is a practical rule of thumb used by acoustical engineers: Measure the noise in both dBA and dBC.
The "Low Frequency" Test
dBC - dBA = ?
Difference is Small (< 10 dB)
The noise is mostly mid/high frequency. (e.g., whistling air, conversation, electric motor whine)
Difference is Large (> 15 dB)
There is a significant low-frequency component. (e.g., diesel engine, bass music, wind turbulence)
Try a Simple Demo (Using Spectrum as a Proxy)
Our browser meter is designed for practical comparisons and includes a frequency spectrum. It does not switch between dBA and dBC modes, but you can still learn what “low-frequency heavy” means by watching where the energy sits.
- Open the Speaker Test (tones) and pick 100 Hz.
- In another tab, open the Online Sound Meter.
- Measure 30 seconds at a fixed position and note the average.
- Repeat with 1,000 Hz at the same device volume setting and compare the spectrum peak location.
- Log your results using this CSV template: weighting-demo-tones.csv.
Quick Reference: dBA vs dBC Levels
Because dBC includes low frequencies that dBA ignores, dBC readings are almost always higher. The gap between them tells you how much "bass" is present.
| Sound Source | dBA (What you hear) | dBC (Actual Energy) | Difference | 
|---|---|---|---|
| Conversational Speech | 60 dBA | 62 dBC | Small (~2 dB) | 
| Vacuum Cleaner | 70 dBA | 75 dBC | Moderate (~5 dB) | 
| Diesel Truck Idling | 85 dBA | 100 dBC | Large (~15 dB) | 
| Bass-Heavy Music | 95 dBA | 110 dBC | Very Large (~15+ dB) | 
| Wind Turbine (Near) | 50 dBA | 70 dBC | Large (~20 dB) | 
Which One Should YOU Use?
For 99% of people reading this, the answer is dBA.
Protecting Your Hearing
If you want to know "Is this safe?", use dBA. All safety charts (like the 85 dB limit) are based on dBA.
Neighborhood Noise Complaints
Most local noise ordinances specify limits in dBA. If your neighbor's dog is barking, measure in dBA.
Home Theater / Car Audio
If you are tuning a subwoofer or testing soundproofing, dBA will ignore the bass you are trying to measure. Use dBC (or Z-weighting/Flat if available).
Conclusion
Acoustics can be complicated, but using a sound meter shouldn't be. Just remember: A is for "Audio" (what humans hear), and C is for "Complete" (the full physical energy).
If you are concerned about noise exposure in your daily life, stick to dBA. And if you've been working in a loud environment and things are starting to sound muffled, don't wait. Use our Free Online Hearing Test to check for any signs of hearing loss.
