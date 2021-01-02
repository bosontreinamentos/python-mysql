# Criar banco de dados:
CREATE DATABASE db_MeusLivros;

# Ver bancos de dados existentes:
SHOW DATABASES;

# Selecionar banco para trabalho
USE db_MeusLivros;

# Como saber qual banco está selecionado
SELECT DATABASE();

# Excluir um banco de dados:
DROP DATABASE db_MeusLivros;

# Criar tabela de autores:
CREATE TABLE tbl_Autores (
  IdAutor SMALLINT AUTO_INCREMENT,
  NomeAutor VARCHAR(30) NOT NULL,
  SobrenomeAutor VARCHAR(60) NOT NULL,
  CONSTRAINT pk_id_autor PRIMARY KEY (IdAutor)
);

DESCRIBE tbl_Autores;

# Criar tabela de Editoras
CREATE TABLE tbl_Editoras (
    IdEditora SMALLINT PRIMARY KEY AUTO_INCREMENT,
    NomeEditora VARCHAR(50) NOT NULL
);

DESCRIBE tbl_Editoras;

# Criar tabela de Assuntos
CREATE TABLE tbl_Assuntos (
  IdAssunto TINYINT AUTO_INCREMENT,
  Assunto VARCHAR(25) NOT NULL,
CONSTRAINT pk_id_assunto PRIMARY KEY (IdAssunto)
);

DESCRIBE tbl_Assuntos;

# Criar tabela de livros
CREATE TABLE IF NOT EXISTS tbl_Livros (
   IDLivro SMALLINT NOT NULL AUTO_INCREMENT, 
   NomeLivro VARCHAR(70) NOT NULL,
   ISBN13 VARCHAR(13) NOT NULL,
   DataPub DATE,
   PrecoLivro DECIMAL(10,2) NOT NULL,
   NumeroPaginas SMALLINT NOT NULL,
   IdEditora SMALLINT NOT NULL,
   IdAssunto TINYINT NOT NULL,
CONSTRAINT pk_id_livro PRIMARY KEY (IDLivro),
CONSTRAINT fk_id_editora FOREIGN KEY (IdEditora)
REFERENCES tbl_Editoras (IdEditora) ON DELETE CASCADE,
CONSTRAINT fk_id_assunto FOREIGN KEY (IdAssunto)
REFERENCES tbl_Assuntos (IdAssunto) ON DELETE CASCADE
);

# Criar tabela associativa entre livros e autores
CREATE TABLE tbl_LivrosAutores (
  IdLivro SMALLINT NOT NULL,
  IdAutor SMALLINT NOT NULL,
CONSTRAINT pk_id_livro_autor PRIMARY KEY (IdLivro, IdAutor),
CONSTRAINT fk_id_livros FOREIGN KEY (IdLivro)
REFERENCES tbl_Livros (IdLivro),
CONSTRAINT fk_id_autores FOREIGN KEY (IdAutor)
REFERENCES tbl_Autores (IdAutor)
);

DESCRIBE tbl_Livros;

USE db_MeusLivros;

ALTER TABLE tbl_Livros AUTO_INCREMENT=100;

# Inserir registros na tabela de editoras:
INSERT INTO tbl_editoras (NomeEditora)
VALUES
('Prentice Hall'), ('O´Reilly'),
('Microsoft Press'), ('Wiley'),
('Mc Graw Hill'), ('Bookman'),
('Novatec'), ('Apress'),
('Sybex'), ('Mike Murach and Associates');

INSERT INTO tbl_editoras (NomeEditora)
VALUES ('MakerMedia');

SELECT * FROM tbl_editoras;

# Inserir registros na tabela de Assuntos:
INSERT INTO tbl_Assuntos (Assunto)
VALUES 
('Ficção'), ('Botânica'),
('Eletrônica'), ('Matemática'),
('Aventura'), ('Literatura'),
('Informática'), ('Suspense');

SELECT * FROM tbl_assuntos;

# Inserir registros na tabela de autores:
INSERT INTO tbl_autores (NomeAutor, SobrenomeAutor)
VALUES
('Daniel', 'Barret'), ('Gerald', 'Carter'), ('Mark', 'Sobell'),
('William', 'Stanek'), ('Richard', 'Blum'), ('Christine', 'Bresnahan'), 
('Richard', 'Silverman'), ('Robert', 'Byrnes'), ('Jay', 'Ts'),
('Robert', 'Eckstein'), ('Paul', 'Horowitz'), ('Winfield', 'Hill'),
('Joel', 'Murach'), ('Paul', 'Scherz'), ('Simon', 'Monk');

