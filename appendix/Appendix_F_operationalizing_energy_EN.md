```markdown
# Appendix F — Operationalizing the “Energy-Efficiency of Intervention” (E*)

## F1. Rationale
We define an ethical intervention as **the minimally sufficient intervention** that achieves non-worsening outcomes. To compare strategies, we aggregate costs and load into a single index **E\***.

## F2. Components of E\*
- **Physiology**: heart-rate variability (HRV: RMSSD/SDNN; ms)
- **Behavior**: time-to-stabilization; frequency of episodes
- **Compute**: local CPU/GPU load, on-device battery impact
- **Social**: false positives; user complaints / appeals

All components are z-scored against a baseline (Phase A). E\* is a weighted sum with weights pre-registered; sensitivity reported in SI.

## F3. Estimation & comparison
- ABA mini-studies (A–B–A′): mixed models (random intercept per participant)
- Pilot RCT: ANCOVA/LMM, group factor (companion vs. active control)
- Strategy comparison is performed **under a fixed intervention budget** (time quota, compute cap), making “thrift” measurable rather than implicit.

## F4. Child scenario
The companion acts as a **supportive external regulator**, not surveillance. Prompts are phrased in the language of care; directive interpretations of intentions are avoided. Primary ethics goal: reduce shame and avoid “I am dangerous / I am guilty” internalizations.

## F5. Reporting
We report: (i) ΔHRV, (ii) Δtime-to-stabilization, (iii) Δepisode rate, (iv) compute footprint, (v) appeals ratio. Lower E\* at non-worse primary outcomes is considered ethically superior.
**Authorship & tools.** Drafted by the human lead author Aleksandr Kolomiets ORCID 0009-0008-5153-5546 with assistance from an AI writing tool (GPT-5 Thinking, “Logos”).
