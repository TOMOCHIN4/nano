# Source Documentation

## Gemini Image Generation API

### API Overview
Google's Gemini API provides image generation capabilities through the Imagen 3 model.

### Model Information
- Model Name: `imagen-3.0-generate-001`
- Capabilities: Text-to-image generation
- Parameters:
  - `prompt`: Text description of desired image
  - `aspect_ratio`: Image aspect ratio (e.g., "1:1", "16:9", "9:16")
  - `output_mime_type`: Output format (default: "image/png")

### Authentication
- Requires API key from Google AI Studio
- API key should be kept secure and not hardcoded

### Python SDK Usage
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("imagen-3.0-generate-001")

response = model.generate_content(
    prompt="your image description",
    generation_config={
        "aspect_ratio": "1:1"
    }
)
```

## Gradio Framework

### Interface Components
- `gr.Textbox`: For API key and prompt input
- `gr.Dropdown`: For aspect ratio and resolution selection
- `gr.Button`: For triggering generation
- `gr.Image`: For displaying generated image

### Security Considerations
- Use `type="password"` for API key input
- Clear API key from memory after use if possible
- Don't log sensitive information

## Hugging Face Spaces Deployment

### Required Files
- `app.py`: Main application file
- `requirements.txt`: Python dependencies
- `README.md`: Space description and documentation

### Configuration
- Runtime: Python 3.10+
- SDK: Gradio
- Hardware: CPU (basic) or GPU (faster)

## Reference Links
- Gemini API: https://ai.google.dev/
- Gradio Documentation: https://www.gradio.app/docs
- Hugging Face Spaces: https://huggingface.co/docs/hub/spaces
