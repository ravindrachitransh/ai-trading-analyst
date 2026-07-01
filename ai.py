import base64
import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_report(stock_data, uploaded_file=None):

    prompt = f"""
    You are an expert stock market analyst.

    Analyze the following stock data:

    {stock_data}

    Generate a professional trading report in this format:

    📈 Trend Summary:
    - Brief explanation of current trend

    📊 Technical Signals:
    - Comment on RSI
    - Comment on volume

    🔮 Outlook:
    - Short-term expectation

    ✅ Recommendation:
    - Buy / Hold / Sell

    Keep the response concise and easy to read.
    """

    # If no image uploaded → normal text-only analysis
    if uploaded_file is None:

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return response.output_text

    # If image uploaded → multimodal analysis
    
    # Debugging: Print info about the uploaded file
    # print("IMAGE RECEIVED")
    # print(uploaded_file)
    
    img_bytes = uploaded_file.file.read()

    # Debugging: Print type and size of the image bytes
    print(type(img_bytes))

    b64 = base64.b64encode(img_bytes).decode()

    data_uri = f"data:{uploaded_file.content_type};base64,{b64}"

    vision_prompt = f"""
    {prompt}

    Also analyze the uploaded trading chart image.

    Identify:
    - trend direction
    - buying/selling pressure
    - hammer candles
    - engulfing candles
    - breakout attempts
    - support/resistance zones
    - unusual volume behavior
    - momentum shifts

    Mention important visible chart patterns clearly.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",

        input=[
            {
                "role": "user",
                "content": [

                    {
                        "type": "input_text",
                        "text": vision_prompt
                    },

                    {
                        "type": "input_image",
                        "image_url": data_uri
                    }
                ]
            }
        ]
    )

    return response.output_text


