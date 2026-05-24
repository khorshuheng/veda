import click

from veda_cli.commands import CommandInvoker, ReadyCommand, VersionCommand


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--version", "show_version", is_flag=True, help="Show version information")
def cli(show_version: bool) -> None:
    invoker = CommandInvoker(
        command_map={
            "version": VersionCommand(),
        },
        default_command=ReadyCommand(),
    )
    selected_command = invoker.resolve(show_version=show_version)
    click.echo(selected_command.execute())


def main() -> None:
    cli(standalone_mode=True)


if __name__ == "__main__":
    main()
