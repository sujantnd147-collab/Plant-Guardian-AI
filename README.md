# Plant Guardian AI — Fixed starter project

This is a mobile-friendly Streamlit web app. It can be opened from Android Chrome or a laptop browser after deployment.

## Files
- `app.py` — app interface, image upload, optional model prediction, and general care checklist.
- `requirements.txt` — packages needed to run the web app.
- `train_model.py` — optional starter script for training a classifier on a labelled dataset.

## Fix the existing GitHub deployment

1. Open your `Plant-Guardian-AI` GitHub repository.
2. Replace the existing root-level `app.py` with this package's `app.py`.
3. Replace `requirements.txt` with this package's `requirements.txt`.
4. You may also upload `train_model.py` and `README.md`.
5. Commit the changes.
6. In Streamlit Community Cloud, open the app's menu and choose Reboot app (or wait for it to redeploy after the commit).

The main file path in Streamlit must be exactly `app.py` and the file must be at the repository root.

## Important: model status

This package does **not** include a trained disease-detection model. Without the model, the app accepts and displays a photo but deliberately does not invent a disease prediction.

To enable predictions, add both files to the repository root:
- `plant_disease_model.keras`
- `class_names.txt` — one class name per line, in the same order as the model output.

## Optional training

Create a folder called `dataset` with one subfolder per labelled class, for example:

```text
dataset/
  Healthy/
  Tomato___Early_blight/
  Tomato___Late_blight/
```

On a computer with Python and TensorFlow installed:

```bash
pip install tensorflow
python train_model.py dataset
```

The script produces the model and label files. Training accuracy alone does not prove real-world reliability. Test with separate images taken in varied lighting and backgrounds.

## Disclaimer

This is an educational prototype, not a confirmed plant diagnosis tool. Verify important plant-health decisions with a local agricultural expert. Do not apply pesticides based only on an app prediction.
