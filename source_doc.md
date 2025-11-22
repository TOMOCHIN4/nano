# Source Documentation

## Google GenAI SDK - Gemini Image Generation API

### SDK Overview
Google's unified GenAI SDK (`google-genai`) provides image generation capabilities through the Gemini image models (codenamed "Nano Banana" 🍌).

**Latest Version**: 1.52.0 (Released: November 21, 2025)

### Gemini Image Model Information

#### Gemini 3 Pro Image (Nano Banana Pro) 🍌⭐
- **Model ID**: `gemini-3-pro-image-preview`
- **Release Date**: November 20, 2025
- **Best for**: Professional-grade asset production
- **Capabilities**:
  - High-resolution output (1K, 2K, 4K visuals)
  - Advanced text rendering for infographics and marketing
  - Complex multi-turn creation tasks
  - Grounding with Google Search
  - Superior composition control
- **Python Requirement**: >=3.10

#### Gemini 2.5 Flash Image (Nano Banana) 🍌⚡
- **Model ID**: `gemini-2.5-flash-image`
- **Release Date**: August 26, 2025
- **Best for**: Fast, efficient image generation
- **Capabilities**:
  - 1024px resolution
  - 2-3x faster than GPT-4o Image
  - State-of-the-art for generation and editing
  - Character consistency across prompts
  - Targeted transformation and local edits
- **Pricing**: $30/million tokens ($0.039/image)
- **Python Requirement**: >=3.10

### Configuration Parameters
- `contents`: List containing the text prompt (and optionally input images)
- `aspect_ratio`: Image aspect ratio via ImageConfig (e.g., "1:1", "16:9", "9:16", "4:3", "3:4")
- `response_modalities`: Must include "IMAGE" for image generation
- `image_config`: ImageConfig object for aspect ratio and other image settings

### Authentication
- Requires API key from Google AI Studio (https://aistudio.google.com/app/apikey)
- API key should be kept secure and not hardcoded
- Supports both Gemini Developer API and Vertex AI

### Python SDK Usage (Gemini Image Models)

**Installation**:
```bash
pip install google-genai>=1.52.0
```

**Basic Usage (Gemini 2.5 Flash Image)**:
```python
from google import genai
from google.genai import types

# Create client
client = genai.Client(api_key="YOUR_API_KEY")

# Configure generation
config = types.GenerateContentConfig(
    response_modalities=["IMAGE"],
    image_config=types.ImageConfig(
        aspect_ratio="16:9",
    ),
)

# Generate image
response = client.models.generate_content(
    model='gemini-2.5-flash-image',
    contents=['A serene landscape with mountains and a lake at sunset'],
    config=config
)

# Access generated image
for part in response.parts:
    if part.inline_data is not None:
        image = part.as_image()  # Returns PIL Image
        image.save("output.png")
```

**Using Gemini 3 Pro Image**:
```python
# Simply change the model ID
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=['Professional marketing banner with bold text: "Gemini 3 Pro"'],
    config=config
)
```

### Migration Notes
- **Old SDK**: `google-generativeai` (DEPRECATED - support ends August 31, 2025)
- **New SDK**: `google-genai` (current, unified)
- **Imagen vs Gemini Image Models**:
  - **Imagen**: Uses `generate_images()` method
  - **Gemini Image**: Uses `generate_content()` with `response_modalities=["IMAGE"]`
- **Key Differences**:
  - Import: `from google import genai` and `from google.genai import types`
  - Setup: `client = genai.Client(api_key=...)`
  - Config: `GenerateContentConfig` with `ImageConfig` for Gemini models
  - Response: Access via `response.parts` and `part.as_image()`

## Gradio Framework

### Version Information
- **Recommended Stable Version**: 5.49.1
- **Latest Version**: 6.0.0 (Released: November 21, 2025 - very new, stability unverified)
- **Python Requirement**: >=3.10
- **Note**: Using 5.49.1 for production stability

### Interface Components
- `gr.Textbox`: For API key and prompt input
- `gr.Dropdown`: For aspect ratio and safety filter selection
- `gr.Button`: For triggering generation
- `gr.Image`: For displaying generated image (type="pil")
- `gr.Blocks`: Container for custom layouts
- `gr.Examples`: Pre-filled example inputs

### Security Considerations
- Use `type="password"` for API key input
- API keys are not stored and only used per request
- Don't log sensitive information
- Gradio 6 includes enhanced security features

## Hugging Face Spaces Deployment

### Required Files
- `app.py`: Main application file
- `requirements.txt`: Python dependencies
- `README.md`: Space description and documentation (with YAML frontmatter)

### README Frontmatter Example
```yaml
---
title: Gemini Image Generation
emoji: 🎨
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: mit
---
```

### Configuration
- **Runtime**: Python 3.10+
- **SDK**: Gradio 5.49.1 (stable)
- **Hardware**: CPU (sufficient) or GPU (faster, optional)

### Dependencies
```
gradio==5.49.1
google-genai>=1.52.0
Pillow>=10.0.0
```

## API Costs and Limits
- Image generation incurs costs per Google's pricing
- Rate limits apply based on API tier
- Check current pricing: https://ai.google.dev/pricing
- Free tier available for testing

## Reference Links
- **Google GenAI SDK**: https://googleapis.github.io/python-genai/
- **Google AI Studio**: https://aistudio.google.com/
- **Gemini API Docs**: https://ai.google.dev/
- **Gradio Documentation**: https://www.gradio.app/docs
- **Hugging Face Spaces**: https://huggingface.co/docs/hub/spaces
- **Migration Guide**: https://ai.google.dev/gemini-api/docs/migrate
