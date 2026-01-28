from pystartertemplate.models.health import HealthOut


def get_health_status() -> HealthOut:
    return HealthOut(status="ok")
