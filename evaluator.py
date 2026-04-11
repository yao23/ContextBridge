"""Simple evaluator for the demo loop."""


def evaluate(output: str) -> str:
    if "logs" in output.lower():
        return "success"
    return "failure"
