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

# 🎨 Gemini Image Generation App

A simple and intuitive Gradio application for generating images using Google's Gemini image models (Nano Banana 🍌).

## Features

- 🔑 Secure API key input
- 🤖 **Model Selection**: Choose between Gemini 3 Pro Image (Nano Banana Pro) or 2.5 Flash Image (Nano Banana)
- 📝 Text-to-image generation with state-of-the-art quality
- 📐 Multiple aspect ratio options (1:1, 16:9, 9:16, 4:3, 3:4)
- 💡 Example prompts for inspiration
- 🎨 Clean and modern UI

## Models Available

### 🍌⭐ Gemini 3 Pro Image (Nano Banana Pro)
- **Release**: November 20, 2025
- **Best for**: Professional-grade image generation
- **Features**: High-resolution (1K/2K/4K), advanced text rendering, complex compositions
- **Model ID**: `gemini-3-pro-image-preview`

### 🍌⚡ Gemini 2.5 Flash Image (Nano Banana)
- **Release**: August 26, 2025
- **Best for**: Fast, efficient image generation
- **Features**: 1024px resolution, 2-3x faster than competitors, high-volume tasks
- **Model ID**: `gemini-2.5-flash-image`

## How to Use

1. **Get API Key**: Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to obtain your API key
2. **Enter API Key**: Paste your API key in the secure input field
3. **Select Model**: Choose between Gemini 3 Pro (quality) or 2.5 Flash (speed)
4. **Write Prompt**: Describe the image you want to generate in detail
5. **Select Aspect Ratio**: Choose your preferred aspect ratio
6. **Generate**: Click the "Generate Image" button and wait for your image

## Tips for Better Results

- Be specific and detailed in your prompts
- Include information about:
  - Style (realistic, artistic, abstract, etc.)
  - Mood and atmosphere
  - Lighting conditions
  - Color palette
  - Composition details
- Reference specific artists or art movements if desired
- Experiment with different aspect ratios for your use case

## Requirements

- Google AI API key (free tier available)
- Internet connection
- Modern web browser

## Technical Details

- **Models**:
  - Gemini 3 Pro Image (`gemini-3-pro-image-preview`)
  - Gemini 2.5 Flash Image (`gemini-2.5-flash-image`)
- **Framework**: Gradio 5.49.1 (stable)
- **API**: Google GenAI Python SDK (google-genai 1.52.0+)
- **Deployment**: Hugging Face Spaces
- **Python**: 3.10+

## Privacy & Security

- Your API key is not stored or logged
- API key is only used for the current generation request
- All processing happens through Google's secure API
- No image data is stored by this application

## Local Development

To run this app locally:

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at `http://localhost:7860`

## API Costs

Image generation using Gemini API may incur costs. Please refer to [Google's pricing page](https://ai.google.dev/pricing) for current rates.

## Limitations

- Generation time: 10-30 seconds per image
- Rate limits apply based on your API tier
- Content policy restrictions apply
- Some prompts may be filtered for safety

## Support

For issues or questions:
- Check [Google AI documentation](https://ai.google.dev/)
- Review [Gradio documentation](https://www.gradio.app/docs)
- Open an issue in this repository

## License

MIT License - feel free to use and modify for your projects

## Acknowledgments

- Google GenAI SDK for unified API access to Imagen models
- Gradio for the modern web interface framework
- Hugging Face for hosting platform
