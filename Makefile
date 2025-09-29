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

search:
	docker compose run --rm tracker python /app/symbol_search.py $(ARGS)

symbols:
	docker compose run --rm tracker python /app/symbol_search.py --stats

help:
	@echo "Available commands:"
	@echo "  make build          - Build Docker image"
	@echo "  make run-tracker    - Run data collection"
	@echo "  make run-backtest   - Run backtest analysis"
	@echo "  make run-sweep      - Run parameter sweep"
	@echo "  make run-report     - Generate report"
	@echo "  make all            - Run full pipeline"
	@echo "  make search ARGS=   - Search symbols (e.g., ARGS='--search bitcoin')"
	@echo "  make symbols        - Show symbol statistics"
	@echo "  make help           - Show this help"