SELECT * FROM tbl_autores;

# Inserir registros na tabela de livros;
INSERT INTO tbl_Livros (NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdAssunto, IdEditora)
VALUES
('Linux Command Line and Shell Scripting','9781118983843', '20150109', 165.55, 816, 7, 4),
('SSH, the Secure Shell','9780596008956', '20050517', 295.41, 672, 7, 2),
('Using Samba','9780596002565', '20031221', 158.76, 449, 7, 2),
('A Arte da Eletrônica', '9788582604342', '20170308', 176.71,  1160, 7, 6),
('Windows Server 2012 Inside Out','9780735666313', '20130125', 179.51,  1584, 7, 3),
('Murach´s MySQL','9781943872367', '20190501', 227.64,  650, 7, 10),
('Practical Electronics for Inventors', '9781259587542', '20160711', 119.58,  1056, 3, 5);

SELECT * FROM tbl_livros;

# Preencher tabela LivrosAutores (associativa) -> relaciona livros com seus autores
INSERT INTO tbl_LivrosAutores (IdLivro, IdAutor)
VALUES 
(100,5), (100,6),
(101,1), (101,7), (101,8),
(102,2), (102,9), (102,10),
(103,11), (103,12),
(104,4),
(105,13),
(106,14), (106,15);

SELECT * FROM tbl_livrosautores;

USE db_meuslivros;

SELECT NomeAutor FROM tbl_Autores;

SELECT * FROM tbl_Autores;

SELECT NomeLivro
FROM tbl_Livros;

SELECT Assunto
FROM tbl_Assuntos;

SELECT NomeEditora
FROM tbl_editoras;

SELECT NomeLivro, PrecoLivro FROM tbl_Livros;

SELECT NomeAutor, SobrenomeAutor
FROM tbl_Autores;

SELECT NomeLivro, ISBN13, DataPub
FROM tbl_Livros;

# Crie uma consulta que retorne os códigos dos livros, seus nomes e a quantidade
# de páginas de cada um.

SELECT NomeLivro, IDLivro, NumeroPaginas
FROM tbl_livros;

# Efetuando consultas com ordenação - cláusula ORDER BY

SELECT * FROM tbl_Livros
ORDER BY NomeLivro ASC;

SELECT NomeLivro, IdEditora
FROM tbl_Livros
ORDER BY IdEditora;

SELECT NomeLivro, PrecoLivro
FROM tbl_Livros
ORDER BY PrecoLivro DESC;

SELECT NomeLivro, DataPub, idAssunto
FROM tbl_Livros
ORDER BY idAssunto, NomeLivro;

# Crie uma consulta que retorne a lista de assuntos em ordem alfabética inversa

SELECT Assunto
FROM tbl_assuntos
ORDER BY Assunto DESC;

# Filtrar os resultados de uma consulta SQL com cláusula WHERE

SELECT NomeLivro, DataPub FROM tbl_Livros WHERE IdEditora = 2;

SELECT IdAutor, NomeAutor FROM tbl_Autores WHERE SobrenomeAutor = 'Stanek';

SELECT IdAssunto FROM tbl_Assuntos WHERE Assunto = 'Terror';

SELECT IdAssunto FROM tbl_Assuntos WHERE Assunto = 'Aventura';

SELECT NomeLivro, PrecoLivro FROM tbl_livros
WHERE PrecoLivro > 200.00
ORDER BY NomeLivro;

# crie uma consulta que mostre os nomes dos livros e datas de publicação somente dos livros
# que tem MENOS de 1000 páginas. Ordenar por data de publicação.

# Colunas a mostrar: Nomes de Livros, Datas de Publicação
# Critérios de Filtro: MENOS de 1000 páginas (< 1000 páginas)
# Critério: ordenar por data de publicação

SELECT NomeLivro, DataPub
FROM tbl_livros
WHERE NumeroPaginas < 1000
ORDER BY DataPub;

# inserir uma nova editora na tabela de editoras:
INSERT INTO tbl_Editoras (NomeEditora)
VALUES ('Bóson Editorial');

# Verificar se o registro foi incluído:
SELECT * FROM tbl_Editoras;

# Excluír o registro com DELETE:
DELETE FROM tbl_Editoras
WHERE IdEditora = 12;

# Resposta do exercício:
INSERT INTO tbl_Editoras VALUES ('Scribner');
INSERT INTO tbl_Assuntos VALUES ('Terror');

