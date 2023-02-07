'''
Run this example in repo root dir.
'''
import scheduler_py3 as schPy3
import json
import uuid
import argparse
import asyncio
import configparser


parser = argparse.ArgumentParser()
parser.add_argument("-f", default="example/schedulersvr/producer.ini",
                    type=str,
                    required=True,
                    help="the producer.ini")
args = parser.parse_args()


async def main():
    # setup configuration
    ini = configparser.ConfigParser()
    ini.read(args.f)
    swagger_conf = schPy3.Configuration()
    swagger_conf.host = ini["scheduler"]["addr"]
    swagger_client = schPy3.ApiClient(swagger_conf)
    sch_api = schPy3.SchedulerSvrApi(swagger_client)

    # pack and send request, handle the response.
    input_body = {
        "a": int(ini["input"]["a"]),
        "b": int(ini["input"]["b"]),
    }
    print(input_body)
    add_task_model = schPy3.AddTaskReq(session_id=str(
        uuid.uuid4()),
        task_type=ini["task"]["type"],
        name=ini["task"]["name"],
        input=json.JSONEncoder().encode(input_body)
    )
    result = sch_api.add_task(add_task_model)
    print(result)
    pass


if __name__ == '__main__':
    asyncio.run(main())
