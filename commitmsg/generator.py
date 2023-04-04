import os
from typing import Tuple

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


class CommitMessageGenerator:
    def __init__(self):
        self._prompt = """
Act as Commit Message Generator. You need to generate short commit messages. 

Output format: [type] message
Available types: feat, fix, docs, test, ci

Example output: [fix] Moved to torch==2.0 from torch==1.12.2
Example output: [feat] Added sampling_rate parameter to TinkoffASRModel
Example output: [docs] Added info about model sampling_rate to README.md
"""
        self._prompt_2 = """Commit Message Generator is ready."""
        self._model_name = "gpt-3.5-turbo"

    def predict(self, diff: str) -> Tuple[str, str]:
        message_history = [
            {"role": "user", "content": self._prompt},
            {"role": "assistant", "content": self._prompt_2},
            {
                "role": "user",
                "content": f"{diff}",
            },
        ]
        assistant_message = openai.ChatCompletion.create(
            model=self._model_name,
            messages=message_history,
        )["choices"][0]["message"]["content"].replace("Output:", "", 1)
        type = str(assistant_message.split("]")[0].replace("[", ""))
        message = str(assistant_message.split("]")[1].strip())
        return type, message

    def __call__(
        self,
        diff: str,
    ) -> Tuple[str, str]:
        """
        Generate commit message from diff.

        Args:
            diff: Diff to generate commit message from.

        Returns:
            Tuple of commit message type and commit message.
        """
        return self.predict(diff)
