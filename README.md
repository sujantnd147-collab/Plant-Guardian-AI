# Plant Guardian AI — Streamlit starter project

## Run locally
1. Install Python 3.10 or newer.
2. Extract this project ZIP.
3. Open a terminal in the `Plant_Guardian_AI` folder.
4. Create and activate a virtual environment (recommended).
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Start the app:
   ```bash
   streamlit run app.py
   ```

## Project layout
- `app.py`: main navigation and dashboard
- `config.py`: shared configuration
- `database.py`: SQLite plant profiles and reminders
- `features/`: one Python module per feature

## Important limitations
This is a working modular UI starter, not a complete trained AI system.
Disease/species/pest/fruit/root image predictions are not enabled. Add a validated
vision model before presenting predictions. Weather works only with a valid
OpenWeatherMap API key entered in the weather page. Rain prediction needs a
forecast endpoint or a trained forecasting model. Sensor readings are manual
until hardware integration is implemented. Crop profitability depends on local
yield, prices and costs and is only an estimate.

Do not use pesticide products or fertilizer doses based on an unverified AI
guess. Follow local regulations, product labels and agricultural advice.
