# Source Documentation

## Google GenAI SDK - Image Generation API

### SDK Overview
Google's unified GenAI SDK (`google-genai`) provides image generation capabilities through the Imagen 3 and Imagen 4 models.

**Latest Version**: 1.52.0 (Released: November 21, 2025)

### Model Information
- **Imagen 3**: `imagen-3.0-generate-002` (recommended)
- **Imagen 4**: `imagen-4.0-generate-001` (newer, may have different pricing)
- **Capabilities**: Text-to-image generation with advanced controls
- **Python Requirement**: >=3.10

### Configuration Parameters
- `prompt`: Text description of desired image
- `aspect_ratio`: Image aspect ratio (e.g., "1:1", "16:9", "9:16", "4:3", "3:4")
- `number_of_images`: Number of images to generate (1-8)
- `output_mime_type`: Output format ("image/png" or "image/jpeg")
- `include_rai_reason`: Include Responsible AI reasoning in response

### Authentication
- Requires API key from Google AI Studio (https://aistudio.google.com/app/apikey)
- API key should be kept secure and not hardcoded
- Supports both Gemini Developer API and Vertex AI

### Python SDK Usage (NEW - google-genai)

**Installation**:
```bash
pip install google-genai>=1.52.0
```

**Basic Usage**:
```python
from google import genai
from google.genai import types

# Create client
client = genai.Client(api_key="YOUR_API_KEY")

# Configure generation
config = types.GenerateImagesConfig(
    number_of_images=1,
    aspect_ratio="1:1",
    output_mime_type="image/png",
)

# Generate image
response = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt='your image description',
    config=config
)

# Access generated image
image = response.generated_images[0].image  # Returns PIL Image
```

### Migration from Old SDK
- **Old SDK**: `google-generativeai` (DEPRECATED - support ends August 31, 2025)
- **New SDK**: `google-genai` (current, unified)
- **Key Changes**:
  - Import: `import google.generativeai as genai` → `from google import genai`
  - Setup: `genai.configure(api_key=...)` → `client = genai.Client(api_key=...)`
  - Generation: `model.generate_content()` → `client.models.generate_images()`

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
