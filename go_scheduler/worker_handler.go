package go_scheduler

import (
	"context"
	"time"

	"github.com/google/uuid"
)

type WorkerHandler struct {
	api *APIClient

	solveFunc func(input string) (out string)
	taskType  string
	workerId  string
	timeWait  time.Duration
}

func NewWorkerHandler(
	api *APIClient,
	solveFunc func(input string) (out string),
	taskType string,
	workerId string,
	timeWait time.Duration,
) *WorkerHandler {
	return &WorkerHandler{
		api:       api,
		solveFunc: solveFunc,
		taskType:  taskType,
		workerId:  workerId,
		timeWait:  timeWait,
	}
}

func (wh *WorkerHandler) Start() {
	go func() {
		tick := time.NewTicker(wh.timeWait)
		for range tick.C {
			getTask, err := wh.fetchTask()
			if err != nil {
				continue
			}
			task := getTask.Task
			task.Output = wh.solveFunc(task.Input)
			err = wh.updateTask(UpdateTaskReq{
				SessionId: uuid.NewString(),
				Task:      task,
			})
			if err != nil {
				continue
			}
		}
	}()
}

func (wh *WorkerHandler) fetchTask() (resp FetchTaskResp, err error) {
	resp, _, err = wh.api.SchedulerSvrApi.FetchTask(context.Background(), FetchTaskReq{
		SessionId: uuid.NewString(),
		TaskType:  wh.taskType,
		WorkerId:  wh.workerId,
	})
	if err != nil {
		return
	}
	return
}

func (wh *WorkerHandler) updateTask(req UpdateTaskReq) (err error) {
	_, _, err = wh.api.SchedulerSvrApi.UpdateTask(context.Background(), req)
	if err != nil {
		return
	}
	return
}
