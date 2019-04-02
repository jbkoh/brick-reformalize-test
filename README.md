Test Code to Evaluate Brick Reformalization
===========================================


# How to run?
- ``pip install -r requirements.txt``
- ``python reason.py``

# Description
Current OWL rules infer redundant classes. In ``test.ttl``, `:temp_sensor` is associated with both Tags ``Sensor`` and ``Tempearture``, which we intended to be an instance of ``Temperature_Sensor`` but the inference engine finds it is also a ``Sensor``.
