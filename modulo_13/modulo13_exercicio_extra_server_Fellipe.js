import express from 'express';
import { inicializarBanco } from './database.js';
import { configurarRotasBlog } from './blogApi.js';

const app = express();
app.use(express.json());

inicializarBanco().then((database) => {
  
  configurarRotasBlog(app, database);
  
  const PORT = 3000;
  app.listen(PORT, () => {
    console.log(`Servidor do Blog rodando na porta ${PORT}`);
  });
}).catch(err => {
  console.error("Erro ao iniciar o servidor:", err);
});