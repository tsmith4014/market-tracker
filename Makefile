build:
	docker compose build

run-tracker:
	docker compose run --rm tracker

run-backtest:
	docker compose run --rm backtest

run-sweep:
	docker compose run --rm sweep

run-report:
	docker compose run --rm report

all:
	make build && make run-tracker && make run-backtest && make run-sweep && make run-report
