-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema estoque_produtos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema estoque_produtos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `estoque_produtos` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `estoque_produtos` ;

-- -----------------------------------------------------
-- Table `estoque_produtos`.`producao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque_produtos`.`producao` (
  `id_producao` INT NOT NULL AUTO_INCREMENT,
  `nome_ingrediente` VARCHAR(255) NOT NULL,
  `unidade_medida` VARCHAR(10) NOT NULL,
  `custo_unitario` DECIMAL(10,2) NOT NULL,
  `data_cadastro` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `ativo` TINYINT(1) NULL DEFAULT '1',
  `estoque_atual` DECIMAL(10,2) NOT NULL DEFAULT '0.00',
  `estoque_minimo` INT NOT NULL DEFAULT '5',
  PRIMARY KEY (`id_producao`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `estoque_produtos`.`movimentos_estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque_produtos`.`movimentos_estoque` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_producao` INT NOT NULL,
  `tipo_movimento` ENUM('entrada', 'saida') NOT NULL,
  `quantidade` DECIMAL(10,2) NOT NULL,
  `data_movimento` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `custo_unitario` DECIMAL(10,2) NULL DEFAULT NULL,
  `observacao` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_producao` (`id_producao` ASC) VISIBLE,
  CONSTRAINT `movimentos_estoque_ibfk_1`
    FOREIGN KEY (`id_producao`)
    REFERENCES `estoque_produtos`.`producao` (`id_producao`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `estoque_produtos`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque_produtos`.`produto` (
  `id_produto` INT NOT NULL AUTO_INCREMENT,
  `nome_produto` VARCHAR(255) NOT NULL,
  `valor_produto` DECIMAL(10,2) NOT NULL,
  `quantidade` DECIMAL(10,2) NOT NULL DEFAULT '0.00',
  `custo` DECIMAL(10,2) NOT NULL DEFAULT '0.00',
  `data_cadastro` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `ativo` TINYINT(1) NULL DEFAULT '1',
  `categoria` VARCHAR(50) NULL DEFAULT 'Sem categoria',
  PRIMARY KEY (`id_produto`),
  UNIQUE INDEX `nome_produto` (`nome_produto` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 23
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `estoque_produtos`.`movimentos_produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque_produtos`.`movimentos_produtos` (
  `id_movimento` INT NOT NULL AUTO_INCREMENT,
  `id_produto` INT NOT NULL,
  `tipo_movimento` ENUM('entrada', 'saida', 'venda') NOT NULL,
  `quantidade` DECIMAL(10,2) NOT NULL,
  `valor_unitario` DECIMAL(10,2) NULL DEFAULT NULL,
  `data_movimento` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `origem_movimento` ENUM('venda', 'baixa') NOT NULL DEFAULT 'venda',
  PRIMARY KEY (`id_movimento`),
  INDEX `id_produto` (`id_produto` ASC) VISIBLE,
  CONSTRAINT `movimentos_produtos_ibfk_1`
    FOREIGN KEY (`id_produto`)
    REFERENCES `estoque_produtos`.`produto` (`id_produto`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `estoque_produtos`.`registro_vendas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque_produtos`.`registro_vendas` (
  `id_venda` INT NOT NULL AUTO_INCREMENT,
  `id_produto` INT NOT NULL,
  `data_venda` DATE NOT NULL,
  `quantidade_vendida` DECIMAL(10,2) NOT NULL,
  `valor_venda_unitario` DECIMAL(10,2) NOT NULL,
  `valor_total` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_venda`),
  INDEX `id_produto` (`id_produto` ASC) VISIBLE,
  CONSTRAINT `registro_vendas_ibfk_1`
    FOREIGN KEY (`id_produto`)
    REFERENCES `estoque_produtos`.`produto` (`id_produto`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
