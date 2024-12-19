from prefect import flow ,variables
from prefect import task

@task
def create_msg():
    env=variables.get("env", default="UNKONW")
    msg= 'hello from prefect! and welcome to '+env + ' Environment' 
    return (msg)


@flow(log_prints=True)
def hello_world():
    print(create_msg())

if __name__ == "__main__":
    hello_world()