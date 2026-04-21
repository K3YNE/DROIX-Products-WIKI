import fs from "node:fs";
import path from "node:path";
import { DatabaseSync } from "node:sqlite";
import type { SQLInputValue } from "node:sqlite";
import { dbPath } from "./paths";

let db: DatabaseSync | null = null;

export type Db = DatabaseSync;

export function getDb() {
  if (db) return db;
  const file = dbPath();
  fs.mkdirSync(path.dirname(file), { recursive: true });
  db = new DatabaseSync(file);
  db.exec("PRAGMA foreign_keys = ON; PRAGMA journal_mode = WAL;");
  ensureSchema(db);
  return db;
}

export function ensureSchema(database: DatabaseSync) {
  database.exec(`
    CREATE TABLE IF NOT EXISTS products (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      slug TEXT UNIQUE,
      title TEXT NOT NULL,
      type TEXT NOT NULL DEFAULT 'bench_only',
      brand TEXT,
      parent_slug TEXT,
      form_factor TEXT,
      platform TEXT,
      apu TEXT,
      gpu TEXT,
      wiki_path TEXT,
      source TEXT NOT NULL DEFAULT 'portal',
      needs_review INTEGER NOT NULL DEFAULT 0,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS product_aliases (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      raw_label TEXT NOT NULL UNIQUE,
      normalized_label TEXT NOT NULL,
      product_id INTEGER,
      confidence REAL NOT NULL DEFAULT 0,
      status TEXT NOT NULL DEFAULT 'needs_review',
      notes TEXT,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS benchmark_definitions (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      key TEXT NOT NULL UNIQUE,
      group_name TEXT NOT NULL,
      metric_name TEXT NOT NULL,
      display_name TEXT NOT NULL,
      unit TEXT,
      higher_is_better INTEGER NOT NULL DEFAULT 1,
      enabled INTEGER NOT NULL DEFAULT 1,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS import_batches (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      source_type TEXT NOT NULL,
      source_path TEXT NOT NULL,
      started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      completed_at TEXT,
      row_count INTEGER NOT NULL DEFAULT 0,
      result_count INTEGER NOT NULL DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS benchmark_runs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      import_batch_id INTEGER,
      product_id INTEGER,
      raw_model TEXT NOT NULL,
      normalized_model TEXT NOT NULL,
      sheet_name TEXT NOT NULL,
      source_row INTEGER NOT NULL,
      source_hidden INTEGER NOT NULL DEFAULT 0,
      tested_on TEXT,
      notes TEXT,
      row_tdp_watts TEXT,
      egpu_product_id INTEGER,
      connection_type TEXT,
      display_mode TEXT,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (import_batch_id) REFERENCES import_batches(id) ON DELETE SET NULL,
      FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL,
      FOREIGN KEY (egpu_product_id) REFERENCES products(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS benchmark_results (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      run_id INTEGER NOT NULL,
      definition_id INTEGER NOT NULL,
      value_numeric REAL,
      value_text TEXT,
      unit TEXT,
      resolution TEXT,
      tdp_watts INTEGER,
      tdp_source TEXT,
      source_cell TEXT NOT NULL,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (run_id) REFERENCES benchmark_runs(id) ON DELETE CASCADE,
      FOREIGN KEY (definition_id) REFERENCES benchmark_definitions(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS import_warnings (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      import_batch_id INTEGER,
      sheet_name TEXT,
      source_row INTEGER,
      source_cell TEXT,
      message TEXT NOT NULL,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (import_batch_id) REFERENCES import_batches(id) ON DELETE CASCADE
    );

    CREATE INDEX IF NOT EXISTS idx_products_slug ON products(slug);
    CREATE INDEX IF NOT EXISTS idx_alias_product ON product_aliases(product_id);
    CREATE INDEX IF NOT EXISTS idx_runs_product ON benchmark_runs(product_id);
    CREATE INDEX IF NOT EXISTS idx_results_run ON benchmark_results(run_id);
    CREATE INDEX IF NOT EXISTS idx_results_definition ON benchmark_results(definition_id);
  `);
}

export function rows<T = Record<string, unknown>>(sql: string, params: unknown[] = []) {
  return getDb().prepare(sql).all(...(params as SQLInputValue[])) as T[];
}

export function row<T = Record<string, unknown>>(sql: string, params: unknown[] = []) {
  return getDb().prepare(sql).get(...(params as SQLInputValue[])) as T | undefined;
}
