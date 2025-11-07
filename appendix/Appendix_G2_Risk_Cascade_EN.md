# Appendix G.2 — Risk Cascade & Consents

**License:** CC BY-NC 4.0 · © Aleksandr Kolomiets, 2025  
**Scope:** high-level protocol for gated escalation. Not psychotherapy.

## G2.0 Overview
Escalation is **confidence-gated** and **consent-driven**. No automatic outbound actions without prior, explicit user selection.

## G2.1 Multi-level consents
- **C0:** “No one” — Companion stays local only.
- **C1:** “Trusted person” — name/contacts provided by the user.
- **C2:** “Professional help” — helplines/clinics (country-specific).
- **C3:** “Emergency services” — only if user opted in and confirms at runtime.

Users can **revoke** any consent instantly.

## G2.2 Triggers & thresholds (illustrative)
- **Signal set:** self-report + linguistic risk markers + optional biomarkers (if provided).  
- **Threshold logic:** escalate only when *multiple* signals persist and the user opts in.

## G2.3 Escalation gates (stepwise)
1) **Mirror** (G.1) → confirm autonomy.  
2) **Offer choices** (tiny steps, yes/no).  
3) **If risk persists + consent allows:** propose **C1** — notify trusted person (draft editable by user).  
4) **If still high + consent allows:** propose **C2** — connect to professional resources.  
5) **C3** only with explicit runtime **yes** and pre-stored preference.

## G2.4 Deflection/shame handling (tone rules)
When signs of deflection/shame appear — reduce intensity, keep distance, **no pressure**. (Prevents over-closeness.)

## G2.5 Child mode (constraints)
Only binary risk flag may leave the device; guardian consent required for any outreach; language simplified; no adult content.

## G2.6 Audit trail (hash chain)
Each significant step can be recorded as a **hash of metadata** (time, class of action, consent level) → external logfile. No raw text/emotions are stored.

## G2.7 Data boundaries
No hidden persuasion; no sharing of raw emotional content; logs are opt-in and minimal.

## G2.8 Out-of-scope
Immediate crisis → show verified hotline list; Companion does not place emergency calls autonomously.

> See also: G.1 Mirror & Separation (normative language and boundaries).
