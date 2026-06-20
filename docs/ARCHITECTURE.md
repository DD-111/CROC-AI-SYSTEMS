# How the platform fits together

## Croc Sentinel — field to cloud

```text
CS-M401–M407 on site
        │
        │ secure link to cloud
        ▼
Online service + control screen
        │
        ├── phone / email / messaging alerts
        ├── linked camera photos
        └── remote device updates
```

**Basics**

- Each organisation sees only its own devices and staff
- Devices in the same group can react together (e.g. sirens together)
- New units are registered at the factory, then claimed on site
- Camera passwords are not stored permanently on field hardware

## Croc Coordination — from alert to action

```text
Alarm arrives
      │
      ▼
Smart layer reads signals + photos
      │
      ▼
Risk score, reasons, suggested steps
      │
      ▼
Notify staff · wait for approval · log everything
```

**Basics**

- Fixed rules always run first; smart text layers on top when available
- If smart services are offline, rule-based results still work
- A lead workflow plans, assigns, checks, and reviews before anything sensitive goes out

## cMax workspace

- See which devices are online and battery or signal health
- Watch alarms and smart results on a map or timeline
- Follow what each automated step did and who approved it
- Overlay buildings and campuses in 2D or 3D

## Safety and access

| Topic | Croc Sentinel | Croc Coordination |
|-------|---------------|-------------------|
| Connection security | Encrypted links to cloud and update server | Encrypted access to coordination service |
| Device commands | Only with authorised keys | Role-based permissions |
| Remote updates | Only from approved download locations | — |
| Data separation | Each customer’s data kept apart | Each customer’s data kept apart |
| History | Full event log | Full decision log |
