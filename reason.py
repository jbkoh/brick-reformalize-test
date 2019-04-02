import owlrl
import rdflib

g = rdflib.Graph()
g.parse('test.ttl', format='turtle')

owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
res = g.query("""
prefix brick: <https://brickschema.org/schema/1.0.3/Brick#>
select ?s where {
    ?s a brick:Sensor.
}
""")

print('\nFound `Sensor`:')
for row in res:
    print(row[0])

res = g.query("""
prefix brick: <https://brickschema.org/schema/1.0.3/Brick#>
select ?s where {
    ?s a brick:Temperature_Sensor.
}
""")
print('\nFound `Temperature_Sensor`:')
for row in res:
    print(row[0])