INSERT INTO tbl_Autores (NomeAutor, SobrenomeAutor)  
VALUES ('Stephen', 'King');

INSERT INTO tbl_Livros (NomeLivro, ISBN13, DataPub, PrecoLivro, IdEditora, IdCategoria, NumeroPaginas)
VALUES ('It', '9781501182099', '20170711', 48.74, 12, 6, 450);

SELECT * FROM tbl_Livros;

DELETE FROM tbl_Editoras WHERE IdEditora =  ;

SELECT * FROM tbl_Livros;
SELECT * FROM tbl_Editoras;

USE db_MeusLivros;

# Trocar o nome de um livro
SELECT * FROM tbl_livros;

UPDATE tbl_Livros
SET NomeLivro = 'SSH, O Shell Seguro'
WHERE IdLivro = 101;

UPDATE tbl_Livros
SET PrecoLivro = PrecoLivro + 10
WHERE IdLivro = 105;

SELECT * FROM tbl_assuntos;

UPDATE tbl_Assuntos
SET Assunto = 'Biologia'
WHERE IdAssunto = 2;

# Usando o TRUNCATE TABLE para limpar tabelas
CREATE TABLE tbl_Emprestimos (
  IdEmprestimo TINYINT PRIMARY KEY,
  NomeLivro VARCHAR (60) NOT NULL,
  NomeEmprestador VARCHAR (50) NOT NULL
);

INSERT INTO tbl_Emprestimos (IdEmprestimo, NomeLivro, NomeEmprestador)
VALUES
  (20,'O Cortiço','João da Silva'),
  (21,'A Moreninha','Marcos de Souza'),
  (22,'Macunaíma','Ana Abreu');
SELECT * FROM tbl_Emprestimos;

TRUNCATE TABLE tbl_Emprestimos;

# Criando nomes alternativos (aliases) com cláusula AS

SELECT NomeLivro AS Livro
FROM tbl_Livros
WHERE IdLivro > 102;

SELECT NomeAutor AS Nome,
SobrenomeAutor Sobrenome
FROM tbl_Autores AS Autores;

SELECT NomeLivro AS Livro, PrecoLivro AS 'Preço do Livro'
FROM tbl_Livros AS Livros
ORDER BY 'Preço do Livro' DESC;

SELECT IdLivro, NomeLivro, IdEditora FROM tbl_Livros
WHERE IdLivro > 102 AND IdEditora < 4;

SELECT IdLivro, NomeLivro, IdEditora FROM tbl_Livros
WHERE IdLivro > 102 OR IdEditora < 4;

SELECT IdLivro, NomeLivro, IdEditora FROM tbl_Livros
WHERE NOT IdEditora = 10;

SELECT IdLivro, NomeLivro, IdEditora FROM tbl_Livros
WHERE IdLivro > 102 AND NOT IdEditora <= 4;

# Revendo Funções de Agregação
SELECT COUNT(*) AS Total FROM tbl_Autores;

SELECT COUNT(DISTINCT idEditora) FROM tbl_Livros;

SELECT MAX(PrecoLivro) AS 'Mais caro' FROM tbl_Livros;

SELECT MIN(PrecoLivro) FROM tbl_Livros;

SELECT AVG(PrecoLivro) AS Média FROM tbl_Livros;

SELECT SUM(PrecoLivro) AS 'Preço Total' FROM tbl_Livros;

SELECT SUM(PrecoLivro) / COUNT(*) AS 'Preço Médio' FROM tbl_Livros;

SELECT COUNT(*) AS 'Quant Livros', SUM(NumeroPaginas) AS 'Páginas Totais',
AVG(NumeroPaginas) 'Média de Págs.' FROM tbl_Livros;

# Como usar a cláusula BETWEEN para filtrar valores
SELECT * FROM tbl_Livros
WHERE DataPub BETWEEN '20040517' AND '20110517';

SELECT NomeLivro AS Livro, PrecoLivro AS Preço FROM tbl_Livros
WHERE PrecoLivro BETWEEN 150.00 AND 200.00;

SELECT NomeLivro, PrecoLivro FROM tbl_Livros
WHERE PrecoLivro BETWEEN 170.00 AND 180.00
OR PrecoLivro BETWEEN 220.00 AND 300.00;

# Filtrar consultas com cláusula LIKE (e também NOT LIKE)
SELECT * FROM tbl_Livros WHERE NomeLivro LIKE 'A%';

SELECT * FROM tbl_Livros WHERE NomeLivro NOT LIKE 'S%';

