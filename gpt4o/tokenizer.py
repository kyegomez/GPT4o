import tiktoken


class GPT4oTokenizer:
    def __init__(
        self,
        model_name: str = "gpt-4o",
        base_model: str = "o200k_base",
        *args,
        **kwargs
    ):  
        self.tokenizer = tiktoken.encoding_for_model(model_name, *args, **kwargs)
    
    def encode(self, text: str, *args, **kwargs):
        """
        Encodes the given text into a list of tokens.

        Args:
            text (str): The input text to be encoded.
            *args: Variable length arguments to be passed to the tokenizer.
            **kwargs: Keyword arguments to be passed to the tokenizer.

        Returns:
            list[int]: The encoded tokens.
        """
        return self.tokenizer.encode(text, *args, **kwargs)

    def decode(self, tokens: list[int], *args, **kwargs):
        """
        Decodes the given list of tokens into text.

        Args:
            tokens (list[int]): The input tokens to be decoded.
            *args: Variable length arguments to be passed to the tokenizer.
            **kwargs: Keyword arguments to be passed to the tokenizer.

        Returns:
            str: The decoded text.
        """
        return self.tokenizer.decode(tokens, *args, **kwargs)