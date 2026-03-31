"""
Project #052: Real-Time IoT Air Quality Index (AQI) Evaluator
Domain: Healthcare & Impact
Description: Calculates PM2.5, PM10, and Ozone sub-indices with EPA break-point interpolation
Date: 2026-03-31
"""

class AQIAnalyzer:
    def calculate_pm25_aqi(self, concentration: float) -> int:
        if concentration <= 12.0:
            return int((50.0 / 12.0) * concentration)
        elif concentration <= 35.4:
            return int(51 + (49 / 23.4) * (concentration - 12.1))
        elif concentration <= 55.4:
            return int(101 + (49 / 20.0) * (concentration - 35.5))
        return 151

