<div align="center">
  <h1>KGSearch</h1>
</div>

![](/_doc/kgsearch.gif)

KGSearch is a minimalist tool for searching and viewing entities in a graph and is dedicated to a local environment. The application provides Django web server


## ✅ Quick Start

```sh
git clone https://github.com/SothanaV/kgsearch.git
docker compose up
```

- open browser http://localhost:8000

## ⭐️ Query

KGSearch suggests performing multiple queries via the `;` separator.

The query `api;data` will be divided into three subqueries `api` and  `data` to visualize the interactions between the entities of our choice.

The `top K` field allows selecting the number of candidate entities retrieved by the search engine (1 by default).

The `neighbours` field selects the number of neighbors to be displayed (1 by default).

The `prune` field removes entities that have fewer than `prune` connections to other entities (1 by default).

## 🤖 Custom KG

- open browser http://localhost:8000/admin/kgsearch/dataset/add/
- default user: `admin` password: `admin`

![](/_doc/add-data.png)

The graph must be saved in CSV format and structured as triples (head, relation, tail) with a comma separator and without column names. Here is an example of a compatible CSV file:

```sh
senegal,neighbor,gambia
senegal,neighbor,mauritania
senegal,neighbor,mali
senegal,neighbor,guinea-bissau
senegal,neighbor,guinea
```

We can also add custom metadata for each entity to be displayed in the user interface using `meta -f`:

```sh
kg meta -f metadata.json
```

The library [Cherche](https://github.com/raphaelsty/cherche) provides the entity search engine. KGSearch relies on a local flask API. The user interface is developed in React and uses the [3D Force-Directed Graph](https://github.com/vasturiano/3d-force-graph) library.

fork form
- original https://github.com/raphaelsty/kgsearch
- https://github.com/wasit7/kgsearch