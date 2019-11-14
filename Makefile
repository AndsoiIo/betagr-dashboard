include .env
export

run_project:
		docker-compose up --build

run_tests:
		docker-compose -f docker-compose.testing.yml build
		docker-compose -f docker-compose.testing.yml run --rm test_admin_dashboard
		docker-compose -f docker-compose.testing.yml down