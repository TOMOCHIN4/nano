import gradio as gr
from google import genai
from google.genai import types
from PIL import Image
import io

# Model configuration
MODELS = {
    "Gemini 3 Pro Image (Nano Banana Pro) 🍌⭐": "gemini-3-pro-image-preview",
    "Gemini 2.5 Flash Image (Nano Banana) 🍌⚡": "gemini-2.5-flash-image",
}


def generate_image(api_key, prompt, model_name, aspect_ratio, safety_filter):
    """
    Generate image using Google GenAI API (Gemini image models)

    Args:
        api_key: Google AI API key
        prompt: Text description for image generation
        model_name: Selected model name
        aspect_ratio: Aspect ratio for the image
        safety_filter: Safety filter level

    Returns:
        Generated image or error message
    """
    if not api_key:
        return None, "❌ Please enter your API key"

    if not prompt:
        return None, "❌ Please enter a prompt"

    try:
        # Create GenAI client
        client = genai.Client(api_key=api_key)

        # Get model ID from selection
        model_id = MODELS[model_name]

        # Configure image generation settings
        config = types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
            ),
        )

        # Generate image using Gemini image model
        response = client.models.generate_content(
            model=model_id,
            contents=[prompt],
            config=config
        )

        # Extract and return the generated image
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                return image, f"✅ Image generated successfully!\nModel: {model_name}\nPrompt: {prompt}\nAspect Ratio: {aspect_ratio}"

        return None, "❌ No image was generated. Please try again with a different prompt."

    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "invalid api key" in error_msg.lower():
            return None, "❌ Invalid API key. Please check your API key and try again."
        elif "QUOTA_EXCEEDED" in error_msg or "quota" in error_msg.lower():
            return None, "❌ Quota exceeded. Please check your API usage limits."
        elif "permission" in error_msg.lower():
            return None, "❌ Permission denied. Please ensure your API key has access to Gemini image models."
        else:
            return None, f"❌ Error: {error_msg}"


# Create Gradio interface
with gr.Blocks(title="Gemini Image Generation", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🎨 Gemini Image Generation App

        Generate images using Google's Gemini image models (Nano Banana 🍌).

        **How to use:**
        1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
        2. Enter your API key below
        3. Select your preferred model (3 Pro or 2.5 Flash)
        4. Write a detailed prompt describing the image you want
        5. Select aspect ratio
        6. Click "Generate Image"
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            api_key_input = gr.Textbox(
                label="🔑 API Key",
                type="password",
                placeholder="Enter your Google AI API key",
                info="Your API key is not stored and only used for this generation"
            )

            model_input = gr.Dropdown(
                label="🤖 Model",
                choices=list(MODELS.keys()),
                value="Gemini 3 Pro Image (Nano Banana Pro) 🍌⭐",
                info="Gemini 3 Pro: Professional quality | 2.5 Flash: Faster generation"
            )

            prompt_input = gr.Textbox(
                label="📝 Prompt",
                placeholder="A serene landscape with mountains and a lake at sunset...",
                lines=5,
                info="Describe the image you want to generate"
            )

            aspect_ratio_input = gr.Dropdown(
                label="📐 Aspect Ratio",
                choices=["1:1", "16:9", "9:16", "4:3", "3:4"],
                value="1:1",
                info="Select the aspect ratio for your image"
            )

            safety_filter_input = gr.Dropdown(
                label="🛡️ Safety Filter",
                choices=["Default", "Low", "High"],
                value="Default",
                info="Content safety filter level"
            )

            generate_btn = gr.Button("🎨 Generate Image", variant="primary", size="lg")

        with gr.Column(scale=1):
            output_image = gr.Image(
                label="Generated Image",
                type="pil",
                height=500
            )
            status_output = gr.Textbox(
                label="Status",
                lines=3,
                interactive=False
            )

    gr.Markdown(
        """
        ---
        ### 💡 Tips for better results:
        - **Choose the right model**: Gemini 3 Pro for professional quality, 2.5 Flash for speed
        - Be specific and detailed in your prompts
        - Include style, mood, lighting, and composition details
        - Mention specific artists or art styles if desired
        - Experiment with different aspect ratios

        ### 🍌 Model Comparison:
        - **Gemini 3 Pro Image (Nano Banana Pro)**: Professional-grade, high-resolution (1K/2K/4K), advanced text rendering
        - **Gemini 2.5 Flash Image (Nano Banana)**: Fast generation, 1024px resolution, efficient for high-volume tasks

        ### ⚠️ Notes:
        - API key is required for each generation
        - Generation may take 10-30 seconds
        - API usage may incur costs based on Google's pricing
        """
    )

    # Connect generate button to function
    generate_btn.click(
        fn=generate_image,
        inputs=[api_key_input, prompt_input, model_input, aspect_ratio_input, safety_filter_input],
        outputs=[output_image, status_output]
    )

    # Example prompts
    gr.Examples(
        examples=[
            ["A futuristic cityscape at night with neon lights and flying cars", "16:9"],
            ["A cute robot playing with a kitten in a garden", "1:1"],
            ["An abstract painting with vibrant colors and geometric shapes", "4:3"],
            ["A serene Japanese zen garden with cherry blossoms", "16:9"],
        ],
        inputs=[prompt_input, aspect_ratio_input],
        label="Example Prompts"
    )


if __name__ == "__main__":
    demo.launch()
