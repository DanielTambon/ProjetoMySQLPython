CREATE DATABASE IF NOT EXISTS sistema_estoque;
USE sistema_estoque;

CREATE TABLE IF NOT EXISTS Produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    quantidade_disponivel INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    quantidade_vendida INT NOT NULL,
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES Produto(id) ON DELETE CASCADE
);
