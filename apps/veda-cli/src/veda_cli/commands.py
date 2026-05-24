from __future__ import annotations

from abc import ABC, abstractmethod

from veda_core import get_version


class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        raise NotImplementedError


class VersionCommand(Command):
    def execute(self) -> str:
        return f"veda-cli 0.1.0 (core {get_version()})"


class ReadyCommand(Command):
    def execute(self) -> str:
        return "veda-cli ready"


class CommandInvoker:
    def __init__(self, command_map: dict[str, Command], default_command: Command) -> None:
        self._command_map = command_map
        self._default_command = default_command

    def resolve(self, show_version: bool) -> Command:
        if show_version:
            return self._command_map["version"]
        return self._default_command
