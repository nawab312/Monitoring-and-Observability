**Creating Alerts in Grafana**

An alert is a mechanism that monitors specific conditions in your data and triggers notifications when those conditions meet predefined thresholds. For example, an alert could notify you if CPU usage exceeds 90% or if a service is down.

Steps to Create an Alert in Grafana:
-Open a Dashboard:
  -Start by creating a new or opening an existing dashboard where you have time-series data visualized.
- Create or Modify a Panel:
  - In Grafana, alerts are typically associated with panels. These panels are where your metrics (data points) are visualized (e.g., graphs, tables).
  - Once you've created your panel, click the "Alert" tab from the panel's settings.
- Set Up Alert Condition:
  - Within the Alert tab, you’ll define the conditions under which the alert will be triggered. You can specify conditions based on the metric (e.g., CPU usage, disk space, etc.) and set the threshold for when to send an alert.
  - Example: You might set an alert condition like “CPU usage > 85% for 5 minutes” to be triggered.
- Configure Alert Evaluation:
  - Alerts are evaluated periodically (e.g., every 1 minute or every 5 minutes). The alert will be triggered if the condition is met continuously over the specified duration (e.g., for 5 minutes or 10 minutes).
  - You can configure the evaluation frequency and threshold.
- Test the Alert:
  - Before finalizing, you can test the alert to ensure it triggers when expected based on the conditions and thresholds.
- Save the Alert:
  - Once the conditions are set and tested, save your alert settings.
