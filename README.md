
# Carbon Emissions Tracker

This project is a simple interactive app built using **Python** and **Streamlit** to help users estimate their personal **carbon footprint** from common daily activities like driving, flying, and electricity use.

## Features
- Input activity and usage (e.g., distance driven or kWh consumed)
- Calculates CO₂ emissions using UK Government emission factors
- Clean and interactive UI with Streamlit

## Technologies Used
- Python
- Streamlit
- Pandas (optional)
- Publicly available emission data

## Emission Factors Used
- Driving: 0.21 kg CO₂/km
- Flying: 0.25 kg CO₂/km
- Electricity: 0.233 kg CO₂/kWh (UK average)

## To Run the App
1. Install dependencies:
```
pip install streamlit
```
2. Run the app:
```
streamlit run app/main.py
```

## Data Sources
- [UK Government GHG Conversion Factors](https://www.gov.uk/government/collections/government-conversion-factors-for-company-reporting)
- [Our World in Data](https://ourworldindata.org/co2-emissions)

## License
Open source under the MIT License.
