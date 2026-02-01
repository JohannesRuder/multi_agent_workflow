import os
import warnings

from dotenv import load_dotenv

try:
    from arize.otel import register
    from openinference.instrumentation.google_adk import (
        GoogleADKInstrumentor,
    )
except Exception:
    register = None
    GoogleADKInstrumentor = None

load_dotenv()


def instrument_adk_with_arize():
    """Instrument the ADK with Arize."""
    if register is None or GoogleADKInstrumentor is None:
        warnings.warn(
            "Arize/OpenInference instrumentation is unavailable; tracing disabled.",
            stacklevel=2,
        )
        return None

    if os.getenv("ARIZE_SPACE_ID") is None:
        warnings.warn("ARIZE_SPACE_ID is not set", stacklevel=2)
        return None
    if os.getenv("ARIZE_API_KEY") is None:
        warnings.warn("ARIZE_API_KEY is not set", stacklevel=2)
        return None

    tracer_provider = register(
        space_id=os.getenv("ARIZE_SPACE_ID"),
        api_key=os.getenv("ARIZE_API_KEY"),
        project_name=os.getenv("ARIZE_PROJECT_NAME", "adk-travel-concierge"),
    )

    GoogleADKInstrumentor().instrument(tracer_provider=tracer_provider)

    return tracer_provider.get_tracer(__name__)
