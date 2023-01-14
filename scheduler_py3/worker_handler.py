from typing import Callable, Optional
import scheduler_py3 as schPy3
import asyncio
import logging
import uuid
import time


class Workerhandler:
    def __init__(
            self,
            scheduler_api: schPy3.SchedulerSvrApi,
            task_type: str,
            solve_func: Callable[[str], str],
            worker_id: str,
            time_wait_s: float = 1
    ) -> None:
        self.scheduler_api = scheduler_api
        self.task_type = task_type
        self.solve_func = solve_func
        self.worker_id = worker_id
        self.time_wait_s = time_wait_s

    async def start(self):
        while True:
            await asyncio.sleep(self.time_wait_s)
            logging.debug("new fetch task tick, {}".format(time.time()))
            resp = await self._fetch_task()
            if resp is None:
                continue
            task: schPy3.TaskContent = resp.task
            output = self.solve_func(task.input)
            task.output = output
            await self._update_task(task)

    async def _fetch_task(self) -> Optional[schPy3.FetchTaskResp]:
        try:
            req = schPy3.FetchTaskReq(
                session_id=str(uuid.uuid4()),
                task_type=self.task_type,
                worker_id=self.worker_id,
            )
            resp = self.scheduler_api.fetch_task(req)
        except Exception as e:
            logging.error(e)
            return None
        return resp

    async def _update_task(self, tc: schPy3.TaskContent):
        try:
            req = schPy3.UpdateTaskReq(
                session_id=str(uuid.uuid4()),
                task=tc,
            )
            _ = self.scheduler_api.update_task(req)
        except Exception as e:
            logging.error(e)
        return None
