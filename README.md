# Pizza API Challenge

A tiny Flask app to manage restaurants, pizzas, and prices.

## Quick Start

```bash
git clone <repo-url>
cd pizza-api
pipenv install --three
pipenv shell
export FLASK_APP=server/app:create_app
flask db init && flask db migrate -m "init" && flask db upgrade
python -m server.seed
flask run
```

Visit `http://127.0.0.1:5000`.

## Routes

* `GET /restaurants`
* `GET /restaurants/<id>`
* `DELETE /restaurants/<id>`
* `GET /pizzas`
* `POST /restaurant_pizzas`

  ```json
  {"price":10,"pizza_id":1,"restaurant_id":2}
  ```

*Note: Price must be 1-30.*


