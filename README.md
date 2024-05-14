[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# GPT4o
Community Open Source Implementation of GPT4o in PyTorch


# Architecture
- TikToken Tokenzier: We know fursure the tokenizer. [Which is here](https://github.com/openai/tiktoken)
- Model understands Images and Audio Natively. There are 2 approaches, process them natively or use encoders for each. I think here they're using encoders like whisper and vit for simplicity and brevity.
- Using DALLE3 as the output head to generate images
- Tokens to denote when to generate an image or audio
- Whisper output head for the audio outputs
- 

# License
MIT
