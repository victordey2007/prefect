from prefect import flow
from prefect.client.schemas.schedules import RRuleSchedule
from dateutil.rrule import rrule, WEEKLY, MO, WE, FR
from datetime import timedelta, datetime
@flow
def my_flow():
    print("Hello from Prefect!")


my_flow.deploy(
name="rrule-example",
  work_pool_name='my-demo-pool',
    schedules=RRuleSchedule(
        rrule='FREQ=DAILY;INTERVAL=5'        
    )


)