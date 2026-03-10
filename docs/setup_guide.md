# Setup Guide

This document explains how to assemble and run the Raspberry Pi Flood Monitoring System.

## Step 1 — Prepare Raspberry Pi

Install Raspberry Pi OS and ensure Python 3 is available.

## Step 2 — Enable Interfaces

Run:

sudo raspi-config

Enable I2C if you are using the BME280 sensor.

## Step 3 — Install Python Dependencies

Run:

pip install -r requirements.txt

## Step 4 — Connect Ultrasonic Water-Level Sensor

Typical wiring:

- TRIG → GPIO23
- ECHO → GPIO24
- VCC → 5V
- GND → Ground

## Step 5 — Connect BME280

Typical wiring:

- VCC → 3.3V
- GND → Ground
- SDA → GPIO2
- SCL → GPIO3

## Step 6 — Run Water-Level Script

python3 src/read_water_level.py

## Step 7 — Test Logging

python3 src/log_flood_data.py

## Step 8 — Test Alerts

python3 src/flood_alerts.py
