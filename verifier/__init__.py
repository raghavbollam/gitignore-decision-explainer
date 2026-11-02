"""Deterministic verifier entry point for the gitignore decision explainer."""

from pathlib import Path

from contract import Task

from .task import VerificationResult, verify_task as verify_explain_decisions


TASKS = {
    Task.EXPLAIN_DECISIONS: verify_explain_decisions,
}


def verify_task(
    task: str,
    arguments: object,
    output: object,
    reference: object | None,
    workspace: Path,
) -> VerificationResult:
    """Dispatch a task submission to its deterministic verifier."""

    return TASKS[Task(task)](
        arguments,
        output,
        reference,
        workspace,
    )