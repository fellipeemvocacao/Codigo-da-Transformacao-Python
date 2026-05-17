import express from 'express';
import { inicializarBanco } from './database.js';

const app = express();
app.use(express.json());

let db;

inicializarBanco().then((database) => {
  db = database;
  
  const PORT = 3000;
  app.listen(PORT, () => {
    console.log(`Servidor rodando e banco SQLite conectado na porta ${PORT}`);
  });
}).catch(err => {
  console.error("Erro ao iniciar o banco de dados:", err);
});

app.post('/enviar-dados', async (req, res) => {
  const { conteudo } = req.body;

  if (!conteudo) {
    return res.status(400).json({ erro: "O campo 'conteudo' é obrigatório." });
  }

  try {
    const resultado = await db.run(
      'INSERT INTO registros (conteudo) VALUES (?)',
      [conteudo]
    );

    res.status(201).json({
      mensagem: "Dados salvos com sucesso!",
      id: resultado.lastID
    });
  } catch (erro) {
    console.error(erro);
    res.status(500).json({ erro: "Erro ao salvar os dados no banco." });
  }
});

app.get('/dados', async (req, res) => {
  try {
    const linhas = await db.all('SELECT * FROM registros ORDER BY data_envio DESC');
    res.json(linhas);
  } catch (erro) {
    res.status(500).json({ erro: "Erro ao buscar dados." });
  }
});