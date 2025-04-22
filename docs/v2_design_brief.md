# V2 Design Brief: Employee Workload Forecaster

## Overview
Following the successful development of the V1 MVP, this document outlines the proposed enhancements for a V2 release. These are based on anticipated user needs, improved decision support, and greater planning functionality for small and medium-sized business teams.

## Key Enhancements

### 1. Feedback Loop Integration
- Add a lightweight feedback module (e.g., thumbs up/down, comment box).
- Track which tasks received GPT suggestions and whether users accepted or modified them.
- Future: Log user friction points to inform continuous product learning and feature prioritization.

### 2. Task Dependency Management
- Introduce optional task dependencies (e.g., “blocked by”, “precedes”).
- Highlight scheduling conflicts where dependent tasks create workload bottlenecks.
- Future: Enable lightweight Gantt view or blockers alert for cross-functional coordination.

### 3. Impact Scoring System
- Add scoring model: Priority × KPI alignment = “Impact Score”.
- Use scores to flag under-supported, high-value tasks.
- Optional: Quadrant visualization (e.g., High Impact / Low Support = urgent action).

### 4. Cross-Team and Department View
- Support filtering by team, role, or department (e.g., Engineering, Ops, Marketing).
- Enable team-level dashboards in addition to individual workload views.
- Plan for support of multi-team structures (e.g., pods or workstreams).

### 5. Decision Summary Export
- One-click export to PDF or HTML summary:
  - Overloaded team members
  - KPI/task alignment status
  - Unstaffed high-priority work
  - GPT recommendations
- Enables async review, stakeholder reporting, sprint planning

## Optional Enhancements
- "What-if" scenario modeling (e.g., remove a team member, shift due date)
- Feedback-powered GPT prompt refinement
- Lightweight audit log for tracking who changed what and when

## Modular Implementation Strategy

| Module                  | Owner        | Notes                                       |
|------------------------|--------------|---------------------------------------------|
| Feedback + Logging     | Frontend Dev | Streamlit input widget or modal             |
| Task Dependencies      | Backend Dev  | Extend data schema; apply validation rules  |
| Impact Scoring         | Data Logic   | Define formula, normalize, and rank         |
| Team Views             | Frontend Dev | Add filters/groupings to dashboard          |
| Export Summaries       | Frontend Dev | Use PDFkit or Streamlit HTML export options |

## V2 Goals
- Enable more strategic planning decisions
- Help teams focus on the highest-impact work
- Support leadership and PMs with actionable, exportable insights

This V2 reflects a shift from a workload visualizer to a proactive planning and prioritization tool