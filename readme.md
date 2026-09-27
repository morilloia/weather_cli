# Weather CLI

A simple command-line tool that fetches and displays a multi-day weather forecast for any city in the world, using the [Open-Meteo](https://open-meteo.com/) API.

## Features

- 🌍 Look up any city by name (geocoding handled automatically)
- 📅 Multi-day forecast (customizable range, default 7 days)
- 🌡️ Daily average, maximum, and minimum temperature
- ☀️ Most representative weather condition per day (calculated via mode of hourly readings)
- ⚠️ Handles connection errors, timeouts, invalid cities, and API errors gracefully

## Example output

```
Weather forecast for Rio das Ostras, BR for the next 3 days:

📅 Date: 2026-09-26,
   Weather: ☀️  Clear sky,
 🌡️  Avg temp: 23.68°C,
 ⬆️  Max temp: 28.30°C,
 ⬇️  Min temp: 20.30°C

📅 Date: 2026-09-27,
   Weather: ⛅  Partly cloudy,
 🌡️  Avg temp: 22.95°C,
 ⬆️  Max temp: 27.00°C,
 ⬇️  Min temp: 19.90°C
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/morilloia/weather-cli.git
   cd weather-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python weather_cli.py "City Name"
```

With a custom number of days:

```bash
python weather_cli.py "Rio das Ostras" --days 3
```

If no `--days` is provided, it defaults to 7.

## How it works

1. The city name is sent to Open-Meteo's **Geocoding API** to retrieve its coordinates.
2. Those coordinates are used to query the **Forecast API** for hourly temperature and weather code data.
3. Hourly data is grouped by day, and daily statistics (average, max, min, most common weather condition) are calculated.
4. Results are printed to the terminal in a readable format.

## Built with

- Python 3
- [`requests`](https://docs.python-requests.org/) — HTTP requests
- `argparse` — command-line argument parsing
- `collections.Counter` — finding the most common weather condition per day

## Author

Israel Morillo — [GitHub](https://github.com/morilloia)

---

# Weather CLI (Português)

Uma ferramenta de linha de comando simples que busca e exibe a previsão do tempo de vários dias para qualquer cidade do mundo, usando a API do [Open-Meteo](https://open-meteo.com/).

## Funcionalidades

- 🌍 Busca qualquer cidade pelo nome (geocodificação automática)
- 📅 Previsão de vários dias (intervalo personalizável, padrão de 7 dias)
- 🌡️ Temperatura média, máxima e mínima diária
- ☀️ Condição climática mais representativa do dia (calculada pela moda das leituras horárias)
- ⚠️ Trata erros de conexão, timeouts, cidades inválidas e erros da API de forma adequada

## Exemplo de saída

```
Weather forecast for Rio das Ostras, BR for the next 3 days:

📅 Date: 2026-09-26,
   Weather: ☀️  Clear sky,
 🌡️  Avg temp: 23.68°C,
 ⬆️  Max temp: 28.30°C,
 ⬇️  Min temp: 20.30°C
```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/morilloia/weather-cli.git
   cd weather-cli
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

```bash
python weather_cli.py "Nome da Cidade"
```

Com um número personalizado de dias:

```bash
python weather_cli.py "Rio das Ostras" --days 3
```

Se `--days` não for informado, o padrão é 7.

## Como funciona

1. O nome da cidade é enviado à **API de Geocoding** do Open-Meteo para obter suas coordenadas.
2. Essas coordenadas são usadas para consultar a **API de Forecast**, obtendo dados horários de temperatura e código climático.
3. Os dados horários são agrupados por dia, e são calculadas estatísticas diárias (média, máximo, mínimo e condição climática mais comum).
4. Os resultados são exibidos no terminal em um formato legível.

## Construído com

- Python 3
- [`requests`](https://docs.python-requests.org/) — requisições HTTP
- `argparse` — leitura de argumentos de linha de comando
- `collections.Counter` — cálculo da condição climática mais comum do dia

## Autor

Israel Morillo — [GitHub](https://github.com/morilloia)
