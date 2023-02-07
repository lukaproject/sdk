'''
Run this example in repo root dir.
'''
import scheduler_py3 as schPy3
from scheduler_py3 import worker_handler
import argparse
import asyncio
import json
import configparser

parser = argparse.ArgumentParser()
parser.add_argument("-f", default="example/schedulersvr/worker.ini",
                    type=str,
                    required=True,
                    help="the worker.ini")
args = parser.parse_args()


def solve_task(input: str) -> str:
    print("get input = {}".format(input))
    obj = json.loads(input)
    result = int(obj["a"]) + int(obj["b"])
    return json.dumps({"result": result})


async def main():
    # set up config
    ini = configparser.ConfigParser()
    ini.read(args.f)
    swagger_conf = schPy3.Configuration()
    swagger_conf.host = ini["scheduler"]["addr"]
    client = schPy3.ApiClient(configuration=swagger_conf)
    sch_api = schPy3.SchedulerSvrApi(api_client=client)
    whandler = worker_handler.Workerhandler(
        scheduler_api=sch_api,
        task_type=ini["task"]["type"],
        solve_func=solve_task,
        worker_id=ini["worker"]["id"],
    )
    await whandler.start()


if __name__ == '__main__':
    asyncio.run(main())
