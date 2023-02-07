package main

import (
	"encoding/json"
	"flag"
	"log"
	"sync"
	"time"

	"github.com/lukaproject/sdk/go_scheduler"
	"gopkg.in/ini.v1"
)

var FileName = flag.String("f", "worker.ini", "worker's configuration")

func solve(input string) (output string) {
	log.Println(input)
	type Input struct {
		A int `json:"a"`
		B int `json:"b"`
	}
	in := &Input{}

	err := json.Unmarshal([]byte(input), in)
	if err != nil {
		log.Println(err)
	}
	res := make(map[string]interface{})
	res["res"] = in.A + in.B
	resByte, err := json.Marshal(&res)
	if err != nil {
		log.Println(err)
	}
	output = string(resByte)
	return
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
	wh := go_scheduler.NewWorkerHandler(
		go_scheduler.NewAPIClient(schedulerCfg),
		solve,
		cfg.Section("task").Key("type").MustString("defaultTask"),
		cfg.Section("worker").Key("id").MustString("defualtId"),
		3*time.Second,
	)
	wh.Start()
	wg := &sync.WaitGroup{}
	wg.Add(1)
	wg.Wait()
}
