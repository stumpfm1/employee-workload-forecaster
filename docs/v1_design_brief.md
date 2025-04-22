# V1 Design Brief: Employee Workload Forecaster

## Overview
This document outlines the scope, purpose, and success criteria for the V1 MVP of the Employee Workload Forecaster. The primary objective was to create a lightweight, low-cost forecasting tool for small and medium-sized business teams to better understand individual workload distribution.

## Target Users
- Startup founders managing lean, multi-role teams
- Project managers and program leads in resource-constrained environments
- Chiefs of Staff and BizOps partners supporting cross-functional delivery
- Operations managers seeking visibility into team capacity

## MVP Goals
- Accept task-level input via CSV upload
- Parse tasks by owner and effort (estimated hours)
- Aggregate and visualize total effort per individual
- Deliver time-to-insight in under 2 minutes
- Require no paid software, backend, or persistent login

## Core Features (V1)
- CSV uploader with task preview
- Column validation (requires 'Owner' and 'Estimated Hours')
- Aggregated workload calculation using `pandas`
- Visual bar chart of workload by team member using `plotly.express`
- Warning for missing required columns

## Deliberate Exclusions (for MVP)
- No dependency management or scheduling logic
- No KPI tagging or impact scoring
- No feedback collection or export functionality
- No GPT integration or task rebalancing
- No persistent storage, accounts, or multi-user support

## Constraints
- Must run locally or via Streamlit Cloud
- Must execute within 1–2 minutes on low-resource machines
- Must require no API keys or authentication setup

## Success Criteria
| Metric                   | Target                            |
|-------------------------|-----------------------------------|
| Time to Insight         | < 2 minutes post-upload            |
| Accuracy                | 100% workload reflection by Owner |
| User Setup Time         | < 5 minutes to get started        |
| Deployment Footprint    | < 100 MB memory, no backend       |

## Notes
This V1 was intentionally scoped to demonstrate core logic, value hypothesis, and visualization capability. It forms the foundation for a more strategic planning tool in V2.
