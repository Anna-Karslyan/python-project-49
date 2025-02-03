# Команда для сборки пакета
build:
	uv build

# Команда для установки пакета
package-install:
	uv tool install dist/*.whl
