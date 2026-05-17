import express from 'express';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

const router = express.Router();
const JWT_SECRET = 'sua_chave_secreta_super_segura';

function verificarToken(req, res, next) {
  const token = req.headers['authorization']?.split(' ')[1];

  if (!token) {
    return res.status(401).json({ erro: "Acesso negado. Token não fornecido." });
  }

  try {
    const verificado = jwt.verify(token, JWT_SECRET);
    req.usuario = verificado;
    next();
  } catch (erro) {
    res.status(403).json({ erro: "Token inválido ou expirado." });
  }
}

export function configurarRotasBlog(app, db) {

  router.post('/auth/registrar', async (req, res) => {
    const { nome, email, senha } = req.body;

    if (!nome || !email || !senha) {
      return res.status(400).json({ erro: "Todos os campos são obrigatórios." });
    }

    try {
      const salt = await bcrypt.genSalt(10);
      const senhaCriptografada = await bcrypt.hash(senha, salt);

      const resultado = await db.run(
        'INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',
        [nome, email, senhaCriptografada]
      );

      res.status(201).json({ mensagem: "Usuário registrado com sucesso!", usuarioId: resultado.lastID });
    } catch (erro) {
      if (erro.message.includes('UNIQUE')) {
        return res.status(400).json({ erro: "Este e-mail já está cadastrado." });
      }
      res.status(500).json({ erro: "Erro ao registrar usuário." });
    }
  });

  router.post('/auth/login', async (req, res) => {
    const { email, senha } = req.body;

    try {
      const usuario = await db.get('SELECT * FROM usuarios WHERE email = ?', [email]);
      if (!usuario) {
        return res.status(400).json({ erro: "E-mail ou senha incorretos." });
      }

      const senhaValida = await bcrypt.compare(senha, usuario.senha);
      if (!senhaValida) {
        return res.status(400).json({ erro: "E-mail ou senha incorretos." });
      }

      const token = jwt.sign(
        { id: usuario.id, email: usuario.email }, 
        JWT_SECRET, 
        { expiresIn: '2h' }
      );

      res.json({ mensagem: "Login efetuado!", token });
    } catch (erro) {
      res.status(500).json({ erro: "Erro ao fazer login." });
    }
  });

  router.post('/posts', verificarToken, async (req, res) => {
    const { titulo, conteudo } = req.body;
    const usuarioId = req.usuario.id;

    if (!titulo || !conteudo) {
      return res.status(400).json({ erro: "Título e conteúdo são obrigatórios." });
    }

    try {
      const resultado = await db.run(
        'INSERT INTO posts (titulo, conteudo, usuario_id) VALUES (?, ?, ?)',
        [titulo, conteudo, usuarioId]
      );

      res.status(201).json({ 
        mensagem: "Post criado com sucesso!", 
        postId: resultado.lastID 
      });
    } catch (erro) {
      res.status(500).json({ erro: "Erro ao criar post." });
    }
  });

  router.get('/posts', async (req, res) => {
    try {
      const posts = await db.all(`
        SELECT posts.id, posts.titulo, posts.conteudo, posts.data_criacao, usuarios.nome AS autor
        FROM posts
        INNER JOIN usuarios ON posts.usuario_id = usuarios.id
        ORDER BY posts.data_criacao DESC
      `);
      res.json(posts);
    } catch (erro) {
      res.status(500).json({ erro: "Erro ao buscar posts." });
    }
  });

  app.use('/api', router);
}