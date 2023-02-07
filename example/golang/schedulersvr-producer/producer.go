package main

import (
	"context"
	"encoding/json"
	"flag"
	"log"

	"github.com/google/uuid"
	"github.com/lukaproject/sdk/go_scheduler"
	"gopkg.in/ini.v1"
)

var FileName = flag.String("f", "producer.ini", "producer's configuration")

func Must(b []byte, err error) []byte {
	if err != nil {
		panic(err)
	}
	return b
}

func main() {
	flag.Parse()
	cfg, err := ini.Load(*FileName)
	if err != nil {
		panic(err)
	}
	// confiugure the cli.
	schedulerCfg := go_scheduler.NewConfiguration()
	schedulerCfg.BasePath = cfg.Section("scheduler").Key("addr").MustString("http://localhost")
	log.Println(schedulerCfg.BasePath)
	cli := go_scheduler.NewAPIClient(schedulerCfg)

	// pack the input
	input := make(map[string]interface{})
	input["a"] = cfg.Section("task").Key("a").MustInt(100)
	input["b"] = cfg.Section("task").Key("b").MustInt(100)

	// send message
	resp, _, err := cli.SchedulerSvrApi.AddTask(context.Background(), go_scheduler.AddTaskReq{
		SessionId: uuid.NewString(),
		Input:     string(Must(json.Marshal(input))),
		TaskType:  cfg.Section("task").Key("type").MustString("defaultTask"),
		Name:      cfg.Section("task").Key("name").MustString("defaultName"),
	})
	if err != nil {
		log.Println(err)
		return
	}
	v, err := json.Marshal(resp)
	if err != nil {
		log.Println(err)
		return
	}
	log.Println(string(v))
}
