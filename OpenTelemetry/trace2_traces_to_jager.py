from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Set up TracerProvider
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure Jaeger Exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Jaeger host (default is localhost)
    agent_port=6831              # Default UDP port for Jaeger
)

# Add the BatchSpanProcessor with the Jaeger exporter
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create a Trace
with tracer.start_as_current_span("example-operation") as span:
    span.set_attribute("example-key", "example-value")  # Add attributes to the span
    print("Trace started!")

    # Simulate a nested span (child span)
    with tracer.start_as_current_span("nested-operation") as nested_span:
        nested_span.set_attribute("nested-key", "nested-value")
        print("Nested operation running!")

print("Trace completed. Check Jaeger UI for the data.")
