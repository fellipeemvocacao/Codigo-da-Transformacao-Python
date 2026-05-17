import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

export async function inicializarBanco() {
  const db = await open({
    filename: './dados_servidor.db',
    driver: sqlite3.Database
  });

  await db.exec(`
    CREATE TABLE IF NOT EXISTS registros (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      conteudo TEXT NOT NULL,
      data_envio DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  return db;
}