from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

#Set up TracerProvider
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Add Exporter
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Create a Trace
with tracer.start_as_current_span("operation") as span:
    span.set_attribute("key", "value")  # Add attributes to the span
    print("Trace started!")  # Log the trace operation
