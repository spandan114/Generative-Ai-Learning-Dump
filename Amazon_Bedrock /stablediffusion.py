import boto3
import json
import base64
import os

prompt_data = """
provide me an 4k hd image of a beach, also use a blue sky rainy season and
cinematic display
"""
prompt_template=[{"text":prompt_data,"weight":1}]
bedrock = boto3.client(service_name="bedrock-runtime")
payload = {
    "text_prompts":prompt_template,
    "cfg_scale": 10,
    "seed": 0,
    "steps":50,
    "width":512,
    "height":512

}

body = json.dumps(payload)
model_id = "stability.stable-diffusion-xl-v0"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
print(response_body)
artifact = response_body.get("artifacts")[0]
image_encoded = artifact.get("base64").encode("utf-8")
image_bytes = base64.b64decode(image_encoded)

# Save image to a file in the output directory.
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
file_name = f"{output_dir}/generated-img.png"
with open(file_name, "wb") as f:
    f.write(image_bytes)





# Use the native inference API to create an image with SDXL 1.0

import base64
import boto3
import json
import os
import random

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Titan Image Generator G1.
model_id = "stability.stable-diffusion-xl-v1"

# Define the image generation prompt for the model.
prompt = "Sri lanka tea plantation."

# Format the request payload using the model's native structure.
native_request = {"text_prompts":[{"text":"Sri lanka tea plantation.","weight":1}],"cfg_scale":10,"steps":50,"seed":0,"width":1024,"height":1024,"samples":1}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
response = client.invoke_model(modelId=model_id, body=request)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract the image data.
base64_image_data = model_response["artifacts"][0]["base64"]

# Save the generated image to a local folder.
i, output_dir = 1, "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
while os.path.exists(os.path.join(output_dir, f"image_{i}.png")):
    i += 1

image_data = base64.b64decode(base64_image_data)

image_path = os.path.join(output_dir, f"image_{i}.png")
with open(image_path, "wb") as file:
    file.write(image_data)

print(f"The generated image has been saved to {image_path}.")
