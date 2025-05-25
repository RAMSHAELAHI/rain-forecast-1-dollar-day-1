import streamlit as st # type: ignore

# OOP Class for Rain Forecast
class RainForecast:
    def __init__(self, humidity, temperature):
        self.humidity = humidity
        self.temperature = temperature

    def predict(self):
        if self.humidity > 80 and self.temperature < 25:
            return "High chance of rain ☔"
        elif self.humidity > 60:
            return "Moderate chance of rain 🌦️"
        else:
            return "Low chance of rain 🌤️"

# Streamlit UI
st.title("🌧️ Rain Forecast App")

humidity = st.slider("Humidity (%)", 0, 100, 70)
temperature = st.slider("Temperature (°C)", -10, 45, 22)

if st.button("Predict"):
    forecast = RainForecast(humidity, temperature)
    result = forecast.predict()
    st.success(result)
