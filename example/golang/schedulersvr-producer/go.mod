module producer

go 1.18

replace github.com/lukaproject/sdk/go_scheduler => ../../../go_scheduler

require (
	github.com/google/uuid v1.3.0
	github.com/lukaproject/sdk/go_scheduler v0.0.0-00010101000000-000000000000
	gopkg.in/ini.v1 v1.67.0
)

require (
	github.com/golang/protobuf v1.5.2 // indirect
	github.com/stretchr/testify v1.8.1 // indirect
	golang.org/x/net v0.5.0 // indirect
	golang.org/x/oauth2 v0.4.0 // indirect
	google.golang.org/appengine v1.6.7 // indirect
	google.golang.org/protobuf v1.28.0 // indirect
)
