# How the platform fits together

**Croc Nexus AI Technologies** is an **AI startup**. AI recognises events, scores urgency, routes calls, and escalates — people respond first; **embodied systems, drones, security devices, and more** on the roadmap.

## Network first

Every deployment assumes the **site has usable internet** (Wi‑Fi or wired). Connected equipment at the site uses that network to reach the cloud; staff phones receive alerts through the same path.

---

## Croc Sentinel — connected to cloud

```text
Equipment at the site
        │
        │  site network (required)
        ▼
Online service + control screen
        │
        ├── phone / email / messaging alerts
        ├── linked camera photos
        └── remote updates
```

- Each organisation sees only its own devices and staff  
- Devices in the same group can react together  
- Sensitive credentials are not stored permanently on local equipment  

---

## Croc Coordination — from alert to action

```text
Something detected
      │
      ▼
Recognise event + urgency (+ camera if linked)
      │
      ├── phone call to admin or assigned agent
      ├── app alert to on-duty staff
      └── audit log
      │
      ▼
Person goes to check on site
      │
      ▼
Resolve · escalate if still open · record outcome
```

**Today:** response depends on **people** — admin or agent travels to the site.  
**Later:** the same pipeline can add **embodied intelligence**, **drones**, **security devices**, and other connected equipment — to **reach the location, patrol, or act on site** — introduced step by step per site.

- Fixed rules always run first; smarter layers add detail when available  
- If smart services are offline, rule-based results and calls still work  
- Sensitive automated steps wait for a person to approve  

---

## Where it applies

Government buildings, malls, hospitals, plazas, parks, roads, traffic junctions, commercial zones, campuses, and residential communities — with **individual home use** on the roadmap. Layout and call lists are configured per site.

---

## CAO (internal small model)

**CAO** is a compact model Croc Nexus is training for in-house coordination — alert scoring, routing, and follow-up. It is **not publicly open** today and remains **exclusive to Croc Nexus AI Technologies**.

Production customers use **Croc Coordination** with rule-based safety logic plus the smart features already shipped. CAO stays **internal to Croc Nexus** until we choose to extend it on our own terms.

---

## Customisation

We are a **startup**: many sites need small changes — extra groups, different escalation paths, or new integrations. All of this runs on **Croc Nexus–owned** cloud, apps, and AI — we do **not** provide branded or white-label apps. We review each request for **fit and timeline** before committing.

See the main README section *Built for your site — on our platform* for typical examples.

---

## Safety and access

| Topic | Croc Sentinel | Croc Coordination |
|:------|:--------------|:------------------|
| Connection security | Encrypted links to cloud and update server | Encrypted access to coordination service |
| Commands | Only with authorised access | Permission by role |
| Remote updates | Only from approved download locations | — |
| Data separation | Each customer’s data kept apart | Each customer’s data kept apart |
| History | Full event log | Full decision log |
