
import torch
from torchvision import models
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt

# Step 1: Load AI model
print("Loading AI model...")

weights = models.MobileNet_V2_Weights.DEFAULT
model = models.mobilenet_v2(weights=weights)
model.eval()

preprocess = weights.transforms()
categories = weights.meta["categories"]

print("AI model loaded successfully!")


# Step 2: Image classification function
def classify_image(image_path):

    try:
        image_path = Path(image_path)

        if not image_path.exists():
            print("Image not found:", image_path)
            return

        # Open image
        image = Image.open(image_path).convert("RGB")

        # Preprocess image
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        # Make prediction
        with torch.inference_mode():
            output = model(input_batch)

        # Calculate probabilities
        probabilities = torch.nn.functional.softmax(
            output[0], dim=0
        )

        # Get top 3 predictions
        top_probabilities, top_indices = torch.topk(
            probabilities, 3
        )

        # Print predictions
        print("\nImage:", image_path)
        print("Predicted Results:")

        for probability, index in zip(
            top_probabilities, top_indices
        ):
            label = categories[index.item()]
            confidence = probability.item() * 100
            print(f"{label}: {confidence:.2f}%")

        # Best prediction
        best_index = top_indices[0].item()
        best_label = categories[best_index]
        confidence = top_probabilities[0].item() * 100

        # Display image and prediction
        plt.figure(figsize=(7, 6))
        plt.imshow(image)

        plt.title(
            f"AI Prediction: {best_label}\n"
            f"Confidence: {confidence:.2f}%",
            fontsize=13
        )

        plt.axis("off")
        plt.tight_layout()
        plt.show()

    except Exception as error:
        print("Error processing image:", error)


# Step 3: Image paths
image_paths = [
    r"E:\jyoti\sample_images\dog.png"
]


# Step 4: Classify images
for image_path in image_paths:
    classify_image(image_path)

print("\nImage classification completed!")
