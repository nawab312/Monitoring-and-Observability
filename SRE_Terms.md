**SLI — Service Level Indicator**
- A quantitative measurement of some aspect of system performance.
- It’s a *metric*, not a goal.
- Examples: Request success rate (e.g., 99.95%), P95 latency (e.g., 180ms), Error rate (e.g., 0.1%)
- Example: “99.97% of HTTP requests returned 2xx or 3xx responses in the last 30 days.”


**SLO — Service Level Objective**
- A target value for an SLI over a defined time window.
- If SLI is the measurement, SLO is the goal.
- Example: “99.9% availability over a rolling 30-day window.”
- Imp: SLOs are internal engineering targets — not legal promises.


**SLA — Service Level Agreement**
- A formal contract with customers defining minimum service level and penalties if breached.


**Error Budget**
- The allowable amount of failure within an SLO window.
- If:
  - SLO = 99.9% availability
  - That means 0.1% failure allowed. That 0.1% = your error budget


**Toil**
- Manual, repetitive, automatable work that:
  - Scales linearly with growth
  - Provides no long-term value
