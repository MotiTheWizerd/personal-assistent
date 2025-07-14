from google.adk.agents import LlmAgent

class ReflectiveAgent(LlmAgent):
    def __init__(self, *args, is_reflect: bool = False, **kwargs):
        """
        :param is_reflect: Optional flag to enable reflection; defaults to False.
        """
        super().__init__(*args, **kwargs)
        self.is_reflect = is_reflect

    def _maybe_reflect(self, text: str) -> str:
        if self.is_reflect:
            return f"(Reflecting…) {text}"
        return text

    async def run_async(self, *args, **kwargs):
        """
        Wraps LlmAgent.run_async to optionally reflect on the final message.
        """
        async for event in super().run_async(*args, **kwargs):
            content = getattr(event, "content", None)
            if content and content.parts:
                last_part = content.parts[-1]
                last_part.text = self._maybe_reflect(last_part.text)
            yield event
