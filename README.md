# Raspberry Pi Flood Monitoring System

An open-source Raspberry Pi flood monitoring system for river-level sensing, rainfall monitoring, local alerts, and resilience-oriented hydrological observation.

This project is designed as a reproducible prototype for engineers, students, and researchers interested in hydrological sensing, climate resilience, and flood-risk monitoring.

## SDG Alignment

Primary:

SDG 6 — Clean Water and Sanitation
SDG 13 — Climate Action

Supporting:

- SDG 11 — Sustainable Cities and Communities

Reliable flood resilience depends on reliable environmental observation. This project demonstrates how low-cost edge devices can improve local visibility into hydrological risk.

## System Overview

The monitoring system uses a Raspberry Pi as a local flood observation node that reads river-level and rainfall-related sensors, stores observations, and supports threshold-based alerts.

Typical monitored variables include:

- water level
- rainfall
- temperature
- humidity
- atmospheric pressure

## Hardware Components

- Raspberry Pi 4 or Raspberry Pi Zero 2 W
- ultrasonic distance sensor
- tipping-bucket rain gauge
- BME280 environmental sensor
- microSD card
- solar power system or fixed supply
- weatherproof enclosure

## System Architecture

The monitoring system follows an edge-observation pipeline:

Water-Level Sensors → Raspberry Pi → Local Logging / Alert Logic → Optional Dashboard / Export

The Raspberry Pi acts as a local flood-monitoring node capable of supporting long-term hydrological observation.

## Repository Structure

raspberry-pi-flood-monitoring-system/

README.md
LICENSE
requirements.txt

src/
  read_water_level.py
  log_flood_data.py
  rainfall_monitor.py
  flood_alerts.py
  anomaly_detection.py

docs/
  setup_guide.md
  deployment_notes.md
  sensor_notes.md

data/
  example_flood_readings.csv

hardware/

## Applications

This prototype supports several environmental and engineering applications:

- river and watershed monitoring
- flood-risk observation
- drainage and stormwater studies
- resilience infrastructure pilots
- hydrology education

## License

This project is released under the MIT License.

## Sustainable Catalyst

This project is part of the Sustainable Catalyst Sustainability Engineering Series.
