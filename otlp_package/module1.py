from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

def set_service_name() :
    rsrc = Resource(attributes={
        SERVICE_NAME: "Python Application"
    })
    return rsrc

def otlpConsoleExporter() :

    provider = TracerProvider()
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)

    # Sets the global default tracer provider
    trace.set_tracer_provider(provider)

    # Creates a tracer from the global tracer provider
    tracer = trace.get_tracer("my.tracer.name")
    return tracer

def otlpHttpExporter() :
    rsrc=set_service_name()
    tracerProvider = TracerProvider(resource=rsrc)
    processor = BatchSpanProcessor(OTLPSpanExporter(
            endpoint="http://localhost:4317/v1/traces"))
    tracerProvider.add_span_processor(processor)
    trace.set_tracer_provider(tracerProvider)
    
    # Acquire a tracer
    tracer = trace.get_tracer("tracer.name")
    return tracer 

def otlpGRPCExporter() :

    tracerProvider = TracerProvider(resource=rsrc)
    processor = BatchSpanProcessor(OTLPSpanExporter(
            endpoint="http://localhost:4317/v1/traces"))
    tracerProvider.add_span_processor(processor)
    trace.set_tracer_provider(tracerProvider)
    
    # Acquire a tracer
    tracer = trace.get_tracer("tracer.name")
    return tracer 