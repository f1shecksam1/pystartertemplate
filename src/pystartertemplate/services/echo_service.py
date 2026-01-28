from pystartertemplate.models.echo import EchoOut


def echo_text(text: str) -> EchoOut:
    return EchoOut(echoed=text)
