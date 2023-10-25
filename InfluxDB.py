# LINK: http://localhost:8086/orgs/2b7aeb5181c10dbc/data-explorer?fluxScriptEditor

# export INFLUXDB_TOKEN=9uIeGKs8pshJ1V2Zs167hIWw0YON_p3gARFALcTN6PZm2PtEBLPyPh3glkllIrjp1O7LIylCQ28LaJyjf17jlA==
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "IE"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)



bucket="GREG"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="IE", record=point)
  time.sleep(1) # separate points by 1 second








  #simple Flux query looks like on its own:
query_api = write_client.query_api()

query = """from(bucket: "GREG")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="IE")

for table in tables:
  for record in table.records:
    print(record)

print('\n\n\n\n')

query_api = write_client.query_api()

query = """from(bucket: "GREG")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="IE")

for table in tables:
    for record in table.records:
        print(record)

