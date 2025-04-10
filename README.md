# Tracing Package for Python Applications


Overview :
----------
This package provides a simple way to integrate tracing into your Python application using OpenTelemetry. It includes functionality to configure and export tracing data to console and OTLP endpoints like HTTP and GRPC , allowing you to observe and monitor your application's performance in real-time.


Features:
---------
  __1.__ Provides easy-to-use functions for setting up tracing.
  
  __2.__ Supports exporting traces using OTLP (OpenTelemetry Protocol).
  
  __3.__ Can be used with Jaeger tracing system.


Installation :
--------------
You can install the tracing package via pip by adding it directly from the GitHub repository.

--->  Command to install the package :

          pip install git+https://github.com/21A91A05F5/otlp_package.git


Usage :
--------

__Step-1 :__   Assign a Service Name for your Python application

---> Initialising a resource for assigning service name.

     #importing Resorce and SERVICE_NAME 

     from opentelemetry.sdk.resources import SERVICE_NAME, Resource

---> Assign service name using resource attribute.

      rsrc = Resource(attributes={
        SERVICE_NAME: "Python"
      })

__Step-2 :__  Importing and initialising tracer 

__1.__ For Exporting to the Console :

    from otlp_package import otlpConsoleExporter
   
    tracer=otlpConsoleExporter()

__2.__ For OTLP Exporter through Http :

    from otlp_package import otlpHttpExporter

    tracer=otlpHttpExporter(rsrc)

__3.__ For OTLP Exporter through gRPC :

    from otlp_package import otlpGRPCExporter

    tracer=otlpGRPCExporter(rsrc)


__Step-3 :__    Start creating spans for your micro-services


    with tracer.start_as_current_span("span_name") as span:
        #write you micro-service functionality


__Step-4 :__   Start running Jaeger

Docker command :

      docker run -d --name jaeger \
        -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
        -e COLLECTOR_OTLP_ENABLED=true \
        -p 6831:6831/udp \
        -p 6832:6832/udp \
        -p 5778:5778 \
        -p 16686:16686 \
        -p 4317:4317 \
        -p 4318:4318 \
        -p 14250:14250 \
        -p 14268:14268 \
        -p 14269:14269 \
        -p 9411:9411 \
        jaegertracing/all-in-one:latest


__Step-5 :__  Start running your Python flask application 

      flask run -p 8080


Example for Usage :(OtlpHttpExporter)
--------------------



    from random import randint
    from flask import Flask

    from opentelemetry.sdk.resources import SERVICE_NAME, Resource
    from otlp_package import otlpHttpExporter

    app = Flask(__name__)

    #Assigning Service Name
    rsrc = Resource(attributes={
            SERVICE_NAME: "Python-Service"
        })
    
    #Initialising Tracer 
    tracer=otlpHttpExporter(rsrc)
    

    @app.route("/rolldice")
    def roll_dice():
        #Creating spans using tracer

        with tracer.start_as_current_span("dice-rolling-trace") as root_span:
            # Initialize a list to store the results of 5 dice rolls
            results = []

            # Create 5 different spans for 5 different dice rolls
            for i in range(1, 7):
                # Each dice roll gets its own span, all are children of the root span
                roll_result = roll(i)
                results.append(roll_result)

            return results
        # return str(roll())

    def roll(roll_id):
        # This creates a new span that's the child of the current one
        with tracer.start_as_current_span(f"roll-{roll_id}") as rollspan:
            res = randint(1, 6)  # Simulate a dice roll
            rollspan.set_attribute("roll.value", res)  # Set an attribute to log the roll result
            return res




Navigate to monitor the trace data in Jaeger :

http://localhost:16686






