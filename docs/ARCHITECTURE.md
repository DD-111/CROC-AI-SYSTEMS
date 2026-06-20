# How the platform fits together

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
Alarm arrives
      │
      ▼
Smart layer reads signals + photos
      │
      ▼
Urgency score, reasons, suggested steps
      │
      ▼
Notify staff · wait for approval · log everything
```

- Fixed rules always run first; smarter layers add detail when available  
- If smart services are offline, rule-based results still work  
- Sensitive steps wait for a person to approve  

---

## CAO (internal small model)

**CAO** is a compact model Croc Nexus is training for in-house coordination — alert scoring, routing, and follow-up. It is **not publicly open** today and remains **exclusive to Croc Nexus AI Technologies**.

Production customers use **Croc Coordination** with rule-based safety logic plus the smart features already shipped. CAO will be offered when we are ready to open it beyond internal use.

---

## Customisation

We are a **startup**: many sites need small changes — extra groups, different escalation paths, branded apps, or new integrations. We review each request for **fit and timeline** before committing.

See the main README section *Built to adapt & customize* for typical examples.

---

## Safety and access

| Topic | Croc Sentinel | Croc Coordination |
|:------|:--------------|:------------------|
| Connection security | Encrypted links to cloud and update server | Encrypted access to coordination service |
| Commands | Only with authorised access | Permission by role |
| Remote updates | Only from approved download locations | — |
| Data separation | Each customer’s data kept apart | Each customer’s data kept apart |
| History | Full event log | Full decision log |
