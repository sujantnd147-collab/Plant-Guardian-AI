# Plant Guardian AI

An advanced beginner-friendly web prototype for plant leaf image screening. It uses a MobileNetV2 transfer-learning model and a Streamlit interface.

## What it does
- Upload a JPG/PNG leaf photo.
- Predict one of the classes represented in your training dataset.
- Display the top prediction and top-three model scores.
- Show general care and monitoring suggestions.

> Important: This is an educational screening tool, not a laboratory diagnosis or pesticide recommendation system. A high model score does not prove the prediction is correct. Validate on images collected outside the training dataset and consult local agricultural experts for consequential decisions.

## 1. Requirements
- Python 3.10 or 3.11 recommended.
- A laptop/PC for local training, or Google Colab with a GPU runtime.
- PlantVillage image-folder dataset (or another correctly labelled image-folder dataset).

## 2. Folder structure
Your dataset folder must contain one folder per class, for example:

```text
data/PlantVillage/
  Tomato___healthy/
  Tomato___Early_blight/
  Tomato___Late_blight/
  Potato___healthy/
  Potato___Early_blight/
```

Each class folder should contain labelled JPG/PNG images. Keep the original dataset's class labels and licence/attribution information.

## 3. Install and train (local computer)
Open a terminal in this project folder:

```bash
python -m venv .venv
```

Activate it:
- Windows: `.venv\\Scripts\\activate`
- macOS/Linux: `source .venv/bin/activate`

Then run:

```bash
pip install -r requirements.txt
python train.py --data_dir data/PlantVillage --epochs 8 --fine_tune_epochs 3
```

Training creates:
- `models/plant_guardian_mobilenet.keras`
- `models/class_names.json`

For a first test, you can set `--fine_tune_epochs 0`.

## 4. Run the website

```bash
streamlit run app.py
```

Streamlit will show a local address (usually http://localhost:8501) to open in your browser.

## 5. Google Colab option
1. Upload this project ZIP to Google Drive and extract it in Colab.
2. Set Runtime → Change runtime type → T4 GPU (if available).
3. Install dependencies with `!pip install -r requirements.txt`.
4. Upload/extract your dataset into `data/PlantVillage`.
5. Run `!python train.py --data_dir data/PlantVillage --epochs 8 --fine_tune_epochs 3`.
6. Run the Streamlit app locally or deploy it after downloading the generated model files.

## 6. Model notes
- The model is not pre-trained for plant diseases when you first download this project. You must train it using your selected labelled dataset.
- The training script uses an 80/20 train-validation split and ImageNet MobileNetV2 transfer learning.
- Validation accuracy is not the same as real-world accuracy. Test with new photos from different phones, backgrounds, lighting, and farms.
- For a stronger final-year project, add a separate external test set, per-class precision/recall/F1, confusion matrix, Grad-CAM visual explanations, and user feedback logging with consent.

## 7. Suggested future upgrades
- Add Grad-CAM heatmaps to show which leaf region influenced a prediction.
- Add plant species selection and region-specific expert-reviewed advice.
- Add a database for scan history (with user consent).
- Add multilingual UI (Tamil/English).
- Add model monitoring and a feedback workflow for uncertain predictions.

## Dataset and attribution
Use a dataset whose licence permits your intended academic and deployment use. Cite the dataset source and its authors in your project report. Do not assume that every copy or mirror has the same licence.
