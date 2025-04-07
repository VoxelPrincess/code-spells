# 💾 SQL, PostgreSQL, Node.js, Fastify & Kysely — Practical Reference Notes / Практические заметки

---

## 🚀 Installation / Установка

### 🐧 Linux

#### 🐘 Install PostgreSQL

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql
```

#### 📦 Install Node.js and npm

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
```

#### 📘 Install TypeScript and dependencies

```bash
npm init -y
npm install typescript tsx fastify kysely pg dotenv
npx tsc --init
```

---

### 🍏 macOS

#### 🐘 Install PostgreSQL

```bash
brew update
brew install postgresql
brew services start postgresql
psql postgres
```

#### 📦 Install Node.js and npm

```bash
brew install node
```

#### 📘 Install TypeScript and dependencies

```bash
npm init -y
npm install typescript tsx fastify kysely pg dotenv
npx tsc --init
```

---

## 🧠 Key Concepts / Ключевые понятия

- **Database (DB)** — structured storage for data / структурированное хранилище данных.
- **SQL** — language for managing and querying databases / язык запросов к базе данных.
- **PostgreSQL** — relational open-source database / реляционная СУБД.
- **ORM** — maps objects to DB tables / отображает объекты на таблицы БД.
- **Fastify** — fast web framework for Node.js / быстрый веб-фреймворк.
- **Kysely** — type-safe SQL builder / типобезопасный генератор SQL.
- **API** — interface for data exchange / интерфейс обмена данными.
- **CRUD** — Create, Read, Update, Delete operations / основные действия с данными.

---

## 🗂️ Migration Scripts / Скрипты миграции

### Example `migrations.sql`:

```sql
DROP TABLE IF EXISTS person CASCADE;
DROP TABLE IF EXISTS movie CASCADE;

CREATE TABLE person (
  id BIGSERIAL PRIMARY KEY,
  person_name TEXT NOT NULL,
  date_of_birth DATE NOT NULL
);

CREATE TABLE movie (
  id BIGSERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  publish_year INTEGER NOT NULL
);

INSERT INTO person (person_name, date_of_birth)
VALUES ('Keanu Reeves', '1964-09-02');

INSERT INTO movie (title, publish_year)
VALUES ('The Matrix', 1999);
```

▶️ Run migration:

```bash
psql mydatabase < migrations.sql
```

---

## 🛠️ Using psql CLI / Использование psql в терминале

```bash
psql postgres           # connect as default user
psql mydatabase         # connect to specific database
\l                      # list databases
\dt                     # list tables
\d table_name           # describe table
\q                      # quit
```

---

## 🔍 Common SQL Queries / Популярные SQL-запросы

```sql
-- Select all
SELECT * FROM person;

-- Select with filter
SELECT * FROM movie WHERE publish_year > 2000;

-- Insert new row
INSERT INTO person (person_name, date_of_birth)
VALUES ('Carrie-Anne Moss', '1967-08-21');

-- Update data
UPDATE movie SET title = 'The Matrix Reloaded' WHERE id = 1;

-- Delete data
DELETE FROM movie WHERE id = 2;

-- Average score
SELECT movie_id, AVG(score) AS average_score FROM review GROUP BY movie_id;
```

---

## 🔄 Transactions / Транзакции

```sql
BEGIN;
UPDATE person SET person_name = 'Neo' WHERE id = 1;
-- COMMIT или ROLLBACK
COMMIT;
-- ROLLBACK; (if you want to cancel changes)
```

---

## 📦 Running with Fastify + Kysely

### Sample Fastify server with PostgreSQL:

```ts
import "dotenv/config";
import Fastify from "fastify";
import pg from "pg";
import { Kysely, PostgresDialect } from "kysely";
import { DB } from "./types"; // generated with kysely-codegen

const { Pool } = pg;

const db = new Kysely<DB>({
  dialect: new PostgresDialect({
    pool: new Pool({ connectionString: process.env.DATABASE_URL }),
  }),
});

const fastify = Fastify({ logger: true });

fastify.get("/person", async (_, reply) => {
  const result = await db
    .selectFrom("person")
    .select(["id", "person_name"])
    .execute();
  reply.send(result);
});

fastify.listen({ port: 3000 }, () => {
  console.log("Server running on http://localhost:3000");
});
```

---

## 🧪 Generate DB types with kysely-codegen

```bash
npm install --save-dev kysely-codegen
DATABASE_URL=postgres://localhost/mydb npx kysely-codegen
```

This generates `types.ts` that matches your current PostgreSQL schema.

---

## ✅ Tips / Советы

- **Always use version control**: commit your schema and seed data.
- **Use `.env` for secrets**: never hard-code database URLs.
- **Check logs**: Fastify logs can help debug issues.
- **Use indexes**: for large queries, add `CREATE INDEX`.

---

- [README](../README.md)