SELECT NomeLivro FROM tbl_Livros WHERE NomeLivro LIKE '_i%';

SELECT NomeLivro AS Livro, PrecoLivro AS Valor
FROM tbl_Livros
WHERE NomeLivro NOT LIKE 'A%' AND PrecoLivro <= 190.00
ORDER BY NomeLivro;

SELECT NomeLivro, DataPub FROM tbl_Livros
WHERE NomeLivro LIKE '__a%';

SELECT NomeLivro, NumeroPaginas FROM tbl_Livros
WHERE NomeLivro LIKE 'A%ca'; 

# Exemplos de junções com INNER JOIN
SELECT * FROM tbl_Livros
INNER JOIN tbl_Editoras
    ON tbl_Livros.IdEditora = tbl_Editoras.IdEditora;
    

SELECT tbl_Livros.NomeLivro, tbl_Livros.ISBN13, tbl_Assuntos.Assunto
FROM tbl_Livros JOIN tbl_Assuntos
    ON tbl_Livros.IdAssunto = tbl_Assuntos.IdAssunto;

SELECT L.NomeLivro AS Livros, E.NomeEditora AS Editoras
FROM tbl_Livros AS L
JOIN tbl_Editoras AS E
	ON L.IdEditora = E.IdEditora
WHERE E.NomeEditora LIKE 'M%';

SELECT L.NomeLivro Livro, C.Assunto Assunto, E.NomeEditora Editora
FROM tbl_Livros L
JOIN tbl_Assuntos C
	ON L.IdAssunto = C.IdAssunto
INNER JOIN tbl_Editoras E
	ON L.IdEditora = E.IdEditora;

SELECT L.NomeLivro Livro, CONCAT(A.NomeAutor, ' ', A.SobrenomeAutor) Autor,
L.PrecoLivro 'Preço do Livro'
FROM tbl_livrosautores LA
JOIN tbl_livros L
	ON L.IdLivro = LA.IdLivro
JOIN tbl_Autores A
	ON A.IdAutor = LA.IdAutor;

# Procedimentos Armazenados (Stored Procedures)
# Sintaxe:
# CREATE PROCEDURE nome_procedimento(parâmetros)
# declarações a executar;
USE db_MeusLivros;

CREATE PROCEDURE verPreço (varLivro smallint)
SELECT CONCAT('O preço do livro ', NomeLivro, ' é ', PrecoLivro) AS Preço
FROM tbl_livros
WHERE IDLivro = varLivro;

CALL verPreço(101);

DROP PROCEDURE verPreço;

CREATE PROCEDURE consultaLivros (varEditora VARCHAR(50))
SELECT CONCAT('O livro ', NomeLivro, ' custa ', PrecoLivro) AS Preço
FROM tbl_Livros
INNER JOIN tbl_editoras
	ON tbl_livros.IDeditora = tbl_editoras.IDEditora
WHERE tbl_editoras.NomeEditora = varEditora;

CALL consultaLivros('O´Reilly');

# Exemplo: aumentar os preços dos livros em X%
DELIMITER //
CREATE PROCEDURE aumentaPreço (X smallint)
BEGIN
	UPDATE tbl_livros
	SET PrecoLivro = PrecoLivro * (1 + x/100);
	SELECT 'Procedimento executado com sucesso!';
END//
DELIMITER ;

SELECT PrecoLivro FROM tbl_livros WHERE IDlivro = 100;
CALL aumentaPreço(10);
SELECT PrecoLivro FROM tbl_livros WHERE IDlivro = 100;

# Parâmetro IN
DELIMITER //
CREATE PROCEDURE editora_livro (IN editora VARCHAR(50))
BEGIN
    SELECT L.NomeLivro, E.NomeEditora
    FROM tbl_Livros L
    INNER JOIN tbl_editoras E
    ON L.IDeditora = E.IDEditora
    WHERE E.NomeEditora = editora;
END//
DELIMITER ;
DROP PROCEDURE editora_livro;
-- Testando o procedimento.
CALL editora_livro('Wiley');

# Parâmetro OUT
DELIMITER //
CREATE PROCEDURE teste_out (IN id INT, OUT livro VARCHAR(50))
BEGIN
	SELECT NomeLivro
	INTO livro
	FROM tbl_Livros
	WHERE IDLivro = id;
END//
DELIMITER ;

CALL teste_out(104, @livro);
SELECT @livro;

SELECT NomeLivro, NumeroPaginas
FROM tbl_livros
WHERE NumeroPaginas NOT BETWEEN 600 AND 1000;