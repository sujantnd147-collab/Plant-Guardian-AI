def care_advice(class_name: str):
    name = class_name.lower()
    if "healthy" in name:
        return [
            "Continue checking new leaves and the underside of leaves weekly.",
            "Water according to the plant and soil needs; avoid keeping soil waterlogged.",
            "Provide suitable light and airflow for this plant species.",
            "Keep a record of changes so early symptoms are easier to notice."
        ]
    advice = [
        "Inspect several leaves and stems; one photo is not enough to confirm a disease.",
        "Remove severely affected fallen plant material where appropriate and clean tools after use.",
        "Avoid overhead watering if leaves remain wet for long periods; improve spacing and airflow.",
        "Check watering, drainage, light, and nutrient conditions because non-disease stress can look similar.",
        "If symptoms spread, consult a local agricultural extension officer before applying any treatment."
    ]
    if "blight" in name:
        advice.insert(1, "Watch for expanding spots or lesions and monitor whether new leaves are affected.")
    if "mildew" in name:
        advice.insert(1, "Look for powdery or fuzzy growth on both leaf surfaces and compare with a reliable local guide.")
    return advice
