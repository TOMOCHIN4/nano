import gradio as gr
from google import genai
from google.genai import types
from PIL import Image
import io


def generate_image(api_key, prompt, aspect_ratio, safety_filter):
    """
    Generate image using Google GenAI API (Imagen model)

    Args:
        api_key: Google AI API key
        prompt: Text description for image generation
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

        # Configure image generation settings
        config = types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio=aspect_ratio,
            output_mime_type="image/png",
        )

        # Generate image using Imagen 3 model
        response = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=config
        )

        # Extract and return the generated image
        if response.generated_images and len(response.generated_images) > 0:
            generated_image = response.generated_images[0]
            # The image attribute is already a PIL Image
            image = generated_image.image

            return image, f"✅ Image generated successfully!\nPrompt: {prompt}\nAspect Ratio: {aspect_ratio}"

        return None, "❌ No image was generated. Please try again with a different prompt."

    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "invalid api key" in error_msg.lower():
            return None, "❌ Invalid API key. Please check your API key and try again."
        elif "QUOTA_EXCEEDED" in error_msg or "quota" in error_msg.lower():
            return None, "❌ Quota exceeded. Please check your API usage limits."
        elif "permission" in error_msg.lower():
            return None, "❌ Permission denied. Please ensure your API key has access to Imagen models."
        else:
            return None, f"❌ Error: {error_msg}"


# Create Gradio interface
with gr.Blocks(title="Gemini Image Generation", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🎨 Gemini Image Generation App

        Generate images using Google's Gemini API (Imagen 3 model).

        **How to use:**
        1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
        2. Enter your API key below
        3. Write a detailed prompt describing the image you want
        4. Select aspect ratio and safety settings
        5. Click "Generate Image"
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
        - Be specific and detailed in your prompts
        - Include style, mood, lighting, and composition details
        - Mention specific artists or art styles if desired
        - Experiment with different aspect ratios

        ### ⚠️ Notes:
        - API key is required for each generation
        - Generation may take 10-30 seconds
        - API usage may incur costs based on Google's pricing
        """
    )

    # Connect generate button to function
    generate_btn.click(
        fn=generate_image,
        inputs=[api_key_input, prompt_input, aspect_ratio_input, safety_filter_input],
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
