import os
import pathlib
import textwrap

import google.generativeai as genai

GCP_API_KEY = os.getenv("GCP_GENERATIVE_CONTENT_API_KEY")
genai.configure(api_key = GCP_API_KEY)

target_name = "gemini-pro"
supported = False
model_operational = False
for m in genai.list_models():
  if target_name in m.name:
    model_operational = True
    if "generateContent" in m.supported_generation_methods:
      supported = True
    break

if not model_operational:
  print("Gemini pro is not operational at this time.")
  exit()
if not supported:
  print("Gemini pro is not supporting generated content at this time.")
  exit()

model = genai.GenerativeModel(target_name)

prompt = input("Ask the genie anything you wish...\n > ")

# IPython magic: https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-time
# %%time
response = model.generate_content(prompt)

print(response.text)

